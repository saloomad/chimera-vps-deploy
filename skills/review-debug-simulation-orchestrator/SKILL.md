---
name: review-debug-simulation-orchestrator
description: Coordinate review, debugging, simulation, replay, backtest, and red-team work for any system. Use when the task is to find what is wrong, understand why it is wrong, compare alternatives, simulate behavior, test failure scenarios, or turn repeated misses into durable fixes.
---

# Review Debug Simulation Orchestrator

Use this as the universal top-level lane for:

- what is broken here
- why did this fail
- what did we miss
- compare old vs new behavior
- simulate the workflow
- replay this without waiting
- backtest this logic
- red-team this system
- turn this failure into a durable improvement

## Core Rule

Do not default to scripts for everything.

Use:

- agent reasoning first for diagnosis, critique, hypothesis generation, and scenario review
- deterministic scripts second for repeatable checks, replay fixtures, scoring, and regression protection

If the question is mainly:

- "what is the bug"
- "what reasoning failed"
- "what did the system miss"
- "what scenarios will break this"

then start with reasoning review, not just a script.

## Read First

Read the support files in `references/` only as needed:

- `mode-selection.md`
- `failure-taxonomy.md`
- `scenario-pack-schema.md`
- `external-patterns.md`
- `OUTPUT_CONTRACT.md`
- `DEFAULT_RED_TEAM_PACK.md`

## Required Inputs

Before acting, identify:

1. target
   - code path
   - workflow
   - document
   - agent
   - strategy
   - control layer
2. failure class
   - structural
   - behavioral
   - reasoning
   - data quality
   - safety
   - performance
3. proof need
   - diagnosis only
   - deterministic validation
   - replay
   - simulation
   - backtest
   - red-team
   - A/B comparison

## Route Selection

Pick the lightest honest lane:

- `reasoning review`: use first when the output feels wrong or the main question is what reasoning failed
- `deterministic artifact check`: use for file, field, contract, and route presence
- `replay`: use for historical or snapshot behavior proof without waiting for live outcomes
- `simulation`: use for what-would-happen scenario testing, with agents first and scripts for fixtures and scoring
- `strategy backtest`: use for edge, walk-forward, or trade-logic quality over history
- `red-team`: use for hostile, contradictory, stale, or illegal-input tests
- `A/B comparison`: use the same fixtures and rubric to compare old vs new
- `learning capture`: use when the issue repeats and should become durable process improvement

## Failure Taxonomy

Classify failures explicitly. Common cases:

- wrong or stale front door
- source exists but consumer ignores it
- contract field missing
- workflow transition illegal or unclear
- reasoning weak despite passing structure checks
- no-trade should win but activation still wins
- replay passes but live runtime remains unproven
- contradiction between agents, workflows, or state owners

## Required Outputs

A good run leaves:

1. one named target
2. one chosen lane
3. one explicit failure taxonomy
4. one result matrix:
   - passed
   - failed
   - still unproven
5. one prioritized improvement list
6. one owner map
7. one durable learning capture when the issue matters beyond the session

## Mandatory Debug Verdict Bundle

The run is incomplete unless it leaves one explicit debug verdict bundle with:

- `target`
- `route`
- `minimal_failing_repro`
- `expected_vs_observed`
- `hypothesis`
- `counter_hypothesis`
- `first_bad_transition`
- `suspected_owner`
- `evidence_used`
- `deterministic_check`
- `winner_or_verdict`
- `regressions`
- `still_unproven`

If the issue is qualitative, say which fields came from reasoning review and which came from deterministic checks.

## When To Spawn Agents

Spawn or use a council when:

- diagnosis is open-ended
- more than one explanation is plausible
- qualitative judgment matters
- you need critique of instructions, decisions, or user usefulness

Do not hide behind scripts when the real question is qualitative.

## Agent-Run Evidence Contract

If the chosen lane is behavior review, simulation, or council critique, do not claim agent behavior was proven unless you captured:

- per-variant transcript, session log, or equivalent agent output artifact
- final decision or verdict artifact
- questions asked
- lanes consulted
- why any helper-only run was downgraded to preflight or prompt/scoring simulation

## Canonical Real Agent-Run Path

When the route is agent-first, use this default path unless the target needs something narrower:

1. run in the current Codex thread or a bounded council
2. use `2` to `3` roles by default:
   - primary diagnosis
   - skeptical challenger
   - builder or remediation when needed
3. write artifacts under `trace/review-debug/<target-or-date>/` or `docs/review-debug/<target-or-date>/`
4. leave `transcript`, `verdict`, and `scorecard` artifacts
5. if that did not happen, label the result `preflight`, `prompt/scoring simulation`, or `deterministic-only review`

Helper-script commands are preflight only unless those agent artifacts exist.

## Local Eval Front Door

On this machine, prefer the stable local wrapper instead of calling a cache-hash-specific plugin-eval path directly:

- `python C:\Users\becke\claudecowork\scripts\plugin_eval_local.py analyze <skill-or-plugin-path> --format markdown`

Use this after a skill change when you want a repeatable local score for token cost, clarity, or route discipline.

## When To Prefer Scripts

Prefer scripts when:

- the check must be repeatable
- the result must be machine-readable
- you need regression protection
- the runner should work under cron, CI, or detached workflows

## External Patterns To Borrow

Use these ideas without copying them blindly:

- LangSmith: dataset + evaluator + experiment structure
- Promptfoo: red-team scenario packs and failure reports
- Braintrust: side-by-side experiment comparison and ongoing scoring

## Closeout Standard

The run is not good enough unless it says:

- what failed
- what was only suspected
- what scripts proved
- what only reasoning review found
- what should be changed next
- what remains unproven
- whether the default adversarial pack was exercised or explicitly skipped
