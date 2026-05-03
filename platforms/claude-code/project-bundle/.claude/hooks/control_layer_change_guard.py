import json
import sys
from pathlib import Path

from receipt_logger import log_receipt


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

    target = extract_target(payload)
    event_name = str(payload.get("hook_event_name") or payload.get("event_name") or "FileChanged")
    if not ((target and looks_like_control_layer(target)) or payload_mentions_control_layer(payload)):
        log_receipt(
            event_name,
            "passed",
            trigger="non_control_layer_change",
            notes="Control-layer guard saw a non-control-layer change and allowed it through.",
        )
        return 0

    pretty_name = Path(target).name or target
    log_receipt(
        event_name,
        "activated",
        trigger="control_layer_change",
        notes=f"Control-layer change detected for {pretty_name}.",
    )
    out = {
        "hookSpecificOutput": {
            "hookEventName": event_name,
            "additionalContext": (
                f"'{pretty_name}' looks like a control-layer file. Use critical-change-guard, "
                "critical-config-instruction-and-compaction-guard-loop.md, and codex-continuity-enforcer. "
                "Do not treat this like a normal edit: keep backup, rollback, proof, and continuity explicit."
            ),
        }
    }
    print(json.dumps(out))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
