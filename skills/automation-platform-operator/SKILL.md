---
name: automation-platform-operator
description: Create, audit, repair, and optimize recurring work across Codex automations, OpenClaw cron, Linux cron, and Windows Scheduled Tasks. Use when working on automations, cron jobs, heartbeats, recurring checks, scheduled tasks, scheduler drift, or recurring audits.
---

# Automation Platform Operator

Use this skill when the job is to decide, create, inspect, or optimize recurring work across platforms.

## What This Skill Covers

- Codex thread heartbeats
- Codex cron automations
- Linux cron on VPS or local Linux
- Windows Task Scheduler
- OpenClaw recurring runtime work when the real owner is the platform scheduler
- recurring-job audits, drift repair, and dead-end prevention

## First Question

Ask: `what is the real owner of this recurring work?`

Choose the smallest honest owner:

- current Codex thread heartbeat
- Codex local cron automation
- root or user cron on Linux
- Windows Scheduled Task
- OpenClaw runtime flow only when it is actually wired and provable

Do not force everything into Codex automations if the real runtime owner is the VPS scheduler.

## Platform Chooser

### Use a Codex thread heartbeat when

- the work belongs to one active thread
- the user wants same-thread follow-through
- the cadence is under an hour
- the work should stop when the objective is complete or blocked

### Use a Codex cron automation when

- the work should start in a fresh chat
- the job is local to this Windows Codex machine
- recurring reporting, reminders, audits, or safe bounded execution are needed
- a human-readable summary is required each run

### Use Linux cron when

- the work belongs to the live VPS or Linux host
- it must keep running even when Codex or the local PC is closed
- the producer is a script, collector, or runtime maintenance job
- the schedule should survive app restarts and chat boundaries

### Use Windows Scheduled Task when

- the work belongs to the Windows machine itself
- it must survive Codex/Claude being closed
- the task runs a local script, sync, capture, watcher, or housekeeping job
- login state, wake behavior, or power conditions matter

### Use OpenClaw flow or runtime scheduling only when

- the platform is the real execution owner
- the flow is already provably wired
- receipts or artifacts prove it actually runs

If `exists` is true but `used` or `auto-triggered` is not proven, do not claim it owns the workflow yet.

## Core Rule

Every recurring job needs all four:

1. a clear objective
2. a state surface to resume from
3. a real receiver of the result
4. a stop or escalation rule

If any of those are missing, the automation is likely to drift or become a dead end.

## Required Prompt Contract

Use this contract for scheduler-owned agent prompts:

1. `Ultimate objective`
2. `Current run mission`
3. `Evidence first`
4. `Resume from previous run`
5. `Allowed actions`
6. `Do not do`
7. `Host unavailable rule`
8. `Review outcome`
9. `Output contract`

## Resume Rule

Recurring work must continue from prior state.

Read in this order when available:

1. last status file or report
2. active handoff or observation ledger
3. PM or task surface
4. fresh runtime proof

If the previous result is missing, say that clearly and rebuild from evidence. Do not silently start a new objective.

## Anti-Dead-End Rule

Make sure another agent or human can pick the work up.

Good receivers:

- `PROJECT_REGISTRY.md`
- `TASK_REGISTRY.md`
- `DELIVERY_JOURNAL.md`
- observation ledgers
- handoffs
- named inbox or report files
- a clear owner in the chat output

Bad receivers:

- only a stale chat reply
- only a log line with no owner
- only a generated report nobody reads

## Host Unavailable Rule

Missing output is not always failure.

For local Windows recurring jobs:

- the PC may have been off, sleeping, disconnected, or blocked from running the scheduler
- treat `job did not run here` separately from `the monitored system is broken`

For remote VPS checks:

- SSH timeout is not equal to remote failure
- wrapper timeout is not equal to agent failure
- look for fresh artifacts before escalating

## Health Checks By Platform

### Codex automations

- inspect `C:\Users\becke\.codex\automations\*\automation.toml`
- check `kind`, `rrule`, `model`, `reasoning_effort`, and prompt shape
- verify the automation has a real receiver and stop rule

### Windows Scheduled Tasks

- use `Get-ScheduledTask`
- inspect triggers, principals, last run time, last result, and power conditions
- verify the task points at stable scripts and working directories

### Linux cron

- inspect `crontab -l`
- inspect `/etc/crontab` or `/etc/cron.d` when system jobs matter
- verify absolute script paths, environment assumptions, and logging

### OpenClaw recurring runtime

- prove the active scheduler surface first
- distinguish repo mirror, config presence, and real runtime execution

## Best Practices

- scripts first, scheduler second
- one short scheduler command that launches a real script
- deterministic cwd and env
- objective-anchored prompts
- silent success for machine-only jobs, clear short alerts for failures
- stable report paths and freshness fields
- same file families every run so diffs are easy to inspect
- explicit owner when a job cannot safely self-fix

## Model Routing

- default automation lane: `gpt-5.4` with reasoning `medium`
- heavier recurring review: `gpt-5.4` with reasoning `high`
- cheap mechanical sweeps: `gpt-5.4-mini` with reasoning `low`
- do not use `gpt-5.5` for routine automations

## ClawHub Skill Verdict

Use these as idea sources, not blind installs.

### `Cron Doctor`

- best value: triage checklist, failure categories, and priority ranking
- keep: command-not-found, permission, missing-path, timeout, network, and rate-limit diagnosis patterns
- do not adopt blindly: its default report path and generic Linux-first assumptions

### `Cron Scheduler`

- best value: schedule validation, backup-before-edit, and service-status checks
- risk: the skill is flagged for review and it includes high-impact add/remove/edit behavior
- verdict: extract patterns, do not install as-is into a live control layer without a separate security and path review

### `Cron Worker Guardrails`

- best value: scripts-first, deterministic cwd/env, and silent-on-success reliability rules
- keep: wrapper-timeout skepticism and anti-brittle-shell guidance
- limit: it is POSIX-focused, so Windows needs equivalent PowerShell patterns instead of direct reuse

## Optimization Loop

When reviewing an existing recurring job, check:

1. is the real objective still the same
2. is the current cadence still justified
3. is the model too expensive or too weak
4. does the prompt resume from the previous run
5. does the job have a real receiver
6. is stale output being classified honestly
7. is the scheduler the right owner
8. should the work be split into executor, audit, and reminder lanes

## Output Contract

When you report back, make the answer usable without opening files:

- what the recurring job is for
- what platform should own it
- what you changed or recommend changing
- what is still risky or blocked
- who should act next
