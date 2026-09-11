#!/usr/bin/env bash
# F2 inject — generation blast-radius fault (blueprint 8.9).
#
# A "teammate" commit to platform-config applicationsets/storefront.yaml empties
# the clusters generator's `cluster-role: workload` selector, so the matrix now
# matches EVERY registered cluster — including in-cluster (the management
# cluster). The ApplicationSet then generates storefront-{dev,staging,prod}-in-cluster
# in addition to the intended -workload set: an unexpectedly large blast radius.
set -euo pipefail
FAULT_ID="F2"
# shellcheck source-path=SCRIPTDIR
# shellcheck source=../lib.sh
source "$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)/../lib.sh"

step "F2 inject — ApplicationSet selector drop (generation)"

gitea_main_sha platform-config | save_state_file main.sha

wt="$(mktemp -d)"
teammate_clone platform-config "${wt}"
# Empty the cluster selector so it matches all clusters (incl. in-cluster).
yq -i '.spec.generators[0].matrix.generators[0].clusters.selector.matchLabels = {}' \
  "${wt}/applicationsets/storefront.yaml"
teammate_push "${wt}" "storefront appset: simplify cluster selector"
rm -rf "${wt}"

ok "F2 injected: selector emptied; expect stray storefront-*-in-cluster Applications"
