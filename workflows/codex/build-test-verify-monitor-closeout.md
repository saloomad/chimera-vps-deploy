# Build Test Verify Monitor Closeout

## Trigger

Use this workflow when a request is more than a tiny one-line answer, especially if it changes code, runtime behavior, monitoring, workflow contracts, or operator expectations.

## Inputs

- objective
- changed files or systems
- producers and consumers touched
- approval boundary
- expected done criteria

## Steps

1. If this is a major build or key decision, run `workflows/codex/major-build-council-and-delivery-loop.md` first.
2. Define the objective in plain English.
3. Name the change surface: files, agents, scripts, reports, cron jobs, configs, or workflows touched.
4. Name the proof shape before implementation:
   - local checks
   - integration checks
   - bounded live proof if reachable
   - honest remaining gaps
5. Implement the smallest real change that can satisfy the objective.
6. Verify producer and consumer integration instead of only file creation.
7. Decide whether the result needs monitoring, a handoff, or a follow-up task.
8. Update tasks, action log, continuity, and lessons truthfully.
9. Regenerate the front-door delivery summary so humans can see the current project/task/action state without stitching it together manually:
   - `DELIVERY_JOURNAL.md`
   - `reports/auto/DELIVERY_JOURNAL_STATUS.json`

## Expected Outputs

- implemented change or blocked plan
- evidence-backed verification result
- monitoring or follow-up decision
- durable closeout updates
- refreshed delivery journal front door
