import json
import sys

from receipt_logger import log_receipt


CONTEXT = """Orchestration precheck is required for this prompt.

Before answering any meaningful request:
- choose one orchestration decision: direct response, light orchestration, bounded build, deep research swarm, or always-on pipeline
- choose the model-routing lane too: planning, execution, review, research, or fast mechanical
- load `sal-communication-contract` and `response-structure-enforcer` for any reply that is more than tiny
- if the current session model does not match the preferred lane, say that plainly instead of pretending it auto-switched
- say why that route fits better than the main alternatives
- say what the ultimate objective is
- say what the current bounded slice is
- say what the done contract is
- say which phase you are in: plan, execute, test or proof, review, or mixed
- include one short carry-forward block with objective status, unapproved items, and remaining work
- carry forward still-relevant open items from prior conversations when they belong to the same project objective; do not limit the block to the current thread only
- organize the block by project objective when more than one objective is still open
- when items are open, give each one a brief plain-English description of what it is and why it still matters

If the prompt looks like continuation, resume, transcript follow-up, or handoff follow-up:
- load `agent-session-resume`
- reconstruct the stopping point before acting
- read the newest `handoffs/` entry plus every file in `session-states/` and `publish-queue/`

If the prompt is non-trivial:
- load `codex-runtime-router`
- check `model-registry` before making model or routing claims
- use `scripts/github_coordination_guard.py startup-summary` as the shared front door when available
- load `github-coordination-gate`, `task-transition-publish`, `platform-live-repo-router`, and `task-change-readiness-gate` when shared publish or repo routing matters

If the task is multi-step or needs follow-through:
- create or update `.claude/OBJECTIVE_CONTRACT.md`
- set `status: active`
- keep `current_phase`, `last_proof`, `next_step`, `review_outcome`, `unapproved_items`, and `remaining_work` current
- keep the shared coordination files current too:
  - `session-states/windows-claude.yaml`
  - `publish-queue/windows-claude.yaml` when the code is not publish-ready
- use `complete` only when the ultimate objective is done
- if a slice lands but the larger mission remains open, record `iterate`
- iterate until the ultimate objective is complete or blocked

If the prompt is switching to another meaningful task while the current one is not fully done:
- do not rely on continuous-session memory
- publish the shared state before changing tasks
- run `task-change-readiness-gate` before deciding the task switch is allowed
- use one of these shared publish statuses:
  - `published-ready`
  - `in-progress-not-ready`
  - `blocked-needs-follow-up`

Preferred lanes:
- planning: gpt-5.5 with high or xhigh
- execution: gpt-5.4 with medium
- review: gpt-5.5 with high when judgment-heavy, otherwise gpt-5.4 with medium
- fast mechanical: gpt-5.4-mini with low

If the prompt is about cron, recurring jobs, scheduled tasks, crontab, timers, stale workers, or automation drift:
- load `cron-doctor` for diagnosis
- load `cron-worker-guardrails` for worker hardening and safe schedule design
- treat `cron-scheduler` as reference-only unless there is explicit approval for live scheduler mutation
- prefer scheduler jobs only as wake-up triggers; keep stateful logic in scripts, workflows, or Task Flow
- if the platform has both a live scheduler and a registry, state which one is the real source of truth before recommending changes

If the prompt is trivial, say the direct route was chosen and why the full loop was unnecessary.
"""


def main() -> int:
    try:
        json.load(sys.stdin)
    except Exception:
        pass

    log_receipt(
        "UserPromptSubmit",
        "activated",
        trigger="meaningful_prompt_precheck",
        notes="Added orchestration precheck context for Claude Code prompt start.",
    )

    out = {
        "hookSpecificOutput": {
            "hookEventName": "UserPromptSubmit",
            "additionalContext": CONTEXT,
        }
    }
    print(json.dumps(out))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
