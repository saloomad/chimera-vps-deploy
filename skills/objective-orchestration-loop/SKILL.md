---
name: objective-orchestration-loop
description: Run every meaningful task through a visible orchestration precheck, then choose the lightest honest route among a direct answer, bounded loop, deep swarm, or always-on pipeline.
---

# Objective Orchestration Loop

Use this skill on every message as a decision layer, not only on large tasks.

The model should always do a fast orchestration precheck, then say plainly:

- whether full orchestration is needed
- which orchestration class fits
- why that route fits better than the main alternatives
- what the done contract is
- what open approvals and remaining work are still being carried forward

Do not silently skip this thinking for meaningful work.
Do not pretend a full loop ran when the direct route was the right choice.

## Core Rule

The default loop for meaningful work is:

`plan -> execute -> review -> repeat until complete`

But the skill must first decide whether that full loop is actually needed.

Important:

- `complete` means the user's real end objective is done
- it does **not** mean one bounded slice or mini-goal finished
- if one slice lands but the real objective is still open, the correct review outcome is `iterate`

Do not silently shrink the user's objective into whatever slice happened to be convenient in the current pass.

## Objective Hierarchy Rule

For any multi-pass task, the skill must track **two levels** of goal:

1. `ultimate_objective`
   - the real user-requested end state
   - this is the thing that decides whether orchestration is truly done

2. `current_slice`
   - the bounded iteration being worked right now
   - this can finish many times before the ultimate objective is done

The skill must never treat `current_slice complete` as `ultimate_objective complete`.

Examples:

- if the user wants `build, test, iterate until the system is good enough`, then:
  - adding one module is a slice
  - proving one symbol is a slice
  - the objective is only complete when the broader testing-and-iteration contract is satisfied

- if the user wants `compare these repos and implement the highest-value first slice`, then:
  - that first slice can be a real completion
  - but only if the original wording actually limited the objective to that slice

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
   - if runtime ownership is unclear, consult `pipeline-enforcement-detector`

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
- if the chosen owner is a same-thread heartbeat or Codex automation, create or update it in the same pass before claiming orchestration is active
- if the user also wants stronger enforcement, route to `hook-opportunity-detector` or `pipeline-enforcement-detector`

## Continuation Ownership Rule

When the work needs more than one pass, the orchestration layer must decide who owns continuation:

1. same-thread heartbeat
2. Codex cron automation
3. platform-native scheduler
4. no automation at all

Pick the lightest owner that can honestly finish the job.

- use a thread heartbeat for current-thread follow-through
- use a Codex automation for local recurring audits, reminders, and bounded executors
- use the platform scheduler when the real runtime owner is Linux cron, Windows Scheduled Tasks, or another always-on system
- do not say orchestration is "in effect" for a multi-pass Codex thread unless the continuation owner was actually created, updated, or explicitly verified as already active in this pass
- if the chosen owner is a thread heartbeat, reuse the current thread's heartbeat when it exists; otherwise create it immediately
- if no safe continuation owner was created or verified, report that as a blocker instead of pretending the orchestration path is live

Do not keep a Codex heartbeat alive forever just because it already exists.

## Automation Prompt Contract

If orchestration chooses an automation or recurring loop, the prompt must name:

- `ultimate objective`
- `current run mission`
- `evidence first`
- `resume from previous result`
- `allowed actions`
- `drift guard`
- `host unavailable rule`
- `review outcome rule`
- `output contract`

The automation must continue from the last unresolved blocker or proof gap before widening scope.

## Previous-Stage Resume Rule

Recurring work must not start each wake as if it is the first run.

Use file-backed state in this order:

1. last automation output or status file
2. latest handoff or observation ledger
3. current PM or task surface
4. fresh proof from this run

If those disagree:

- prefer fresh proof over older summaries
- say what changed
- keep the original objective unless the user explicitly replaced it

## Drift And Objective-Loss Guard

The automation or recurring loop may discover the next slice only when it still serves the same `ultimate_objective`.

Allowed:

- next missing proof
- next unresolved blocker
- next safe bounded fix
- next missing owner or receiver

Not allowed:

- starting a different project because the current one slowed down
- promoting a side observation into the new main goal
- calling the whole objective complete because one slice landed

If no meaningful progress was possible this run:

- record why
- preserve the objective
- decide `iterate` or `blocked` honestly

## Host-Unavailable Rule

When recurring work depends on a local machine or remote reachability:

- separate `host unavailable` from `system unhealthy`
- a missing local run can mean the PC was off or asleep
- a wrapper or SSH timeout can coexist with fresh remote artifacts
- do not claim everything is broken without independent evidence

If reachability is the only problem, say that plainly and avoid wider failure claims.

## Scrape Artifact Truth Rule

When a workflow is fundamentally a scraping or screenshot workflow:

- treat the captured artifact as the primary truth surface
- treat transport metadata, hidden API responses, or weak page-side status text as secondary signals
- if a usable screenshot, DOM artifact, OCR output, or extracted file exists, analyze that artifact before declaring the workflow blocked

Recovery order for scrape-driven lanes:

1. verify whether the real artifact exists
2. inspect the artifact directly
3. patch parser, crop, OCR, or replay assumptions if the artifact is usable but under-read
4. only then escalate auth/session/runtime blockers

Do not let `response missing`, `API empty`, or similar metadata become the reason a scrape workflow stops if the actual captured artifact can still be parsed honestly.

## Persistent Parent Bundle Rule

When a parent trading agent owns a reusable judgment lane and spawned children are expected to help:

- maintain `SPAWN_CONTEXT.md` and `THOUGHTS.md` as the default child handoff
- let spawned workers read those first before narrow task artifacts
- if a new screenshot or chart review worker is added, give it a bounded output contract and a parent consumer
- do not create orphan child analyses that never flow back into the summary or bundle

## Enforcement Decision Rule

If the objective includes words like:

- `enforce`
- `auto trigger`
- `hook`
- `workflow owner`
- `pipeline`
- `prove what fired`

then also consult:

- `C:\Users\becke\.codex\skills\hook-opportunity-detector\SKILL.md`
- `C:\Users\becke\.codex\skills\pipeline-enforcement-detector\SKILL.md`
- `C:\Users\becke\claudecowork\workflows\codex\platform-enforcement-selection-and-receipt-loop.md`

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
- `unapproved_items`
- `remaining_work`
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

- `ultimate_objective`
- `current_slice`
- `orchestration_class`
- `chosen_path`
- `current_phase`
- `current_reality`
- `unapproved_items`
- `remaining_work`
- `objective_done_criteria`
- `slice_done_criteria`
- `last_proof`
- `next_step`
- `stop_condition`
- `review_outcome`

Use `review_outcome` with only:

- `complete`
- `iterate`
- `blocked`

Interpret them strictly:

- `complete`
  - the `ultimate_objective` is done
- `iterate`
  - the current slice finished or moved the work, but the `ultimate_objective` is still open
- `blocked`
  - the `ultimate_objective` cannot safely continue without something external

For multi-pass bounded builds and deep research swarms:

- keep this contract in a short file-backed `plan.md`
- prefer the template at `C:\Users\becke\claudecowork\workflows\codex\OBJECTIVE_PLAN_TEMPLATE.md`

For direct tasks:

- the contract can stay in-chat only

## Carry-Forward Enforcement

On meaningful replies, the orchestration layer must keep a short carry-forward status block visible to the user.

That block must cover:

- `objective status`
  - `ultimate_objective`
  - `current_slice`
  - whether the broader objective is still open
- `unapproved or decision-needed items`
  - anything still waiting for approval, ranking, or confirmation
  - if none, say `none`
- `remaining project work`
  - the meaningful tasks still left before the broader objective is done
  - if none, say `none`

Formatting rule:

- aggregate the carry-forward items in one short block
- accumulate still-relevant open items from prior conversations when they belong to the same project objective; do not limit the block to the current thread only
- organize the block by project objective when more than one objective is still open
- for each open item, include a brief plain-English description
- say why it is still open or why it still matters

Do not let those items disappear just because the thread temporarily shifted to a side topic.
Do not pull in unrelated older work.
If a slice finished but the larger objective is still open, the carry-forward block must still show the unresolved work.

## Mandatory Phases

### 1. Plan

Always begin by deciding:

- what the real user objective is
- what the current bounded slice is
- which orchestration class fits it
- what counts as done
- which platform should own each part
- which model and reasoning level fit this phase
- whether a heartbeat, hook, slash command, Task Flow, Lobster, or scheduler should be involved
- whether a build council is needed before execution
- whether a file-backed `plan.md` is required

Plan output must name:

- ultimate objective
- current slice
- orchestration class
- chosen path
- current reality
- objective done criteria
- slice done criteria
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
- meaningful change lifecycle and enforcement
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

Review must not confuse slice completion with objective completion.

If a bounded implementation slice is done but the broader requested mission still requires more building, testing, or iteration:

- do **not** say `complete`
- say `iterate`
- restate the next slice against the same `ultimate_objective`

Review must check:

- did the objective actually move
- did only the slice complete, or did the real objective complete
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
