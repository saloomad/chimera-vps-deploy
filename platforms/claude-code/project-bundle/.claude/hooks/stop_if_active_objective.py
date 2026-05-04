import json
import re
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
        return ""
    return CONTRACT_PATH.read_text(encoding="utf-8", errors="replace")


def coordination_current() -> tuple[bool, str]:
    if not CONTRACT_PATH.exists() or not GUARD_PATH.exists():
        return True, ""
    try:
        result = subprocess.run(
            [
                sys.executable,
                str(GUARD_PATH),
                "validate-platform",
                "--coordination-root",
                str(COORDINATION_ROOT),
                "--platform",
                "windows-claude",
                "--contract",
                str(CONTRACT_PATH),
            ],
            check=False,
            capture_output=True,
            text=True,
        )
    except Exception as exc:
        return False, f"Could not run shared coordination validation: {exc}"
    payload = (result.stdout or "").strip()
    return result.returncode == 0, payload[:2000]


def main() -> int:
    text = read_contract()
    active = re.search(r"^status:\s*active\s*$", text, flags=re.IGNORECASE | re.MULTILINE) is not None
    coordination_ok, coordination_payload = coordination_current()

    if (not active) and coordination_ok:
        log_receipt(
            "Stop",
            "passed",
            decision="allow",
            trigger="no_active_objective",
            notes="Stop hook allowed closeout because no active objective contract remained.",
        )
        return 0

    log_receipt(
        "Stop",
        "blocked",
        decision="deny",
        trigger="active_objective_guard" if active else "stale_shared_coordination_guard",
        notes="Stop hook blocked closeout because the objective is still active or shared coordination is stale.",
    )
    reasons = []
    if active:
        reasons.append(
            "The objective contract is still marked active. Run the review step, make the review outcome explicit as complete, iterate, or blocked, and update the contract first."
        )
    if not coordination_ok:
        reasons.append(
            "Shared coordination is stale relative to the objective contract. Update `session-states/windows-claude.yaml` and `publish-queue/windows-claude.yaml` before stopping."
        )
        if coordination_payload:
            reasons.append("Guard output: " + coordination_payload)
    out = {
        "decision": "block",
        "reason": " ".join(reasons),
    }
    print(json.dumps(out))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
