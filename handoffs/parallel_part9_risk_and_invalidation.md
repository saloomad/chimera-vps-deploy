# Parallel Fork Proposal: Part 9 - Risk And Invalidation

## Objective

Define the `Risk And Invalidation` section so Deezoh can answer:

- what can break the thesis
- what can weaken the thesis without fully breaking it
- what missing or stale information matters enough to downgrade confidence
- whether the setup is safe to promote, watch-only, or reject

This section is not where the trade idea is created.
It is where the current idea is stress-tested.

## Section Owner

- primary owner: `Deezoh`
- supporting inputs:
  - `chart-analyzer`
  - `indicators / momentum writer`
  - `derivatives / positioning writer`
  - `liquidation writer`
  - `macro writer`
  - `news writer`
  - `market-intel writer`

Plain-English owner rule:

- specialists expose their own risks inside their sections
- Deezoh is the one that gathers those risks here, decides which ones matter, and states the invalidation clearly

## What Belongs Here

- thesis-breaking price levels or conditions
- thesis-weakening conditions
- key contradiction between sections
- event risk that can invalidate timing or bias
- missing or stale data that materially lowers trust
- reasons the setup should be downgraded from `tradeable` to `watch_only` or `reject`
- the exact condition that flips bias from long to neutral, short to neutral, or from either side to `wait`
- whether the invalidation is price-based, time-based, event-based, flow-based, or data-quality-based

## What Does Not Belong Here

- full support and resistance mapping
- full indicator readouts
- full macro narrative
- full derivatives explanation
- entry, stop, scale, or take-profit execution plan
- listing all setup candidates in detail
- broad commentary that belongs in `Final Decision`

Simple rule:

- this section says what can go wrong and what proves the idea is no longer good
- it does not restate the whole thesis

## Exact Recommended Fields

```md
## Risk And Invalidation

- owner:
- source:
- observed_at_utc:
- max_age_minutes:
- freshness_state:
- stale_reason:

- section_status:
- setup_scope:
- current_bias_under_review:
- invalidation_state:
- invalidation_type:
- hard_invalidation:
  - trigger:
  - level_or_condition:
  - required_confirmation:
  - expected_action:
- soft_invalidation:
  - trigger:
  - level_or_condition:
  - required_confirmation:
  - expected_action:
- thesis_flip_condition:
- timing_failure_condition:
- key_risks:
  - risk_id:
    severity:
    category:
    description:
    trigger_or_warning:
    timeframe_scope:
    status:
    owner_source:
- contradiction_summary:
- stale_or_missing_inputs_that_matter:
  - input_name:
    issue_type:
    age_or_problem:
    impact_on_decision:
- confidence_penalties:
  - reason:
    penalty_weight:
- overall_risk_grade:
- promotion_gate:
- safe_if_wrong_note:
- evidence:
  - item
  - item
  - item
```

## Allowed Values

### `section_status`

- `complete`
- `partial`
- `blocked`

### `setup_scope`

- `symbol_wide`
- `specific_setup`
- `multi_setup_shared`

### `current_bias_under_review`

- `long`
- `short`
- `neutral`
- `wait`
- `mixed`

### `invalidation_state`

- `clearly_defined`
- `partially_defined`
- `not_defined`

### `invalidation_type`

Use one or more of:

- `price_level`
- `zone_loss`
- `structure_break`
- `time_failure`
- `event_risk`
- `flow_shift`
- `volatility_regime_change`
- `data_quality_failure`

### `required_confirmation`

- `intrabar_touch`
- `close_on_execution_tf`
- `close_on_confirmation_tf`
- `two_closes`
- `event_print`
- `not_applicable`

### `expected_action`

- `downgrade_to_watch`
- `reject_setup`
- `flip_to_neutral`
- `rebuild_thesis`
- `refresh_data_first`

### `severity`

- `low`
- `medium`
- `high`
- `critical`

### `category`

- `price_structure`
- `indicator_conflict`
- `derivatives_positioning`
- `liquidation_exposure`
- `macro_event`
- `news_catalyst`
- `market_structure`
- `execution_timing`
- `data_quality`

### `status`

- `active`
- `watch`
- `triggered`
- `cleared`

### `issue_type`

- `missing`
- `stale`
- `contradictory`
- `weak_source`

### `penalty_weight`

- `light`
- `moderate`
- `heavy`

### `overall_risk_grade`

- `acceptable`
- `cautious`
- `high_risk`
- `untradeable`

### `promotion_gate`

- `promote`
- `watch_only`
- `hold`
- `reject`

## Definitions

### `hard_invalidation`

The condition that means the setup thesis is no longer valid enough to keep.

Examples:

- long thesis loses the higher-timeframe reclaim zone on close
- short thesis reclaims breakdown resistance and holds above it
- expected breakout fails and returns fully into prior range with acceptance

### `soft_invalidation`

The condition that does not fully kill the setup, but lowers confidence enough to reduce urgency or wait for a better re-entry.

Examples:

- momentum fades before entry
- derivatives crowding worsens
- price reaches entry zone but reaction is weak

### `thesis_flip_condition`

The explicit condition that changes the directional bias itself.

Example:

- bullish retest idea flips to neutral if 4h structure loses prior breakout shelf

### `timing_failure_condition`

The idea may still be directionally right, but the current entry timing is no longer good.

Example:

- price drifts sideways too long after trigger
- CPI is due in 45 minutes and timing edge is gone

### `contradiction_summary`

Short explanation of which sections disagree in a way that matters now.

Example:

- technical structure is bullish, but funding is crowded and macro event risk is too close for clean promotion

### `confidence_penalties`

The reasons confidence should be reduced even if the setup is not fully invalidated.

These are not random feelings.
They should map to a real weakness:

- stale macro
- missing liquidation map
- conflicting higher timeframe
- unclear event timing

## How Deezoh Knows It Is Filled Enough

Minimum required before Deezoh can mark this section `complete`:

- one `hard_invalidation` is explicitly defined
- one `expected_action` is defined for invalidation
- at least `2` meaningful `key_risks` are listed when risk exists
- `stale_or_missing_inputs_that_matter` is either filled or explicitly `none_material`
- `overall_risk_grade` is present
- `promotion_gate` is present
- `evidence` includes concrete reasons, not vague wording

When `partial` is acceptable:

- upstream sections are still filling
- but Deezoh can already state:
  - the biggest current risk
  - the current invalidation condition
  - whether the setup should stay `watch_only`

When this section must stay `blocked`:

- Deezoh cannot define invalidation honestly
- too many material upstream sections are missing or stale
- the setup bias is still too undefined to judge risk

## Source Order

Recommended source order for this section:

1. `Technical Structure`
   - best source for hard invalidation levels, zone loss, structure breaks, and timing failure tied to price
2. `Indicators And Momentum Signals`
   - best source for momentum fade, divergence conflict, and confirmation failure
3. `Derivatives And Positioning`
   - best source for crowding, squeeze risk, and leveraged wrong-way conditions
4. `Liquidation Heat Map`
   - best source for nearby sweep risk and magnet risk
5. `Macro And Cross-Asset`
   - best source for regime/event invalidation and timing hazard
6. `News And Catalysts`
   - best source for scheduled catalyst danger and headline-driven thesis damage
7. `Structural / Market Intel`
   - best source for broader context risks that do not show cleanly on the chart
8. `Deezoh synthesis`
   - final owner that decides which risks are material enough to carry forward here

Plain-English rule:

- Deezoh should not invent risk in a vacuum
- Deezoh should pull concrete risk from the earlier sections and only synthesize the final judgment here

## Known Proof / Capability Notes

- This section is more of a synthesis section than a raw-data section, so it does not require a chart to be visible if earlier sections are already filled honestly.
- The current bundle workflow already has freshness fields and stale rules; this section should reuse them instead of pretending old risks are current.
- Earlier live desk work already proved that fresh-looking reports can still hide stale, empty, or partial upstream truth. That makes `stale_or_missing_inputs_that_matter` mandatory here.
- Deezoh is the correct owner because this section requires cross-lane judgment, not just one-source extraction.
- `chart-analyzer` is still the main owner for hard price invalidation inputs.
- `macro` and `news` matter here even when they do not change the directional thesis, because they can still invalidate timing.
- This section can be written without a chart image when the upstream structure, indicator, derivatives, macro, and event sections are filled well. A chart is helpful for visual confirmation, but not required to answer Part 9.
- If upstream sections are weak, this section must downgrade confidence instead of filling the gap with fake certainty.

## Ideal Example Response

```md
## Risk And Invalidation

- owner: Deezoh
- source: Technical Structure + Derivatives And Positioning + Macro And Cross-Asset + News And Catalysts
- observed_at_utc: 2026-05-05T12:18:00Z
- max_age_minutes: 20
- freshness_state: fresh
- stale_reason: none

- section_status: complete
- setup_scope: specific_setup
- current_bias_under_review: long
- invalidation_state: clearly_defined
- invalidation_type:
  - price_level
  - structure_break
  - event_risk
- hard_invalidation:
  - trigger: 4h breakout retest fails and closes back below the reclaim shelf
  - level_or_condition: BTC loses 63800 to 63920 on a 4h close
  - required_confirmation: close_on_confirmation_tf
  - expected_action: reject_setup
- soft_invalidation:
  - trigger: price reaches entry area but momentum stays weak and funding crowds harder into longs
  - level_or_condition: 1h response is flat while funding worsens and taker follow-through does not appear
  - required_confirmation: close_on_execution_tf
  - expected_action: downgrade_to_watch
- thesis_flip_condition: if 4h structure loses the reclaim shelf and accepts back into prior range, bullish bias flips to neutral and needs rebuild
- timing_failure_condition: if CPI is less than 60 minutes away before entry confirmation, this setup loses timing quality and should not be promoted
- key_risks:
  - risk_id: R1
    severity: high
    category: price_structure
    description: the long thesis depends on holding the breakout retest zone
    trigger_or_warning: clean 4h close below 63800 to 63920
    timeframe_scope: 4h
    status: active
    owner_source: chart-analyzer
  - risk_id: R2
    severity: medium
    category: derivatives_positioning
    description: crowded long positioning could create a sweep before continuation
    trigger_or_warning: funding rises while OI expands without clean spot-led follow-through
    timeframe_scope: 1h to 4h
    status: active
    owner_source: derivatives writer
  - risk_id: R3
    severity: medium
    category: macro_event
    description: nearby CPI can invalidate timing even if structure remains bullish
    trigger_or_warning: major event window opens before trigger confirmation
    timeframe_scope: same day
    status: active
    owner_source: macro writer
- contradiction_summary: technical structure supports the long, but crowded derivatives and nearby macro event risk reduce confidence in immediate promotion
- stale_or_missing_inputs_that_matter:
  - input_name: liquidation heat map
    issue_type: missing
    age_or_problem: no fresh heat map in current pass
    impact_on_decision: sweep risk cannot be fully judged, so confidence is capped
- confidence_penalties:
  - reason: liquidation map missing
    penalty_weight: moderate
  - reason: CPI event risk is close
    penalty_weight: moderate
- overall_risk_grade: cautious
- promotion_gate: watch_only
- safe_if_wrong_note: if the reclaim shelf fails, do not rationalize the long thesis; reject and rebuild from the new structure
- evidence:
  - the long idea only works while the 4h reclaim shelf holds
  - derivatives are supportive but not clean enough to ignore crowding risk
  - macro timing risk is close enough to reduce promotion quality
```

