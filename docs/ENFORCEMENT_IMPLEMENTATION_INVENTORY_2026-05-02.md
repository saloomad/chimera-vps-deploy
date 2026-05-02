# Enforcement Implementation Inventory

Updated: 2026-05-02

## What This Is

This file is the running inventory of the enforcement and orchestration surfaces we have, how they are used, and whether they are only documented, wired, or verified live.

Status labels:

- `implemented`
  - the file or config exists
- `wired`
  - instructions or workflows point to it
- `verified live`
  - there is proof it is actively used in the target runtime
- `partial`
  - some pieces are wired, but live proof is incomplete
- `opportunity`
  - good next feature to add, but not yet implemented

## Core Starter Stack

### `prompt-upgrade-engineer`
- Role: turn rough asks into a stronger internal execution brief
- Status: `implemented`, `wired`
- Used for: prompt shaping, better file/tool selection, better visible answer shape

### `sal-communication-contract`
- Role: force beginner-friendly explanations and proof translation
- Status: `implemented`, `wired`
- Used for: context-first replies, jargon translation, end summaries

### `vibe-coding-operator`
- Role: main build-and-finish front door for meaningful software work
- Status: `implemented`, `wired`
- Used for: starter stack routing, workflow choice, PM/testing/closeout guardrails

### `objective-orchestration-loop`
- Role: choose the route and enforce `plan -> execute -> review -> repeat`
- Status: `implemented`, `wired`
- Used for: orchestration class selection, done contracts, review outcomes

### `vibe-coding-monitor`
- Role: detect friction, weak proof, missed activation, and explanation failures
- Status: `implemented`, `wired`, `partial`
- Used for: optimization queue, instruction improvement, discoverability checks
- Note: still needs stronger live proof/receipt usage across future sessions

## Workflow And Lifecycle Enforcement

### `WORKFLOW_CATALOG.md`
- Role: menu of which workflow to use
- Status: `implemented`, `wired`
- Used for: choosing the correct workflow instead of improvising

### `meaningful-change-lifecycle-and-enforcement-loop.md`
- Role: mandatory full-lifecycle workflow for meaningful changes
- Status: `implemented`, `wired`
- Used for: workflow selection, enforcement selection, dependent-surface updates, testing, review, docs, monitoring

### `critical-config-instruction-and-compaction-guard-loop.md`
- Role: mandatory governance workflow for risky control-layer edits such as config, instructions, hooks, skills, workflows, detectors, and compaction continuity
- Status: `implemented`, `wired`
- Used for: backup, rollback, proof, continuity protection, PM truth, and control-layer review before closeout

### `build-test-verify-monitor-closeout.md`
- Role: implementation closeout workflow
- Status: `implemented`, `wired`
- Used for: implementation proof, enforcement-surface check, dependent-surface check, closeout

## Detector Layer

### `codex-workflow-detector`
- Role: detect when a repeatable process should become a workflow
- Status: `implemented`, `wired`
- Used for: repeated process capture, explanation-friction workflow capture

### `codex-skill-opportunity-detector`
- Role: detect when a repeated pattern should become a reusable skill
- Status: `implemented`, `wired`
- Used for: repeated explanation fixes, repeated manual work, risky recurring tasks

### `codex-feature-opportunity-detector`
- Role: detect when a Codex/platform-native feature should be used instead of custom glue
- Status: `implemented`, `wired`
- Used for: docs lookup, automations, browser tooling, connectors, official feature routing

## Platform Feature Routers

### `openclaw-feature-router`
- Role: decide which OpenClaw feature fits a problem
- Status: `implemented`, `wired`
- Used for: choosing between hooks, Task Flow, Lobster, standing orders, cron, background tasks

### `openclaw-hook-engineer`
- Role: design or review OpenClaw hooks
- Status: `implemented`, `wired`
- Used for: event-driven enforcement

### `openclaw-taskflow-architect`
- Role: design or review durable recurring Task Flow ownership
- Status: `implemented`, `wired`
- Used for: restart-safe recurring orchestration

### `openclaw-standing-orders-designer`
- Role: design persistent authority and boundaries
- Status: `implemented`, `wired`
- Used for: recurring authority, escalation boundaries, program scope

### `openclaw-lobster-workflow-designer`
- Role: design bounded deterministic Lobster pipelines
- Status: `implemented`, `wired`
- Used for: structured subflows inside bigger recurring systems

## Platform Surfaces

### Windows Codex
- Best surfaces: `AGENTS.md`, skills, workflows, thread heartbeat
- Status: `implemented`, `wired`, `partial`
- Note: no separately verified general hook API in this runtime

### Claude Code
- Best surfaces: hooks, slash commands, `CLAUDE.md`, subagents
- Status: local live hook bundle is `implemented`; shared mirrored bundle is `partial` until the new files are pushed and reused elsewhere
- Verified live now: `UserPromptSubmit`, `SessionStart`, `PostToolUse`, `Stop`
- Strengthened in this pass: `PreToolUse`, `PostToolUseFailure`, `SubagentStop`

### OpenClaw / Kimi VPS
- Best surfaces: hooks, Task Flow, Lobster, standing orders, cron/timers, background tasks
- Status: docs and routing are `implemented`; live audit says the surface is still `partial`
- Verified live now:
  - `hooks.internal.entries.message-router.enabled = true`
  - `hooks.internal.entries.mandatory-bootstrap.enabled = true`
  - `hooks.internal.entries.on_agent_spawn.enabled = true`
  - `hooks.internal.entries.on_compact_before.enabled = true`
  - `hooks.internal.entries.on_compact_after.enabled = true`
  - `hooks.internal.entries.on_gateway_restart.enabled = true`
  - `tools.alsoAllow` includes `lobster`
  - `orchestration/taskflow.json` exists with enabled flow definitions
- Important live gap:
  - many workspace hooks exist on disk but are not currently enabled
  - several Lobster workflow files still referenced the retired `/home/open-claw/openclawtrading` path before this repair pass
- Note: on-disk files are not the same as verified live use

### OpenCowork / OpenCode
- Best surfaces today: rules, project config, native agents, native commands, native skills, permissions, file-backed plans, shared workflows, handoffs
- Status: `implemented`, `wired`, `partial`
- Verified by official docs in this pass:
  - project rules via `AGENTS.md`
  - project config via `opencode.json`
  - custom agents
  - custom commands
  - native skill discovery from `.opencode`, `.claude`, and `.agents` paths
  - permission gating
- Note: no separately verified native hook surface has been proven yet

### Hermes VPS
- Best surfaces today: shared instructions, schedulers, file contracts
- Status: `implemented`, `wired`, `partial`
- Opportunity: stronger enforced trading-lane pattern using the same OpenClaw-style recurring model where feasible

## Official Feature Research We Are Using

### Claude Code
- Hooks reference: [https://code.claude.com/docs/en/hooks](https://code.claude.com/docs/en/hooks)
- Hooks guide: [https://code.claude.com/docs/en/hooks-guide](https://code.claude.com/docs/en/hooks-guide)

### OpenClaw
- Hooks: [https://docs.openclaw.ai/automation/hooks](https://docs.openclaw.ai/automation/hooks)
- Task Flow: [https://docs.openclaw.ai/automation/taskflow](https://docs.openclaw.ai/automation/taskflow)
- Lobster: [https://docs.openclaw.ai/tools/lobster](https://docs.openclaw.ai/tools/lobster)
- Automation overview: [https://docs.openclaw.ai/automation/index](https://docs.openclaw.ai/automation/index)

### OpenCode
- Agents: [https://opencode.ai/docs/agents/](https://opencode.ai/docs/agents/)
- Config: [https://opencode.ai/docs/config](https://opencode.ai/docs/config)
- CLI: [https://opencode.ai/docs/cli/](https://opencode.ai/docs/cli/)
- Rules: [https://opencode.ai/docs/rules](https://opencode.ai/docs/rules)
- Skills: [https://opencode.ai/docs/skills/](https://opencode.ai/docs/skills/)
- Permissions: [https://opencode.ai/docs/permissions/](https://opencode.ai/docs/permissions/)
- Modes: [https://opencode.ai/docs/modes/](https://opencode.ai/docs/modes/)

## What Still Needs To Be Built

- OpenClaw follow-through repair:
  - finish syncing repaired `/root/openclawtrading` paths into live Lobster workflows
  - decide which disabled hooks should actually be enabled
  - prove which Task Flow paths are truly running, not only configured
- scenario tests proving the starter stack and lifecycle are actually followed
- activation receipts showing which skills/hooks/workflows truly fired

## Reusable Verifier

- `scripts/verify_platform_enforcement_surfaces.ps1`
  - checks the local Claude hook bundle
  - checks the committed OpenCode bundle
  - checks live OpenClaw enabled-hook keys and key Lobster path truth
