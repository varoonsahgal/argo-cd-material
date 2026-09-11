#!/usr/bin/env bash
# F2 revert — restore the selector AND remove the stray in-cluster Applications.
#
# Because the ApplicationSet uses applicationsSync=create-update, reverting the
# Git change does NOT delete the already-generated in-cluster Applications; they
# must be removed deliberately. They target in-cluster/argocd, which the
# storefront AppProject forbids, so they deployed nothing — an orphan delete is
# safe and exact.
set -euo pipefail
FAULT_ID="F2"
# shellcheck source-path=SCRIPTDIR
# shellcheck source=../lib.sh
source "$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)/../lib.sh"

step "F2 revert — restore selector and delete stray in-cluster Applications"
sha="$(cat "$(state_path main.sha)" 2>/dev/null || true)"
gitea_reset_main platform-config "${sha}"

for env in dev staging prod; do
  app_delete_orphan "storefront-${env}-in-cluster"
done
ok "F2 reverted: selector restored; in-cluster Applications removed"
