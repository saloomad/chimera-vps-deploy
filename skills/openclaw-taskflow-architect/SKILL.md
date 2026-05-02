---
name: openclaw-taskflow-architect
description: Design or review Task Flow as the durable state owner for recurring OpenClaw workflows, especially when restarts, recurring cadence, or multi-step ownership matter.
triggers:
  - task flow
  - taskflow
  - durable state
  - recurring flow
  - restart safe workflow
---

# OpenClaw Task Flow Architect

Use this skill when the workflow must survive restarts, keep durable state, or manage recurring multi-step progress.

## Read First

- `openclaw-feature-router`
- `objective-orchestration-loop`
- `openclaw-orchestration-proof-router`
- `../../docs/PLATFORM_ORCHESTRATION_AND_HOOKS_MATRIX_2026-05-02.md`

## What Task Flow Is

- the durable flow owner above detached tasks
- the right place for recurring multi-step state
- the place to express restart-safe orchestration ownership

## When To Use It

- recurring monitor or trading cycles
- stateful flow across restarts
- multi-step work that should not be rebuilt from chat context

## When Not To Use It

- one tiny detached task
- a pure event reaction
- a single direct answer

## Current Chimera Truth

- live file: `/root/.openclaw/workspace/orchestration/taskflow.json`
- shared local mirror: `C:\Users\becke\claudecowork\orchestration\taskflow.json`
- current best use in Chimera: own the lean market cycle while delegating bounded investigation to Lobster

## Output Contract

Leave behind:

- flow owner
- state contract
- triggers or schedule
- child workflow references
- stop conditions
- proof of restart-safe ownership
