# Platform Orchestration And Hooks Matrix

Updated: 2026-05-01

## Purpose

This document says which orchestration and enforcement features are actually worth using on each Chimera platform.

The goal is not to force one platform to mimic another.
The goal is to keep one shared orchestration contract while using the strongest native feature surface each platform really has.

## Shared Contract

Every meaningful task should pass through:

1. orchestration precheck
2. route selection
3. visible done contract
4. plan
5. execute
6. test or proof
7. review
8. stop or iterate

## Platform Matrix

| Platform | Best native orchestration surfaces | Best native enforcement surfaces | Important limits | Best use in Chimera |
|---|---|---|---|---|
| Windows Codex | shared skills, subagents, thread continuation when exposed | `AGENTS.md`, bootstrap, thread heartbeat or automation when available | no verified OpenClaw-style hooks in this runtime | local implementation, repo edits, durable artifact production, closeout proof |
| Claude Code desktop | subagents, custom slash commands, project and user config | hooks, `CLAUDE.md`, slash commands | no durable continuation after close | planning, review, prompt shaping, workflow enforcement at prompt or tool boundaries |
| OpenClaw / Kimi VPS | Task Flow, Lobster, background tasks, standing orders, cron | hooks, standing orders, Linux timers and services | workspace hooks are opt-in; on-disk files are not proof of live use | live recurring runtime, durable state, bounded deterministic subflows, event reactions |
| Hermes VPS | shared instructions, Linux schedulers, file contracts | Linux timer or service layer, shared skills | no separately verified native hook or flow system in current evidence | second-opinion lane, tightly gated experiments, proof review |
| OpenCowork / OpenCode | shared docs, adapters, provider config | file-backed handoffs and wrappers | no verified native hook or skill auto-load surface in current evidence | planning, review, synthesis, controlled manual orchestration |

## Which Hooks Fit Which Platform

### Windows Codex

Suitable:

- none as a verified native hook model in this runtime
- use skills, startup notes, and thread automation instead

Avoid:

- pretending there is a general hook API like Claude Code or OpenClaw

### Claude Code Desktop

Suitable:

- `UserPromptSubmit` for orchestration precheck and route suggestion
- `PreToolUse` for guardrails before risky tools
- `PostToolUse` for proof capture and closeout reminders
- `Notification` for idle or permission flow reminders
- slash commands for repeatable orchestration entry points

### OpenClaw / Kimi VPS

Suitable:

- `message:received` to suggest the best feature
- `agent:bootstrap` to inject mandatory startup files
- session or compaction hooks for continuity capture
- gateway restart hook for runtime health checks

Pair with:

- Task Flow for durable recurring state
- Lobster for bounded deterministic subflows
- cron only as a wake-up trigger

### Hermes

Suitable:

- only use verified local surfaces
- until a native hook system is proven, prefer file contracts and Linux timers

### OpenCowork / OpenCode

Suitable:

- adapters, wrapper scripts, and shared docs
- do not overclaim a native hook system until it is verified

## OpenClaw Workflow-Within-Workflow Pattern

The main recommended Chimera pattern is:

- standing order defines authority
- cron or timer wakes the work
- Task Flow owns durable recurring state
- Lobster owns a bounded deterministic subflow
- hooks enforce event-driven checks and routing hints
- background tasks provide detached-work audit and control

## Recommended OpenClaw Hooks

- `message-router`
  - suggest best feature based on the inbound request
- `mandatory-bootstrap`
  - inject the current must-read startup files
- `on_session_start`
  - remind the agent of the current shared contract
- `on_compact_before` and `on_compact_after`
  - preserve unfinished orchestration state
- `on_gateway_restart`
  - verify runtime health and gate state
