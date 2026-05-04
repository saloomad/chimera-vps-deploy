---
name: codex-continuity-enforcer
description: Force Codex to update continuation, kanban, work log, memory, and lessons after meaningful work so future sessions can resume from files instead of chat.
triggers:
  - update continuation
  - save continuity
  - before ending
  - close out the work
  - keep this for next session
---

# Codex Continuity Enforcer

Use this skill after every meaningful implementation, audit, decision, or task-state change.

Also use it before and after compaction, session split, or other context-loss boundaries when the current objective would be hard to resume from chat alone.

## Read First

- `harnesses/codex/chimera/CONTINUATION.md`
- `harnesses/codex/chimera/KANBAN.md`
- `harnesses/codex/chimera/WORK_LOG.md`
- `harnesses/codex/chimera/memory/MEMORY.md`
- `harnesses/codex/chimera/memory/LESSONS.md`
- `workflows/codex/task-and-continuity-closeout.md`

## Write Targets

Always update the smallest truthful set of:

- `harnesses/codex/chimera/CONTINUATION.md`
- `harnesses/codex/chimera/KANBAN.md`
- `harnesses/codex/chimera/WORK_LOG.md`
- `harnesses/codex/chimera/memory/MEMORY.md`
- `harnesses/codex/chimera/memory/LESSONS.md`
- `tasks/TASK_REGISTRY.md`
- `trace/ACTION_LOG.md`

## Minimum Closeout Standard

1. record what changed
2. record what is actually done
3. record what still remains
4. record the evidence path
5. record the next owner or next step

For compaction-sensitive work, also record:

6. the current objective contract
7. the current slice
8. the stop condition
9. any PM file that became the source of truth

Do not end meaningful work with only a chat summary if future sessions will need the state.
