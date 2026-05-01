---
name: change-capture-and-versioning
description: Capture meaningful instruction, prompt, workflow, skill, Paperclip, automation, and system changes into a separate versioned history instead of leaving them trapped in dirty working trees or chat.
---

# Change Capture And Versioning

Use this skill when the task is about:

- saving meaningful changes automatically
- commits or version history for prompts, instructions, workflows, or system changes
- separating full backups from change history
- capturing Paperclip/OpenClaw/Codex control-layer changes

## Read First

On the current workspace:

- `operations/change-capture/CAPTURE_POLICY.md`
- `operations/change-capture/capture_profiles.json`
- `operations/change-capture/change_capture_decision_schema.json`
- `workflows/codex/change-capture-and-save-loop.md`

If Linux OpenClaw is involved, also read:

- `/root/openclawtrading/operations/change-capture/CAPTURE_POLICY.md`
- `/root/openclawtrading/agents/cron-manager/AGENTS.md`
- `/root/openclawtrading/agents/system-ops/AGENTS.md`

## Core Rule

Do not auto-commit the dirty main repos directly.

Use separate capture repos:

- Windows default: `C:\Users\becke\change-capture`
- Linux default: `/root/change-capture`

## Operating Model

1. deterministic collector finds allowlisted changes
2. agent reviewer decides `save`, `ignore`, or `defer`
3. deterministic applier mirrors selected files into the capture repo and commits them

## What Usually Counts As Worth Saving

- `AGENTS.md`, `SOUL.md`, `HEARTBEAT.md`, `USER.md`, `TOOLS.md`
- prompt-engineering artifacts
- workflows
- skills
- hooks
- Paperclip setup scripts and exported org state
- cron and automation config
- system scripts changed to alter behavior or results

## What Usually Does Not

- logs
- caches
- backup archives
- runtime report churn
- secrets or auth files

## Outputs

- candidate manifest
- decision JSON
- versioned mirror in the capture repo
- journal entry explaining why the snapshot was saved or ignored

## Linux Ownership

- recurring reviewer: `cron-manager`
- policy steward: `system-ops`
- routed consumer for deferred or broken states: `orchestrator`
