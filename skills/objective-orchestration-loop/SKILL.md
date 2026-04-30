---
name: objective-orchestration-loop
description: Run every meaningful task through a mandatory plan, execute, review loop until review says the objective is complete, blocked, or needs escalation. Use for orchestration-class selection, phase control, heartbeat continuation, quality gates, and platform-optimized model routing.
---

# Objective Orchestration Loop

Use this skill for any non-trivial task.

The default rule is:

`plan -> execute -> review -> repeat until complete`

Do not stop after one pass just because code changed or a report was written.

## First Decision: Pick The Right Orchestration Class

Before the first plan phase, classify the task into one of these four shapes:

1. `direct task`
   - one bounded step
   - little or no durable state
   - no recurring continuation path needed

2. `bounded build`
   - several implementation steps
   - may need heartbeats, retries, or proof loops
   - still centered on one concrete objective

3. `deep research swarm`
   - evidence-heavy research, thesis building, postmortems, large comparisons
   - multiple research dimensions
   - explicit verification and synthesis phases
   - use the separate `deep-research-swarm` skill

4. `always-on pipeline`
   - recurring monitor, watcher, or trading loop
   - should stay lean and stateful
   - must not turn every cycle into a full research swarm

If the task is not a research/report job, do not force it into the deep swarm.

## State Contract

Every meaningful pass should be able to restate the current state in this shape:

- `objective`
- `orchestration_class`
- `current_phase`
- `current_reality`
- `last_proof`
- `next_step`
- `stop_condition`

Use files, state notes, control files, or checkpoints when the task spans platforms or wakes.

## Mandatory Phases

### 1. Plan

Always begin by deciding:

- what the real objective is
- which orchestration class fits it
- what counts as done
- which platform should own each part
- which model and reasoning level fit this phase
- whether a heartbeat or recurring continuation path is needed

Plan output must name:

- objective
- orchestration class
- current reality
- done criteria
- last proof
- next execution step
- review checks
- stop condition

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

## Quality Gate Rule

Use explicit gates between major phases when the task has enough surface area to drift.

Good gate questions:

- did the required file or runtime artifact appear
- did the proof step actually validate the claim
- did the output meet the minimum quality bar
- is the next phase still the right route
- should a failed slice be rerun instead of advancing the whole task

For `deep research swarm`, gates should exist between:

- landscape and decomposition
- decomposition and parallel research
- research and cross-verification
- cross-verification and targeted validation
- validation and insight extraction
- insight extraction and writing

For `always-on pipeline`, gates should stay lean:

- input freshness
- setup validity
- conflict and risk validation
- decision quality
- position-state integrity

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

## Platform Worker Routing

When the task fans out into several workers, keep these roles distinct:

- `orchestrator`
  - owns decomposition, routing, gates, and stop decisions
- `worker`
  - does one bounded slice
- `verifier`
  - checks evidence, contradictions, or proof completeness
- `reviewer`
  - decides complete, iterate, or blocked

Cheap workers are preferred first.
Escalate only failed or ambiguous slices.

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

### Codex Thread Heartbeat Rule

When the platform is the Codex desktop app and the objective needs continuation in the current thread:

- create or update a thread heartbeat named `Thread Objective Completion Guard`
- use a moderate cadence such as every 30 minutes unless the task clearly needs faster follow-up
- keep the heartbeat concise and cheap first
- prefer the lowest-cost route that can still do the next bounded step well
- escalate reasoning or model only if review says the result is weak or ambiguous
- stop the heartbeat when review says `complete`
- stop the heartbeat when review says `blocked`
- stop the heartbeat after `3` consecutive wakes with no meaningful visible progress
- after that stop, require fresh manual user input before any further attempts

Important:

- a Codex thread heartbeat is attached to one thread, not all future threads
- therefore the enforcement rule is: any Codex thread that begins a real multi-pass orchestration should create or update its own guarded heartbeat when continuation is needed
- do not leave a Codex heartbeat running forever

If the platform does not support native recurring continuation:

- still use the same plan/execute/review logic
- leave behind a durable next-step handoff
- say plainly that the continuation path is manual or platform-limited

## Always-On Pipeline Rule

Do not run the full deep research swarm on every trading or monitoring cycle.

The lean pipeline loop should be:

1. monitor inputs
2. detect setup
3. gather only the needed specialists
4. validate freshness, conflicts, and risk
5. decide `execute`, `watch`, or `reject`
6. manage the position or state
7. review and update state

Use `deep-research-swarm` only when the job is materially larger than a normal cycle, such as:

- weekly BTC or market thesis
- major event-driven setup
- deep ambiguity needing cross-verification
- post-trade failure analysis

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
- orchestration class used
- result quality: `strong`, `acceptable`, or `weak`
- review outcome: `complete`, `iterate`, or `blocked`
- next better route if the result was weak

## Good Orchestration Example

`plan: objective = sync Kimi runtime standard`

`execute: install shared skills, bootstrap, continuity files`

`review: Kimi files exist, but fresh startup proof still missing`

`iterate: next pass should run fresh Kimi startup proof`

## Deep Research Example

`plan: objective = build a weekly BTC thesis`

`orchestration_class: deep research swarm`

`gate: do not start synthesis until dimension outputs and cross-verification exist`

`review: only rerun failed or contradictory dimensions`
