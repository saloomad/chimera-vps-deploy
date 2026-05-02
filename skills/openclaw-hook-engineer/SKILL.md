---
name: openclaw-hook-engineer
description: Design, review, or enable OpenClaw hooks for event-driven enforcement, feature suggestions, bootstrap injection, and workflow guardrails.
triggers:
  - openclaw hooks
  - hook engineer
  - event driven enforcement
  - message router hook
  - bootstrap hook
---

# OpenClaw Hook Engineer

Use this skill when the right answer is to react to an event rather than poll or manually repeat work.

## Read First

- `openclaw-feature-router`
- `objective-orchestration-loop`
- `../../docs/PLATFORM_ORCHESTRATION_AND_HOOKS_MATRIX_2026-05-02.md`

## What Hooks Are

- event-driven scripts that run inside Gateway lifecycle and message flow
- the best place for lightweight enforcement, routing hints, or bootstrap behavior

## Good Hook Jobs

- startup or bootstrap injection
- message feature suggestion
- post-step validation
- continuity capture around compaction or session boundaries
- lightweight "what else must be updated" enforcement after a meaningful action

## Bad Hook Jobs

- heavy long-running orchestration
- exact-time scheduling
- durable multi-step flow ownership
- pretending a hook is the whole workflow engine

## Current Chimera Truth

- live hooks home: `/root/.openclaw/workspace/hooks/`
- workspace hooks are opt-in and disabled by default until enabled
- Chimera already has message-router, bootstrap, memory, compaction, and session hooks on disk

## Output Contract

Leave behind:

- event
- trigger reason
- what the hook changes
- why a hook fits better than Task Flow or cron
- enablement steps
- rollback path
- what workflow and proof layer still own the broader objective
