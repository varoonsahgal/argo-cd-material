#!/usr/bin/env bash
# apply-argocd-config.sh — install/upgrade Argo CD from the vendored chart with
# the course values (blueprint section 8.6). Stands in for "the platform pipeline
# that manages Argo CD declaratively." Injects the admin and team-a-dev passwords
# at runtime from per-VM credential files so NO secret is ever committed.
#
# Usage: apply-argocd-config.sh [extra-values.yaml ...]
#   Extra values files are layered on top of the base values (later wins). Resets
#   use this to add the capstone RBAC overlay or restore F7's resource limits.
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
# shellcheck source=lib/common.sh
source "${SCRIPT_DIR}/lib/common.sh"

BASE_VALUES="${ARGOCD_VALUES_FILE:-${COURSE_REPOS_SRC}/platform-config/argocd/values.yaml}"

main() {
  require_cmd helm kubectl argocd
  [ -f "${COURSE_CHART_PATH}" ] || die "vendored chart not found: ${COURSE_CHART_PATH} (run bootstrap)"
  [ -f "${BASE_VALUES}" ] || die "base values not found: ${BASE_VALUES}"

  step "Applying Argo CD configuration (chart ${ARGOCD_CHART_VERSION}, ${ARGOCD_VERSION})"

  # Compute bcrypt hashes with the argocd CLI (no htpasswd dependency).
  local admin_pw admin_hash team_pw team_hash mtime
  admin_pw="$(read_cred "${COURSE_CRED_DIR}/argocd-admin.txt")"
  admin_hash="$(argocd account bcrypt --password "${admin_pw}")"
  mtime="$(date -u +%Y-%m-%dT%H:%M:%SZ)"

  local runtime_secrets; runtime_secrets="$(mktemp)"
  chmod 600 "${runtime_secrets}"
  {
    echo "configs:"
    echo "  secret:"
    echo "    argocdServerAdminPassword: \"${admin_hash}\""
    echo "    argocdServerAdminPasswordMtime: \"${mtime}\""
  } > "${runtime_secrets}"

  # The team-a-dev local account password (Lab 5) lives in argocd-secret under the
  # accounts.<name>.password key. Add it only if the credential exists.
  if [ -f "${COURSE_CRED_DIR}/team-a-dev.txt" ]; then
    team_pw="$(read_cred "${COURSE_CRED_DIR}/team-a-dev.txt")"
    team_hash="$(argocd account bcrypt --password "${team_pw}")"
    {
      echo "    extra:"
      echo "      accounts.team-a-dev.password: \"${team_hash}\""
      echo "      accounts.team-a-dev.passwordMtime: \"${mtime}\""
    } >> "${runtime_secrets}"
  fi

  # Pre-create the Redis auth secret (redisSecretInit.enabled=false in values).
  # The chart's redis-secret-init pre-install hook Job shares a single, unweighted
  # pre-install hook with its own RBAC; under the pinned Helm 4 the Job can run
  # before its RoleBinding is effective and fail 403 (BackoffLimitExceeded),
  # hanging `helm --wait`. Provisioning the secret here removes that hook race.
  kmgmt get ns "${ARGOCD_NAMESPACE}" >/dev/null 2>&1 || kmgmt create ns "${ARGOCD_NAMESPACE}" >/dev/null
  if ! kmgmt -n "${ARGOCD_NAMESPACE}" get secret argocd-redis >/dev/null 2>&1; then
    local redis_pw
    # Bound the input first so nothing downstream closes an infinite pipe (SIGPIPE
    # under `set -o pipefail`); cut reads its finite input to EOF.
    redis_pw="$(head -c 512 /dev/urandom | LC_ALL=C tr -dc 'A-Za-z0-9' | cut -c1-32)"
    kmgmt -n "${ARGOCD_NAMESPACE}" create secret generic argocd-redis \
      --from-literal=auth="${redis_pw}" >/dev/null
    kmgmt -n "${ARGOCD_NAMESPACE}" label secret argocd-redis \
      app.kubernetes.io/name=argocd-redis \
      app.kubernetes.io/part-of=argocd --overwrite >/dev/null
    ok "pre-created argocd-redis secret (redisSecretInit disabled)"
  fi

  # Assemble -f arguments: base, runtime secrets, then any extra overlays.
  local helm_args=(upgrade --install argocd "${COURSE_CHART_PATH}"
    --kube-context "${MGMT_CONTEXT}"
    -n "${ARGOCD_NAMESPACE}" --create-namespace
    -f "${BASE_VALUES}" -f "${runtime_secrets}")
  local extra
  for extra in "$@"; do
    [ -f "${extra}" ] || die "extra values file not found: ${extra}"
    helm_args+=(-f "${extra}")
  done
  helm_args+=(--wait --timeout 300s)

  helm "${helm_args[@]}"
  rm -f "${runtime_secrets}"

  ok "Argo CD release applied"

  # A concise readiness check independent of --wait.
  kmgmt -n "${ARGOCD_NAMESPACE}" rollout status deploy/argocd-server --timeout=180s >/dev/null
  kmgmt -n "${ARGOCD_NAMESPACE}" rollout status deploy/argocd-repo-server --timeout=180s >/dev/null
  ok "argocd-server and argocd-repo-server are ready"
}

main "$@"
