# PM Front-Door Reconciliation Loop

## Trigger

Use this workflow when:

- `DELIVERY_JOURNAL.md`, `PROJECT_REMINDERS.md`, or status files may be stale
- project/task/action counts look wrong
- local PM truth may have drifted from live or generated front-door summaries
- the user asks what is really current in PM surfaces

## Inputs

- `DELIVERY_JOURNAL.md`
- `reports/auto/DELIVERY_JOURNAL_STATUS.json`
- `projects/PROJECT_REGISTRY.md`
- `tasks/TASK_REGISTRY.md`
- `trace/ACTION_LOG.md`
- `projects/PROJECT_REMINDERS.md`
- live OpenClaw PM surfaces if reachable

## Steps

1. Start from the source stack, not the generated front door.
2. Compare project/task/action truth against the front-door surfaces.
3. If live OpenClaw is relevant and reachable, compare live truth too.
4. Rebuild or refresh generated front-door surfaces after meaningful fixes.
5. Run the smallest useful smoke check.
6. Publish one honest result:
   - reconciled
   - iterate
   - blocked

## Expected Outputs

- reconciled PM front door or clear drift diagnosis
- honest local-only or live-verified status
- next action if the mismatch is still open
