# CHECKPOINT - 2026-05-08 Orchestration Successor Heartbeat Rule

## What changed

- Hardened the orchestration stop logic again after a real regression:
  - a stale narrower heartbeat had been deleted even though the broader same-objective improvement backlog was still open
- Updated the source-of-truth orchestration skill:
  - `C:\Users\becke\.codex\skills\objective-orchestration-loop\SKILL.md`
- Added a new explicit rule:
  - `Stale Sub-Objective Heartbeat Rule`
- Updated the workflow layer:
  - `workflows/codex/openclaw-role-orchestration-loop.md`
- Updated the deterministic policy layer:
  - `scripts/orchestration_policy.py`
- Updated deterministic proof:
  - `scripts/tests/orchestration_policy_matrix.py`
- Logged the regression durably in:
  - `chimera-vps-deploy/handoffs/ORCHESTRATION_ISSUES.md`

## New rule in plain English

If a heartbeat is stale because it is scoped to an older narrower slice, but the broader same-objective work is still open:

1. do not delete it as cleanup
2. first retarget that heartbeat, or create a successor heartbeat in the same pass
3. only retire the stale heartbeat after the replacement continuation owner is live

Deleting a stale narrower heartbeat without a same-pass successor now counts as an orchestration miss.

## Proof

- local deterministic policy matrix:
  - `python scripts/tests/orchestration_policy_matrix.py`
  - result: `PASS`
- skill validation:
  - `python -X utf8 C:\Users\becke\.codex\skills\.system\skill-creator\scripts\quick_validate.py C:\Users\becke\.codex\skills\objective-orchestration-loop`
  - result: `Skill is valid!`
- current-thread continuation owner restored:
  - heartbeat id: `thread-objective-completion-guard-5`
  - cadence: `10` minutes
  - scope: broader same-objective orchestration-improvement work, not the older narrower stop-rule slice

## Git evidence

- current branch:
  - `add-remaining-files`
- branch divergence from `origin/main...HEAD`:
  - behind `10`
  - ahead `61`

## Still open

- keep proving on future real sessions that stale heartbeat prompts are retargeted instead of deleted
- mirror the new stale-heartbeat successor rule into the top-level instruction surfaces that operators read before the skill body
- the repo still is not back on the user's `main-first` publication rule
