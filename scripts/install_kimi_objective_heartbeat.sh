#!/usr/bin/env bash
set -euo pipefail

REPO_ROOT="${1:-/root/chimera-deploy}"
WORKSPACE="${2:-/root/openclawtrading}"

install -d /etc/systemd/system
install -d "$WORKSPACE/harnesses/codex/chimera"

install -m 0644 "$REPO_ROOT/systemd/kimi-objective-heartbeat.service" /etc/systemd/system/kimi-objective-heartbeat.service
install -m 0644 "$REPO_ROOT/systemd/kimi-objective-heartbeat.timer" /etc/systemd/system/kimi-objective-heartbeat.timer
install -m 0755 "$REPO_ROOT/scripts/run_objective_orchestration_heartbeat.sh" /usr/local/bin/run_objective_orchestration_heartbeat.sh

if [ ! -f "$WORKSPACE/harnesses/codex/chimera/OBJECTIVE_HEARTBEAT.md" ]; then
  install -m 0644 \
    "$REPO_ROOT/automation_specs/objective-orchestration-heartbeat/OBJECTIVE_HEARTBEAT_TEMPLATE.md" \
    "$WORKSPACE/harnesses/codex/chimera/OBJECTIVE_HEARTBEAT.md"
fi

systemctl daemon-reload
systemctl enable --now kimi-objective-heartbeat.timer
systemctl start kimi-objective-heartbeat.service
systemctl status kimi-objective-heartbeat.timer --no-pager -n 20 || true
