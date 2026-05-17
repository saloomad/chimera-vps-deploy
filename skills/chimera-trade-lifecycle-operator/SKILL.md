---
name: chimera-trade-lifecycle-operator
description: Use this when the question is how the full Chimera trade process works in real life, which documents exist at each phase, how to run live cycle tests, how thesis-stop reviews fit in, and how to improve the system with historical or outcome-based review.
---

# Chimera Trade Lifecycle Operator

Use this skill when the question is:

- how does the whole trade lifecycle work?
- which document is used in which phase?
- what fills each phase in OpenClaw?
- how do I run a live cycle?
- how do I test this with historical data?
- how do we improve the workflow from actual results?

## Read First

1. `C:\Users\becke\.codex\CHIMERA_BOOTSTRAP.md`
2. `C:\Users\becke\claudecowork\workflows\codex\chimera-screener-to-trade-document-flow.md`
3. `C:\Users\becke\claudecowork\orchestration\lobster\chimera-trade-lifecycle.lobster`
4. `C:\Users\becke\claudecowork\agents\deezoh\WORKFLOW.md`
5. the phase packet templates under `chimera-vps-deploy/skills/`

## The Primary Phase Documents

1. `CHIMERA_SCREENER_PACKET_TEMPLATE.md`
   - market-wide discovery
   - long, short, watch, and no-trade books
2. `CHIMERA_RESEARCH_BUNDLE_TEMPLATE.md`
   - deep per-symbol analysis
3. `CHIMERA_ENTRY_WATCH_PACKET_TEMPLATE.md`
   - exact wait / wake / trigger contract
4. `CHIMERA_ACTIVE_TRADE_PACKET_TEMPLATE.md`
   - active management truth
5. `CHIMERA_TRADE_CLOSEOUT_TEMPLATE.md`
   - post-trade review and improvement capture

Auxiliary review packet:

6. `CHIMERA_THESIS_STOP_REVIEW_TEMPLATE.md`
   - review good ideas that died before activation
   - explain why patience or rejection was correct

Every phase should keep:

- previous and next document links
- why the desk moved to this phase
- what alternative phase was rejected
- Deezoh decision trace

## What Runs Every Cycle

Even when no trade advances, the system should still refresh:

- `SCOUT_REPORT.json`
- `DEEZOH_SCREENER_CONSUMPTION.json`
- `RESEARCH_BUNDLE_latest.json`
- `DEEZOH_BUNDLE_TAIL_CONSUMPTION.json`
- `ENTRY_WATCH_PACKET_latest.json`
- `ACTIVE_TRADE_PACKET_latest.json`
- `TRADE_CLOSEOUT_PACKET_latest.json`
- `THESIS_STOP_REVIEW_PACKET_latest.json`
- `LIFECYCLE_LEARNING_QUEUE.json`
- `SYMBOL_LIFECYCLE_STATE.json`
- `CHIMERA_LIFECYCLE_CONTEXT.json`

Why:

- the desk still needs context
- macro and market state still matter
- the bundle still teaches the system what the market is doing
- only the promoted phase should change, not the presence of data

Important:

- all packet snapshots may exist each cycle
- only one phase should be the primary owner now
- use lifecycle state to decide that owner instead of assuming it from one mode flag

## Live VPS Cycle

Primary live cycle runner:

- `/root/openclawtrading/scripts/run_chimera_trade_lifecycle_cycle.sh`

It refreshes:

1. report truth
2. screener bridge
3. research bundle
4. bundle-tail decision bridge
5. entry-watch packet
6. active-trade packet
7. trade-closeout packet
8. thesis-stop review packet
9. lifecycle learning queue
10. symbol lifecycle state
11. lifecycle context summary

Most important live operator outputs:

- `/root/openclawtrading/reports/auto/DEEZOH_SCREENER_CONSUMPTION.json`
- `/root/openclawtrading/reports/auto/RESEARCH_BUNDLE_latest.json`
- `/root/openclawtrading/reports/auto/DEEZOH_BUNDLE_TAIL_CONSUMPTION.json`
- `/root/openclawtrading/reports/auto/ENTRY_WATCH_PACKET_latest.json`
- `/root/openclawtrading/reports/auto/ACTIVE_TRADE_PACKET_latest.json`
- `/root/openclawtrading/reports/auto/TRADE_CLOSEOUT_PACKET_latest.json`
- `/root/openclawtrading/reports/auto/THESIS_STOP_REVIEW_PACKET_latest.json`
- `/root/openclawtrading/reports/auto/LIFECYCLE_LEARNING_QUEUE.json`
- `/root/openclawtrading/reports/auto/SYMBOL_LIFECYCLE_STATE.json`
- `/root/openclawtrading/reports/auto/CHIMERA_LIFECYCLE_CONTEXT.json`
- `/root/openclawtrading/reports/auto/DEEZOH_PIPELINE_ROUND_STATE.json`
- `/root/openclawtrading/reports/auto/CHIMERA_PIPELINE_OBSERVABILITY.json`
- `/root/openclawtrading/reports/auto/CHIMERA_PIPELINE_OBSERVABILITY.md`

## Pipeline Observability

Every live cycle should end with the observability reports.

They answer:

- which data sources were used
- which sources are fresh, aging, stale, or missing
- which scripts and agents contributed
- what Deezoh currently believes
- whether Deezoh should progress, wait, reject, or ask for more data
- where new information will be added
- what learning should feed future thoughts and memory patterns

Primary builder:

- `scripts/build_chimera_pipeline_observability.py`

Skill:

- `chimera-pipeline-observability-operator`

## Historical Testing

Use the existing proof lanes:

- `scripts/backtest_technical_structure_section.py`
- `scripts/backtest_indicators_and_momentum_section.py`
- `scripts/full_lifecycle_replay.py`
- `scripts/run_chimera_review_debug_orchestration.py`
- `chimera-bundle-consumer-simulation`
- `openclaw-replay-and-backtest`
- `strategy-backtest-lab`

Historical questions to ask:

- would the screener have promoted the right coin?
- should the desk have stayed in screener?
- should it have moved to full bundle sooner or later?
- should it have stayed in entry-watch instead of activating?
- did the final outcome prove the earlier phase decisions were right or wrong?

Replay split:

- section backtests answer whether one section is honest enough
- `full_lifecycle_replay.py` answers whether the whole phase chain behaves logically

## Improvement Loop

Do not only review the final trade result.

Also review:

- screener promotion quality
- bundle decision quality
- entry-watch timing quality
- activation timing quality
- management quality

Patch the weakest owner:

- packet template
- agent instructions
- workflow
- data source order
- report contract

Use the review/debug runner when the question is:

- which phase branch is broken?
- which packet is missing a required transition explanation?
- should the system patch data, logic, workflow, or instructions first?

## Closeout Rule

When this skill is used well, it should leave:

- one clear live or historical test target
- one current phase explanation
- one list of the documents and owners involved
- one set of improvement findings tied to the weakest owner
