---
name: objective-orchestration-loop
description: Run every meaningful task through a visible orchestration precheck, then choose the lightest honest route: direct answer, bounded loop, deep swarm, or always-on pipeline.
---

# Objective Orchestration Loop

Use this skill on every message as a decision layer, not only on large tasks.

The model should always do a fast orchestration precheck, then say plainly:

- whether full orchestration is needed
- which orchestration class fits
- why that route fits better than the main alternatives
- what the done contract is

Do not silently skip this thinking for meaningful work.
Do not pretend a full loop ran when the direct route was the right choice.

## Core Rule

The default loop for meaningful work is:

`plan -> execute -> review -> repeat until complete`

But the skill must first decide whether that full loop is actually needed.

## Mandatory Per-Message Precheck

Before every non-trivial reply, decide one of these orchestration decisions:

1. `direct response`
   - the ask is small, self-contained, and should finish in one pass
   - no durable orchestration state is worth creating

2. `light orchestration`
   - still one pass, but the answer should show objective, route, and done contract
   - good for analysis, advice, comparisons, and bounded planning

3. `bounded build`
   - several real steps are needed
   - use the full `plan -> execute -> review` loop

4. `deep research swarm`
   - evidence-heavy research across dimensions with verification and synthesis
   - use the separate `deep-research-swarm` skill

5. `always-on pipeline`
   - recurring monitor or runtime loop
   - use the platform-native scheduler, flow, or runtime automation when available

The model should choose the lightest route that is still honest and sufficient.

## Automatic Trigger Cues

Treat the full loop as mandatory when the user asks for continued follow-through, not only when they name the skill.

Auto-trigger the stronger orchestration path when the request includes cues like:

- `continue until complete`
- `continue until done`
- `keep going`
- `until the objective is achieved`
- `until the contract is achieved`
- `do not stop`
- `stay on this`
- `use orchestration`
- `keep checking`
- `follow through`
- `work it until done`

When these cues appear:

- classify the orchestration shape before doing more work
- write or restate the done contract
- decide whether a continuation path is required on the current platform

## First Decision: Pick The Right Orchestration Class

Before the first plan phase, classify the task into one of these four shapes:

1. `direct task`
   - one bounded step
   - little or no durable state
   - no recurring continuation path needed

2. `bounded build`
   - several implementation or verification steps
   - may need retries, proof loops, or continuation
   - still centered on one concrete objective
   - may need a file-backed `plan.md`

3. `deep research swarm`
   - evidence-heavy research, thesis building, postmortems, large comparisons
   - multiple research dimensions
   - explicit verification and synthesis phases

4. `always-on pipeline`
   - recurring monitor, watcher, or trading loop
   - should stay lean and stateful
   - must not turn every cycle into a full research swarm

If the task is not a research or report job, do not force it into the deep swarm.

## Transparency Contract

For any meaningful task, the user should be able to see the contract without opening files.

Use this visible structure in the reasoning and, when helpful, in the user-facing answer:

- `orchestration_decision`
- `orchestration_class`
- `reason_for_route`
- `objective`
- `done_contract`
- `dimensions` when the work truly has several separable dimensions
- `current_phase`
- `next_step`
- `review_outcome`

Read `references/TRANSPARENCY_CONTRACT.md` for the compact output shape.

## File-First State Rule

When work fans out across workers, platforms, or wakes, do not trust chat memory as the state store.

Use files, control notes, checkpoints, or explicit artifacts as the real state.

For `deep research swarm`, that normally means:

- `plan.md`
- dimension outputs
- verification output
- insights output
- final deliverable output

## State Contract

Every meaningful pass should be able to restate the current state in this shape:

- `objective`
- `orchestration_class`
- `chosen_path`
- `current_phase`
- `current_reality`
- `done_criteria`
- `last_proof`
- `next_step`
- `stop_condition`
- `review_outcome`

Use `review_outcome` with only:

- `complete`
- `iterate`
- `blocked`

For multi-pass bounded builds and deep research swarms:

- keep this contract in a short file-backed `plan.md`
- prefer the template at `C:\Users\becke\claudecowork\workflows\codex\OBJECTIVE_PLAN_TEMPLATE.md`

For direct tasks:

- the contract can stay in-chat only

## Mandatory Phases

### 1. Plan

Always begin by deciding:

- what the real objective is
- which orchestration class fits it
- what counts as done
- which platform should own each part
- which model and reasoning level fit this phase
- whether a heartbeat, hook, slash command, Task Flow, Lobster, or scheduler should be involved
- whether a build council is needed before execution
- whether a file-backed `plan.md` is required

Plan output must name:

- objective
- orchestration class
- chosen path
- current reality
- done criteria
- last proof
- current phase
- next execution step
- review checks
- stop condition

Workflow choice should also be explicit.

Use:

- `C:\Users\becke\claudecowork\workflows\codex\WORKFLOW_CATALOG.md`

to choose the right loop for:

- direct software work
- bounded build
- major build with council
- project start
- project finish
- GitHub publish and shared sync
- dependency update
- test failure and proof repair
- workflow and skill promotion
- PM/front-door reconciliation
- trading and operator loops

If a major build or architecture tradeoff exists, route through:

- `major-build-council-orchestrator`
- `C:\Users\becke\claudecowork\workflows\codex\major-build-council-and-delivery-loop.md`

before normal execution continues.

### 2. Execute

Do the smallest real work that moves the objective forward.

Execution includes:

- code changes
- file updates
- repo sync
- live runtime checks
- bounded repairs
- safe installs
- platform-native configuration

### 3. Review

Review decides one of only three outcomes:

1. `complete`
2. `iterate`
3. `blocked`

Review must check:

- did the objective actually move
- did the files or runtime really change
- did the proof step match the claim
- did the output meet the minimum quality bar
- should the next pass stay on the same route
- should the next pass escalate model, reasoning, or platform

## Test And Verification Rule

Do not hide testing inside vague “review” language.

For meaningful implementation work, call out:

- `plan`
- `execute`
- `test or proof`
- `review`

If no real test ran, say so plainly.

## Dimensions Rule

Use dimensions only when they make the task easier to reason about.

Good dimension use:

- platform-by-platform research
- several independent failure modes
- several evidence lanes that need cross-verification
- multi-part design decisions like runtime, automation, routing, and UX

Bad dimension use:

- one tiny code fix
- a simple answer that does not benefit from fan-out

## Quality Gates

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
- if the platform does not expose a reliable quota surface, say `quota=not exposed`
- do not fake hidden model switches

## Platform Feature Routing

Read `references/PLATFORM_PHASE_MATRIX.md` for model routing and `references/PLATFORM_ORCHESTRATION_FEATURES_2026-05-01.md` for feature surfaces.

Key rule:

- do not claim a hook, heartbeat, or scheduler path exists on a platform unless it is verified there
- prefer platform-native enforcement when it exists
- otherwise fall back to skill, file, and handoff enforcement

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

## Heartbeat And Automation Rule

If the objective is larger than one pass and the platform supports recurring continuation:

- start or update the native continuation path
- keep it running until review says `complete` or `blocked`
- make it continue safe approved work only
- make it cheap first
- stop after repeated no-progress wakes

If the platform does not support native recurring continuation:

- keep the same logic in files and closeout
- leave behind a durable next-step handoff
- say plainly that the continuation path is manual or platform-limited

## Codex Thread Heartbeat Rule

When the platform is the Codex desktop app and the objective needs continuation in the current thread:

- create or update a thread heartbeat named `Thread Objective Completion Guard`
- choose cadence from the expected length of one meaningful pass
- do not create a heartbeat for a `direct task` that should finish in one pass
- stop the heartbeat when review says `complete`
- stop the heartbeat when review says `blocked`
- stop after `3` consecutive wakes with no meaningful visible progress

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

## Required Closeout

Every meaningful pass should capture:

- phase reached
- platform used
- model used
- reasoning used
- orchestration decision used
- orchestration class used
- result quality: `strong`, `acceptable`, or `weak`
- review outcome: `complete`, `iterate`, or `blocked`
- next better route if the result was weak

If the direct route was chosen, say why the full loop was not worth invoking.
