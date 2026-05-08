# GitHub Coordination Operating Guide

Updated: 2026-05-04

## Purpose

Explain how Chimera now uses GitHub during startup, task transitions, unfinished work, and platform-specific publishing.

Use these three files together:

- this operating guide
- `docs/GITHUB_COORDINATION_ARCHITECTURE_2026-05-04.md`
- `docs/GITHUB_COORDINATION_FILE_USAGE_REGISTRY_2026-05-04.md`

## The Four Repos

### `saloomad/chimera`

Project code and project-level workflows.

### `saloomad/chimera-vps-deploy`

Shared coordination truth:

- handoffs
- shared skills
- platform mirrors
- `session-states/`
- `publish-queue/`

### `saloomad/chimera-windows-live`

Windows-only live config, scripts, and platform surfaces.

### `saloomad/chimera-linux-live`

Linux-only live config, OpenClaw runtime surfaces, cron, and platform surfaces.

## Why This Exists

The old failure mode was:

- work happened locally
- the agent changed tasks
- nothing shared was updated
- another platform resumed from stale GitHub truth

The new rule is:

task transition is a publish boundary, not only session end.

In plain English:

before an agent starts another real task, it must leave behind enough shared GitHub truth that the next platform will not be confused.

## Startup Logic

Before meaningful work, every platform must:

1. fetch or pull `chimera-vps-deploy`
2. read the newest handoff
3. read all `session-states/*.yaml`
4. read all `publish-queue/*.yaml`
5. decide what unfinished slice should continue

## Task Transition Logic

Before leaving one meaningful task for another, every platform must publish one of:

- `published-ready`
- `in-progress-not-ready`
- `blocked-needs-follow-up`

Minimum shared update:

- `session-states/<platform>.yaml`
- `publish-queue/<platform>.yaml` when code is not publish-ready

Minimum proof:

- the guard says the platform is ready
- the next platform can tell what is done, what is unfinished, and where the real code belongs

## Enforcement

### Strongest enforcement

- Claude Code hooks
- OpenCowork hook bundle
- shared guard script

### Medium enforcement

- Windows Codex, Kimi VPS, OpenCode, and Space Agent startup docs
- shared skills
- platform bootstraps

### Current stronger wrappers beyond docs

- Claude Code:
  native `UserPromptSubmit` hook can now deny a new meaningful task when `windows-claude` shared coordination state is stale
- OpenCode:
  stronger objective-start wrapper now requires the shared task-transition validator before a new meaningful task should begin
- Space Agent:
  still wrapper-only from the versioned surfaces we have; no separately proven native hard-stop API is available in this repo

### Windows Codex recurring publisher

Windows Codex now has a recurring runner:

- `C:\Users\becke\claudecowork\scripts\run_windows_codex_github_coordination_sync.ps1`
- registered by:
  - `C:\Users\becke\claudecowork\scripts\register_windows_codex_github_coordination_task.ps1`

What it does automatically:

- refreshes and publishes `session-states/windows-codex.yaml`
- refreshes and publishes `publish-queue/windows-codex.yaml`
- auto-publishes safe documentation-only updates when the repo is not mixed with code edits

Safe documentation-only autopublish currently covers:

- main repo PM and registry surfaces:
  - `DOCUMENT_REGISTRY.md`
  - `INDEX.md`
  - `PROJECT_REGISTRY.md`
  - `TASK_REGISTRY.md`
  - `ACTION_LOG.md`
  - `DELIVERY_JOURNAL.md`
  - `tracking/`
  - `research/platforms/`
  - `workflows/codex/`
- deploy repo documentation surfaces:
  - `handoffs/`
  - `docs/`

Guardrail:

- if non-document code edits are mixed into the same repo, the runner must skip safe-doc autopublish instead of committing a mixed unsafe slice

## Shared Skills

All platforms should read:

- `skills/github-coordination-gate`
- `skills/task-transition-publish`
- `skills/platform-live-repo-router`
- `skills/task-change-readiness-gate`

## The New Automatic Gate

The new gate skill is `task-change-readiness-gate`.

In plain English, it asks:

- are we actually safe to leave this task?
- is the shared GitHub state current?
- can another platform understand what is unfinished?

If the answer is no, the platform should not move on yet.

For OpenClaw specifically:

- the live intake hook should check the `kimi-vps` coordination state when a message looks like a new meaningful task
- the live bootstrap should inject the GitHub task-transition workflow so spawned agents see it early

## Proof

Use:

- `scripts/github_coordination_guard.py`
- `scripts/verify_github_coordination_system.py`

Windows Codex now has a safe recurring runner for the coordination files:

- `scripts/run_windows_codex_github_coordination_sync.ps1`
- `scripts/register_windows_codex_github_coordination_task.ps1`

That runner only refreshes and publishes:

- `session-states/windows-codex.yaml`
- `publish-queue/windows-codex.yaml`

It does not auto-commit arbitrary project code from dirty repos.

## Why The Files Exist

These files are not supposed to sit around unused.

They break into three jobs:

- workflow file:
  the exact steps to follow before leaving one task and starting another
- guide:
  the plain-English explanation for humans
- file usage registry:
  the truth table that says which files are read automatically, when they are used, and how we prove they are wired

The no-dead-end rule is:

if a durable coordination file does not have a reader, a trigger, and a proof surface, it is not done yet.

## What "Integrated" Means

A platform is only integrated when all of these are true:

1. its startup docs tell it to read the shared coordination files
2. its platform instructions mention the shared skills
3. its enforcement surface points to the guard or the workflow
4. the shared validation script passes
5. the live runtime surfaces that matter on that platform were actually updated

## What Still Requires Real Pulls

Editing the shared repo does not magically update every running platform.

The platforms still need to pull the changed coordination repo or receive the mirrored skill copy in their native local skill home.

## Workflow In One Short Example

1. work on task A
2. decide task A is not fully done
3. update `session-states/<platform>.yaml`
4. update `publish-queue/<platform>.yaml`
5. run the readiness gate
6. if the gate passes, start task B
7. if the gate fails, fix the shared state first
