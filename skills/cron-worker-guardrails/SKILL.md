---
name: cron-worker-guardrails
slug: cron-worker-guardrails
version: 1.0.5
license: MIT
description: |
  Use when: hardening OpenClaw cron/background workers (POSIX shells: bash/sh) against brittle quoting,
  cwd/env drift, and false pipeline failures (SIGPIPE, pipefail + head).
  Don't use when: the issue is application logic rather than execution-wrapper reliability.
  Output: a scripts-first hardening checklist + safe patterns (silent-on-success, deterministic cwd/env, rollback-friendly).
metadata:
  openclaw:
    emoji: "🧯"
---

# Cron Worker Guardrails (POSIX)

A reliability-first checklist for **OpenClaw cron workers** and any unattended automation.

## Scope (important)

- This skill is **POSIX-focused** (bash/sh examples).
- The *principles* are portable, but if you're on Windows/PowerShell you'll need equivalent patterns.

## The `NO_REPLY` convention

Many OpenClaw setups treat emitting exactly `NO_REPLY` as "silent success" (no human notification).

- If your runtime does not support `NO_REPLY`, interpret it as: **print nothing on success**.

## Quick Start

1) **Scripts-first:** move logic into a repo script (recommended: `tools/<job>.py` or `tools/<job>.sh`).
2) **One command in cron:** cron should run *one short command* (no multi-line `bash -lc '...'`).
3) **Deterministic cwd/env:** `cd` to the repo (or have the script do it), and document required env vars.
4) **Silent on success:** print nothing (or exactly `NO_REPLY`) when OK; only emit a short alert when broken.

Also see:
- `references/cron-agent-contract.md`
- `references/pitfalls.md`
- `references/schedule-optimization.md`

## Why this skill exists

Cron failures are rarely "logic bugs". In practice they're often:
- brittle shell quoting (`bash -lc '...'` nested quotes)
- command substitution surprises (`$(...)`)
- one-liners that hide escaping bugs (`python -c "..."`)
- cwd/env drift ("works locally, fails in cron")
- pipelines that fail for the wrong reason (`pipefail` + `head` / SIGPIPE)

The fix is boring but effective: **scripts-first + deterministic execution + silent-on-success**.

## Portability rules (still apply)

Even on POSIX, do **not** hardcode deployment-specific absolute paths tied to one machine.

Prefer:
- repo-relative paths
- environment variables you document
- minimal wrappers that `cd` into the repo

## Safe recurring-job creation rules

Use this skill not only to harden existing jobs, but also to design new recurring jobs safely.

Before recommending a schedule, answer these first:

1. **Should this even be a scheduler job?**
- For OpenClaw, prefer hooks for event reactions, Task Flow for durable pipeline state, standing orders for recurring authority, and schedulers only for wake-up.
- If the work is stateful, approval-heavy, or needs rich branching, cron is usually the wrong owner.

2. **What is the job contract?**
- exact owner
- exact trigger reason
- exact inputs
- exact output/report surface
- success should be silent
- failure should be short and actionable

3. **What is the safe cadence?**
- pick the slowest cadence that still meets the need
- avoid frequent wake-ups for jobs that mostly check and do nothing
- prefer offset schedules so heavy jobs do not pile up at `:00`

4. **How will overlap be prevented?**
- every recurring job should define overlap policy:
  - reject overlap
  - queue overlap
  - idempotent re-entry
- for Linux cron wrappers, prefer a lock such as `flock` if overlap would be harmful

5. **How will freshness and proof be shown?**
- define the report/log/output path before adding the schedule
- define what mtimes or receipts prove the job truly fired

6. **How will it fail closed?**
- missing upstream data should produce a bounded warning, not destructive fallback behavior

If these answers are missing, do not recommend a new recurring schedule yet.

## Schedule optimization checklist

When creating or reviewing a scheduled job, optimize for:

- **idempotency**: reruns should not duplicate state unless intended
- **single responsibility**: one recurring job, one main purpose
- **observability**: a known output, receipt, or report proves it ran
- **jitter / staggering**: avoid large groups of jobs all waking at once
- **UTC-first timing**: document timezone assumptions explicitly
- **bounded runtime**: schedule slower than the normal worst-case runtime
- **minimal privilege**: the job should not own control-plane mutation unless explicitly approved
- **clear rollback**: scheduler changes should be easy to undo

For safer schedule design patterns and examples, use `references/schedule-optimization.md`.

## Common failure patterns -> fixes

### 1) `unexpected EOF while looking for matching ')'`

Likely causes:
- unclosed `$(...)` from command substitution
- broken nested quotes in `bash -lc ' ... '`

Fix pattern:
- Replace the whole multi-line shell block with a script.
- Cron calls exactly one short command, for example:
  - `python3 tools/<job>.py`

### 2) False failure from `pipefail` + `head` (SIGPIPE)

Symptom:
- command exits non-zero even though the output you wanted is fine

Fix pattern:
- avoid `pipefail` when piping into `head`
- or better: do the filtering in a script (read only what you need)

### 3) "Works locally, fails in cron"

Common causes:
- wrong working directory
- missing env vars
- different PATH

Fix pattern:
- `cd` into the repo (or have the script do it)
- keep dependencies explicit and documented

## Git footgun: `git push` rejected (non-fast-forward)

Symptom:
- `! [rejected] ... (non-fast-forward)` when automation pushes to a **long-lived PR/feature branch**.

Conservative fix (no force-push):
- On rejection, fetch the remote branch, transplant your new local commits onto it (cherry-pick), then retry push once.

## Copy/paste hardening header (portable)

Use this near the top of a cron prompt (2 lines, low-noise):

- **Hardening (MUST):** follow `references/cron-agent-contract.md` (scripts-first, deterministic cwd, silent-on-success).
- Also apply the `cron-worker-guardrails` skill. If parsing/multi-step logic is needed, write/run a small `tools/*.py` script.

## Role split with the other cron skills

- `cron-doctor`
  - use when the job already looks broken or stale
  - answers: did it run, fail, or never fire

- `cron-worker-guardrails`
  - use when designing or editing the worker/wrapper
  - answers: is the recurring job safe, deterministic, quiet, and schedulable

- `cron-scheduler`
  - treat as reference only unless explicitly approved for mutation
  - borrow its useful ideas:
    - backup before destructive changes
    - validate schedule format
    - show next-run expectations
  - do not let it silently own live scheduler changes in Chimera
