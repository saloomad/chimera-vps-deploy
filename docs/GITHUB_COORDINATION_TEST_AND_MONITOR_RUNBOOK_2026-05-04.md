# GitHub Coordination Test And Monitor Runbook

Updated: 2026-05-04

## Purpose

Explain how to test, validate, and monitor the GitHub coordination system after changes.

## Smoke Tests

### 1. Guard self-test

```bash
python scripts/github_coordination_guard.py self-test
```

Expected:

- active task with current queue passes
- missing queue fails
- stale state fails
- complete with false queue passes

### 2. System verification

```bash
python scripts/verify_github_coordination_system.py
```

Expected:

- required repos exist
- required skills exist
- required docs and workflow exist
- platform files mention the coordination skills
- platform state files validate
- the task-change gate skill is present and referenced

### 3. Startup summary

```bash
python scripts/github_coordination_guard.py startup-summary --coordination-root .
```

Expected:

- latest handoff is visible
- all platform states appear
- all publish-queue files appear

### 4. OpenClaw runtime gate smoke

Expected:

- a new-task style message passes when `kimi-vps` shared state is current
- a new-task style message is warned or blocked when `kimi-vps` shared state is stale or missing
- the hook writes a receipt that shows whether the gate passed or failed

### 5. OpenClaw bootstrap injection smoke

Expected:

- a fresh agent workspace is created if needed
- the GitHub task-transition workflow is injected
- the GitHub operating guide is injected
- the bootstrap hook finishes without file-write errors

## Manual Scenarios

### Scenario A: finished slice

Expected:

- `session-states/<platform>.yaml` updates
- `publish-queue/<platform>.yaml` says `publish_required: false`
- correct repo gets pushed

### Scenario B: unfinished slice but new task starts

Expected:

- `session-states/<platform>.yaml` updates
- `publish-queue/<platform>.yaml` says `publish_required: true`
- local-only changes are listed

### Scenario C: blocked slice

Expected:

- `session-states/<platform>.yaml` updates
- `publish-queue/<platform>.yaml` records the blocker and next owner

### Scenario D: OpenClaw tries to switch tasks too early

Expected:

- the intake hook warns that shared GitHub state must be fixed first
- the response points to the missing or stale coordination file
- a gate receipt is written for audit

### Scenario E: OpenClaw switches tasks after honest shared update

Expected:

- the intake hook says the task-change gate passed
- the next task may begin without hidden publish debt

## Monitoring Routine

Run after meaningful coordination changes and at least once per day on the main coordination host:

1. `verify_github_coordination_system.py`
2. `github_coordination_guard.py startup-summary`
3. review newest handoff
4. review any platform queue file with `publish_required: true`
5. on OpenClaw, review the latest gate receipts when runtime gate logic changed

## Failure Signs

- a platform changed tasks but its queue file stayed stale
- a platform state file is older than its objective contract
- a platform startup doc does not mention the shared coordination skills
- a platform claims work is shared but GitHub has no matching repo or push
- OpenClaw accepts a new meaningful task without a current `kimi-vps` coordination state
- OpenClaw bootstrap says it injected the workflow but the new workspace never received the GitHub coordination files
