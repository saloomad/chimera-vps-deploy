---
name: pipeline-enforcement-detector
description: Detect when a recurring or risky workflow should be owned by the right runtime surface such as Task Flow, Lobster, standing orders, commands, schedules, or review gates instead of ad hoc chat reminders.
triggers:
  - pipeline enforcement
  - what should own this workflow
  - trading pipeline
  - recurring workflow
  - enforce this pipeline
---

# Pipeline Enforcement Detector

Use this skill when the question is not only "what should happen?" but "what should reliably own this over time?"

## Auto Trigger Rules

Run this skill when:

1. a pipeline is recurring
2. order matters across multiple steps
3. restart-safe state matters
4. approval gates matter
5. the workflow touches live trading or other high-impact automation
6. the user asks how to enforce or own a workflow across platforms

## Read First

- `C:\Users\becke\claudecowork\orchestration\taskflow.json`
- `C:\Users\becke\claudecowork\docs\PLATFORM_ORCHESTRATION_AND_HOOKS_MATRIX_2026-05-02.md`
- `C:\Users\becke\claudecowork\docs\PLATFORM_WORKFLOW_AND_SKILL_ENFORCEMENT_CATALOG_2026-05-02.md`
- `C:\Users\becke\claudecowork\workflows\codex\platform-enforcement-selection-and-receipt-loop.md`
- `C:\Users\becke\.codex\skills\openclaw-feature-router\SKILL.md`

## Decision Order

1. if the pipeline is event-driven, consider hooks first
2. if the pipeline needs durable recurring state, prefer Task Flow
3. if the pipeline needs a bounded deterministic subflow, prefer Lobster
4. if the pipeline needs recurring authority and limits, prefer standing orders
5. if the platform lacks those surfaces, use commands, permissions, and review gates
6. if exact time matters but logic ownership does not, use a scheduler only as a wake-up

## Platform Guidance

### OpenClaw / Kimi VPS

Preferred order:

1. hooks for event reactions
2. Task Flow for durable cadence and state
3. Lobster for deterministic subflows
4. standing orders for recurring authority
5. scheduler for wake-up only

### Hermes

Preferred order:

1. runtime bridge scripts
2. scheduler-backed rebuilds
3. receipt capture
4. shared instructions

### OpenCode / OpenCowork / Codex

Preferred order:

1. workflows
2. commands
3. permissions
4. review gates
5. receipts

## Minimum Output

When this skill triggers, leave behind:

1. the chosen runtime owner
2. why it fits
3. what should not own the pipeline
4. required proof path
5. receipt path if possible
