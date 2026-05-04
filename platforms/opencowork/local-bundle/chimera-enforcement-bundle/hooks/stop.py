import json
import os
import re
import subprocess
import sys
from pathlib import Path


PROJECT_DIR = Path(os.environ.get("CLAUDE_PROJECT_DIR", r"C:\Users\becke\claudecowork"))
LOGGER = PROJECT_DIR / "scripts" / "log_activation_receipt.py"
CONTRACT = PROJECT_DIR / ".claude" / "OBJECTIVE_CONTRACT.md"
COORDINATION_ROOT = PROJECT_DIR / "chimera-vps-deploy"
GUARD = COORDINATION_ROOT / "scripts" / "github_coordination_guard.py"


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
            "Stop",
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


def coordination_current() -> tuple[bool, str]:
    if not CONTRACT.exists() or not GUARD.exists():
        return True, ""
    try:
        result = subprocess.run(
            [
                sys.executable,
                str(GUARD),
                "validate-platform",
                "--coordination-root",
                str(COORDINATION_ROOT),
                "--platform",
                "opencowork-local",
                "--contract",
                str(CONTRACT),
            ],
            check=False,
            capture_output=True,
            text=True,
        )
    except Exception as exc:
        return False, f"Could not run shared coordination validation: {exc}"
    return result.returncode == 0, (result.stdout or "").strip()[:2000]


def main() -> int:
    try:
        json.load(sys.stdin)
    except Exception:
        pass

    active = active_contract()
    coordination_ok, coordination_payload = coordination_current()

    if (not active) and coordination_ok:
        log_receipt("passed", decision="allow", trigger="no_active_objective", notes="Stop allowed.")
        return 0

    log_receipt(
        "blocked",
        decision="deny",
        trigger="active_objective_guard" if active else "stale_shared_coordination_guard",
        notes="Stop blocked while the objective is active or shared coordination is stale.",
    )
    reasons = []
    if active:
        reasons.append(
            "The objective contract is still active. Review it, update proof, review state, unapproved items, and remaining work, then mark it complete, iterate, or blocked honestly."
        )
    if not coordination_ok:
        reasons.append(
            "Shared coordination is stale. Update `chimera-vps-deploy/session-states/opencowork-local.yaml` and `chimera-vps-deploy/publish-queue/opencowork-local.yaml` before stopping."
        )
        if coordination_payload:
            reasons.append("Guard output: " + coordination_payload)
    print(
        json.dumps(
            {
                "decision": "block",
                "reason": " ".join(reasons),
            }
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
