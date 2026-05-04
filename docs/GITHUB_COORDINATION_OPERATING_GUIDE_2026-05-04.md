# GitHub Coordination Operating Guide

Updated: 2026-05-04

## Purpose

Explain how Chimera now uses GitHub during startup, task transitions, unfinished work, and platform-specific publishing.

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

## Enforcement

### Strongest enforcement

- Claude Code hooks
- OpenCowork hook bundle
- shared guard script

### Medium enforcement

- Windows Codex, Kimi VPS, OpenCode, and Space Agent startup docs
- shared skills
- platform bootstraps

## Shared Skills

All platforms should read:

- `skills/github-coordination-gate`
- `skills/task-transition-publish`
- `skills/platform-live-repo-router`

## Proof

Use:

- `scripts/github_coordination_guard.py`
- `scripts/verify_github_coordination_system.py`

## What "Integrated" Means

A platform is only integrated when all of these are true:

1. its startup docs tell it to read the shared coordination files
2. its platform instructions mention the shared skills
3. its enforcement surface points to the guard or the workflow
4. the shared validation script passes

## What Still Requires Real Pulls

Editing the shared repo does not magically update every running platform.

The platforms still need to pull the changed coordination repo or receive the mirrored skill copy in their native local skill home.
