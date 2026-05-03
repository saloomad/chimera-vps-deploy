import json
import re
import sys
from pathlib import Path

from receipt_logger import log_receipt


PROJECT_DIR = Path(__file__).resolve().parents[2]
CONTRACT_PATH = PROJECT_DIR / ".claude" / "OBJECTIVE_CONTRACT.md"


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

    agent_name = payload.get("agent_name") or payload.get("subagent_name") or "subagent"
    log_receipt(
        "SubagentStop",
        "activated",
        trigger="subagent_review_gate",
        notes=f"Subagent review gate ran for {agent_name}.",
    )
    out = {
        "hookSpecificOutput": {
            "hookEventName": "SubagentStop",
            "additionalContext": (
                f"{agent_name} finished. Do not accept the result blindly. Check whether it actually solved the "
                "assigned slice, what files it changed, what proof or tests it produced, what risks remain, and "
                "whether the result is strong enough to move the objective forward. Before deciding complete, "
                "iterate, or blocked, update `.claude/OBJECTIVE_CONTRACT.md`. If the subagent exposed a repeated "
                "pattern, missing workflow, missing skill, missing hook, or reusable lesson, load "
                "`codex-workflow-detector`, `codex-skill-opportunity-detector`, `hook-opportunity-detector`, "
                "`pipeline-enforcement-detector` when runtime ownership is involved, and `codex-lesson-harvester` "
                "or `cross-project-ai-lessons` when the lesson should help future projects."
            ),
        }
    }
    print(json.dumps(out))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
