---
name: codex-task-and-project-capture
description: Detect new work, new follow-ups, new blockers, or new projects and write them into the task registry, job board, and kanban instead of leaving them only in chat.
triggers:
  - add this to tasks
  - make a task
  - new project
  - backlog this
  - capture this follow-up
  - there is still work left
---

# Codex Task And Project Capture

Use this skill whenever the conversation creates real work that should survive the session.

## Auto Trigger Rules

Run this skill when:

1. the user asks for something new that is more than a one-line answer
2. a new blocker or follow-up appears
3. a comparison reveals a missing implementation step
4. a repeated theme should become a tracked project
5. a new task is needed to close a real gap safely later

## Read First

- `projects/PROJECT_REGISTRY.md`
- `tasks/TASK_REGISTRY.md`
- `tasks/JOB_BOARD.md`
- `harnesses/codex/chimera/KANBAN.md`
- `harnesses/codex/chimera/PROJECT_CARD.md`

## Write Targets

- `projects/PROJECT_REGISTRY.md` when a new project is needed
- `tasks/TASK_REGISTRY.md` for new or updated tasks
- `tasks/JOB_BOARD.md` when routing/ownership changes
- `harnesses/codex/chimera/KANBAN.md`
- `trace/ACTION_LOG.md` if the capture itself is a meaningful project-management action

## Capture Standard

Each task or project entry should define:

1. owner
2. objective
3. done criteria
4. dependencies
5. consumers
6. next step

Do not leave a meaningful follow-up only in chat if it should survive the session.

