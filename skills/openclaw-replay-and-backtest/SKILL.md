---
name: openclaw-replay-and-backtest
description: Use replay, scenario suites, snapshot re-runs, and historical artifact comparisons to test OpenClaw or Chimera behavior faster than waiting for live outcomes, while separating system replay from strategy backtest.
---

# OpenClaw Replay And Backtest

Use this skill when the fastest truthful proof is replaying the system against older inputs instead of waiting for live trades or live incidents.

## Read First

- `workflows/codex/build-test-verify-monitor-closeout.md`
- `C:\Users\becke\claudecowork\scripts\full_lifecycle_replay.py`
- `docs/OPENCLAW_T052_LIVE_DESK_CONTRACT_REPAIR_2026-04-18.md`
- `tasks/TASK_REGISTRY.md`
- the specific reports, snapshots, or scripts involved

Historical note:

- older `_remote_edit` simulator paths may still exist in the repo
- do not treat them as current truth unless they are explicitly re-proven

## Modes

1. current-state snapshot capture then replay
2. existing scenario-suite run
3. historical artifact comparison
4. optimization or replay loop over multiple snapshots

## Important Distinctions

- `system replay`: did the workflow, contracts, and outputs behave correctly?
- `strategy backtest`: did the trade logic have edge over history?
- `historical market context`: build the point-in-time data bundle first when the job needs multi-timeframe candles, indicators, and catalysts at a past cutoff
- `pipeline simulation`: compare desk behavior and process quality, not just trade outcome

Do not blur those together.

## Preferred Routing

- if the user wants the historical data bundle itself, use `historical-market-context`
- if the user wants strategy-only historical testing, use `strategy-backtest-lab`
- if the user wants Deezoh or workflow testing, use `pipeline-simulation-lab`

## Rules

- Historical artifacts are historical context, not current truth.
- Do not leak hindsight into current decision files or current live state.
- Record the exact fixture set, command, outputs, and limitations.
- If replay proves only local behavior, do not imply live integration is proven too.
- Prefer current-path replay surfaces over retired `/home/open-claw/...` or stale `_remote_edit` references.

## First-Divergence Protocol

When replay is used as debug proof:

1. freeze the fixture set
2. run each producer, consumer, and state transition in order
3. record the first divergence from the expected state
4. classify the fault as:
   - producer
   - consumer
   - ownership logic
   - scoring/eval logic
5. stop claiming "replay failed" without naming that first divergence

## Write Targets

- `docs/` for replay proof reports
- `tasks/TASK_REGISTRY.md` when replay exposes a real gap
- `trace/ACTION_LOG.md`
- continuity files when the replay result matters next session

## Success Condition

A replay result should say:

1. what was replayed
2. which mode was used
3. what passed
4. what failed
5. what is still unproven in live runtime
