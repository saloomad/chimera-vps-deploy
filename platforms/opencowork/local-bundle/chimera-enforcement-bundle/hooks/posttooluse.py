import json
import os
import re
import subprocess
import sys
from pathlib import Path


PROJECT_DIR = Path(os.environ.get("CLAUDE_PROJECT_DIR", r"C:\Users\becke\claudecowork"))
LOGGER = PROJECT_DIR / "scripts" / "log_activation_receipt.py"
CONTRACT = PROJECT_DIR / ".claude" / "OBJECTIVE_CONTRACT.md"


def active_contract() -> bool:
    if not CONTRACT.exists():
        return False
    text = CONTRACT.read_text(encoding="utf-8", errors="replace")
    return re.search(r"^status:\s*active\s*$", text, flags=re.IGNORECASE | re.MULTILINE) is not None


def main() -> int:
    try:
        payload = json.load(sys.stdin)
    except Exception:
        payload = {}

    if LOGGER.exists():
        subprocess.run(
            [
                sys.executable,
                str(LOGGER),
                "--platform",
                "opencowork-local",
                "--surface",
                "hook",
                "--name",
                "PostToolUse",
                "--status",
                "activated",
                "--trigger",
                str(payload.get("tool_name", "")).lower(),
                "--notes",
                "OpenCowork post-tool reminder ran.",
                "--project-dir",
                str(PROJECT_DIR),
            ],
            check=False,
            capture_output=True,
            text=True,
        )

    context = "After a meaningful tool step, make proof, dependent updates, and next action explicit."
    if active_contract():
        context = (
            "An active objective contract exists. After this tool step, update proof, dependent surfaces, "
            "current phase, next step, and review state explicitly."
        )
    out = {"hookSpecificOutput": {"hookEventName": "PostToolUse", "additionalContext": context}}
    print(json.dumps(out))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
