---
name: codex-lesson-harvester
description: Detect bugs, blockers, recoveries, and repeated judgment mistakes that should become durable lessons for future sessions and future projects.
triggers:
  - what did we learn
  - capture the lesson
  - do not repeat this
  - root cause
  - failure pattern
  - remember this next time
---

# Codex Lesson Harvester

Use this skill when something failed, was fixed, or taught us a reusable rule.

## Auto Trigger Rules

Run this skill when:

1. a fix required root-cause investigation
2. a test exposed a real failure mode
3. a comparison showed one pattern is better than another
4. a recovery depended on a subtle rule
5. a repeated frustration should become a lesson instead of a future repeat
6. `SubagentStop` or `Stop` exposed a reusable review or closeout rule

## Read First

- `trace/ACTION_LOG.md`
- `harnesses/codex/chimera/memory/MEMORY.md`
- `harnesses/codex/chimera/memory/LESSONS.md`
- `docs/`

## Write Targets

- `harnesses/codex/chimera/memory/MEMORY.md` for stable facts and decisions
- `harnesses/codex/chimera/memory/LESSONS.md` for mistakes, recoveries, and better behaviors
- `docs/` when a lesson deserves a dedicated report or playbook
- `tasks/TASK_REGISTRY.md` if the lesson reveals unfinished work

## Lesson Format

Each lesson should say:

1. what happened
2. why it happened
3. what better behavior looks like
4. what evidence supports the lesson
5. where in the workflow or hook chain the lesson should be enforced next time

## Repeated Communication Failure Rule

If the user is frustrated because the answer pointed at files instead of explaining them:

1. capture that as a lesson immediately
2. update the instruction layer if this is a repeated pattern
3. summarize the artifact contents in plain English in the next reply
4. treat file paths as evidence only, not as the explanation itself
5. if orchestration or simulation was claimed, say plainly whether it really ran or whether only scaffolding exists
