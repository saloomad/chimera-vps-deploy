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
  - use when the behavior should guide the agent before work starts
- `skill`
  - use when the behavior should be reusable by agents directly
- `workflow`
  - use when the behavior is a step-by-step sequence
- `detector`
  - use when the system should notice that a skill or workflow is missing or should activate
- `hook`
  - use when the behavior should run automatically on an event
- `slash command`
  - use when the user or agent should be able to trigger a repeatable entry point on demand
- `Task Flow`
  - use when OpenClaw needs durable recurring multi-step state
- `Lobster`
  - use when OpenClaw needs a bounded deterministic subflow
- `standing order`
  - use when recurring work needs ongoing authority and boundaries
- `scheduler`
  - use when the system needs a wake-up or cadence
- `monitor`
  - use when drift, repeated failure, or stale behavior should be detected later
- `wrapper script`
  - use when a platform lacks stronger native hooks and needs a repeatable wrapper

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

- `hooks`
  - for event-driven checks, routing hints, bootstrap injection, and continuity capture
- `Task Flow`
  - for restart-safe recurring state across a larger program
- `Lobster`
  - for smaller deterministic subflows inside the larger recurring program
- `standing orders`
  - for ongoing authority, boundaries, and escalation rules
- `cron or timers`
  - for wake-up cadence, not for owning business logic
- `background tasks`
  - for detached work audit and control

Best OpenClaw hook jobs:

- `message:received`
  - detect the request type and suggest the right feature or workflow
- `agent:bootstrap`
  - inject must-read startup files and current guardrails
- `session start`
  - enforce the current contract at the beginning of work
- `pre-compact` and `post-compact`
  - preserve unfinished objective state around compaction
- `gateway restart`
  - run runtime health checks or restore required context

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

- `UserPromptSubmit`
  - before the main answer starts
  - best for orchestration precheck, starter-stack reminders, and prompt shaping
- `PreToolUse`
  - before a tool runs
  - best for risky-command guardrails, write-scope checks, and "did we choose the workflow yet" checks
- `PostToolUse`
  - after a tool succeeds
  - best for proof capture, "what else must be updated" reminders, and closeout enforcement
- `PostToolUseFailure`
  - after a tool fails
  - best for debugging guidance, retry routing, and failure capture
- `PostToolBatch`
  - after a batch of tool calls
  - best for batch review or "run monitor / review now" checks
- `Stop`
  - when Claude is about to stop
  - best for blocking premature closeout if review is still missing
- `SubagentStop`
  - when a subagent finishes
  - best for requiring proof or integration review before accepting the subagent result
- `TaskCreated` and `TaskCompleted`
  - best when task creation/completion itself should be gated
- `InstructionsLoaded`
  - best for confirming the instruction layer loaded correctly
- `PreCompact` and `PostCompact`
  - best for continuity capture around compaction
- `SessionStart` and `SessionEnd`
  - best for startup reminders and final capture

- `InstructionsLoaded`
  - best for confirming that startup rules, shared context pointers, and the starter stack were actually loaded

- `ConfigChange`
  - best for forcing the risky control-layer workflow when settings, instructions, or routing config change

- `FileChanged`
  - best for reacting when control-layer files such as `AGENTS.md`, `CLAUDE.md`, `opencode.json`, skills, workflows, or PM continuity files change

- `PreCompact` and `PostCompact`
  - best for protecting continuation, PM state, objective state, and proof state around compaction

Hook handler types in Claude Code:

- `command`
  - best default for production use
- `http`
  - good when the hook should call a service
- `mcp_tool`
  - good when the enforcement is best exposed through MCP
- `prompt`
  - useful for policy checks with an LLM
- `agent`
  - experimental; use carefully, and prefer command hooks for critical production behavior

Important Claude Code limits:

- hooks cannot magically do all orchestration for you
- `PostToolUse` cannot undo an action that already happened
- `Stop` fires when the answer ends, not only when the task is actually complete
- continuation after close still depends on files or another platform

### Control-Layer Hook Policy

When the changed file is part of the control layer, the system should not treat it like a normal code edit.

Treat these as control-layer files:

- `AGENTS.md`
- `CLAUDE.md`
- startup docs
- `.claude/settings.json`
- `opencode.json`
- `.opencode/*`
- local plugin registry or bundle files
- skill files
- workflow files
- detector files
- continuation, kanban, work-log, task, or PM front-door files

For these changes, prefer:

- `PreToolUse`
  - warn or block casual edits
  - require `critical-change-guard`
- `PostToolUse`
  - require proof, dependent-surface review, and continuity update
- `Stop`
  - prevent closeout until the risky control-layer workflow is reviewed
- `FileChanged`
  - route to `critical-config-instruction-and-compaction-guard-loop.md`

### Compaction Continuity Policy

Use compaction hooks to force state capture before context is compressed away.

Before compaction:

- save objective state
- save current slice
- save proof path
- save PM state if it changed
- save continuation next step

After compaction:

- restore the objective contract
- restate the next step
- verify PM and continuation files are still the truth source
- decide whether the result is `iterate`, `complete`, or `blocked`

### OpenCowork / OpenCode

Current honest truth:

- we still do not have a separately verified native hook surface here like Claude Code or OpenClaw
- but OpenCode does have verified native project surfaces for:
  - `AGENTS.md` rules
  - `opencode.json` config
  - custom agents
  - custom commands
  - native skill discovery
  - permission rules

So the best enforcement surfaces here are:

- startup docs and rules
- project config
- native agents
- native commands
- native skills
- permission rules
- file-backed `plan.md`
- shared workflows
- explicit handoffs
- review gates

Use them like this:

- `startup docs and rules`
  - load the starter stack and current guardrails
- `project config`
  - set default agent, permission guardrails, and shared instruction files
- `native agents`
  - separate planning, build, and review roles cleanly
- `native commands`
  - give repeatable entry points like objective start, review, and close
- `native skills`
  - load reusable process knowledge on demand
- `permission rules`
  - slow down risky shell or file actions without blocking normal work
- `plan.md`
  - hold state for multi-step work
- `shared workflows`
  - enforce the process shape
- `handoffs`
  - enforce continuation across sessions

Do not pretend OpenCode has a proven hook API until it actually does.

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

## Best Chimera Pattern

For most OpenClaw recurring systems:

- standing order gives authority
- scheduler wakes the work
- Task Flow owns the durable recurring state
- Lobster owns bounded deterministic subflows
- hooks enforce event-driven checks and routing
- monitors detect drift
- closeout workflows decide complete vs iterate vs blocked
