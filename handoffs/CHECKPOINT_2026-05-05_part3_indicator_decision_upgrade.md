# CHECKPOINT — Part 3 indicator decision upgrade

Date: 2026-05-05
Operator: Codex

## Objective

Tighten `Part 3: Indicators And Momentum Signals` so it is more useful to Deezoh when deciding:

- long now
- short now
- wait for reset
- wait for trigger
- no edge

## What changed

- upgraded the Part 3 template in `CHIMERA_RESEARCH_BUNDLE_TEMPLATE.md`
- upgraded `agents/indicator-analyst/AGENTS.md`
- upgraded the source-truth note in `2026-05-05-indicators-and-momentum-source-matrix.md`
- created a new live BTC decision-focused example:
  - `research/platforms/2026-05-05-btc-part3-deezoh-example.md`

## Main upgrades

- added decision fields:
  - `indicator_decision_verdict`
  - `preferred_direction_now`
  - `decision_confidence`
  - `why_not_long_now`
  - `why_not_short_now`
  - `why_wait_if_waiting`
- added timing and weighting fields:
  - `execution_timeframe_owner`
  - `higher_timeframe_owner`
  - `dominant_indicator_timeframe`
  - `lower_timeframe_noise_verdict`
  - `timeframe_weighting_summary`
  - `higher_timeframe_vs_lower_timeframe_verdict`
  - `continuation_vs_exhaustion_verdict`
  - `setup_timing_state`
- added trigger / invalidation fields:
  - `long_trigger_from_indicators`
  - `short_trigger_from_indicators`
  - `next_indicator_trigger`
  - `indicator_invalidation_for_long_bias`
  - `indicator_invalidation_for_short_bias`
  - `indicator_invalidation_condition`
- added chart-confirmation boundary:
  - `chart_confirmation_needed`
  - `chart_confirmation_state`
  - `chart_confirmation_reason`
- added divergence nuance:
  - `divergence_class`
  - `divergence_confirmation_state`

## Important rule changes

- shorthand summaries are now optional extras only
- required Part 3 fields must still be filled
- historical divergence must not be promoted to active divergence casually
- chart confirmation is mandatory when a current-swing divergence claim would change the trade verdict

## BTC example verdict

Current BTC indicator read:

- verdict: `wait_for_reset`
- preferred direction: `long`
- why:
  - 4h and 1d still own bullish directional bias
  - 15m and 1h are too stretched for a clean fresh chase
  - current short case is weaker than the reset-long case

## VPS sync proof

Updated and synced to live surfaces:

- `/root/openclawtrading/agents/indicator-analyst/AGENTS.md`
- `/root/.openclaw/workspace/agents/indicator-analyst/AGENTS.md`
- `/root/openclawtrading/skills/CHIMERA_RESEARCH_BUNDLE_TEMPLATE.md`
- `/root/.openclaw/kimi-skills/CHIMERA_RESEARCH_BUNDLE_TEMPLATE.md`
- `/root/.openclaw/workspace/research/platforms/2026-05-05-btc-part3-deezoh-example.md`

Remote grep proved the new fields are present on the live VPS copies.

## Remaining work

- Part 3 is now much more decision-useful, but it can still improve further once Deezoh consumes it in a live or replay bundle and we see which fields it still underuses
- the rest of the research bundle sections still need the same level of decision-grade tightening
