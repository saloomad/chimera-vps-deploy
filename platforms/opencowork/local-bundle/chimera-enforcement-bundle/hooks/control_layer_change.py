import json
import os
import subprocess
import sys
from pathlib import Path


PROJECT_DIR = Path(os.environ.get("CLAUDE_PROJECT_DIR", r"C:\Users\becke\claudecowork"))
LOGGER = PROJECT_DIR / "scripts" / "log_activation_receipt.py"
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


def log_receipt(status: str, *, trigger: str, notes: str) -> None:
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
            "FileChanged",
            "--status",
            status,
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


def payload_mentions_control_layer(payload: dict) -> bool:
    try:
        blob = json.dumps(payload).replace("\\", "/").lower()
    except Exception:
        return False
    return any(marker in blob for marker in CONTROL_LAYER_MARKERS)


def main() -> int:
    try:
        payload = json.load(sys.stdin)
    except Exception:
        payload = {}

    event_name = str(payload.get("hook_event_name") or payload.get("event_name") or "FileChanged")
    target = extract_target(payload)
    if not ((target and looks_like_control_layer(target)) or payload_mentions_control_layer(payload)):
        log_receipt("passed", trigger="non_control_layer_change", notes="OpenCowork control-layer guard allowed a non-control-layer change.")
        return 0

    pretty_name = Path(target).name or target or "control-layer file"
    log_receipt("activated", trigger="control_layer_change", notes=f"OpenCowork control-layer guard ran for {pretty_name}.")
    out = {
        "hookSpecificOutput": {
            "hookEventName": event_name,
            "additionalContext": (
                f"'{pretty_name}' looks like a control-layer file. Use critical-change-guard, "
                "critical-config-instruction-and-compaction-guard-loop.md, and codex-continuity-enforcer. "
                "Keep backup, rollback, proof, and continuity explicit."
            ),
        }
    }
    print(json.dumps(out))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
