# Platform Orchestration And Hooks Matrix

Updated: 2026-05-02

## What This Is

This document answers one practical question:

"When we want to force the system to do the right thing, which enforcement surface should we use on each platform?"

## Shared Rule For Any Meaningful Change

Every meaningful create, build, fix, refactor, workflow change, skill change, or automation change should cover:

1. the workflow
2. the enforcement surface
3. the implementation
4. dependent surfaces that also need updating
5. testing and proof
6. implementation review
7. documentation
8. continuity and PM updates
9. monitoring or follow-through
10. complete vs iterate vs blocked review

If a change only exists in one file and nowhere else was updated, it is probably incomplete.

## The Main Enforcement Choices

- `instruction`
- `skill`
- `workflow`
- `detector`
- `hook`
- `slash command`
- `Task Flow`
- `Lobster`
- `standing order`
- `scheduler`
- `monitor`
- `wrapper script`

## Platform Summary

### OpenClaw / Kimi VPS

Best native enforcement surfaces:

- workspace hooks
- Task Flow
- Lobster
- standing orders
- cron or Linux timers
- background tasks

Use them like this:

- hooks for event-driven checks, routing hints, bootstrap injection, and continuity capture
- Task Flow for restart-safe recurring state across a larger program
- Lobster for smaller deterministic subflows inside the larger recurring program
- standing orders for ongoing authority, boundaries, and escalation rules
- cron or timers for wake-up cadence, not for owning business logic
- background tasks for detached work audit and control

Best OpenClaw hook jobs:

- `message:received`
- `agent:bootstrap`
- `session start`
- `pre-compact` and `post-compact`
- `gateway restart`

Do not use OpenClaw hooks for:

- heavy long-running orchestration
- exact-time scheduling
- full recurring-state ownership

Use Task Flow or a scheduler-backed loop for those.

### Claude Code

Best native enforcement surfaces:

- hooks
- slash commands
- `CLAUDE.md`
- subagents

Verified current hook events from the official Claude Code docs include:

- `UserPromptSubmit`
- `UserPromptExpansion`
- `PreToolUse`
- `PermissionRequest`
- `PermissionDenied`
- `PostToolUse`
- `PostToolUseFailure`
- `PostToolBatch`
- `SubagentStart`
- `SubagentStop`
- `TaskCreated`
- `TaskCompleted`
- `Stop`
- `StopFailure`
- `Notification`
- `InstructionsLoaded`
- `ConfigChange`
- `CwdChanged`
- `FileChanged`
- `WorktreeCreate`
- `WorktreeRemove`
- `PreCompact`
- `PostCompact`
- `SessionStart`
- `SessionEnd`
- `Elicitation`
- `ElicitationResult`
- `TeammateIdle`

The practical ones we should use most:

- `UserPromptSubmit` for orchestration precheck, starter-stack reminders, and prompt shaping
- `PreToolUse` for risky-command guardrails, write-scope checks, and workflow checks
- `PostToolUse` for proof capture, "what else must be updated" reminders, and closeout enforcement
- `PostToolUseFailure` for failure capture and retry routing
- `PostToolBatch` for batch review
- `Stop` for blocking premature closeout
- `SubagentStop` for subagent proof and integration review
- `TaskCreated` and `TaskCompleted` when task gating matters
- `InstructionsLoaded` for checking loaded instruction layers
- `PreCompact` and `PostCompact` for continuity capture
- `SessionStart` and `SessionEnd` for startup reminders and final capture

Hook handler types in Claude Code:

- `command`
- `http`
- `mcp_tool`
- `prompt`
- `agent`

Important Claude Code limits:

- hooks cannot do all orchestration for you
- `PostToolUse` cannot undo an action that already happened
- `Stop` fires when the answer ends, not only when the task is truly complete
- continuation after close still depends on files or another platform

### OpenCowork / OpenCode

Current honest truth:

- we do not have a separately verified native hook surface here like Claude Code or OpenClaw

So the best enforcement surfaces here are:

- startup docs
- wrappers
- file-backed `plan.md`
- shared skills
- shared workflows
- explicit handoffs
- review gates

Do not pretend OpenCowork has a proven hook API until it actually does.

## Recommended Default By Need

If the need is:

- "force good startup behavior"
  - use startup docs, bootstrap hooks, or `UserPromptSubmit`
- "force risky tool guardrails"
  - use `PreToolUse` or OpenClaw event hooks
- "force proof and closeout"
  - use `PostToolUse`, `Stop`, `SubagentStop`, and the closeout workflows
- "force recurring ownership"
  - use Task Flow plus standing orders
- "force event reaction"
  - use hooks
- "force exact cadence"
  - use cron or timers
- "force repeated step sequence"
  - use a workflow
- "force reusable agent behavior"
  - use a skill
- "force the system to notice drift"
  - use a monitor or detector
