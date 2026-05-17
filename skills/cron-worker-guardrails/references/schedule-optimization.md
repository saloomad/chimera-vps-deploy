# Schedule Optimization (Portable Principles; Cron-Centric)

Use this when deciding whether to add a recurring job at all, and if yes, how to schedule it safely.

## 1) Choose the right owner first

Before adding a cron schedule, decide whether the job really belongs to:

- a hook
- a Task Flow / workflow engine
- a standing order / rule
- a scheduler wake-up

Rule of thumb:
- use schedulers for **wake-up**
- use workflows for **stateful logic**
- use hooks for **event reactions**

If the job needs rich branching, approvals, or multi-step coordination, a plain recurring scheduler is probably the wrong owner.

## 2) Define the job contract

Every recurring job should state:

- purpose
- owner
- trigger cadence
- inputs
- output/report path
- success signal
- failure signal
- overlap policy

If these are unclear, the schedule is premature.

## 3) Cadence design

Prefer:

- the slowest cadence that still meets the goal
- offset schedules instead of bunching everything at `:00`
- explicit timezone notes, ideally UTC-first

Examples:

- `5,35 * * * *`
  - better than `0,30 * * * *` when many collectors already cluster on the hour
- `17 2 * * *`
  - better than `0 2 * * *` for a daily report if midnight boundaries create crowding

## 4) Overlap and locking

If a previous run may still be active when the next one starts:

- reject overlap with a lock
- or make the worker fully idempotent

Linux pattern:

```bash
flock -n /tmp/my_job.lock bash -lc 'cd /repo && python3 tools/my_job.py'
```

Use a lock when:

- the job writes shared files
- the job can issue duplicate alerts
- the job can trigger duplicate side effects

## 5) Runtime budget

Do not schedule a job at an interval shorter than its realistic runtime budget.

Bad:

- a 10-minute job scheduled every 5 minutes

Better:

- schedule slower
- split into smaller workers
- or move the stateful part into a workflow engine

## 6) Logging and proof

Every recurring job should have at least one of:

- a durable report file
- a machine-readable status file
- a bounded log with timestamps
- an activation receipt

Freshness alone is not enough. The output should make it possible to tell:

- did the job fire
- did it succeed
- did it produce useful content

## 7) Failure behavior

Prefer:

- short actionable failures
- no destructive fallback behavior
- no noisy success spam

If upstream inputs are missing:

- fail closed
- report what was missing
- do not invent substitute truth

## 8) Scheduler mutation safety

Before changing a live schedule:

- back up the existing schedule
- review the exact command path
- review the working directory
- review secrets/env assumptions
- define rollback

Do not give unattended automation silent power to mutate live scheduling unless explicitly approved.
