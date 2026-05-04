---
name: task-change-readiness-gate
description: Confirm whether a platform is actually allowed to leave the current meaningful task and start another one. Use when switching tasks, parking unfinished work, closing a slice, or checking whether shared GitHub coordination is current enough to move on. Triggers: can I move on, switch tasks, task gate, readiness gate, before next task, allowed to start another task.
---

# Task Change Readiness Gate

Use this skill right before a platform leaves one meaningful task and starts another.

## Plain-English Purpose

This is the "are we really safe to move on?" gate.

It stops the agent from doing this:

- work locally
- feel mostly done
- jump to another task
- leave other platforms blind

## What This Skill Must Confirm

Before another meaningful task starts, all of these must be true:

1. the current slice has an honest review outcome
2. the shared coordination files are up to date
3. unfinished work is visible in `publish-queue/<platform>.yaml`
4. the next platform can tell what is still open
5. the repo owner for the real code change is clear

If any of those are false, the task change is **not ready**.

## The Three Allowed Results

### 1. Ready To Move

Use when:

- `session-states/<platform>.yaml` is current
- `publish-queue/<platform>.yaml` is current
- the current slice is either published, honestly parked, or honestly blocked

What it means:

- the agent may start the next meaningful task

### 2. Not Ready - Update Shared State First

Use when:

- the current task changed but shared files did not
- review outcome is still implicit
- local-only changes are not described

What it means:

- update shared state first
- do not start the next meaningful task yet

### 3. Not Ready - Repo Ownership Unclear

Use when:

- it is not clear whether the work belongs in:
  - `chimera`
  - `chimera-vps-deploy`
  - `chimera-windows-live`
  - `chimera-linux-live`

What it means:

- run `platform-live-repo-router`
- decide the real owner before moving on

## Required Check Order

1. read the newest handoff
2. read `session-states/*.yaml`
3. read `publish-queue/*.yaml`
4. check the current objective contract or task truth
5. confirm the platform file for the current task is current
6. confirm the publish queue is current if the code is not publish-ready
7. confirm the next action is explicit
8. confirm repo ownership

## Fast Proof Command

Windows:

```powershell
python C:\Users\becke\claudecowork\chimera-vps-deploy\scripts\github_coordination_guard.py validate-platform --coordination-root C:\Users\becke\claudecowork\chimera-vps-deploy --platform windows-codex
```

Linux:

```bash
python3 /root/chimera-deploy/scripts/github_coordination_guard.py validate-platform --coordination-root /root/chimera-deploy --platform kimi-vps
```

## What To Say Out Loud

When this skill triggers, the answer should say:

- what we are working on
- whether the current task is ready to leave
- what is missing if it is not ready
- what exact file or repo must be updated next

Use plain English.
Do not answer with only branch names, file names, or git jargon.

## Works With

- `github-coordination-gate`
- `task-transition-publish`
- `platform-live-repo-router`
- `sal-communication-contract`
- `GITHUB_TASK_TRANSITION_AND_PUBLISH_LOOP.md`

---
*task-change-readiness-gate v1.0 | 2026-05-04 | Chimera shared skill*
