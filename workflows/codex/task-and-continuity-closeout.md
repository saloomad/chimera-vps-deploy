# Task And Continuity Closeout Workflow

## Trigger

Use this workflow after meaningful work, especially after a fix, test, audit, or task-state change.

## Inputs

- current task status
- evidence paths
- files changed
- blockers or remaining risks

## Steps

1. Update the task state truthfully.
2. Append or fix the action log entry with evidence and next step.
3. Update kanban to reflect what is done and what remains.
4. Update continuation with the current focus and next steps.
5. Add a work-log entry for the new meaningful block.
6. Add stable facts or lessons if future sessions would benefit.
7. Regenerate `DELIVERY_JOURNAL.md` and `reports/auto/DELIVERY_JOURNAL_STATUS.json` so the front-door summary stays aligned with the real registries and action log.

## Expected Outputs

- current task registry
- current action log
- current continuation pack
- current delivery journal front door
