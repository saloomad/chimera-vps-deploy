# Agent Orchestration Mode

Use this mode when the point of the test is:
- what Deezoh would do
- what Deezoh would ask
- how the pipeline would react
- whether a new instruction or workflow build behaves better
- whether a failure condition is handled honestly

## Core Flow

1. Build or select the shared input truth.
   - historical bundle
   - synthetic scenario
   - live snapshot

2. Pick the variants to compare.
   - baseline
   - candidate
   - optional bull/bear/critic/judge review

3. Run each variant through a fresh agent session.
   - no hidden thread context
   - same scenario payload
   - same output contract

4. Capture the outputs.

5. Use deterministic helpers only after the runs.
   - validate JSON shape
   - score expectations
   - compare builds
   - package the report

6. If the top builds tie on deterministic scoring, run a judge agent.
   - do not pretend the tie is a finished answer
   - compare ownership clarity, routing quality, state discipline, and next-step clarity
   - record plainly that the judge broke the tie

## Output Contract

Each agent run should return JSON with:
- `scenario_name`
- `build_name`
- `understanding`
- `decision`
- `routing_line`
- `recommended_actions`
- `questions`
- `risks`
- `used_capabilities`
- `tags`
- `should_escalate`
- `should_block`
- `asked_question`
- `notes`

Contract rules:

- `asked_question` must be `true` whenever `questions` is non-empty.
- `should_escalate` means "needs advisory routing or human/owner attention"; it does not mean a specialist gets decision authority.
- `should_block` means "do not advance the trade/state until a required safety, freshness, or evidence problem is resolved."
- Specialist lanes recommend, warn, and falsify; they do not create locked gates unless a separate safety block is triggered.
- Active-trade scenarios should manage the open position. Do not reopen a fresh-entry debate unless invalidation, data failure, or regime change breaks the original thesis.

## Good Variant Shapes

`baseline_stage_questions`
- simpler stage-oriented read
- useful as a regression floor

`standard_loop_questions`
- asks the same small set of core questions every cycle
- useful for making sure the desk never skips the basics
- weak when the situation needs specialized evidence

`adaptive_question_routing`
- starts with the same core questions
- then selects follow-up questions and specialist lanes based on situation, phase, timeframe, and missing evidence
- useful for testing real Deezoh/Orchestrator behavior

`orchestrated_agent_first`
- classifies the situation
- checks timeframe ownership or conflict
- asks what evidence is still missing
- names which specialist lanes it would query
- prefers wait or no-trade over forcing a setup

## Iteration Rule

Use a bounded loop:
- run the first comparison
- inspect the first clear miss
- tighten the scenario, prompt, or contract
- rerun once
- if the rerun still ties, use the judge stage instead of inflating tags forever

Do not let this turn into an infinite retry loop.

## What To Judge

Score at least these:
- decision quality
- process quality
- honesty about uncertainty or missing data
- whether the right next questions were asked
- whether the right specialist lanes were named
- whether the compact routing line names the owner, current state, unblock condition, and next actor
- whether the system avoided forcing a trade
- whether Deezoh kept final decision ownership instead of letting a specialist gate the trade
- whether Orchestrator routed, tracked, and recorded the follow-up work

## Stop Rule For This Objective

The active simulation heartbeat can stop only when:

- the scenario pack covers at least:
  - stale input
  - missing strategy proof
  - timeframe conflict
  - pre-event fakeout
  - liquidity trap or crowded derivatives
  - active trade management
  - no-trade / stand-down
- judge-on-tie is built into the normal loop
- Deezoh question behavior has been tested against standard-loop and adaptive-routing variants
- the results are recorded in task, action, and continuity files
- any live OpenClaw behavior change has either been mirrored and verified or clearly left as a blocked follow-up
