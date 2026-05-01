# OpenClaw Platform Enforcement Notes

Updated: 2026-05-01

## Current Live Truth

- Lobster workflow files exist live under `/root/.openclaw/workspace/orchestration/lobster/`
- Task Flow file exists live under `/root/.openclaw/workspace/orchestration/taskflow.json`
- workspace hooks exist live under `/root/.openclaw/workspace/hooks/`
- many workspace hooks are still disabled until explicitly enabled

## Practical Enforcement Pattern

- `Task Flow`
  - use as the durable owner for recurring multi-step state
- `Lobster`
  - use for bounded deterministic subflows inside the bigger flow
- `Hooks`
  - use for event-driven enforcement and suggestion
- `Standing orders`
  - use for persistent authority and boundaries
- `Cron`
  - use as the wake-up mechanism, not the workflow engine
- `Background tasks`
  - use for detached work audit and control

## Important Correction

Lobster is not “plain YAML” as a file type.

The official docs describe `.lobster` workflow files whose contents can be written in YAML or JSON form.

That means:

- extension: `.lobster`
- content shape: YAML or JSON style

## What To Avoid

- do not call a file “enabled” just because it exists on disk
- do not confuse cron with orchestration logic
- do not use heartbeat as the main pipeline engine when Task Flow or a scheduler-backed loop is the better fit
