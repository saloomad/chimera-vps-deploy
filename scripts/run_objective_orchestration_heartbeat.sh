#!/usr/bin/env bash
set -euo pipefail

REPO_ROOT="${1:-/root/chimera-deploy}"
KIMI_HOME="${KIMI_HOME:-/root/.kimi}"
WORKSPACE="${WORKSPACE:-/root/openclawtrading}"
CONTROL_FILE="${CONTROL_FILE:-$WORKSPACE/harnesses/codex/chimera/OBJECTIVE_HEARTBEAT.md}"
PROMPT_TEMPLATE="${PROMPT_TEMPLATE:-$REPO_ROOT/automation_specs/objective-orchestration-heartbeat/PROMPT.md}"
LOG_DIR="${LOG_DIR:-$KIMI_HOME/heartbeat_logs}"
KIMI_BIN="${KIMI_BIN:-/root/.local/bin/kimi}"
LOCK_FILE="${LOCK_FILE:-/tmp/kimi-objective-heartbeat.lock}"

mkdir -p "$LOG_DIR"

exec 9>"$LOCK_FILE"
if ! flock -n 9; then
  echo "heartbeat already running"
  exit 0
fi

if [ ! -x "$KIMI_BIN" ]; then
  echo "missing kimi binary: $KIMI_BIN" >&2
  exit 1
fi

if [ ! -f "$PROMPT_TEMPLATE" ]; then
  echo "missing prompt template: $PROMPT_TEMPLATE" >&2
  exit 1
fi

if [ ! -f "$CONTROL_FILE" ]; then
  echo "missing heartbeat control file: $CONTROL_FILE"
  exit 0
fi

status="$(awk -F': ' '/^status:/ {print $2; exit}' "$CONTROL_FILE" | tr -d '\r')"
if [ "$status" != "active" ]; then
  echo "heartbeat skipped because status=$status"
  exit 0
fi

timestamp="$(date -u +%Y%m%dT%H%M%SZ)"
log_file="$LOG_DIR/objective-heartbeat-$timestamp.log"

python3 - "$KIMI_BIN" "$KIMI_HOME" "$PROMPT_TEMPLATE" "$log_file" <<'PY'
import pathlib
import subprocess
import sys

kimi_bin = pathlib.Path(sys.argv[1])
kimi_home = pathlib.Path(sys.argv[2])
prompt_template = pathlib.Path(sys.argv[3])
log_file = pathlib.Path(sys.argv[4])

prompt = prompt_template.read_text(encoding="utf-8")
cmd = [
    str(kimi_bin),
    "--print",
    "--final-message-only",
    "-w",
    str(kimi_home),
    "-p",
    prompt,
]
res = subprocess.run(cmd, text=True, capture_output=True)
combined = (res.stdout or "") + ("\n" + res.stderr if res.stderr else "")
log_file.write_text(combined.strip() + "\n", encoding="utf-8")
sys.stdout.write(combined)
raise SystemExit(res.returncode)
PY

new_status="$(awk -F': ' '/^status:/ {print $2; exit}' "$CONTROL_FILE" | tr -d '\r')"
echo "heartbeat finished with status=$new_status"
