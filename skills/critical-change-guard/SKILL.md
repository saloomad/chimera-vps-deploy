---
name: critical-change-guard
description: Protect critical project changes. Use before modifying high-risk logic, production workflows, orchestration, automation, trading execution, authentication, data pipelines, or shared instructions. Enforces backup, test planning, rollback planning, evaluation, implementation, and documentation.
triggers:
  - critical change
  - risky change
  - before we change this
  - production change
  - orchestration change
  - pipeline change
  - backup and test
  - rollback plan
---

# Critical Change Guard

Use this skill before making changes that could break real project behavior.

## Critical Change Definition

Treat a change as critical if it touches:
- execution logic
- orchestration or automation
- production cron or heartbeat behavior
- authentication, secrets, or permissions
- shared prompts, instructions, or agent behavior
- startup docs, continuation rules, or compaction governance
- hook configs, plugin configs, or project configs
- skills, workflows, detectors, or PM truth surfaces
- schemas, data migration, or irreversible file changes
- systemwide dependencies

Examples of risky control-layer files:

- `AGENTS.md`
- `CLAUDE.md`
- `.claude/settings.json`
- `opencode.json`
- `.opencode/*`
- local plugin registry or bundle files
- skill `SKILL.md` files
- workflow files
- task, continuation, kanban, work-log, action-log, or PM front-door files

## Required Pre-Flight

Before implementation:

1. Define the objective
2. Define the risk
3. Identify affected files and systems
4. Decide how to back up current state
5. Decide how to test before and after
6. Define rollback steps
7. Define success criteria
8. Decide which continuity or PM surfaces must be updated if the change lands
9. Decide whether compaction or session split could hide important state

## Backup Rules

At minimum, preserve one of:
- git state or branch checkpoint
- file backup or copied config
- exported current config or report snapshot
- command history needed to restore prior behavior

Do not make irreversible changes without a recovery path.

## Test Planning Rules

Plan tests before implementation:
- unit checks for changed logic when practical
- integration check for the main path
- smoke test for system startup or main workflow
- explicit manual verification if automation is not enough

If a test cannot be run, say that clearly and reduce change scope if needed.

## Implementation Rules

When possible:
- change one risk area at a time
- avoid combining unrelated refactors with critical fixes
- verify immediately after each risky step

For control-layer changes, also use:

- `critical-config-instruction-and-compaction-guard-loop.md`
- `codex-continuity-enforcer`

## Required Output

For a critical change, report:

1. Objective
2. Risks
3. Backup method
4. Test plan
5. Rollback plan
6. What changed
7. Verification result
8. Remaining risk
9. Continuity or PM surfaces updated
