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
            "choose the model-routing lane honestly for planning, execution, review, or fast mechanical work, "
            "and if the current session model does not match the preferred lane, say that plainly instead of pretending it auto-switched, "
            "and before meaningful task intake read the shared `handoffs/`, `session-states/`, and `publish-queue/` surfaces, "
            "using `chimera-vps-deploy/scripts/github_coordination_guard.py startup-summary` when available, "
            "and load the shared skills `github-coordination-gate`, `task-transition-publish`, `platform-live-repo-router`, and `task-change-readiness-gate` when shared publish or repo routing matters, "
            "and if the prompt is about cron, recurring jobs, scheduled tasks, crontab, timers, or automation drift, load cron-doctor for diagnosis and cron-worker-guardrails for safe job design, "
            "treat cron-scheduler as reference-only unless there is explicit approval for scheduler mutation, "
            "state the workflow and enforcement surface plainly, keep the receipt path visible, "
            "include one short carry-forward block with objective status, unapproved items, and remaining work, "
            "and give each open item a brief plain-English description, "
            "and if the work edits instructions, config, hooks, skills, workflows, detectors, or compaction behavior, "
            "route through critical-change-guard and the critical control-layer workflow, "
            "and if another meaningful task is starting before the current one is publish-ready, update the shared session-state and publish-queue files first and run `task-change-readiness-gate` before allowing the switch."
        ),
        }
    }
    print(json.dumps(out))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
