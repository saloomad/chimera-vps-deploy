---
name: pipeline-simulation-lab
description: Simulate and compare Chimera desk behavior using scenarios, snapshots, and desk-variant A/B tests. Use when the task is to test Deezoh and the pipeline, compare two workflow implementations, check whether instruction changes improved decisions, or measure process quality separately from trade outcome. Default to agent-run simulation for behavior tests and use scripts only as deterministic helpers for fixtures, validation, or scoring.
---

# Pipeline Simulation Lab

Use this skill when the question is about the desk behavior, not just the trade rule.

This is for:
- what would the pipeline do
- what would Deezoh decide
- what questions would Deezoh ask
- which specialist agents would Deezoh or Orchestrator use
- whether the desk should use a standard loop, adaptive questions, or both
- did the new instructions improve the process
- did a workflow fix reduce bad decisions
- which desk variant handles mixed cases better
- instruction A/B
- enforcement A/B
- build compare
- failure injection
- local or verified snapshot compare
- bounded orchestration runs that combine several checks

## Not The Same As Strategy Backtest

This skill tests workflow and decision process.

It does **not** mainly answer whether a raw strategy had edge.
For that, use `strategy-backtest-lab`.

## Agent-First Rule

If the question is "what would Deezoh, the council, or the pipeline actually do?", run agents first.

Default order:
1. prepare or select the scenario, snapshot, or historical bundle
2. run isolated agent simulations or councils for the behavior under test
3. use the deterministic helper only for packaging fixtures, validating contracts, or scoring and comparing captured outputs

Do not treat the helper script as the primary simulator when the point of the test is agent behavior.

Important:

- if the run only rendered prompts, scored tags, or compared canned outputs, do not claim real agent behavior was proven
- call it prompt/scoring simulation unless isolated agents or councils actually ran

## Agent-Run Evidence Contract

If the result claims agent behavior was tested, capture:

- per-variant transcript, session log, or equivalent output artifact
- final decision artifact
- questions asked
- lanes consulted
- why any helper-only or prompt-only run was downgraded

Without that bundle, treat the run as preflight or prompt/scoring simulation only.

## Current Objective Queue

Use this queue when continuing Sal's approved simulation and orchestration work:

1. Deezoh question-behavior tests
   - compare fixed checklist questions against adaptive situation-based questions
   - judge whether Deezoh asked the right agents and why
   - verify whether Orchestrator should route the follow-up work

2. Pipeline interaction tests
   - simulate Deezoh, Orchestrator, council, and specialist-lane handoffs
   - record what questions were asked, who answered, what stayed blocked, and what moved forward

3. Historical readiness checks
   - confirm whether the historical-market-context builder has enough price, timeframe, indicator, derivatives, news, and calendar context for the scenario
   - label missing historical context plainly instead of pretending it exists

4. Strategy/backtest readiness checks
   - use strategy-backtest-lab when the question is edge or PnL
   - use this skill when the question is Deezoh or pipeline behavior

5. Live OpenClaw implementation checks
   - when a simulation improvement changes the expected runtime behavior, mirror the rule into the relevant OpenClaw agent or workflow file
   - verify live access and runtime proof separately from local skill proof

## Deezoh Question Model

Default to a hybrid question model:

- stable core questions every loop:
  - what changed since last cycle
  - what is the current situation
  - what is the best long case
  - what is the best short case
  - what is the best no-trade case
  - what evidence is stale or missing
  - what would unlock the next state

- adaptive follow-up questions based on context:
  - event-risk cases ask catalyst, strategy, derivatives, and challenger
  - timeframe-conflict cases ask chart, indicator, strategy, and entry-watch
  - liquidity-trap cases ask market-maker, derivatives, chart, and challenger
  - stale-data cases ask Orchestrator to repair or downgrade the input before Deezoh acts
  - active-trade cases ask execution, entry-watch, market-maker, indicator, and challenger

Do not force every specialist to answer every loop. Use Orchestrator to route only the useful lanes, while keeping Deezoh responsible for the final decision.

## Deterministic Helper

`C:\Users\becke\claudecowork\trading_system\scripts\labs\pipeline_simulation_lab.py`

## Modes

Read [references/MODES.md](references/MODES.md) before choosing.
For the real agent-run comparison loop, also read [references/AGENT_ORCHESTRATION_MODE.md](references/AGENT_ORCHESTRATION_MODE.md).

## Helper Commands

Scenario suite:

```powershell
python C:\Users\becke\claudecowork\trading_system\scripts\labs\pipeline_simulation_lab.py `
  --mode scenario-suite
```

Compare desk variants:

```powershell
python C:\Users\becke\claudecowork\trading_system\scripts\labs\pipeline_simulation_lab.py `
  --mode variant-compare `
  --include-snapshots `
  --snapshot-limit 12
```

A/B compare two versions:

```powershell
python C:\Users\becke\claudecowork\trading_system\scripts\labs\pipeline_simulation_lab.py `
  --mode a-b-test `
  --variant-a hybrid_desk `
  --variant-b timeframe_handoff `
  --include-snapshots
```

Failure injection:

```powershell
python C:\Users\becke\claudecowork\trading_system\scripts\labs\pipeline_simulation_lab.py `
  --mode failure-injection
```

Build or instruction compare:

```powershell
python C:\Users\becke\claudecowork\trading_system\scripts\labs\pipeline_simulation_lab.py `
  --mode build-compare `
  --results-a C:\path\to\results_a.json `
  --results-b C:\path\to\results_b.json `
  --label-a baseline `
  --label-b candidate
```

Bounded orchestration pass:

```powershell
python C:\Users\becke\claudecowork\trading_system\scripts\labs\pipeline_simulation_lab.py `
  --mode orchestration `
  --include-live-snapshot `
  --results-a C:\path\to\results_a.json `
  --results-b C:\path\to\results_b.json `
  --label-a baseline `
  --label-b candidate `
  --max-iterations 2
```

If no local OpenClaw scenario folders are present, this lab falls back to bundled synthetic regression cases instead of pretending real fixtures exist.

## Rules

1. Agent-run simulation is the default for behavior testing.
2. Score process quality and decision quality separately.
3. Be honest about what is simulated and what is not.
4. Current scenario and variant replay are fast desk regressions, not full every-agent historical life simulation unless agents actually ran.
5. A snapshot compare is only `live` if the source was actually verified live. Otherwise call it a local snapshot and treat it as weaker evidence.
6. Use this lab to prove whether a pipeline or instruction change helped before trusting live behavior.
7. If a scenario grades itself from derived expectations inside the same artifact set, call out the circularity and downgrade the result.
