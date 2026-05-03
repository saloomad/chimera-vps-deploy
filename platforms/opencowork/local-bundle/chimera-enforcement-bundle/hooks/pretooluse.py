import json
import os
import re
import subprocess
import sys
from pathlib import Path


PROJECT_DIR = Path(os.environ.get("CLAUDE_PROJECT_DIR", r"C:\Users\becke\claudecowork"))
LOGGER = PROJECT_DIR / "scripts" / "log_activation_receipt.py"
CONTRACT = PROJECT_DIR / ".claude" / "OBJECTIVE_CONTRACT.md"
DANGEROUS_PATTERNS = [r"\brm\s+-rf\b", r"\bgit\s+reset\b", r"\bgit\s+checkout\s+--\b"]
CONTROL_LAYER_MARKERS = [
    "agents.md",
    "claude.md",
    ".claude/settings.json",
    "opencode.json",
    ".opencode/",
    "skills/",
    "workflow",
    "continuation.md",
    "kanban.md",
    "work_log.md",
    "task_registry.md",
    "action_log.md",
]


def log_receipt(status: str, *, decision: str = "", trigger: str = "", notes: str = "") -> None:
    if not LOGGER.exists():
        return
    subprocess.run(
        [
            sys.executable,
            str(LOGGER),
            "--platform",
            "opencowork-local",
            "--surface",
            "hook",
            "--name",
            "PreToolUse",
            "--status",
            status,
            "--decision",
            decision,
            "--trigger",
            trigger,
            "--notes",
            notes,
            "--project-dir",
            str(PROJECT_DIR),
        ],
        check=False,
        capture_output=True,
        text=True,
    )


def active_contract() -> bool:
    if not CONTRACT.exists():
        return False
    text = CONTRACT.read_text(encoding="utf-8", errors="replace")
    return re.search(r"^status:\s*active\s*$", text, flags=re.IGNORECASE | re.MULTILINE) is not None


def extract_target(payload: dict) -> str:
    candidates = [
        payload.get("file_path"),
        payload.get("path"),
        payload.get("tool_input", {}).get("file_path"),
        payload.get("tool_input", {}).get("path"),
    ]
    for value in candidates:
        if isinstance(value, str) and value.strip():
            return value
    return ""


def looks_like_control_layer(path_text: str) -> bool:
    lowered = path_text.replace("\\", "/").lower()
    return any(marker in lowered for marker in CONTROL_LAYER_MARKERS)


def main() -> int:
    try:
        payload = json.load(sys.stdin)
    except Exception:
        payload = {}

    tool_name = str(payload.get("tool_name", ""))
    command = str(payload.get("tool_input", {}).get("command", ""))
    lowered = command.lower()
    for pattern in DANGEROUS_PATTERNS:
        if re.search(pattern, lowered):
            log_receipt("blocked", decision="deny", trigger="destructive_command_guard", notes=command[:160])
            out = {
                "hookSpecificOutput": {
                    "hookEventName": "PreToolUse",
                    "permissionDecision": "deny",
                    "permissionDecisionReason": "Blocked a destructive command. Use a safer, reversible path.",
                }
            }
            print(json.dumps(out))
            return 0

    target = extract_target(payload)
    if target and looks_like_control_layer(target):
        log_receipt("activated", trigger="control_layer_change", notes=f"Control-layer pre-tool guard ran for {target[:160]}.")
        out = {
            "hookSpecificOutput": {
                "hookEventName": "PreToolUse",
                "additionalContext": (
                    "This looks like a control-layer edit. Use critical-change-guard, "
                    "critical-config-instruction-and-compaction-guard-loop.md, and codex-continuity-enforcer. "
                    "Keep backup, rollback, proof, and continuity explicit."
                ),
            }
        }
        print(json.dumps(out))
        return 0

    context = "Before mutating work, keep the workflow, proof path, and dependent updates explicit."
    if active_contract():
        context = (
            "An active objective contract exists. Before and after this mutating step, keep the workflow, proof path, "
            "dependent updates, and review state explicit."
        )

    log_receipt("activated", trigger=tool_name.lower(), notes=f"Pre-tool guard ran for {tool_name}.")
    out = {
        "hookSpecificOutput": {
            "hookEventName": "PreToolUse",
            "additionalContext": context,
        }
    }
    print(json.dumps(out))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
