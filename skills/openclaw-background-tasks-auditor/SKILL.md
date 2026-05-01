---
name: openclaw-background-tasks-auditor
description: Use the OpenClaw background-task layer as a control plane for detached work: audit it, route it, explain it, and decide when Task Flow should sit above it.
triggers:
  - background tasks
  - detached work
  - task ledger
  - audit tasks
  - task maintenance
---

# OpenClaw Background Tasks Auditor

Use this skill when detached work exists or should exist and you need to inspect, control, or explain it.

## What Background Tasks Are

- the detached-work ledger
- where cron runs, subagent runs, and other background work can be audited
- not the same thing as the orchestration logic itself

## When To Use It

- audit detached work
- inspect stuck or silent runs
- decide notify or cancel policy
- decide whether Task Flow should sit above a task set

## Current Chimera Truth

- low-level OpenClaw task ledgers exist live
- human-facing Chimera task/front-door surfaces still need fresher alignment than the low-level ledger alone

## Output Contract

Leave behind:

- what detached work exists
- whether it is observable enough
- whether Task Flow should own the bigger sequence
- maintenance or notification changes needed
