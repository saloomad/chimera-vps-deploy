# Enforcement Implementation Inventory

Updated: 2026-05-02

## Purpose

This file is the shared implementation inventory for enforcement, orchestration, hooks, workflows, detectors, and related platform features across Chimera.

## Core Starter Stack

- `prompt-upgrade-engineer` - prompt shaping - `implemented`, `wired`
- `sal-communication-contract` - explanation contract - `implemented`, `wired`
- `vibe-coding-operator` - main software-work front door - `implemented`, `wired`
- `objective-orchestration-loop` - route and review loop - `implemented`, `wired`
- `vibe-coding-monitor` - friction and activation review - `implemented`, `wired`, `partial`

## Workflow And Lifecycle Layer

- `WORKFLOW_CATALOG.md` - workflow selection menu - `implemented`, `wired`
- `meaningful-change-lifecycle-and-enforcement-loop.md` - mandatory full-lifecycle workflow - `implemented`, `wired`
- `build-test-verify-monitor-closeout.md` - proof and closeout workflow - `implemented`, `wired`

## Detector Layer

- `codex-workflow-detector` - promote repeated processes into workflows - `implemented`, `wired`
- `codex-skill-opportunity-detector` - promote repeated patterns into skills - `implemented`, `wired`
- `codex-feature-opportunity-detector` - route toward platform-native features - `implemented` locally, shared mirror not yet present

## OpenClaw Feature Layer

- `openclaw-feature-router` - choose between hooks, Task Flow, Lobster, standing orders, cron, background tasks - `implemented`, `wired`
- `openclaw-hook-engineer` - event-driven enforcement design - `implemented`, `wired`
- `openclaw-taskflow-architect` - durable recurring state design - `implemented`, `wired`
- `openclaw-standing-orders-designer` - recurring authority design - `implemented`, `wired`
- `openclaw-lobster-workflow-designer` - bounded deterministic subflow design - `implemented`, `wired`

## Platform Status Summary

- Windows Codex - skills/workflows/instructions/heartbeat - `partial`
- Claude Code - hooks/slash commands/instructions - guidance `implemented`, live hook config still `partial`
- OpenClaw / Kimi VPS - hooks/Task Flow/Lobster/standing orders/schedulers - guidance `implemented`, some live enablement still `partial`
- OpenCowork / OpenCode - config/docs/wrappers/workflows - `partial`, no separately verified native hook API in the current evidence set
- Hermes VPS - shared instructions/schedulers/file contracts - `partial`

## Main Official Docs

- Claude Code hooks: `https://code.claude.com/docs/en/hooks`
- Claude Code hooks guide: `https://code.claude.com/docs/en/hooks-guide`
- OpenClaw hooks: `https://docs.openclaw.ai/automation/hooks`
- OpenClaw Task Flow: `https://docs.openclaw.ai/automation/taskflow`
- OpenClaw Lobster: `https://docs.openclaw.ai/tools/lobster`
- OpenCode agents: `https://opencode.ai/docs/agents/`
- OpenCode config: `https://opencode.ai/docs/config`
- OpenCode CLI: `https://opencode.ai/docs/cli/`

## Main Remaining Gaps

- live Claude Code hook configs
- live OpenClaw enablement audit
- OpenCode/OpenCowork wrapper enforcement
- scenario tests and activation receipts
