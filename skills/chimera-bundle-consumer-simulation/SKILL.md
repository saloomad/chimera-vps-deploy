---
name: chimera-bundle-consumer-simulation
description: Simulate how Deezoh and the desk consume a Chimera research bundle, compare bundle versions, and loop section, agent, and strategy improvements until the packet becomes more decision-useful. Use when the question is whether the document, instructions, and agents are good enough for real desk decisions.
---

# Chimera Bundle Consumer Simulation

Use this skill when the question is:

- would Deezoh make the right decision from this bundle?
- is a section useful enough for real trading decisions?
- did the new instructions improve the desk behavior?
- is the strategy lane helping or just narrating?
- are optional YouTube or idea overlays helping safely?
- did the desk progress to the right phase at the right time?
- did the actual result expose a wrong earlier decision?

## Read First

1. `C:\Users\becke\.codex\CHIMERA_BOOTSTRAP.md`
2. `C:\Users\becke\.codex\skills\objective-orchestration-loop\SKILL.md`
3. `C:\Users\becke\.codex\skills\pipeline-simulation-lab\SKILL.md`
4. `C:\Users\becke\.codex\skills\strategy-backtest-lab\SKILL.md`
5. `C:\Users\becke\.codex\skills\openclaw-replay-and-backtest\SKILL.md`
6. `C:\Users\becke\claudecowork\chimera-vps-deploy\skills\CHIMERA_RESEARCH_BUNDLE_TEMPLATE.md`
7. `C:\Users\becke\claudecowork\chimera-vps-deploy\skills\CHIMERA_ENTRY_WATCH_PACKET_TEMPLATE.md`
8. `C:\Users\becke\claudecowork\chimera-vps-deploy\skills\CHIMERA_ACTIVE_TRADE_PACKET_TEMPLATE.md`
9. `C:\Users\becke\claudecowork\chimera-vps-deploy\skills\CHIMERA_TRADE_CLOSEOUT_TEMPLATE.md`
10. the owning agent docs for the sections or phase under test
11. the newest worked example or live bundle snapshot

## What This Skill Must Produce

This is not only a prose review.

This is also not only a script pass.

Use a hybrid review every time:

- deterministic scripts for contracts, workflow labels, replay, and lifecycle invariants
- agent reasoning for:
  - whether the best setup really deserved to win
  - whether Deezoh asked the most decision-changing next question
  - whether more data was needed before promotion
  - whether the strongest rejected alternative lost for the right reason

It must leave:

- one clear consumer test target
- one clear phase-transition or outcome-review target
- one simulated or replay-backed Deezoh decision pass
- one gap list
- one patch set to the relevant section or agent docs
- one source-order clarification when needed
- one checkpoint if the contract changed materially

## Core Loop

1. choose the consumer test
   - section-only
   - bundle-end
   - phase-transition
   - outcome-review
   - strategy edge
   - optional overlay safety
2. decide the correct proof lane
   - `pipeline-simulation-lab` if the question is desk behavior
   - `strategy-backtest-lab` if the question is edge
   - `openclaw-replay-and-backtest` if the question is historical bundle truth
3. load the current bundle or worked example
4. ask the desk-grade questions:
   - what is the best long?
   - what is the best short?
   - what is the best no-trade?
   - what exact trigger is still missing?
   - what strategy family is this?
   - what evidence is real versus optional?
   - why did the desk progress to this phase?
   - what was the strongest rejected alternative?
   - did the actual result prove this progression was right, early, late, or wrong?
5. record where the packet fails:
   - vague field
   - weak owner
   - wrong source order
   - missing trigger
   - missing strategy proof
   - optional context too strong
   - missing transition reason
   - no decision trace
   - no result-linked review mechanism
6. patch the section, owning agent, or workflow
7. rerun the consumer read
8. mirror durable changes to:
   - `C:\Users\becke\.codex\skills`
   - `C:\Users\becke\.claude\skills`
   - `C:\Users\becke\.openclaw\skills`
   - `C:\Users\becke\claudecowork\chimera-vps-deploy\skills`
  - `/root/openclawtrading/skills`
  - `/root/.openclaw/kimi-skills`

## Default Hybrid Test Stack

Run these when the question is about market-condition coverage, Deezoh reasoning quality, or phase progression quality:

- `scripts/run_hybrid_market_condition_scenario_matrix.py`
- `scripts/tests/deezoh_specialist_workflow_alignment_smoke.py`
- `scripts/tests/deezoh_observation_suite_smoke.py`
- `scripts/tests/current_focus_full_lifecycle_smoke.py` when lifecycle closeout behavior matters

Then do an agent review on top of the outputs.

Minimum review questions:

- did the chosen workflow fit the actual market condition
- did the correct symbol and side win
- did no-trade stay alive strongly enough
- did Deezoh ask for more data when the reports were stale, contradictory, or event-controlled
- did the learning and closeout surfaces capture something useful, or just say pass/fail

## Phase Transition Rule

Do not test only the final posture.

Also test whether the desk should have:

- stayed in screener
- progressed to full bundle
- stayed in bundle instead of moving to entry-watch
- stayed in entry-watch instead of activating
- reduced or closed earlier during management

The simulation is weak if it cannot say why a phase change was correct or incorrect.

## Result Review Rule

When closeout truth exists, score the decision path itself:

- screener decision quality
- bundle decision quality
- entry-watch timing quality
- activation timing quality
- management quality

Then patch the weakest owner:

- document template
- agent instructions
- source order
- report contract

## Strategy Rule

If the question is "does this playbook have edge?", do not stop at pipeline simulation.

Also run or inspect:

- `strategy-backtest-lab`
- runtime strategy artifacts such as:
  - `STRATEGY_REPORT.json`
  - `STRATEGY_TRACKER.json`
  - `combo_results.json`

## Optional Context Rule

Optional YouTube or idea overlays may only:

- add a question
- add a watchlist hint
- lower confidence
- flag contradiction

They may not:

- choose the winning setup
- override a live trigger
- override strategy or risk evidence

## Closeout Shape

Always close with:

- what Deezoh can now answer better
- what is still weak
- whether the next proof lane is:
  - strategy backtest
  - bundle replay
  - pipeline simulation
