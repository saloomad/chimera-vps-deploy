---
name: openclaw-lobster-workflow-designer
description: Design or review bounded deterministic OpenClaw workflows using `.lobster` files, with clear gates, approvals, and proof of where Lobster fits in Chimera.
triggers:
  - lobster workflow
  - .lobster
  - lobster pipeline
  - deterministic workflow
  - openclaw lobster
---

# OpenClaw Lobster Workflow Designer

Use this skill when the task needs one bounded, explicit workflow with known steps, branches, approvals, or rerun gates.

## Read First

- `openclaw-feature-router`
- `objective-orchestration-loop`
- `openclaw-orchestration-proof-router`
- `../../docs/PLATFORM_ORCHESTRATION_AND_HOOKS_MATRIX_2026-05-01.md`

## What Lobster Is

- a bounded workflow file with `.lobster` extension
- good for deterministic step graphs
- good for approval-friendly checkpoints
- good for workflow-in-workflow subflows inside a larger runtime

## When To Use It

- the steps are known ahead of time
- the flow needs explicit gates
- the flow should be readable on disk
- the flow is a sub-process inside a bigger loop

## When Not To Use It

- durable recurring state across restarts by itself
- pure event reactions
- open-ended deep research

## Current Chimera Truth

- live Lobster home: `/root/.openclaw/workspace/orchestration/lobster/`
- shared local mirror: `C:\Users\becke\claudecowork\orchestration\lobster\`
- Chimera already uses Lobster for trading and review subflows
- enablement still depends on the OpenClaw tool/config surface, not only file presence

## Output Contract

Leave behind:

- why Lobster fits
- parent workflow if this is nested
- inputs
- steps
- gates
- approval points
- failure or rerun policy
- proof path
