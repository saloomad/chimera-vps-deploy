---
name: codex-skill-opportunity-detector
description: Detect when repeated work, repeated failure, or a risky multi-step process should become a reusable skill or workflow, then create or update the artifact instead of leaving it in chat.
triggers:
  - this should be a skill
  - create a skill
  - repeated failure
  - repeated task
  - make this reusable
  - capture this pattern
  - this keeps happening
---

# Codex Skill Opportunity Detector

Use this skill when a session reveals a pattern that should stop relying on memory.

## Auto Trigger Rules

Create or update a reusable artifact when any of these are true:

1. the same failure happened twice
2. the same manual task happened three times
3. a risky procedure has more than five steps
4. the same explanation is being repeated
5. a rule is important enough that forgetting it would create real damage

## Read First

- `C:\Users\becke\.codex\skills\workflow-skill-capture\SKILL.md`
- `docs/WORKFLOW_AND_SKILL_CAPTURE_POLICY.md`
- `tasks/TASK_REGISTRY.md`
- `trace/ACTION_LOG.md`
- `harnesses/codex/chimera/memory/LESSONS.md`
- `workflows/codex/reusable-pattern-capture.md`
- `C:\Users\becke\claudecowork\workflows\codex\WORKFLOW_CATALOG.md`

## Decide What To Create

- Create or update a `skill` when the agent should apply the behavior directly
- Create or update a `workflow` when the team needs a repeatable step sequence
- Create both when the pattern is important for both people and agents
- Do nothing only if the pattern is clearly one-off

Promotion rule:

- create a `workflow` when order matters
- create a `skill` when the agent should apply the behavior directly
- create both when the pattern is high importance, recurring, and cross-platform
- mirror into `chimera-vps-deploy` when the pattern matters outside local Codex

## Write Targets

When this triggers, write to the smallest useful set of:

- `.claude/skills/<new-skill-name>/SKILL.md`
- `workflows/codex/`
- `docs/`
- `tasks/TASK_REGISTRY.md`
- `trace/ACTION_LOG.md`
- `harnesses/codex/chimera/CONTINUATION.md`
- `harnesses/codex/chimera/KANBAN.md`
- `harnesses/codex/chimera/WORK_LOG.md`
- `harnesses/codex/chimera/memory/LESSONS.md`
- `chimera-vps-deploy/skills/`
- `chimera-vps-deploy/workflows/codex/`

## Minimum Output

For each captured pattern, leave behind:

1. the trigger
2. the read inputs
3. the expected output
4. where the new artifact lives
5. what future sessions should do differently
6. whether the pattern should be shared cross-platform
