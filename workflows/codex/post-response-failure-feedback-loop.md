# Post Response And Failure Feedback Loop

Use this workflow after:

- a confusing response
- a weak explanation
- a failed tool step
- a blocked closeout
- a repeated user correction
- a report that was not good enough
- a subagent result that did not meet the slice objective

## Loop Type

- bounded loop, then recurring review

## Purpose

Everything should have a feedback loop.

This workflow forces the system to:

- flag what went wrong
- decide whether the fix belongs in a skill, workflow, hook, runtime owner, or lesson
- write the issue down in markdown
- review it later instead of forgetting it

## Required Write Targets

- `docs/AGENT_IMPROVEMENT_BACKLOG_2026-05-03.md`
- `chimera-vps-deploy/handoffs/ORCHESTRATION_ISSUES.md` when orchestration or enforcement drift is involved
- a skill, workflow, or registry update when the issue is clearly fixable now

## Required Skills

- `vibe-coding-monitor`
- `codex-lesson-harvester`
- `codex-workflow-detector`
- `codex-skill-opportunity-detector`
- `hook-opportunity-detector`
- `pipeline-enforcement-detector` when runtime ownership is the issue

## Issue Record Format

For each issue, capture:

1. date
2. trigger
3. symptom
4. likely root cause
5. current impact
6. fix applied now
7. further fix still needed
8. which platform it belongs to
9. which skill, workflow, hook, or runtime owner should prevent it next time

## Review Rule

When meaningful work starts or a failure repeats, read the backlog first if the task touches:

- communication
- orchestration
- model routing
- resume behavior
- PM continuity
- control-layer edits
- platform parity
- trading pipeline ownership
