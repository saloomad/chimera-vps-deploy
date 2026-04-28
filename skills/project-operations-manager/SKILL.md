---
name: project-operations-manager
description: Front-door project management skill for this workspace. Use when the team needs one place to check project state, update delivery tracking, choose the right project-management sub-skill or workflow, monitor whether work is still healthy, or decide what to do next based on the current situation.
triggers:
  - project management
  - check all projects
  - update project status
  - what should we work on next
  - delivery journal
  - update tasks and projects
  - check progress
  - monitor the project
  - what is still open
  - keep the project organized
---

# Project Operations Manager

Use this as the project-management front door when the work is about:

- checking overall project state
- updating tasks, project status, or continuity
- deciding which existing project-management skill or workflow to use
- monitoring whether delivery/reporting is healthy
- turning "what do we do now?" into a real tracked next step

This skill does not replace the existing specialist skills.
It decides which ones to use, in what order, and which files must be updated.

## What This Skill Is For

Plain English:

- `DELIVERY_JOURNAL.md` is the readable front door for humans
- the registries and logs behind it are the canonical truth
- this skill reads the situation, chooses the right project-management path, and makes sure updates land in the right places

## Read First

Always start with:

- `DELIVERY_JOURNAL.md`
- `reports/auto/DELIVERY_JOURNAL_STATUS.json`
- `projects/PROJECT_REGISTRY.md`
- `tasks/TASK_REGISTRY.md`
- `trace/ACTION_LOG.md`
- `harnesses/codex/chimera/KANBAN.md`

If the request also depends on live OpenClaw reminder truth, read these too when they exist:

- live `projects/PROJECT_REMINDERS.md`
- live `reports/auto/PROJECT_REMINDERS_STATUS.json`

If the request is about continuity across sessions, also read:

- `harnesses/codex/chimera/CONTINUATION.md`
- `harnesses/codex/chimera/WORK_LOG.md`
- `harnesses/codex/chimera/memory/MEMORY.md`
- `harnesses/codex/chimera/memory/LESSONS.md`

## Situation Classifier

After reading the front door, classify the request into one or more of these situations:

1. `status_check`
- User wants to know what is active, done, blocked, drifting, or next.

2. `capture_or_update`
- New work, a new blocker, a new follow-up, or a changed owner/done-criteria needs to be recorded.

3. `closeout_and_continuity`
- Meaningful work finished and the durable state needs to be updated for future sessions.

4. `monitoring_or_drift`
- The user wants to know if the project system, monitors, reports, or automations are still working.

5. `governance_or_structure`
- The user wants standards, operating model, workflows, SOPs, or project setup improved.

6. `delivery_consulting`
- The user wants the real blocker, root cause, best next step, or highest-leverage fix.

## Which Existing Skill To Use

Choose the smallest matching set:

- `codex-task-and-project-capture`
  - use when work must be added or updated in tasks/projects/kanban

- `codex-continuity-enforcer`
  - use after meaningful work to update continuation, work log, memory, lessons, and related registries

- `openclaw-monitor-and-brief`
  - use for monitor/cron/report-consumer/"what is happening now?" requests

- `cross-project-governance`
  - use for standards, project operating model, harness structure, workflows, and documentation standards

- `objective-delivery-consultant`
  - use when the user needs practical consulting:
    - what is broken
    - what is blocking progress
    - what is the best next move
    - what should be fixed now

## Which Workflow To Use

Load these when relevant:

- `workflows/codex/task-and-continuity-closeout.md`
  - after meaningful work

- `workflows/codex/build-test-verify-monitor-closeout.md`
  - after larger implementation or monitoring work

- `workflows/codex/openclaw-monitoring-and-consumer-loop.md`
  - for monitoring, consumer-path, or drift questions

- `workflows/codex/major-build-council-and-delivery-loop.md`
  - for larger changes, important design decisions, or multi-step delivery work

- `workflows/codex/session-governance-and-split-recommendation.md`
  - when the work should be split into cleaner threads/projects

## Default Operating Sequence

For most project-management requests:

1. Read the front door:
   - `DELIVERY_JOURNAL.md`
   - `reports/auto/DELIVERY_JOURNAL_STATUS.json`
2. Verify whether the front door is healthy:
   - if the status file shows drift, repair that first or call it out plainly
3. Classify the situation
4. Load the right sub-skill(s)
5. Make the smallest real update that keeps the project truth durable
6. Refresh the delivery journal if meaningful project state changed
7. If meaningful work happened, update continuity
8. Name the next step and who owns it

## Write Targets

Update only the smallest truthful set:

- `projects/PROJECT_REGISTRY.md`
- `tasks/TASK_REGISTRY.md`
- `tasks/JOB_BOARD.md`
- `trace/ACTION_LOG.md`
- `harnesses/codex/chimera/KANBAN.md`
- `harnesses/codex/chimera/CONTINUATION.md`
- `harnesses/codex/chimera/WORK_LOG.md`
- `harnesses/codex/chimera/memory/MEMORY.md`
- `harnesses/codex/chimera/memory/LESSONS.md`
- `DELIVERY_JOURNAL.md`
- `reports/auto/DELIVERY_JOURNAL_STATUS.json`

## Delivery Journal Rule

If project/task/action-log/kanban truth changed meaningfully, refresh:

- `scripts/project_journaling/generate_delivery_journal.py`
- `scripts/tests/delivery_journal_smoke.py`

Do not leave the front door stale if you changed the backend truth.

## What Good Output Looks Like

When answering the user:

1. say what changed or what the current state is
2. say why it matters in real life
3. say what is still open only if it is truly still open
4. say what happens next
5. point to the exact durable files

## Typical Uses

Examples:

- "check all project progress and tell me what matters"
- "update the project state after this work"
- "find what is slipping or stale"
- "what should we do next"
- "is the journal still healthy"
- "keep everything organized"

## Important Rule

Do not stop at "here is what remains" if the next repair step is obvious and safe.
If the front door or continuity layer exposes a repairable bookkeeping problem, fix it in the same run when possible.
