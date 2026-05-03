import json
import os
import subprocess
import sys
from pathlib import Path


PROJECT_DIR = Path(os.environ.get("CLAUDE_PROJECT_DIR", r"C:\Users\becke\claudecowork"))
LOGGER = PROJECT_DIR / "scripts" / "log_activation_receipt.py"


def log_receipt() -> None:
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
            "UserPromptSubmit",
            "--status",
            "activated",
            "--trigger",
            "meaningful_prompt_precheck",
            "--notes",
            "OpenCowork local enforcement prompt-start hook ran.",
            "--project-dir",
            str(PROJECT_DIR),
        ],
        check=False,
        capture_output=True,
        text=True,
    )


def main() -> int:
    try:
        json.load(sys.stdin)
    except Exception:
        pass
    log_receipt()
    out = {
        "hookSpecificOutput": {
            "hookEventName": "UserPromptSubmit",
            "additionalContext": (
                "Run the orchestration precheck, use the shared starter stack for meaningful work, "
                "state the workflow and enforcement surface plainly, keep the receipt path visible, "
                "and if the work edits instructions, config, hooks, skills, workflows, detectors, or compaction behavior, "
                "route through critical-change-guard and the critical control-layer workflow."
            ),
        }
    }
    print(json.dumps(out))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
