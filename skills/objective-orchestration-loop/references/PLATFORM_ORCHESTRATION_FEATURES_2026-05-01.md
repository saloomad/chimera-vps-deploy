# Platform Orchestration Features

Updated: 2026-05-01

## Windows Codex

- strongest verified surfaces:
  - shared skills
  - local `AGENTS.md` and bootstrap rules
  - subagents
  - thread-scoped continuation when the runtime exposes heartbeat or automation support
- limits:
  - no verified OpenClaw-style hook system in this runtime
  - do not claim a general cross-thread hook layer exists
- best enforcement:
  - orchestration precheck on every message
  - visible done contract
  - thread heartbeat only for real multi-pass work

## Claude Code

- strongest verified surfaces:
  - hooks
  - custom slash commands
  - subagents
  - `CLAUDE.md`
  - project and user settings
- limits:
  - no durable native continuation after the session closes
- best enforcement:
  - `UserPromptSubmit` hook for orchestration precheck
  - `PreToolUse` or `PostToolUse` hooks for guardrails
  - project slash commands for repeatable orchestration entry points

## OpenClaw / Kimi VPS

- strongest verified surfaces:
  - hooks
  - Lobster
  - Task Flow
  - background tasks
  - cron
  - standing orders
  - Linux service and timer layer
- limits:
  - workspace hooks are opt-in and disabled by default until enabled
  - features on disk are not the same as verified live usage
- best enforcement:
  - Task Flow owns durable recurring state
  - Lobster owns bounded deterministic subflows
  - hooks enforce event-driven rules
  - standing orders define authority
  - cron or timers only wake work

## Hermes VPS

- strongest verified surfaces:
  - shared instructions
  - Linux scheduler and service layer
  - file-first continuity
- limits:
  - no separately verified native hook or flow feature surface in the current evidence set
- best enforcement:
  - same orchestration contract
  - Linux-native scheduling when continuation is required
  - cross-platform review for weak or ambiguous outputs

## OpenCowork / OpenCode

- strongest verified surfaces:
  - shared docs and adapters
  - provider config
  - file-backed handoffs
- limits:
  - no verified native skill auto-load or hook system in the current evidence set
- best enforcement:
  - orchestration precheck in the platform adapter
  - file-backed plan, review, and handoff
  - route long-lived automation to a platform with a proven scheduler
