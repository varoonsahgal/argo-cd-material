#!/usr/bin/env bash
# F3 revert — remove the duplicate WITHOUT cascade, then restore Git.
#
# Deleting team-root with cascade would prune platform-agent-dup which, because
# it shares the live Deployment with platform-agent, would delete the running
# workload. So the strays are orphan-deleted first (leaving the shared workload
# owned by the real platform-agent), and only then is Git restored.
set -euo pipefail
FAULT_ID="F3"
# shellcheck source-path=SCRIPTDIR
# shellcheck source=../lib.sh
source "$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)/../lib.sh"

step "F3 revert — orphan-delete strays, restore Git"
app_delete_orphan "platform-agent-dup"
app_delete_orphan "team-root"

sha="$(cat "$(state_path main.sha)" 2>/dev/null || true)"
gitea_reset_main platform-config "${sha}"
app_hard_refresh "platform-root"
ok "F3 reverted: duplicates removed; platform-agent retains sole ownership"
