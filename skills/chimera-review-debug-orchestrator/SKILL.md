---
name: chimera-review-debug-orchestrator
description: "Route Chimera or OpenClaw reviews into the right proof lanes and use agent reasoning first for diagnosis. Use when the task is to find what is broken, explain why it is broken, simulate scenarios, compare alternatives, red-team workflow failures, or turn repeated misses into durable fixes."
---

# Chimera Review Debug Orchestrator

Use this skill when the question is:

- what is broken in this system
- where can this workflow fail
- how do we review this honestly
- should this use replay, simulation, or backtest
- turn this failure into a durable fix
- compare two workflow versions
- prove that an improvement really helped

## Read First

Always read:

- `C:\Users\becke\.codex\CHIMERA_BOOTSTRAP.md`
- `C:\Users\becke\.codex\skills\review-debug-simulation-orchestrator\SKILL.md`
- `C:\Users\becke\.codex\skills\objective-orchestration-loop\SKILL.md`

Open these only when needed:

- `openclaw-orchestration-proof-router`
- `pipeline-simulation-lab`
- `openclaw-replay-and-backtest`
- `strategy-backtest-lab`
- `chimera-bundle-consumer-simulation`
- `learning-loop`
- `chimera-hybrid-scenario-lab`
- `references/source-patterns.md`
- `references/CHIMERA_FAILURE_MAP.md`
- `references/CHIMERA_AGENT_FIRST_NOTES.md`
- `references/CHIMERA_ROUTE_OVERRIDES.md`
- `references/CHIMERA_RED_TEAM_CASES.md`
- `references/CHIMERA_AB_JUDGING_NOTES.md`
- `references/CHIMERA_DEBUG_VERDICT_TEMPLATE.md`

## What This Skill Does

This is the Chimera adapter skill.

It sits on top of the universal router and does not replace:

- `review-debug-simulation-orchestrator`
- `pipeline-simulation-lab`
- `strategy-backtest-lab`
- `openclaw-replay-and-backtest`
- `chimera-bundle-consumer-simulation`
- `learning-loop`

It chooses between them for Chimera-specific targets and turns the result into:

- a bug list
- a failure matrix
- a next-fix plan
- a durable learning item

When the target is the screener-to-bundle-to-trade lifecycle itself, also read:

- `C:\Users\becke\.codex\skills\chimera-lifecycle-review-council\SKILL.md`

## Agent-First Rule

Do not default to scripts for open-ended bug-finding.

Start with agent reasoning or a council when the question is:

- why did Deezoh make the wrong choice
- what did the workflow miss
- why does the packet feel wrong even when contracts pass
- what scenario would break this
- what was the strongest rejected alternative

Use scripts only as helpers when the question is:

- does the file exist
- does the field exist
- does replay still pass
- does the contract or invariant hold

When the synthetic-vs-natural comparison lane exists, treat it as a live follow-through surface, not just a report.

Minimum review questions:

- if a natural analogue is still unresolved, who should act next and why
- has the unresolved case become `aging_watch` or `stale_watch`
- should the current green proof be blocked until the stale case is reviewed
- if a real outcome exists, was the synthetic lesson `right`, `late`, `wrong`, or still incomplete

## Route Selection

Choose the lightest honest proof lane:

- `reasoning review or council`: first when the failure is qualitative, ambiguous, or behavior-driven
- `live packet and workflow check`: when the question is whether current runtime artifacts are honest
- `system replay`: lifecycle proof without waiting for live outcomes
- `pipeline behavior simulation`: what Deezoh, Lobster, Task Flow, or the workflow would do
- `strategy backtest`: edge, returns, win rate, walk-forward behavior, or indicator logic
- `bundle consumer review`: whether the document or packet helps Deezoh choose well
- `red-team or mutation review`: contradictory, stale, partial, or illegal inputs
- `learning capture`: repeated misses that should become tracked improvements
- `hybrid scenario matrix`: whether enough market conditions and progression paths were actually tested

## Canonical Chimera Agent-Run Path

For qualitative Chimera review, default to:

1. one primary reviewer
2. one skeptic or challenger
3. one builder or fixer when the issue is actionable

Default artifact sinks:

- `trace/review-debug/chimera/` for transcripts and interim verdicts
- `research/platforms/` for the durable plain-English proof note
- `reports/auto/CHIMERA_REVIEW_DEBUG_REPORT.json` when a machine-readable verdict is needed

If these artifacts do not exist, do not claim the Chimera lane had a real agent-run review. Call it:

- `preflight`
- `prompt/scoring simulation`
- or `deterministic-only proof`

## Required Outputs

Every run should leave:

1. one named target
2. one chosen proof lane
3. one list of failure situations or weak spots
4. one result matrix:
   - passed
   - failed
   - still unproven
5. one improvement owner map
6. one durable learning capture or queue update

## Mandatory Chimera Debug Verdict

Every meaningful run must answer:

- why this symbol won
- why the strongest alternative lost
- which artifact, owner, or transition flipped the decision
- what single smallest change would most likely have prevented the miss

Also leave one compact verdict bundle using `references/CHIMERA_DEBUG_VERDICT_TEMPLATE.md`.

## Failure Situation Checklist

Check these classes explicitly:

- stale or wrong front-door wrapper
- source file exists but consumer does not use it
- packet exists but phase ownership is wrong
- lifecycle state can jump illegally
- no-trade should have won but activation still happened
- active trade exists but management packet is missing
- closeout should exist but review is missing
- replay passes but live runtime is still unproven
- section backtest passes but whole workflow still fails
- workflow says one thing, Task Flow says another, Lobster says another
- scripts pass but decision causality is still unclear
- simulation grades against derived expectations instead of observed truth
- routing is correct mechanically but the wrong symbol or wrong side still wins

## Current Chimera Default Test Stack

For the trade lifecycle, default to:

- scenario pack: `python scripts/run_chimera_review_debug_scenario_pack.py`
- council prompt-pack: `python scripts/build_chimera_council_case.py --mode prompt-pack --scenario <scenario-json>`
- council coverage: `python scripts/run_chimera_council_trace_coverage.py`
- fixture roots:
  - `trading_system/scripts/labs/fixtures/chimera_scenario_packs/agent`
  - `trading_system/scripts/labs/fixtures/chimera_scenario_packs/pipeline`
  - `trading_system/scripts/labs/fixtures/chimera_scenario_packs/invariants`
- live surfaces:
  - `scripts/run_chimera_trade_lifecycle_cycle.sh`
  - `reports/auto/CHIMERA_LIFECYCLE_CONTEXT.json`
  - `reports/auto/SYMBOL_LIFECYCLE_STATE.json`
- replay: `scripts/full_lifecycle_replay.py`
- consumer review: `chimera-bundle-consumer-simulation`
- learning sink: `reports/auto/LIFECYCLE_LEARNING_QUEUE.json`
- real council trace sink: `trace/review-debug/chimera-lifecycle/`
- local skill eval: `python C:\Users\becke\claudecowork\scripts\plugin_eval_local.py analyze C:\Users\becke\.codex\skills\chimera-review-debug-orchestrator --format markdown`

## Real Council Trace Rule

Do not call the Chimera council harness strong just because one trace exists.

Require:

- one complete saved trace for each active adversarial Chimera scenario family
- `transcript.md`
- `verdict.json`
- `scorecard.json`
- trace coverage proof from `scripts/run_chimera_council_trace_coverage.py`

## Current Known Weak Spots

Be especially skeptical of:

- circular grading inside synthetic snapshot scenarios
- prompt-rendering or scoring frameworks that claim agent-first without running real isolated agents
- stale `_remote_edit` replay surfaces
- helper-grade sections that still pass a loose narrative review but fail the stricter quality gate

## Improvement Standard

Do not stop at "pass" if the system still cannot answer:

- why this symbol won
- why the alternative lost
- who caused the wrong transition
- what smallest repro shows the failure
- what should be patched first

## Replay Divergence Protocol

When replay is part of the proof:

1. freeze the fixture set
2. run each relevant producer, consumer, and state transition in order
3. record the first divergence from the expected state
4. classify the fault as:
   - producer
   - consumer
   - ownership logic
   - scoring/eval logic
5. do not stop at "replay failed" without naming that first divergence

## Closeout Standard

The run is only good if it says:

- what failed
- where it failed
- why that proof lane was the right one
- what should be changed next
- what is still unproven
