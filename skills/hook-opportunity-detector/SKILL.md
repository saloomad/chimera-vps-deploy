---
name: hook-opportunity-detector
description: Detect when a repeated instruction, risky event, or explanation failure should become a hook or automatic event reaction instead of staying a manual reminder.
triggers:
  - this should auto trigger
  - this needs a hook
  - make this automatic
  - enforce on event
  - stop me from forgetting this
---

# Hook Opportunity Detector

Use this skill when the system keeps relying on reminders but the better answer is an event-driven reaction.

## Auto Trigger Rules

Create or update a hook-oriented surface when any of these are true:

1. the same reminder happens before every meaningful task
2. a risky tool call should be checked before it runs
3. proof or closeout should be checked after a tool runs
4. the agent keeps trying to stop before the objective is truly done
5. the same user frustration comes from a missed event guard
6. a platform can react automatically at prompt start, tool use, stop, session start, or runtime events
7. risky control-layer files keep being edited without the right workflow
8. compaction keeps causing missing continuation, PM drift, or lost objective state

## Read First

- `C:\Users\becke\claudecowork\docs\PLATFORM_ORCHESTRATION_AND_HOOKS_MATRIX_2026-05-02.md`
- `C:\Users\becke\claudecowork\docs\ENFORCEMENT_IMPLEMENTATION_INVENTORY_2026-05-02.md`
- `C:\Users\becke\claudecowork\docs\PLATFORM_WORKFLOW_AND_SKILL_ENFORCEMENT_CATALOG_2026-05-02.md`
- `C:\Users\becke\claudecowork\workflows\codex\platform-enforcement-selection-and-receipt-loop.md`
- `C:\Users\becke\.codex\skills\codex-feature-opportunity-detector\SKILL.md`

## Decision Order

1. confirm the pattern is repeated enough to deserve automation
2. choose the platform-native hook surface when it is real
3. if a real hook surface is not proven, fall back to:
   - commands
   - permissions
   - file-backed plans
   - startup docs
   - workflows
4. add an activation receipt path when possible
5. update the inventory and workflow catalog

## Platform Guidance

### Claude Code

Best events:

- `UserPromptSubmit`
- `SessionStart`
- `PreToolUse`
- `PostToolUse`
- `PostToolUseFailure`
- `Stop`
- `SubagentStop`
- `InstructionsLoaded`
- `ConfigChange`
- `FileChanged`
- `PreCompact`
- `PostCompact`

### OpenClaw

Best surfaces:

- hooks for runtime events
- plugin hooks when deeper interception is needed

### OpenCowork

Best surfaces:

- local plugin hooks
- local plugin commands
- local local-skill bundle

### OpenCode

No separately proven native hook API in this project right now.
Use agents, commands, rules, skills, permissions, and review gates instead of pretending a hook exists.

## Minimum Output

When this skill triggers, leave behind:

1. the trigger pattern
2. the chosen platform surface
3. why that surface fits better than the alternatives
4. the activation receipt path
5. the follow-up docs or skill updates needed
6. whether risky control-layer or compaction governance also needs the critical guard workflow
