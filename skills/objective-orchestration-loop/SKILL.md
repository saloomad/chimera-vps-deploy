---
name: objective-orchestration-loop
description: Run every meaningful task through a mandatory plan, execute, review loop until review says the objective is complete, blocked, or needs escalation. Use for orchestration, phase control, heartbeat continuation, and platform-optimized model routing.
---

# Objective Orchestration Loop

Use this skill for any non-trivial task.

The default rule is:

`plan -> execute -> review -> repeat until complete`

Do not stop after one pass just because code changed or a report was written.

## Mandatory Phases

### 1. Plan

Always begin by deciding:

- what the real objective is
- what counts as done
- which platform should own each part
- which model and reasoning level fit this phase
- whether a heartbeat or recurring continuation path is needed

Plan output must name:

- objective
- current reality
- done criteria
- next execution step
- review checks

### 2. Execute

Do the smallest real work that moves the objective forward.

Execution includes:

- code changes
- file updates
- repo sync
- live runtime checks
- bounded repairs
- safe installs

If execution reveals new facts, update the plan and keep going.

### 3. Review

Review decides one of only three outcomes:

1. `complete`
2. `iterate`
3. `blocked`

Review must check:

- did the objective actually move
- did the files or runtime really change
- did the proof step match the claim
- should the next pass stay on the same model
- should the next pass escalate model or reasoning

If review says `iterate`, go back to plan with the new facts and continue.

If review says `blocked`, capture the blocker durably and stop honestly.

## Runtime Header

Start user-facing replies with:

`Runtime: model=<name> | reasoning=<effort> | quota=<value-or-not-exposed> | phase=<plan|execute|review|mixed> | why=<short reason>`

Rules:

- use the real active model and reasoning level
- try to read quota or usage from the platform's native CLI or config helper first
- if the platform does not expose a reliable quota surface, say `quota=not exposed`
- do not fake hidden model switches

## Model Routing By Phase

Read `references/PLATFORM_PHASE_MATRIX.md` for the platform matrix.

Default routing pattern:

- `plan`: strongest available planning model with higher reasoning
- `execute`: cheaper stable implementation model
- `review`: stronger review model if the result is ambiguous, otherwise stable bounded review model

## Phase Escalation Rule

If review says the output is weak:

1. raise reasoning first
2. split mixed work into cleaner phases
3. rerun review on a stronger model
4. rerun execution on a stronger model only if needed

Do not keep looping on the same weak route without explaining why.

## Heartbeat Rule

If the objective is larger than one pass and the platform supports recurring continuation:

- start or update a heartbeat or recurring automation
- keep it running until review says `complete` or `blocked`
- make the heartbeat continue safe approved work only
- make the heartbeat update continuity, task, and action truth after meaningful progress

If the platform does not support native recurring continuation:

- still use the same plan/execute/review logic
- leave behind a durable next-step handoff
- say plainly that the continuation path is manual or platform-limited

## Platform Optimization Rule

Keep the same logic across platforms, but adapt to the real local home:

- Windows Codex: `C:\Users\becke\.codex\`
- Windows Claude Code: `C:\Users\becke\.claude\`
- OpenCode: `C:\Users\becke\.config\opencode\`
- Kimi VPS: `/root/.kimi/`
- OpenClaw workspace: `/root/openclawtrading/` and legacy `.openclaw/workspace` surfaces when still relevant
- Hermes VPS: `/root/.hermes/`

Do not blindly copy Windows-only paths, CLI assumptions, or automation claims into Linux platforms.

## Required Closeout

Every meaningful pass should capture:

- phase reached
- platform used
- model used
- reasoning used
- result quality: `strong`, `acceptable`, or `weak`
- review outcome: `complete`, `iterate`, or `blocked`
- next better route if the result was weak

## Good Orchestration Example

`plan: objective = sync Kimi runtime standard`

`execute: install shared skills, bootstrap, continuity files`

`review: Kimi files exist, but fresh startup proof still missing`

`iterate: next pass should run fresh Kimi startup proof`
