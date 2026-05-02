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
HEARTBEAT_TIMEOUT_SEC="${HEARTBEAT_TIMEOUT_SEC:-420}"

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

python3 - "$KIMI_BIN" "$KIMI_HOME" "$PROMPT_TEMPLATE" "$log_file" "$CONTROL_FILE" "$HEARTBEAT_TIMEOUT_SEC" <<'PY'
import pathlib
import re
import subprocess
import sys
import time

kimi_bin = pathlib.Path(sys.argv[1])
kimi_home = pathlib.Path(sys.argv[2])
prompt_template = pathlib.Path(sys.argv[3])
log_file = pathlib.Path(sys.argv[4])
control_file = pathlib.Path(sys.argv[5])
timeout_sec = int(sys.argv[6])
status_close_grace_sec = 5

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

def normalize_review_outcome() -> None:
    if not control_file.exists():
        return
    text = control_file.read_text(encoding="utf-8", errors="replace")
    status_match = re.search(r"^status:\s*(.+?)\s*$", text, flags=re.MULTILINE)
    review_match = re.search(r"^last_review_outcome:\s*(.+?)\s*$", text, flags=re.MULTILINE)
    status = status_match.group(1).strip().lower() if status_match else ""
    review = review_match.group(1).strip().lower() if review_match else ""

    normalized = None
    if status == "active" and review not in {"iterate", "blocked"}:
        normalized = "iterate"
    elif status == "complete" and review != "complete":
        normalized = "complete"
    elif status == "blocked" and review != "blocked":
        normalized = "blocked"

    if normalized is None:
        return

    if review_match:
        text = re.sub(
            r"^last_review_outcome:\s*.*$",
            f"last_review_outcome: {normalized}",
            text,
            count=1,
            flags=re.MULTILINE,
        )
    else:
        text = text.rstrip() + f"\nlast_review_outcome: {normalized}\n"

    note = f"- Runner normalization: forced last_review_outcome to `{normalized}` to match status `{status}`.\n"
    if "## Notes" in text:
        text = text.rstrip() + "\n" + note
    else:
        text = text.rstrip() + "\n\n## Notes\n\n" + note

    control_file.write_text(text, encoding="utf-8")


def read_control_status() -> str:
    if not control_file.exists():
        return ""
    text = control_file.read_text(encoding="utf-8", errors="replace")
    status_match = re.search(r"^status:\s*(.+?)\s*$", text, flags=re.MULTILINE)
    return status_match.group(1).strip().lower() if status_match else ""

proc = subprocess.Popen(cmd, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
started = time.monotonic()
close_detected_at = None
close_note = ""

while True:
    try:
        stdout, stderr = proc.communicate(timeout=1)
        break
    except subprocess.TimeoutExpired:
        elapsed = time.monotonic() - started
        if elapsed >= timeout_sec:
            proc.kill()
            stdout, stderr = proc.communicate()
            combined = (stdout or "") + ("\n" + stderr if stderr else "")
            log_file.write_text((combined.strip() + "\nheartbeat timed out\n").strip() + "\n", encoding="utf-8")
            sys.stdout.write(combined)
            sys.stderr.write(f"\nheartbeat timed out after {timeout_sec}s\n")
            raise SystemExit(124)

        current_status = read_control_status()
        if current_status in {"complete", "blocked"}:
            if close_detected_at is None:
                close_detected_at = time.monotonic()
            elif time.monotonic() - close_detected_at >= status_close_grace_sec:
                proc.terminate()
                try:
                    stdout, stderr = proc.communicate(timeout=10)
                except subprocess.TimeoutExpired:
                    proc.kill()
                    stdout, stderr = proc.communicate()
                close_note = f"\nheartbeat runner stopped Kimi after control file reached status={current_status}\n"
                break
        else:
            close_detected_at = None

combined = (stdout or "") + ("\n" + stderr if stderr else "") + close_note
log_file.write_text(combined.strip() + "\n", encoding="utf-8")
sys.stdout.write(combined)
normalize_review_outcome()
if close_note:
    raise SystemExit(0)
raise SystemExit(proc.returncode)
PY

new_status="$(awk -F': ' '/^status:/ {print $2; exit}' "$CONTROL_FILE" | tr -d '\r')"
echo "heartbeat finished with status=$new_status"
