#!/usr/bin/env bash
# capstone-check.sh — report the capstone restoration progress PER AREA, without
# naming any cause or fix (blueprint 8.9, CAP-P3).
#
#   capstone-check.sh [--local]
#
# It groups the observable signals into the areas a responder triages and prints
# "resolved" or "unresolved" for each. It never says which fault caused an area
# to be unresolved and never suggests a repair — that separation is what keeps it
# usable both during the capstone and by the instructor. Exit code is 0 when
# every area is resolved, 1 otherwise (handy for the solution validation).
set -euo pipefail

# ---- parse --local before sourcing common ----
COURSE_LOCAL=0
for arg in "$@"; do
  case "${arg}" in
    --local) COURSE_LOCAL=1 ;;
    -h|--help) grep '^#' "$0" | sed 's/^# \{0,1\}//'; exit 0 ;;
    *) echo "unknown argument: ${arg}" >&2; exit 2 ;;
  esac
done
export COURSE_LOCAL

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
# shellcheck source=lib/common.sh
source "${SCRIPT_DIR}/lib/common.sh"

# The Applications a fully-restored capstone platform should have (CP-capstone-restored).
EXPECTED_APPS="platform-root platform-quotas platform-netpol platform-agent \
storefront-dev-workload storefront-staging-workload storefront-prod-workload team-a-guestbook"

UNRESOLVED=0

# Print one area line and tally unresolved areas.
area() {
  local label="$1" state="$2" detail="${3:-}"
  if [ "${state}" = "resolved" ]; then
    printf '  %s%-10s%s %s\n' "${_c_green}" "resolved" "${_c_reset}" "${label}"
  else
    printf '  %s%-10s%s %s%s\n' "${_c_red}" "unresolved" "${_c_reset}" "${label}" \
      "${detail:+  (${detail})}"
    UNRESOLVED=$((UNRESOLVED + 1))
  fi
}

# --- helpers (kubectl only; offline) ---
app_names() { kmgmt -n "${ARGOCD_NAMESPACE}" get applications -o jsonpath='{.items[*].metadata.name}' 2>/dev/null; }
appf() { kmgmt -n "${ARGOCD_NAMESPACE}" get application "$1" -o jsonpath="{$2}" 2>/dev/null; }
deploy_available() {
  local d avail
  d="$1"
  avail="$(kmgmt -n "${ARGOCD_NAMESPACE}" get deploy "${d}" -o jsonpath='{.status.availableReplicas}' 2>/dev/null)"
  [ -n "${avail}" ] && [ "${avail}" != "0" ]
}

# --- Area 1: Argo CD platform components -----------------------------------
check_platform_components() {
  local d ok_all=1
  for d in argocd-repo-server argocd-server; do
    deploy_available "${d}" || ok_all=0
  done
  # application-controller is a StatefulSet.
  local ready
  ready="$(kmgmt -n "${ARGOCD_NAMESPACE}" get statefulset argocd-application-controller \
    -o jsonpath='{.status.readyReplicas}' 2>/dev/null)"
  [ -n "${ready}" ] && [ "${ready}" != "0" ] || ok_all=0
  if [ "${ok_all}" -eq 1 ]; then area "argo cd platform components" resolved
  else area "argo cd platform components" unresolved "a core component is not serving"; fi
}

# --- Area 2: Workload cluster connectivity ---------------------------------
check_connectivity() {
  local live stored
  live="$(kwork -n argocd-access get secret argocd-manager-token \
    -o go-template='{{ index .data "token" | base64decode }}' 2>/dev/null || true)"
  stored="$(kmgmt -n "${ARGOCD_NAMESPACE}" get secret cluster-workload \
    -o go-template='{{ index .data "config" | base64decode }}' 2>/dev/null | yq -r '.bearerToken' 2>/dev/null || true)"
  if kwork get ns >/dev/null 2>&1 && [ -n "${stored}" ] && [ "${stored}" != "null" ] \
     && [ "${live}" = "${stored}" ]; then
    area "workload cluster connectivity" resolved
  else
    area "workload cluster connectivity" unresolved "cluster credential does not authenticate"
  fi
}

# --- Area 3: Source rendering ----------------------------------------------
check_source_rendering() {
  local bad
  bad="$(kmgmt -n "${ARGOCD_NAMESPACE}" get applications -o json 2>/dev/null \
    | yq -r '.items[] | select(.status.conditions[]? | .type == "ComparisonError") | .metadata.name' 2>/dev/null \
    | tr '\n' ' ' | sed 's/ *$//')"
  if [ -z "${bad}" ]; then area "application source rendering" resolved
  else area "application source rendering" unresolved "manifests fail to render"; fi
}

# --- Area 4: Generation and ownership --------------------------------------
check_generation_ownership() {
  local name stray="" warned=""
  for name in $(app_names); do
    case " ${EXPECTED_APPS} " in
      *" ${name} "*) : ;;
      *) stray="${stray} ${name}" ;;
    esac
  done
  warned="$(kmgmt -n "${ARGOCD_NAMESPACE}" get applications -o json 2>/dev/null \
    | yq -r '.items[] | select(.status.conditions[]? | .type == "SharedResourceWarning") | .metadata.name' 2>/dev/null \
    | tr '\n' ' ' | sed 's/ *$//')"
  if [ -z "${stray# }" ] && [ -z "${warned}" ]; then
    area "application generation and ownership" resolved
  else
    area "application generation and ownership" unresolved "unexpected or shared-owner Applications"
  fi
}

# --- Area 5: Deployment policy ---------------------------------------------
check_policy() {
  local name bad=""
  for name in $(app_names); do
    local phase msg
    phase="$(appf "${name}" '.status.operationState.phase')"
    msg="$(appf "${name}" '.status.operationState.message')"
    if [ "${phase}" = "Failed" ] && printf '%s' "${msg}" | grep -qiE 'forbidden|cannot |RBAC|denied'; then
      bad="${bad} ${name}"
    fi
  done
  if [ -z "${bad# }" ]; then area "deployment policy (permissions)" resolved
  else area "deployment policy (permissions)" unresolved "a sync is being denied"; fi
}

# --- Area 6: Workload runtime health ---------------------------------------
check_runtime_health() {
  local name ok_all=1
  for name in ${EXPECTED_APPS}; do
    local h s
    h="$(appf "${name}" '.status.health.status')"
    s="$(appf "${name}" '.status.sync.status')"
    if [ "${h}" != "Healthy" ] || [ "${s}" != "Synced" ]; then ok_all=0; fi
  done
  if [ "${ok_all}" -eq 1 ]; then area "workload runtime health" resolved
  else area "workload runtime health" unresolved "not all workloads are Synced/Healthy"; fi
}

main() {
  require_cmd kubectl yq
  step "Capstone restoration status by area"
  check_platform_components
  check_connectivity
  check_source_rendering
  check_generation_ownership
  check_policy
  check_runtime_health
  echo
  if [ "${UNRESOLVED}" -eq 0 ]; then
    ok "all areas resolved"
    return 0
  fi
  warn "${UNRESOLVED} area(s) still unresolved"
  return 1
}

main
