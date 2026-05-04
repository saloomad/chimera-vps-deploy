import json
import subprocess
import sys
from pathlib import Path

from receipt_logger import log_receipt


PROJECT_DIR = Path(__file__).resolve().parents[2]
CONTRACT_PATH = PROJECT_DIR / ".claude" / "OBJECTIVE_CONTRACT.md"
COORDINATION_ROOT = Path(__file__).resolve().parents[5]
GUARD_PATH = COORDINATION_ROOT / "scripts" / "github_coordination_guard.py"


def read_contract() -> str:
    if not CONTRACT_PATH.exists():
        return "No objective contract file found yet. For meaningful multi-step work, create or update `.claude/OBJECTIVE_CONTRACT.md`, including unapproved_items and remaining_work."
    text = CONTRACT_PATH.read_text(encoding="utf-8", errors="replace").strip()
    if not text:
        return "Objective contract file exists but is empty."
    return "Current objective contract:\n\n" + text[:3000]


def read_coordination_summary() -> str:
    if not GUARD_PATH.exists():
        return (
            "Shared coordination guard not found. Read `handoffs/`, `session-states/`, and `publish-queue/` in the "
            "shared Chimera repo before meaningful work."
        )
    try:
        result = subprocess.run(
            [
                sys.executable,
                str(GUARD_PATH),
                "startup-summary",
                "--coordination-root",
                str(COORDINATION_ROOT),
            ],
            check=False,
            capture_output=True,
            text=True,
        )
    except Exception:
        return (
            "Could not run the shared coordination guard. Manually read `handoffs/`, `session-states/`, and "
            "`publish-queue/` before meaningful work."
        )
    summary = result.stdout.strip() or "No summary produced."
    return "Shared coordination summary:\n\n" + summary[:3000]


def main() -> int:
    log_receipt(
        "SessionStart",
        "activated",
        trigger="session_context_load",
        notes="Loaded objective contract context at session start.",
    )
    out = {
        "hookSpecificOutput": {
            "hookEventName": "SessionStart",
            "additionalContext": read_contract()
            + "\n\n"
            + read_coordination_summary()
            + "\n\nCarry forward a short visible block in meaningful replies that shows objective status, unapproved items, and remaining work with brief plain-English descriptions. Accumulate still-relevant open items from prior conversations when they belong to the same project objective, organize them by project objective when needed, and do not limit that block to the current thread only."
            + "\n\nAlso run model routing honestly: planning usually wants gpt-5.5 high, execution usually wants gpt-5.4 medium, and review should pick the stronger judgment lane when needed. If the current session is on the wrong lane, say so plainly instead of pretending it auto-switched."
            + "\n\nFor meaningful replies, load `sal-communication-contract` and `response-structure-enforcer`. If the session is a continuation of prior work, load `agent-session-resume` before acting."
            + "\n\nBefore another meaningful task starts, update `session-states/windows-claude.yaml`. If code is not ready to publish, also update `publish-queue/windows-claude.yaml`.",
        }
    }
    print(json.dumps(out))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
