# CHECKPOINT — Part 3 reversal/entry-watch upgrade and simulation skill

Date: 2026-05-05
Operator: Codex

## Objective

Make `Part 3: Indicators And Momentum Signals` more useful for Deezoh by adding:

- reversal-watch signals
- overbought/oversold meaning by timeframe
- explicit entry-watch and confirmation logic
- a reusable skill for section-upgrade simulation and proof

## What changed

Updated:

- `chimera-vps-deploy/skills/CHIMERA_RESEARCH_BUNDLE_TEMPLATE.md`
- `agents/indicator-analyst/AGENTS.md`
- `agents/indicator-analyst/TOOLS.md`
- `research/platforms/2026-05-05-indicators-and-momentum-source-matrix.md`
- `research/platforms/2026-05-05-btc-part3-deezoh-example.md`

Created:

- `C:\Users\becke\.codex\skills\chimera-research-bundle-section-upgrader/SKILL.md`
- `chimera-vps-deploy/skills/chimera-research-bundle-section-upgrader/SKILL.md`

Mirrored:

- local Claude skill copy
- local OpenClaw skill copy
- VPS repo mirror
- VPS Kimi runtime skill mirror

## Part 3 additions

Added decision-useful fields for:

- overbought/oversold interpretation by timeframe
- reversal-watch signals by timeframe
- reversal escalation ladder
- reset vs true reversal test
- current entry blockers
- reset targets by timeframe
- long/short entry-watch checklists
- long/short confirmation sequences
- required volume and participation confirmation
- required trend-filter hold/break conditions
- watch cancel / expire conditions

## BTC example verdict

Current BTC Part 3 example now says:

- `indicator_decision_verdict: wait_for_reset`
- `preferred_direction_now: long`
- long case still stronger than short case
- short-term timing stretched
- higher timeframe bias still bullish
- reversal-watch exists, but active reversal proof is not there yet

## Skill purpose

`chimera-research-bundle-section-upgrader` now packages the real workflow:

1. read section + owner + latest source truth
2. build one live or replay example
3. run trader/expert review
4. upgrade template and owning agent
5. refresh source matrix
6. choose the right next proof lane:
   - `pipeline-simulation-lab` for Deezoh/workflow behavior
   - `strategy-backtest-lab` for strategy edge

## VPS proof

Remote grep proved the live VPS copies contain:

- `indicator_decision_verdict`
- `long_entry_watch_checklist`
- `overbought_oversold_interpretation_by_timeframe`
- `reversal_watch_signals_by_timeframe`
- the new `chimera-research-bundle-section-upgrader` skill

## Remaining work

- run the new skill on the next bundle sections, not just Part 3
- test how Deezoh actually consumes the richer Part 3 fields in a full bundle or replay
- keep tightening any fields that still read informative but not actionable
