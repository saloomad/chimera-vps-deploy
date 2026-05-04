import json
import re
import sys
from pathlib import Path

from receipt_logger import log_receipt


PROJECT_DIR = Path(__file__).resolve().parents[2]
CONTRACT_PATH = PROJECT_DIR / ".claude" / "OBJECTIVE_CONTRACT.md"
CONTROL_LAYER_MARKERS = [
    "agents.md",
    "claude.md",
    "opencode.json",
    ".opencode",
    ".claude/hooks",
    "\\skills\\",
    "/skills/",
    "\\workflows\\",
    "/workflows/",
]


def payload_text(payload: dict) -> str:
    try:
        return json.dumps(payload.get("tool_input", {}), ensure_ascii=False).lower()
    except Exception:
        return str(payload.get("tool_input", "")).lower()


def contract_active() -> bool:
    if not CONTRACT_PATH.exists():
        return False
    text = CONTRACT_PATH.read_text(encoding="utf-8", errors="replace")
    return re.search(r"^status:\s*active\s*$", text, flags=re.IGNORECASE | re.MULTILINE) is not None


def main() -> int:
    try:
        payload = json.load(sys.stdin)
    except Exception:
        payload = {}

    if not contract_active():
        return 0

    tool_name = str(payload.get("tool_name", ""))
    trigger = "control_layer_followup" if any(marker in payload_text(payload) for marker in CONTROL_LAYER_MARKERS) else tool_name.lower()
    log_receipt(
        "PostToolUse",
        "activated",
        trigger=trigger,
        notes="Post-tool proof reminder ran while an objective contract was active.",
    )

    extra = ""
    if trigger == "control_layer_followup":
        extra = (
            " Because this touched the control layer, also review whether the workflow catalog, enforcement inventory, "
            "platform registry, or shared mirrors need updates, and whether a detector or learning skill should run."
        )

    out = {
        "hookSpecificOutput": {
            "hookEventName": "PostToolUse",
            "additionalContext": (
                "An active objective contract exists. After this tool step, update `.claude/OBJECTIVE_CONTRACT.md` "
                "with current_slice, last_proof, current_phase, next_step, review_outcome, unapproved_items, and "
                "remaining_work. Keep unapproved_items and remaining_work as short aggregated lists with plain-English "
                "descriptions, and carry them into the next meaningful reply. Make test or proof explicit if the tool "
                "changed the system. If the bounded slice moved or another task is about to start, also update "
                "`session-states/windows-claude.yaml`, and update `publish-queue/windows-claude.yaml` whenever the "
                "code is still not publish-ready." + extra
            ),
        }
    }
    print(json.dumps(out))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
