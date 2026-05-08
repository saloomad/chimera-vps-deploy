# CHECKPOINT - execution, strategy, and optional-context bundle upgrade

Date: 2026-05-05
Operator: Codex

## Objective

Close the remaining bundle-end gaps by adding:

- a real execution-plan section
- a strategy and historical-edge section
- a safe optional-learning section
- an updated final-decision flow that consumes all three

## What changed

Updated:

- `chimera-vps-deploy/skills/CHIMERA_RESEARCH_BUNDLE_TEMPLATE.md`
- `agents/position-sizer/AGENTS.md`
- `agents/position-sizer/TOOLS.md`
- `agents/entry-watch/AGENTS.md`
- `agents/deezoh/FINAL_DECISION.md`
- `scripts/youtube_analyst/update_agent_overlays.py`
- `scripts/idea_system/validate_ideas.py`

Created:

- `agents/strategy/STRATEGY_AND_HISTORICAL_EDGE.md`
- `agents/youtube-analyst/BUNDLE_OPTIONAL_CONTEXT.md`
- `research/platforms/2026-05-05-execution-plan-orders-and-risk-source-matrix.md`
- `research/platforms/2026-05-05-btc-part11-execution-plan-orders-and-risk-example.md`
- `research/platforms/2026-05-05-strategy-and-historical-edge-source-matrix.md`
- `research/platforms/2026-05-05-btc-part12-strategy-and-historical-edge-example.md`
- `research/platforms/2026-05-05-final-decision-source-matrix-v2.md`
- `research/platforms/2026-05-05-btc-part13-final-decision-example.md`
- `research/platforms/2026-05-05-optional-learning-and-idea-overlays-source-matrix.md`
- `research/platforms/2026-05-05-btc-part14-optional-learning-and-idea-overlays-example.md`
- `research/platforms/2026-05-05-btc-full-bundle-deezoh-consumption-proof-v2.md`

## Main bundle changes

### Part 11

`Part 11` is now `Execution Plan, Orders, And Risk`.

It now includes:

- trigger contract
- order plan
- alert plan
- leverage and risk caps
- confidence-based sizing
- risk/reward
- stop/target structure

### Part 12

New strategy section:

- strategy family
- regime fit
- historical edge
- evidence type
- strategy failure modes

### Part 13

Final decision now explicitly consumes:

- setup ranking
- execution readiness
- strategy fit
- optional context as non-authoritative helper

### Part 14

Optional learning and idea overlays are now:

- explicitly optional
- explicitly non-overriding
- only allowed to add questions, watchlist hints, confidence downgrades, or contradiction flags

## Script fixes

Patched stale Linux defaults:

- `update_agent_overlays.py` now defaults to `/root/openclawtrading`
- `validate_ideas.py` now defaults to `/root/openclawtrading/reports/auto/IDEAS` and supports env override

## Council takeaways folded in

- execution council: Part 11 needed a stricter trigger/order/alert contract
- strategy council: strategy should stay a regime-and-playbook filter, not the live final judge
- optional-context council: YouTube and idea lanes should remain additive and explicitly non-authoritative

## Remaining work

- mirror and live-proof are complete for the upgraded docs and the two script default fixes
- later tighten the strategy runtime artifacts if you want `STRATEGY_REPORT.json` itself upgraded to the same contract
- later run a live Deezoh consumer pass that reads the upgraded sections from the real runtime instead of only the worked examples
