# Chimera Research Bundle Template

Use this template when multiple agents or specialist lanes are contributing to one shared research document.

Goal:

- every lane contributes in the same shape
- missing data is obvious
- Deezoh or the final judge can consume one consistent packet
- replay, backtesting, and review become easier
- the bundle can start incomplete and get enriched over time without pretending unknown fields are known

## How To Use It

- one symbol per bundle
- one timestamped pass per bundle
- a bundle may start with only partial information
- unknown values stay `unknown`, `pending`, `stale`, or `not_fetched_yet`
- each section has an owner
- each owner updates only their section and freshness stamps
- if a section has no reliable data, write `missing` and say why
- do not turn missing data into fake certainty
- the same symbol can have more than one setup candidate in the same bundle

## How It Really Works

This is a living packet, not a one-shot report.

That means:

- the request or trigger may only know the symbol at first
- timeframe intent may be unknown early
- freshness cannot be assumed from one old read
- later lanes must update their own timestamps and stale state

Do not treat an old field as current just because it exists.

## Field Status Rules

Use these values when a field is not simply known:

- `known`
- `inferred`
- `pending`
- `unknown`
- `missing`
- `stale`
- `not_applicable`

## Freshness Contract

Every section that depends on fetched data must carry:

- `owner`
- `source`
- `observed_at_utc`
- `max_age_minutes`
- `freshness_state`
- `stale_reason`

Freshness state must be one of:

- `fresh`
- `stale`
- `missing`
- `not_checked`

Rule:

- if `now - observed_at_utc > max_age_minutes`, the field or section must be marked `stale`
- do not silently reuse old values
- if a later lane reads a stale section, it must either refresh it or explicitly carry the stale warning forward

## Ownership Rule

Do not say "the agent knows".

Use concrete owners:

- `request source`
  - user request, screener hit, automation, replay runner
- `symbol classifier`
  - fills asset type / market classification
- `data fetcher`
  - fills raw fetched data plus timestamps
- `section writer`
  - interprets one lane using the latest available data
- `final judge`
  - consumes all lanes but should not invent missing upstream facts

## Bundle Header

```md
# Research Bundle

- bundle_id:
- symbol:
- trigger_source: user_intent / screener / automation / replay / shadow
- bundle_created_at_utc:
- bundle_last_updated_at_utc:
- asset_type: crypto / stock / etf / index / pending
- current_price:
- source_mode: live / replay / shadow / mixed
- overall_data_quality: strong / acceptable / weak / incomplete
- linked_previous_documents:
  - document_type:
    document_id:
    transition_reason:
- linked_next_documents:
  - document_type:
    expected_owner:
    trigger_to_open:
- transition_in_reason:
- transition_out_candidates:
  - next_phase:
    why_it_would_open:
    why_it_is_not_open_yet:
- decision_trace_id:
- decision_owner:
```

## Screener Packet Relationship

The screener is not `Part 13` of this bundle.

Use a separate upstream document:

- `CHIMERA_SCREENER_PACKET_TEMPLATE.md`

That packet decides which symbols deserve deeper analysis.

This per-symbol bundle should only reference the screener in `Part 1: Instrument And Context`.

If a coin was selected by the screener, Part 1 must preserve:

- `trigger_source: screener_hit`
- `screener_packet_id`
- `screener_rank`
- `screener_book`
- `screener_reason`
- `analysis_depth_decision`
- `specialist_questions_from_screener`

## Phase Relationship

This bundle is the deep per-symbol analysis packet.

It is not the only document in the lifecycle.

Use this linked phase model:

1. `CHIMERA_SCREENER_PACKET_TEMPLATE.md`
   - market-wide discovery
   - decides which symbols deserve deeper work
2. `CHIMERA_RESEARCH_BUNDLE_TEMPLATE.md`
   - deep per-symbol analysis
   - answers the full structure, indicator, derivatives, catalyst, setup, execution, strategy, and final-decision questions
3. `CHIMERA_ENTRY_WATCH_PACKET_TEMPLATE.md`
   - narrower wait-to-trigger contract once the desk wants a real wake condition
4. `CHIMERA_ACTIVE_TRADE_PACKET_TEMPLATE.md`
   - active paper or live trade management packet
5. `CHIMERA_TRADE_CLOSEOUT_TEMPLATE.md`
   - post-trade review and learning packet

Rule:

- do not reuse the screener packet as the per-symbol deep bundle
- do not reuse the deep bundle as the live management packet
- keep the ids linked instead of duplicating every field blindly

## 1. Instrument And Context

Owner:

- request source + symbol classifier + data fetchers

Fill:

```md
## Instrument And Context

- symbol:
- symbol_status: known / pending / inferred
- trigger_source:
- request_or_trigger_text:
- request_priority: normal / urgent / scheduled / follow_up
- analysis_profile: regular_analysis / scalp_check / intraday_review / swing_review / replay_review / shadow_comparison
- screener_intake:
  - screener_packet_id:
  - screener_observed_at_utc:
  - screener_rank:
  - screener_book: long_book / short_book / watch_book / no_trade_case / not_applicable
  - screener_reason:
  - analysis_depth_decision: auto_bundle / chart_first / indicator_first / positioning_first / watch_only / reject_now / not_applicable
  - specialist_questions_from_screener:
    - lane:
      question:
  - screener_intake_status: known / inferred / pending / not_applicable
- trade_intent: scalp / intraday / swing / position / unknown
- trade_intent_status: known / inferred / pending
- timeframe_profile:
  - execution_tf:
  - confirmation_tf:
  - higher_bias_tf:
- timeframe_profile_status: known / inferred / pending
- venue_or_market:
- venue_status: known / inferred / pending
- asset_type:
- current_price:
- current_price_owner:
- current_price_observed_at_utc:
- current_price_max_age_minutes:
- current_price_freshness_state:
- base_case_horizon:
- benchmark:
- section_owner:
- section_last_updated_at_utc:
- section_freshness_state:
- key_caveats:
- transition_context:
  - why_this_symbol_reached_bundle_phase:
  - why_not_chart_only:
  - why_not_indicator_only:
  - why_not_reject_now:
```

Purpose:

- identify what we know so far
- show what is still unknown
- prevent later lanes from assuming hidden context
- stamp the first freshness / stale warnings into the bundle
- link screener-selected symbols back to the upstream screener packet when relevant

Who Deezoh asks to fill this part:

- `request source`
  - supplies what triggered the run
  - examples:
    - user request
    - screener hit
    - automation run
    - replay/shadow runner
- `symbol classifier`
  - identifies what the symbol actually is
  - examples:
    - crypto
    - stock
    - commodity
    - forex
    - ETF
    - index
- `price/context source`
  - supplies current price, venue, and first timestamped context

How Deezoh knows this part is filled enough:

Minimum required before moving on:

- `symbol` is known
- `trigger_source` is known
- `source_mode` is known
- `asset_type` is at least known or explicitly pending
- `section_last_updated_at_utc` is present

If these are not true:

- Deezoh should keep this section marked `incomplete`
- later sections may still start if they can add useful facts
- but the final decision should not treat the bundle as ready

When this part is `complete enough`:

- the run has a known symbol
- the trigger is known
- the mode is known
- the current known/unknown state is explicit
- nothing in this section is pretending to be known when it is not

Multiple-choice / allowed values for Part 1:

- `trigger_source`
  - `user_request`
  - `screener_hit`
  - `automation_run`
  - `replay_runner`
  - `shadow_runner`
- `request_priority`
  - `normal`
  - `urgent`
  - `scheduled`
  - `follow_up`
- `analysis_profile`
  - `regular_analysis`
  - `scalp_check`
  - `intraday_review`
  - `swing_review`
  - `replay_review`
  - `shadow_comparison`
- `screener_book`
  - `long_book`
  - `short_book`
  - `watch_book`
  - `no_trade_case`
  - `not_applicable`
- `analysis_depth_decision`
  - `auto_bundle`
  - `chart_first`
  - `indicator_first`
  - `positioning_first`
  - `watch_only`
  - `reject_now`
  - `not_applicable`
- `trade_intent`
  - `scalp`
  - `intraday`
  - `swing`
  - `position`
  - `unknown`
- `asset_type`
  - `crypto`
  - `stock`
  - `commodity`
  - `forex`
  - `etf`
  - `index`
  - `pending`
- `source_mode`
  - `live`
  - `replay`
  - `shadow`
  - `mixed`
- `current_price_freshness_state`
  - `fresh`
  - `stale`
  - `missing`
  - `not_checked`
- `section_freshness_state`
  - `fresh`
  - `stale`
  - `incomplete`
  - `missing`

Ideal response examples:

Example A - early user request, still incomplete:

```md
## Instrument And Context

- symbol: BTCUSDT
- symbol_status: known
- trigger_source: user_request
- request_or_trigger_text: "look at BTC"
- request_priority: normal
- analysis_profile: regular_analysis
- screener_intake:
  - screener_packet_id: not_applicable
  - screener_observed_at_utc: not_applicable
  - screener_rank: not_applicable
  - screener_book: not_applicable
  - screener_reason: not_applicable
  - analysis_depth_decision: not_applicable
  - specialist_questions_from_screener: []
  - screener_intake_status: not_applicable
- trade_intent: unknown
- trade_intent_status: pending
- timeframe_profile:
  - execution_tf: unknown
  - confirmation_tf: unknown
  - higher_bias_tf: unknown
- timeframe_profile_status: pending
- venue_or_market: pending
- venue_status: pending
- asset_type: pending
- current_price: unknown
- current_price_owner: not_fetched_yet
- current_price_observed_at_utc: unknown
- current_price_max_age_minutes: unknown
- current_price_freshness_state: not_checked
- base_case_horizon: unknown
- benchmark: pending
- section_owner: Deezoh coordinator
- section_last_updated_at_utc: 2026-05-04T20:05:00Z
- section_freshness_state: incomplete
- key_caveats: initial request only; symbol known but context not fetched yet
```

Example B - screener hit on a commodity:

```md
## Instrument And Context

- symbol: XAUUSD
- symbol_status: known
- trigger_source: screener_hit
- request_or_trigger_text: "momentum screener flagged XAUUSD on 1h"
- request_priority: urgent
- analysis_profile: intraday_review
- screener_intake:
  - screener_packet_id: scout-2026-05-04T20-06Z
  - screener_observed_at_utc: 2026-05-04T20:06:00Z
  - screener_rank: 2
  - screener_book: long_book
  - screener_reason: XAUUSD was flagged by the screener as a momentum continuation candidate after cross-market filtering
  - analysis_depth_decision: chart_first
  - specialist_questions_from_screener:
    - lane: chart-analyzer
      question: confirm whether 1h breakout acceptance is real or only a failed push
    - lane: macro-bias
      question: confirm whether DXY and yields support the gold continuation read
  - screener_intake_status: known
- trade_intent: intraday
- trade_intent_status: inferred
- timeframe_profile:
  - execution_tf: 1h
  - confirmation_tf: 4h
  - higher_bias_tf: 1d
- timeframe_profile_status: inferred
- venue_or_market: spot gold / CFD feed
- venue_status: known
- asset_type: commodity
- current_price: 3384.2
- current_price_owner: price/context source
- current_price_observed_at_utc: 2026-05-04T20:06:00Z
- current_price_max_age_minutes: 5
- current_price_freshness_state: fresh
- base_case_horizon: 1 to 2 days
- benchmark: gold vs DXY / yields / risk tone
- section_owner: Deezoh coordinator
- section_last_updated_at_utc: 2026-05-04T20:06:00Z
- section_freshness_state: fresh
- key_caveats: macro and news not yet attached
```

Example C - automated regular analysis pass:

```md
## Instrument And Context

- symbol: BTCUSDT
- symbol_status: known
- trigger_source: automation_run
- request_or_trigger_text: "scheduled regular analysis"
- request_priority: scheduled
- analysis_profile: regular_analysis
- screener_intake:
  - screener_packet_id: not_applicable
  - screener_observed_at_utc: not_applicable
  - screener_rank: not_applicable
  - screener_book: not_applicable
  - screener_reason: not_applicable
  - analysis_depth_decision: not_applicable
  - specialist_questions_from_screener: []
  - screener_intake_status: not_applicable
- trade_intent: swing
- trade_intent_status: inferred
- timeframe_profile:
  - execution_tf: 4h
  - confirmation_tf: 1d
  - higher_bias_tf: 1w
- timeframe_profile_status: inferred
- venue_or_market: Binance
- venue_status: known
- asset_type: crypto
- current_price: 64188
- current_price_owner: price/context source
- current_price_observed_at_utc: 2026-05-04T20:07:00Z
- current_price_max_age_minutes: 5
- current_price_freshness_state: fresh
- base_case_horizon: 2 to 7 days
- benchmark: BTC vs total crypto risk tone, DXY, Nasdaq
- section_owner: Deezoh coordinator
- section_last_updated_at_utc: 2026-05-04T20:07:00Z
- section_freshness_state: fresh
- key_caveats: user intent not explicit; timeframe profile inferred from automation profile
```

## 2. Technical Structure

Owner:

- chart structure writer

Fill:

```md
## Technical Structure

- owner:
- source:
- observed_at_utc:
- max_age_minutes:
- freshness_state:
- stale_reason:

- timeframe_structure:
  - 15m:
    - trend_state:
    - market_phase:
    - structure_quality:
  - 1h:
    - trend_state:
    - market_phase:
    - structure_quality:
  - 4h:
    - trend_state:
    - market_phase:
    - structure_quality:
  - 1d:
    - trend_state:
    - market_phase:
    - structure_quality:
  - 1w:
    - trend_state:
    - market_phase:
    - structure_quality:
- timeframe_alignment:
- controlling_timeframe:
- trendliness:
- dominant_structure:
- active_patterns:
  - item 1
  - item 2
- critical_structure_points:
  - item 1
  - item 2
- support_zones:
  - timeframe:
    zone:
    zone_type:
    source:
    touch_points:
    strength:
  - timeframe:
    zone:
    zone_type:
    source:
    touch_points:
    strength:
- resistance_zones:
  - timeframe:
    zone:
    zone_type:
    source:
    touch_points:
    strength:
  - timeframe:
    zone:
    zone_type:
    source:
    touch_points:
    strength:
- multi_timeframe_confluence_zones:
  - zone:
    timeframes:
    sources:
    confluence_reason:
- structure_tools_used:
  - fibonacci
  - vwap
  - volume_profile
  - order_block
  - fvg
- structural_bias: bullish / bearish / mixed
- confidence: 0-100
- evidence:
  - item 1
  - item 2
  - item 3
- field_sources:
  - field:
    primary_source:
    fallback_source_used:
    host:
    timeframe:
    status:
    why_this_source_won:
```

Objective:

- describe what price structure is doing across timeframes
- identify the strongest support and resistance zones
- show where multiple structure tools agree
- say whether price structure supports a long, a short, or neither
- make the exact source choice visible field by field so Deezoh can trust or challenge it

Definitions:

- `trend_state`
  - `uptrend`
  - `downtrend`
  - `range`
  - `transition`
  - `reversal_attempt`

- `structure_quality`
  - `clean`
    - price structure is readable, levels are respected, trend/range is clear
  - `mixed`
    - some structure is present, but important signals conflict or lower/higher timeframes disagree
  - `messy`
    - frequent fakeouts, overlapping zones, poor level respect, unclear trend

- `market_phase`
  - `breakout`
  - `breakout_retest`
  - `pullback`
  - `continuation`
  - `range_rotation`
  - `range_compression`
  - `expansion`
  - `trend_exhaustion`
  - `reversal_attempt`
  - `price_discovery`

- `timeframe_alignment`
  - explicitly state agreement or conflict from `15m -> 1w`
  - example:
    - `15m bullish, 1h bullish, 4h bullish, 1d mixed, 1w bearish`

- `trendliness`
  - how orderly the move is
  - use:
    - `high`
    - `medium`
    - `low`

How to think about support and resistance zones:

- do not give only one nearest level
- include multiple important zones
- include the timeframe each zone comes from
- include what created the zone:
  - fibonacci
  - VWAP
  - POC / VAH / VAL
  - order block
  - FVG
  - prior structure
- include touch count when available
- prefer multi-timeframe confluence zones over isolated single-source levels

Preferred source order for this section:

1. local Chimera structure scripts
   - `volume_profile.py` for POC / VAH / VAL
   - `fibonacci_calculator.py` for retracement levels
   - `vwap_calculator.py` for VWAP levels and distance
   - `order_block_detector.py` for OB zones
   - `fvg_detector.py` for FVG zones
2. `multi_timeframe_analyzer.py`
   - use only as a helper for `1h` / `4h` / `1d` alignment
   - do not treat it as the full structure owner
3. `tvremix` structure tools
   - use `analyze_smc_tool` and `analyze_swing_tool` with the documented `interval` parameter
   - use them one timeframe at a time as structure helpers
   - do not confuse them with `analyze_multi_timeframe`, which still has the duplicated lower-timeframe payload issue
4. `tradingview-mcp` / `tradingview-jackson`
   - use only when direct chart access is truly callable
   - best for chart-backed visual confirmation, screenshots, Pine outputs, and alert/surface-level proof
   - do not assume `registered` means usable; the chart target must actually exist
5. Bitget `technical-analysis`
   - use only when the runtime is actually proven on the current host
   - local Windows and live VPS proof now exist for `scripts/bitget_technical_analysis.py`
   - keep it as support context, not the owner of Part 2
6. `hot_zones_generator_v2.py`
   - use carefully for confluence clustering
   - good for ranked zone grouping, but some internals are still partly stubbed

What is proven to work right now:

- local `volume_profile.py`
  - works for:
    - POC
    - VAH
    - VAL
- local `fibonacci_calculator.py`
  - works for:
    - nearest support
    - retracement map
- local `vwap_calculator.py`
  - works for:
    - VWAP
    - standard deviation bands
    - distance from VWAP
- local `order_block_detector.py`
  - works for:
    - fresh bullish/bearish OB counts and zones
- local `fvg_detector.py`
  - works for:
    - unfilled bullish/bearish FVG counts and zones
- local per-timeframe structure stack as a whole
  - worked across:
    - `15m`
    - `1h`
    - `4h`
    - `1d`
    - `1w`
  - and produced distinct timeframe-specific zone outputs
- `multi_timeframe_analyzer.py`
  - now runs locally and can support `1h` / `4h` / `1d` alignment

What is only partial or needs care:

- `tvremix.analyze_smc_tool`
  - useful for:
    - one-timeframe structure overview
    - extra BOS / CHoCH / OB / FVG context
  - caution:
    - call it with `interval`
    - treat it as one-timeframe help, not as cross-timeframe truth
- `tvremix.analyze_swing_tool`
  - useful for:
    - one-timeframe swing map
    - trendline / fib-style context
  - caution:
    - call it with `interval`
    - treat it as one-timeframe help, not as cross-timeframe truth
- `tvremix.analyze_multi_timeframe`
  - useful for:
    - broad confluence summary
    - higher-timeframe bias check
  - caution:
    - current proof showed duplicated payloads across `15m`, `1h`, `4h`, and `1D`, and direct re-tests can also return `No data for BTCUSDT`, so do not trust it as sole multi-timeframe truth until that is fixed
- `tradingview-jackson`
  - can be strong when a live TradingView chart target exists
  - current live VPS proof showed:
    - CDP browser up
    - but no chart targets available
    - so Jackson was registered but not usable for chart state / screenshots / alerts there
- `tradingview_api.py`
  - works for daily-style screener snapshots
  - not a full multi-timeframe structure engine
- `candlestick_classifier.py`
  - works only in a very lightweight way right now
  - good for simple pattern checks, not a rich pattern engine yet
- `multi_timeframe_analyzer.py`
  - supports `1h` / `4h` / `1d` alignment
  - still more alignment-helper than full structure owner
  - no real zone map by itself
- Bitget `technical-analysis`
  - the local Windows and live VPS runners are now proven
  - keep it as host-proven support context, not the full structure owner
- `hot_zones_generator_v2.py`
  - runs and produces zones
  - but some internals still rely on stubs / mock-style logic, so use as helper, not sole truth

## 3. Indicators And Momentum Signals

Owner:

- indicators / momentum writer

Fill:

```md
## Indicators And Momentum Signals

- owner:
- source:
- observed_at_utc:
- max_age_minutes:
- freshness_state:
- stale_reason:
- key_questions_answered:
  - is higher-timeframe momentum supporting or fighting the structure read?
  - is short-term timing extended, reset, or turning?
  - are trend filters aligned or conflicted?
  - is volatility compressing, expanding, or exhausted?
  - is volume confirming the move?
  - is divergence active now or only historical?
  - is the current weakness just a reset, or a real reversal attempt?
  - what exactly should Deezoh watch for next before entering?
- timeframe_source_map:
  - 15m:
  - 1h:
  - 4h:
  - 1d:
  - 1w:
- source_confidence_by_timeframe:
  - 15m:
  - 1h:
  - 4h:
  - 1d:
  - 1w:
- chart_confirmation_needed: yes / no
- chart_confirmation_state: not_needed / pending / confirmed / contradicted
- chart_confirmation_reason:

- indicator_timeframes_covered:
  - 15m:
  - 1h:
  - 4h:
  - 1d:
  - 1w:
- indicator_set_used:
  - RSI
  - MACD
  - stochastic_or_kdj
  - OBV
  - CCI
  - ADX
  - Bollinger
  - ATR
  - Williams_R
  - EMA
  - SMA
  - DMI
  - Ichimoku
- momentum_state_by_timeframe:
  - 15m:
      summary:
      timing_verdict:
        state: ready_now / early_for_long / early_for_short / wait_for_reset / wait_for_trigger / exhausted / conflicting
        explanation:
  - 1h:
      summary:
      timing_verdict:
        state: ready_now / early_for_long / early_for_short / wait_for_reset / wait_for_trigger / exhausted / conflicting
        explanation:
  - 4h:
      summary:
      timing_verdict:
        state: ready_now / early_for_long / early_for_short / wait_for_reset / wait_for_trigger / exhausted / conflicting
        explanation:
  - 1d:
      summary:
      timing_verdict:
        state: ready_now / early_for_long / early_for_short / wait_for_reset / wait_for_trigger / exhausted / conflicting
        explanation:
  - 1w:
      summary:
      timing_verdict:
        state: ready_now / early_for_long / early_for_short / wait_for_reset / wait_for_trigger / exhausted / conflicting
        explanation:
- execution_timeframe_owner:
- higher_timeframe_owner:
- dominant_indicator_timeframe:
- lower_timeframe_noise_verdict: noise / meaningful_pullback / reversal_risk
- timeframe_weighting_summary:
- higher_timeframe_vs_lower_timeframe_verdict:
- continuation_vs_exhaustion_verdict:
- setup_timing_state: ready_now / early / late / reset_needed / trigger_needed / no_edge
- indicator_decision_verdict: long_now / short_now / wait_for_reset / wait_for_trigger / no_edge
- preferred_direction_now: long / short / none
- decision_confidence:
- long_trigger_from_indicators:
- short_trigger_from_indicators:
- next_indicator_trigger:
- indicator_invalidation_for_long_bias:
- indicator_invalidation_for_short_bias:
- indicator_invalidation_condition:
- chase_risk: low / medium / high
- why_not_long_now:
- why_not_short_now:
- why_wait_if_waiting:
- current_entry_blockers_now:
  - item 1
  - item 2
- reset_targets_by_timeframe:
  - 15m:
  - 1h:
  - 4h:
- trigger_timeframe_required:
- confirmation_timeframe_required:
- long_entry_watch_checklist:
  - item 1
  - item 2
  - item 3
- short_entry_watch_checklist:
  - item 1
  - item 2
  - item 3
- long_confirmation_sequence:
  - step 1
  - step 2
  - step 3
- short_confirmation_sequence:
  - step 1
  - step 2
  - step 3
- required_volume_confirmation:
- required_participation_confirmation:
- required_trend_filter_hold_for_long:
- required_trend_filter_break_for_short:
- watch_cancels_if:
- watch_expires_if:
- oscillator_state_by_timeframe:
  - 15m:
      RSI:
      stochastic_or_kdj:
      CCI_or_WilliamsR:
  - 1h:
      RSI:
      stochastic_or_kdj:
      CCI_or_WilliamsR:
  - 4h:
      RSI:
      stochastic_or_kdj:
      CCI_or_WilliamsR:
  - 1d:
      RSI:
      stochastic_or_kdj:
      CCI_or_WilliamsR:
  - 1w:
      RSI:
      stochastic_or_kdj:
      CCI_or_WilliamsR:
- trend_filter_state_by_timeframe:
  - 15m:
      MACD:
      EMA_SMA_stack:
      ADX_DMI:
      Ichimoku:
  - 1h:
      MACD:
      EMA_SMA_stack:
      ADX_DMI:
      Ichimoku:
  - 4h:
      MACD:
      EMA_SMA_stack:
      ADX_DMI:
      Ichimoku:
  - 1d:
      MACD:
      EMA_SMA_stack:
      ADX_DMI:
      Ichimoku:
  - 1w:
      MACD:
      EMA_SMA_stack:
      ADX_DMI:
      Ichimoku:
- volatility_and_expansion_state_by_timeframe:
  - 15m:
      Bollinger:
      ATR:
  - 1h:
      Bollinger:
      ATR:
  - 4h:
      Bollinger:
      ATR:
  - 1d:
      Bollinger:
      ATR:
  - 1w:
      Bollinger:
      ATR:
- volume_confirmation_state_by_timeframe:
  - 15m:
      OBV:
      volume_vs_average:
      CMF_or_MFI:
  - 1h:
      OBV:
      volume_vs_average:
      CMF_or_MFI:
  - 4h:
      OBV:
      volume_vs_average:
      CMF_or_MFI:
  - 1d:
      OBV:
      volume_vs_average:
      CMF_or_MFI:
  - 1w:
      OBV:
      volume_vs_average:
      CMF_or_MFI:
- overbought_oversold_interpretation_by_timeframe:
  - 15m:
      state:
      meaning_now:
      healthy_reset_looks_like:
      breakdown_warning:
  - 1h:
      state:
      meaning_now:
      healthy_reset_looks_like:
      breakdown_warning:
  - 4h:
      state:
      meaning_now:
      healthy_reset_looks_like:
      breakdown_warning:
  - 1d:
      state:
      meaning_now:
      healthy_reset_looks_like:
      breakdown_warning:
  - 1w:
      state:
      meaning_now:
      healthy_reset_looks_like:
      breakdown_warning:
- confirmation_or_non_confirmation:
- dominant_indicator_story:
- overbought_oversold_state:
- indicator_agreement:
- momentum_alignment:
- divergence_present: yes / no / unclear
- active_divergence_verdict: active / historical_only / conflicting / none
- divergence_type: bullish / bearish / hidden / mixed / none
- divergence_class: regular / hidden / mixed / none
- divergence_confirmation_state: confirmed_at_current_swing / unconfirmed / broken / historical_only
- divergence_scope:
- divergence_reference_window:
- divergence_recency:
- reversal_watch_signals_by_timeframe:
  - 15m:
  - 1h:
  - 4h:
  - 1d:
  - 1w:
- reversal_escalation_ladder:
  - early_warning:
  - better_reversal_risk:
  - confirmed_reversal_attempt:
- reset_vs_true_reversal_test:
- divergence_by_indicator:
  - RSI:
  - MACD:
  - OBV:
  - stochastic_or_kdj:
  - CCI:
- divergence_family_verdict:
  - momentum_oscillators:
  - volume_indicators:
  - trend_indicators:
- indicator_conflicts:
  - item 1
  - item 2
- momentum_strength:
- momentum_bias:
- evidence:
  - item 1
  - item 2
  - item 3
```

Objective:

- explain what the indicators and momentum are saying
- say whether momentum supports, weakens, or contradicts the structure read
- identify whether overbought / oversold conditions matter
- identify whether real divergence is present
- answer whether timing is ready now, early, late, or needs reset
- answer whether indicators favor long now, short now, or waiting
- answer which reversal-watch signals matter and what Deezoh should wait for next

Hard rule:

- do not replace the owned Part 3 fields with compressed custom blocks
- shorthand summaries like `RSI_state_by_timeframe` or `MACD_state_by_timeframe` are optional extras only
- the required Part 3 fields above must still be filled

Definitions:

- `momentum_state_by_timeframe`
  - answer the trader question:
    - `is momentum accelerating, fading, flat, or conflicting on this timeframe?`
  - use states such as:
    - `accelerating_bullish`
    - `slowing_bullish`
    - `accelerating_bearish`
    - `slowing_bearish`
    - `flat`
    - `conflicted`
- `timing_verdict`
  - every timeframe must say whether it supports immediate action, argues for patience, or warns against chasing
  - use:
    - `ready_now`
    - `early_for_long`
    - `early_for_short`
    - `wait_for_reset`
    - `wait_for_trigger`
    - `exhausted`
    - `conflicting`
- `oscillator_state_by_timeframe`
  - use this for timing-style indicators:
    - `RSI`
    - `stochastic_or_kdj`
    - `CCI_or_WilliamsR`
  - question answered:
    - `is the market stretched, resetting, or offering better timing?`
- `overbought_oversold_interpretation_by_timeframe`
  - explain the meaning of stretch by timeframe
  - always answer:
    - is this strength or exhaustion?
    - what would a healthy reset look like?
    - what loss or failure would turn reset into breakdown?
  - timeframe nuance:
    - `15m` or `1h` overbought often means chase risk more than regime change
    - `4h` overbought can still be trend continuation, but usually wants reset before a fresh entry
    - `1d` overbought can mean late-trend strength, not an automatic short
    - `1w` overbought or mixed affects regime confidence more than entry timing
- `RSI`
  - professional nuances:
    - `>70` = overbought
    - `<30` = oversold
    - `40-90` can function as a bullish regime range
    - `10-60` can function as a bearish regime range
    - holding `40-50` in an uptrend can be healthy support, not weakness
    - repeated failure near `50-60` in a downtrend can confirm bearish continuation
  - always state:
    - regime range
    - slope direction
    - key reclaim or failure level
    - whether the reading means strength or stretch in the current regime
- `stochastic_or_kdj`
  - use for timing, not as sole trend truth
  - professional nuances:
    - crossing up from low levels can mark reset timing
    - crossing down from high levels can mark exhaustion
    - embedded high readings can stay bullish in strong trends
    - KDJ `J > 100` or `< 0` marks extreme stretch in crypto
  - always state:
    - embedded vs reset
    - whether the cross is trend-following or countertrend
- `CCI_or_WilliamsR`
  - secondary stretch / reversal context
  - professional nuances:
    - `CCI > 100` = strong upside impulse
    - `CCI < -100` = strong downside impulse
    - `Williams %R near 0` = overbought
    - `Williams %R near -100` = oversold
- `trend_filter_state_by_timeframe`
  - use for slower confirmation indicators:
    - `MACD`
    - `EMA_SMA_stack`
    - `ADX_DMI`
    - `Ichimoku`
- `MACD`
  - question answered:
    - `is trend momentum confirming, weakening, or crossing?`
  - professional nuances:
    - bullish cross above zero is stronger than bullish cross below zero
    - bearish cross below zero is stronger than bearish cross above zero
    - histogram expanding = momentum expansion
    - histogram shrinking = momentum fade even if the trend still looks bullish
  - always state:
    - zero-line location
    - signal-line relationship
    - histogram expansion or contraction
    - whether the signal is early, mature, or fading
- `EMA_SMA_stack`
  - question answered:
    - `is the moving-average stack aligned or tangled?`
  - professional nuances:
    - `20 > 50 > 200` = bullish stack
    - `20 < 50 < 200` = bearish stack
    - `20/50 cross` = short-to-medium shift
    - `50/200 golden cross` = long-term bullish regime confirmation
    - `50/200 death cross` = long-term bearish regime confirmation
  - always state:
    - slope and spacing
    - whether price is accepted above or below the stack
    - whether the stack is acting as dynamic support or resistance or becoming tangled
- `ADX_DMI`
  - question answered:
    - `is there a real trend, and which side controls it?`
  - professional nuances:
    - `ADX < 20` = weak / ranging
    - `ADX > 25` = real trend
    - `ADX > 40` = very strong trend
    - `+DI above -DI` = bulls control direction
    - `-DI above +DI` = bears control direction
  - always state:
    - whether ADX is rising or falling
    - whether trend strength is building or decaying
- `Ichimoku`
  - question answered:
    - `is the broader filter supportive without needing a visual chart?`
  - professional nuances:
    - price above cloud = bullish regime
    - price below cloud = bearish regime
    - price inside cloud = transition / chop
    - tenkan above kijun = bullish short-term control
    - senkou A above senkou B = bullish future cloud
  - always state:
    - future cloud state or twist
    - cloud thickness when it matters
    - chikou confirmation when available
- `volatility_and_expansion_state_by_timeframe`
  - uses:
    - `Bollinger`
    - `ATR`
  - question answered:
    - `is volatility compressing, expanding, or already blown out?`
- `Bollinger`
  - professional nuances:
    - low bandwidth = squeeze / compression
    - widening bands = expansion
    - walking the upper band can be strength, not an automatic short
    - walking the lower band can be weakness, not an automatic long
- `ATR`
  - question answered:
    - `how large is normal movement and is the move abnormally volatile?`
- `volume_confirmation_state_by_timeframe`
  - uses:
    - `OBV`
    - `volume_vs_average`
    - `CMF_or_MFI`
  - question answered:
    - `is participation confirming or diverging from price?`
- `OBV`
  - professional nuances:
    - rising OBV confirms buying pressure
    - falling OBV confirms selling pressure
    - price making new highs without OBV confirmation is a warning
  - always state:
    - whether OBV is confirming price highs or lows
    - whether OBV is leading, lagging, or diverging
- `indicator_agreement`
  - say whether the main indicators agree or conflict
  - examples:
    - `broad_bullish_agreement`
    - `broad_bearish_agreement`
    - `mixed`
    - `weak_signal`
- `momentum_alignment`
  - explicitly state agreement or conflict from `15m -> 1w`
  - example:
    - `15m and 1h momentum are bullish, 4h is fading, 1d is neutral, 1w is still bearish`
- `timeframe_source_map`
  - record which source actually filled each timeframe
  - this matters because some sources only cover `1h` / `4h` / `1d`, while others are one-timeframe snapshots
- `source_confidence_by_timeframe`
  - use:
    - `strong`
    - `acceptable`
    - `weak`
    - `partial`
- `active_divergence_verdict`
  - separate a live/current divergence from an old divergence found somewhere in the lookback window
  - use:
    - `active`
    - `historical_only`
    - `conflicting`
    - `none`
- `divergence_class`
  - use:
    - `regular`
    - `hidden`
    - `mixed`
    - `none`
- `divergence_confirmation_state`
  - say whether the divergence is:
    - `confirmed_at_current_swing`
    - `unconfirmed`
    - `broken`
    - `historical_only`
- `indicator_agreement`
- `divergence_scope`
  - say where the divergence exists:
    - `single_indicator`
    - `multi_indicator`
    - `single_timeframe`
    - `multi_timeframe`
- `divergence_by_indicator`
  - say which exact indicators are diverging
- `divergence_family_verdict`
  - interpret similar indicators together
  - examples:
    - if `RSI`, `stochastic`, and `CCI` all diverge, momentum oscillators are warning the move is tiring
    - if `OBV` diverges, participation is not confirming price
    - if `MACD` diverges while RSI does not, trend momentum may be fading before the oscillator stack fully rolls over
- `divergence_reference_window`
  - state how much history the divergence scan covered
  - example:
    - `last 260 candles on 4h`
- `divergence_recency`
  - state when the strongest relevant divergence actually occurred
  - example:
    - `latest bullish OBV divergence printed on 2026-04-28 12:00 UTC`
- `reversal_watch_signals_by_timeframe`
  - list the actual signals Deezoh should watch
  - examples:
    - `1h RSI loses bull-range support`
    - `1h MACD histogram rolls over before or into cross`
    - `4h MACD stops expanding and starts fading`
    - `4h RSI leaves bull range`
    - `OBV makes lower high vs price high`
    - `downside volume expands instead of cooling off`
    - `ADX rolls down while -DI takes control`
    - `Ichimoku loses kijun or cloud support`
- `reversal_escalation_ladder`
  - use:
    - `early_warning`
    - `better_reversal_risk`
    - `confirmed_reversal_attempt`
- `reset_vs_true_reversal_test`
  - give one direct answer on whether current weakness still looks like a healthy pullback or a real trend-break attempt
- `current_entry_blockers_now`
  - list the exact reasons Deezoh should not enter yet
- `long_entry_watch_checklist` and `short_entry_watch_checklist`
  - list the conditions Deezoh should watch before upgrading the long or short case
- `long_confirmation_sequence` and `short_confirmation_sequence`
  - ordered confirmation steps, not one-line summaries
- `reset_targets_by_timeframe`
  - say what kind of cooldown or reclaim Deezoh is waiting for on the trigger timeframes
- `required_volume_confirmation` and `required_participation_confirmation`
  - state what price-only moves still lack confirmation
- `required_trend_filter_hold_for_long` and `required_trend_filter_break_for_short`
  - state what trend filters must hold or fail before the bias changes
- `watch_cancels_if` and `watch_expires_if`
  - keep the waiting state honest instead of indefinite
- `higher_timeframe_vs_lower_timeframe_verdict`
  - answer whether the lower timeframe is:
    - `pullback_against_higher_tf_trend`
    - `true_reversal_attempt`
    - `trend_continuation`
    - `noise_inside_range`
- `continuation_vs_exhaustion_verdict`
  - answer whether the indicator stack says:
    - `healthy_continuation`
    - `late_but_intact`
    - `exhaustion_risk`
    - `rollover_risk`
- `setup_timing_state`
  - use:
    - `ready_now`
    - `early`
    - `late`
    - `reset_needed`
    - `trigger_needed`
    - `no_edge`
- `indicator_decision_verdict`
  - end the section with a plain-English decision line
  - answer:
    - `long_now`
    - `short_now`
    - `wait_for_reset`
    - `wait_for_trigger`
    - `no_edge`
- `confirmation_or_non_confirmation`
  - state whether price highs or lows are being confirmed by momentum and participation indicators, or whether price is moving without confirmation
- `chart_confirmation_needed`
  - use `yes` when:
    - calling divergence `active` or `current`
    - swing-context confirmation would change the verdict from `wait` to `long_now` or `short_now`
    - the claim depends on visual pattern context instead of raw indicator state
  - use `no` for routine raw indicator reads, alignment checks, and historical divergence labels
- `indicator_conflicts`
  - call out the specific indicator disagreements that matter
  - example:
    - `RSI is bullish on 1h, but MACD histogram is fading on 4h`
- `momentum_strength`
  - use:
    - `high`
    - `medium`
    - `low`

What belongs here:

- indicator state
- momentum acceleration or fading
- divergence
- overbought / oversold context
- cross-timeframe indicator agreement or conflict
- EMA / SMA stack state
- DMI / ADX trend-strength confirmation
- Ichimoku filter state
- Bollinger / ATR volatility state
- OBV / CMF / MFI volume confirmation

What does not belong here as the main story:

- support / resistance zone mapping
- order blocks / FVGs as structure tools
- derivatives positioning
- macro / news interpretation
- Fibonacci retracement as zone map
- Volume Profile / POC / VAH / VAL as zone map

Preferred source order for this section:

1. local Chimera indicator scripts
   - `calculator.py`
     - primary owner for:
       - RSI
       - MACD
       - EMA / SMA
       - ADX / DMI-style state
       - stochastic
       - CCI
       - ATR
       - Bollinger
       - VWAP
       - Williams %R
       - Ichimoku
   - `multi_divergence_detector.py`
     - primary owner for historical/lookback divergence fields
   - `multi_timeframe_analyzer.py`
     - alignment helper for `1h` / `4h` / `1d`
2. Bitget `technical-analysis`
   - strongest support source for recent indicator series and extra fields like:
     - KDJ
     - SuperTrend
     - DMI
     - CMF
     - OBV histogram
     - VWAP
3. `tradingview-jackson`
   - use when a live chart target exists
   - visual arbitration layer for active divergence, trigger timing, and swing-context confirmation
   - best for chart-backed study reads and visual proof
4. `mcp__market_data__.technical_analysis`
   - external cross-check only
   - useful for:
     - RSI
     - MACD
     - EMA / MA
     - ATR
     - rough support/resistance
5. `tvremix.get_full_technicals`
   - fast snapshot helper when available
   - not the primary owner on this host
6. `tvremix.analyze_multi_timeframe`
   - confluence hint only
   - current proof showed duplicated lower-timeframe payloads, so do not trust it as sole multi-timeframe truth

What is proven to work right now:

- local `calculator.py`
  - now works for:
    - RSI
    - MACD
    - EMA / SMA
    - ADX / +DI / -DI
    - stochastic
    - CCI
    - ATR
    - Bollinger
    - VWAP
    - Williams %R
    - Ichimoku
- Bitget `technical-analysis`
  - works for:
    - MACD
    - RSI
    - KDJ
    - Bollinger
    - SuperTrend
    - DMI
    - EMA
    - VWAP
    - OBV
    - CMF
- local `multi_timeframe_analyzer.py`
  - now runs locally for:
    - `1h`
    - `4h`
    - `1d`
  - useful for:
    - partial alignment
    - momentum confirmation
- local `multi_divergence_detector.py`
  - works for:
    - RSI divergence
    - MACD divergence
    - OBV divergence
    - stochastic divergence
    - CCI divergence
  - treat it as historical divergence detection across a lookback window, not automatic proof of an active live divergence
- `mcp__market_data__.technical_analysis`
  - works as a rough external cross-check for:
    - RSI
    - MACD
    - MA / EMA trend
    - ATR
  - use carefully for Bollinger interpretation on current proof

What is only partial or needs care:

- `tradingview-jackson`
  - only reliable when the host exposes a real chart target
  - chart-backed when available, blocked when not
- `tvremix.get_full_technicals`
  - useful snapshot helper, but not the strongest current owner on this host
- `tvremix.analyze_multi_timeframe`
  - broad confluence hint only until duplicated lower-timeframe payload issue is fixed
- `candlestick_classifier.py`
  - pattern helper only, not a momentum owner

Boundary with `Part 2: Technical Structure`:

- `Part 2` answers:
  - where price is
  - what the structure and zones are
  - what support / resistance / confluence matters
- `Part 3` answers:
  - whether indicators support that structure
  - whether the move is stretched, strengthening, or fading
  - whether timing is favorable now or needs reset

Boundary calls:

- `Volume Profile`, `POC`, `VAH`, `VAL`, and `Fibonacci` belong primarily to `Part 2`
- `VWAP` belongs to:
  - `Part 2` when used as a zone / confluence level
  - `Part 3` when used as fair-value acceptance or trend confirmation
- `EMA / SMA` belong to:
  - `Part 3` for stack state, crosses, and trend filters
  - `Part 2` only when used as dynamic support / resistance context

Backtest note:

- the downstream backtest lane is proven usable for indicator-driven strategies
- sampled proof:
  - `strategy_backtest_lab.py --strategies "stoch_rsi_bounce" --symbols "BTC/USDT" --timeframes "4h"`
  - result:
    - `VERDICT: PASS`
    - `Trades: 38`
    - `WR: 60.53%`
    - `PF: 2.44`
    - `Return: 18.0%`
- use that to test indicator combinations downstream
- do not treat backtest results as ownership of the live indicator section itself

## 4. Derivatives And Positioning

Owner:

- sentiment / derivatives agent

Fill:

```md
## Derivatives And Positioning

- open_interest_state:
- funding_state:
- taker_pressure:
- retail_positioning:
- smart_money_positioning:
- squeeze_risk:
- derivatives_bias: bullish / bearish / mixed
- evidence:
  - item 1
  - item 2
  - item 3
```

## 5. Liquidation Heat Map

Owner:

- market-maker

Fill:

```md
## Liquidation Heat Map

- owner:
- source:
- source_mode:
- observed_at_utc:
- max_age_minutes:
- freshness_state:
- stale_reason:
- applicability:
- blocker_state:
- blocker_detail:

- windows_covered:
  - 12h
  - 24h
  - 48h
  - 3d
  - 1w

- blocked_windows:
  - window:
    blocker_state:
    blocker_detail:

- current_price_reference:
- current_price_reference_observed_at_utc:

- vulnerable_side:
- heatmap_balance_state:
- sweep_bias:
- confidence:

- structured_zone_extractor:
  - owner:
  - method:
  - status:
  - notes:

- agent_heatmap_analysis:
  - owner:
  - image_analysis_mode:
  - model_used:
  - analysis_status:
  - cluster_notional_mode:
  - zone_confirmation_state:
  - confirmed_levels:
    - price_zone:
      confirmation_role:
      confidence:
      reasoning:
  - additional_levels:
    - price_zone:
      level_role:
      confidence:
      reasoning:
  - cluster_size_review:
    - price_zone:
      side:
      relative_size:
      peak_count:
      strength:
      intensity:
      interpretation:
  - chart_read_summary:
  - supports_structured_zones:
  - disagreements_with_structured_zones:
  - what_matters_most_now:

- nearest_above_cluster:
  - price_zone:
  - window:
  - intensity:
  - cluster_type:
  - distance_pct:
  - evidence_source:

- nearest_below_cluster:
  - price_zone:
  - window:
  - intensity:
  - cluster_type:
  - distance_pct:
  - evidence_source:

- strongest_clusters:
  - window:
    side:
    price_zone:
    intensity:
    distance_pct:
    cluster_role:
    evidence_source:

- max_pain_zone:
  - price_zone:
  - window:
  - confidence:
  - evidence_source:

- squeeze_or_trap_state:
- liquidity_path_scenario:
- setup_interaction:
- invalidates_or_delays_setup:
- evidence:
  - item 1
  - item 2
```

Allowed values:

- source_mode:
  - exact_heatmap_structured
  - exact_heatmap_vision
  - exact_heatmap_structured_plus_agent_review
  - browser_scrape_maxpain_only
  - derivatives_proxy_only
  - missing

- freshness_state:
  - fresh
  - stale
  - missing
  - not_checked

- applicability:
  - required
  - useful_optional
  - not_applicable

- blocker_state:
  - none
  - coinglass_window_locked
  - login_missing
  - chart_not_rendered
  - screenshot_timeout
  - symbol_unsupported
  - proxy_only
  - unknown

- vulnerable_side:
  - longs
  - shorts
  - both
  - unclear

- heatmap_balance_state:
  - long_heavy
  - short_heavy
  - two_sided
  - thin
  - unclear

- sweep_bias:
  - up_first
  - down_first
  - two_sided_squeeze
  - no_clear_sweep
  - unclear

- cluster_type:
  - long_liquidation
  - short_liquidation
  - mixed

- cluster_role:
  - nearest_magnet
  - primary_magnet
  - secondary_magnet
  - sweep_then_reverse
  - invalidates_if_hit

- squeeze_or_trap_state:
  - none
  - long_squeeze_risk
  - short_squeeze_risk
  - two_sided_squeeze_risk
  - stop_hunt_risk
  - unclear

- setup_interaction:
  - supports_long
  - supports_short
  - supports_wait
  - mixed
  - not_applicable

- image_analysis_mode:
  - chart_agent_review
  - screenshot_vision_review
  - not_run

- analysis_status:
  - complete
  - partial
  - blocked
  - not_run

- zone_confirmation_state:
  - confirms_core_levels
  - confirms_with_additions
  - partially_confirms
  - disagrees_with_structured_read
  - not_run

- invalidates_or_delays_setup:
  - none
  - delays_long
  - delays_short
  - invalidates_long
  - invalidates_short
  - forces_wait

Required interpretation:

- say where the closest meaningful clusters are
- say which side is more exposed
- say whether price is likely to move toward a sweep first
- say whether the heat map confirms, delays, or fights the setup
- keep OCR/structured extraction as the numeric owner for exact zones when it works
- add a separate agent heatmap-analysis read that confirms those zones, flags disagreements, and can add extra relevant levels
- say plainly when the section is only proxy-grade or partially blocked

How Deezoh knows this part is filled enough:

- `owner` is present
- `source_mode` is present
- `observed_at_utc` is present
- `freshness_state` is present
- `applicability` is present
- one of these is true:
  - both `nearest_above_cluster` and `nearest_below_cluster` are filled from exact evidence
  - or the section explicitly says it is blocked or proxy-only with `blocker_state` and `blocker_detail`
- if exact structured extraction succeeded, `agent_heatmap_analysis` should be present unless it is explicitly marked `not_run` with a reason
- if exact structured extraction is missing but a screenshot review still ran, the section should say that plainly and may use `SCREENSHOT_PLUS_AGENT_REVIEW` rather than pretending exact clusters exist
- `setup_interaction` is present

Source order:

1. `trading_system/scripts/coinglass_heatmap_exact.py`
   - strongest exact structured path when it returns real clusters
2. `trading_system/scripts/liquidation_heatmap.py`
   - screenshot capture helper, not the final analyst by itself
3. `trading_system/scripts/coinglass_maxpain_scraper.py` and `MAXPAIN_SUMMARY.json`
   - good for magnet/max-pain support, not enough to replace true cluster extraction
4. `liquidation-vision-analyzer`
   - agent/screenshot review lane for confirming structured zones and adding visual context or extra levels
5. market-maker proxy rows
   - useful for pressure context only, not exact sweep targets

Current tested truth:

- Windows local:
  - `BTC 24h` exact structured CoinGlass extraction works
  - `12h`, `48h`, `3d`, and `1w` currently return honest blocked-window JSON instead of fake clusters
  - `ETH 24h` and `SOL 24h` exact extraction also work after the latest axis/extractor fixes
- Live VPS:
  - Playwright screenshot and browser max-pain scraping work
  - exact CoinGlass heatmap extraction is now proved for `BTC 24h`, `ETH 24h`, and `SOL 24h`
  - current gap is not exact extraction; it is making the separate agent-review lane a standard second pass
- CoinAnk:
  - treat as proof helper only when it actually renders; do not assume it is the primary truth source

## 6. Macro And Cross-Asset

Owner:

- macro-bias agent

Objective:

- explain whether the broader outside backdrop supports, weakens, delays, or complicates the setup
- separate event-timing risk from directional macro regime
- show which external lanes are actually covered this run and which ones are still missing
- tell Deezoh what macro confirms now, what it does not confirm yet, and how much weight to give it

This section should answer:

  - is there a macro event window that should delay action right now?
  - what is SPX saying?
  - what is Nasdaq saying?
  - what is VIX saying?
  - what are DXY and yields saying?
  - what are gold and oil saying?
  - what is China or broader Asia risk context saying when it matters?
  - how should outside macro change the way we read the internal crypto structure from `Part 8`?
- which macro lanes are covered this run, and which ones are missing?
- how much weight should Deezoh give macro in this decision?
- what should Deezoh wait for before promoting conviction?

Boundary note:

- `Part 8` is the primary owner of `BTC.D`, `USDT.D`, and `TOTAL3` internal-crypto structure
- `Part 6` may reference them only when outside macro changes how they should be interpreted

Fill:

```md
## Macro And Cross-Asset

- owner:
- source:
- source_mode:
- observed_at_utc:
- max_age_minutes:
- freshness_state:
- stale_reason:
- section_status:
- asset_focus_profile:

- macro_workflow:
- macro_tradeability_state:
- controlling_macro_driver_now:
- macro_regime_state:
- cross_asset_regime_state:
- macro_time_horizon:
- macro_recommendation_state:
- how_deezoh_should_use_macro_now:
- recommendation_weight:
- macro_recommendation_explanation:
- deezoh_context_now:
- when_partial_macro_is_still_usable:
- what_macro_confirms_now:
  - item 1
- what_macro_does_not_confirm_yet:
  - item 1
- exact_vs_proxy_boundary:
- stale_or_proxy_lanes_that_limit_confidence:
  - item 1
- chart_confirmation_upgrade_path:

- event_risk_window:
    - state:
    - controlling_event:
    - event_country:
    - event_importance:
    - hours_to_event_or_since:
    - why_it_matters_now:

  - macro_indicator_snapshot:
    - inflation_context:
    - jobs_context:
    - growth_context:
    - policy_context:
    - why_these_matter_now:

  - fed_policy_context:
    - latest_fomc_signal:
    - policy_bias:
    - cut_hike_hold_context:
    - source_quality:
    - explanation:

  - market_implied_policy_path:
    - state:
    - source:
    - source_page:
    - probability_method:
    - next_meeting_date:
    - dominant_target_range:
    - dominant_probability_pct:
    - secondary_target_range:
    - secondary_probability_pct:
    - current_target_band:
    - current_midpoint_pct:
    - next_move_direction:
    - next_move_probability_pct:
    - implied_post_meeting_rate_pct:
    - delta_vs_current_bps:
    - updated_text:
    - page_cache_notice:
    - explanation:
    - coverage_state:

  - global_macro_context:
    - china_context:
    - global_liquidity_or_stress_context:
    - geopolitical_macro_context:
    - why_it_matters_now:

- broad_equity_event_context:
  - state:
  - relevant_names_or_theme:
  - why_it_matters_for_spx_ndx_or_crypto:
  - source:

- asset_specific_macro_focus:
  - primary_lane_1:
  - primary_lane_2:
  - secondary_lane_1:

  - lane_coverage:
    - calendar:
      coverage_state:
      source:
    - spx:
      coverage_state:
      source:
    - ndx:
      coverage_state:
      source:
    - vix:
      coverage_state:
      source:
    - dxy:
      coverage_state:
      source:
  - yields:
    coverage_state:
    source:
  - gold:
    coverage_state:
    source:
    - oil:
      coverage_state:
      source:
    - china:
      coverage_state:
      source:
    - btc_d:
      coverage_state:
      source:
  - usdt_d:
    coverage_state:
    source:
  - total3_ex_btc_eth:
    coverage_state:
    source:

- spx_lane:
      - relationship_context:
      - current_direction_state:
      - source_quality:
      - interpretation:
      - explanation:
      - why_it_is_moving:
      - supports_or_fights_setup:

  - ndx_lane:
      - relationship_context:
      - current_direction_state:
      - source_quality:
      - interpretation:
      - explanation:
      - why_it_is_moving:
      - supports_or_fights_setup:

  - vix_lane:
      - relationship_context:
      - current_direction_state:
      - source_quality:
      - interpretation:
      - explanation:
      - why_it_is_moving:
      - supports_or_fights_setup:

- dxy_lane:
    - relationship_context:
    - current_direction_state:
    - source_quality:
    - interpretation:
    - explanation:
    - why_it_is_moving:
    - supports_or_fights_setup:

- yields_lane:
    - relationship_context:
    - current_direction_state:
    - source_quality:
    - interpretation:
    - explanation:
    - why_it_is_moving:
    - supports_or_fights_setup:

- gold_lane:
    - relationship_context:
    - current_direction_state:
    - source_quality:
    - interpretation:
    - explanation:
    - why_it_is_moving:
    - supports_or_fights_setup:

- oil_lane:
      - relationship_context:
      - current_direction_state:
      - source_quality:
      - interpretation:
      - explanation:
      - why_it_is_moving:
      - supports_or_fights_setup:

  - china_lane:
      - relationship_context:
      - current_direction_state:
      - source_quality:
      - interpretation:
      - explanation:
      - why_it_is_moving:
      - supports_or_fights_setup:

- btc_d_lane:
  - btc_d_signal:
  - interpretation:
  - supports_or_fights_setup:

- usdt_d_lane:
  - usdt_d_signal:
  - interpretation:
  - supports_or_fights_setup:

- total3_ex_btc_eth_lane:
  - total3_signal:
  - fear_greed_signal:
  - interpretation:
  - explanation:
  - supports_or_fights_setup:

- cross_asset_correlation_context:
  - base_asset:
  - vs_dxy:
  - vs_spx:
  - vs_t10y:
  - vs_gold:
  - vs_oil:
  - notes:

- macro_tailwinds:
  - item 1
- macro_headwinds:
  - item 1
- macro_conflicts:
  - item 1
- missing_macro_lanes_that_matter:
  - item 1
- what_macro_should_make_deezoh_do:
  - item 1
- what_macro_should_not_be_used_for:
    - item 1

- what_would_improve_macro_case:
    - item 1
- what_would_break_macro_case:
    - item 1

  - explanation_support_used:
    - macro_indicator_helper:
    - news_helper:
    - direct_web_lookup_used:
    - why_extra_explanation_was_needed:

- macro_bias:
- macro_confidence:
- plain_english_macro_take:
- what_this_means_for_btc:
- what_this_means_for_alts:
- evidence:
  - item 1
  - item 2
```

Allowed values:

- source_mode:
  - report_driven
  - direct_market_data
  - mixed_sources
  - helper_only
  - missing

- freshness_state:
  - fresh
  - stale
  - mixed
  - missing
  - not_checked

- section_status:
  - complete_enough
  - partial
  - degraded
  - blocked

- asset_focus_profile:
  - btc_like_crypto
  - eth_alt_like_crypto
  - gold_like_macro_metal
  - oil_like_energy
  - equity_index_like
  - single_stock_like
  - fx_like
  - custom

- macro_workflow:
  - pre_event_control
  - post_event_digest
  - cross_asset_divergence
  - unusual_behavior_precedent_capture
  - data_degraded_mode

- macro_tradeability_state:
  - supportive
  - mixed_but_tradeable
  - caution_reduce_risk
  - wait_for_event
  - blocked_by_macro
  - blocked_by_missing_data

- macro_regime_state:
  - risk_on
  - mild_risk_on
  - mixed
  - mild_risk_off
  - risk_off
  - event_locked
  - degraded

- cross_asset_regime_state:
  - confirming_risk
  - conflicting
  - defensive
  - neutral
  - partially_covered
  - degraded

- macro_recommendation_state:
  - tailwind
  - mild_tailwind
  - neutral
  - mixed_caution
  - tactical_only
  - wait_for_clarity
  - headwind

- how_deezoh_should_use_macro_now:
  - conviction_support
  - timing_filter_only
  - context_only
  - caution_overlay
  - wait_for_confirmation

- recommendation_weight:
  - high
  - medium
  - low
  - low_due_to_missing_lanes

- event_risk_window.state:
  - clear
  - upcoming_48h
  - imminent_12h
  - live_event
  - post_event_digest
  - unknown

- lane_coverage.*.coverage_state:
  - exact
  - helper_only
  - partial
  - missing
  - not_applicable

- macro_bias:
  - bullish
  - bearish
  - mixed
  - wait
  - blocked

Use this section differently by asset:

- `btc_like_crypto`
    - primary lanes are usually `calendar`, `spx`, `ndx`, `vix`, `dxy`, `yields`, `btc_d`, `usdt_d`, and `total3_ex_btc_eth`
- `eth_alt_like_crypto`
    - primary lanes are usually `calendar`, `spx`, `ndx`, `vix`, `dxy`, `yields`, `btc_d`, `usdt_d`, and `total3_ex_btc_eth`
- `gold_like_macro_metal`
  - primary lanes are usually `calendar`, `dxy`, `yields`, `spx`, `gold`, and `oil`
- `oil_like_energy`
  - primary lanes are usually `calendar`, `dxy`, `yields`, `spx`, `oil`, and `gold`

Important:

- do not pretend `spx`, `dxy`, `yields`, `gold`, or `oil` were covered if the run only had `BTC.D`, `USDT.D`, fear and greed, or TOTAL3
- `MACRO_BIAS.json` can own `macro_workflow` and `macro_tradeability_state` when it is fresh, but it is not enough by itself to claim full cross-asset coverage
- `CROSS_ASSET.json` is currently helper-grade unless a richer direct market-data lane also confirmed the read
- `mcp__market_data__.cross_asset` is the strongest current relationship-context owner for BTC versus `SPX`, `DXY`, `gold`, `oil`, `VIX`, and `10Y`
- `mcp__market_data__.rates_yields` is the strongest current direct source for the yields lane
- `mcp__market_data__.crypto_market` global stats or fresh `MARKET_CONTEXT.json` are the strongest current BTC.D / ETH.D / USDT.D / broad crypto-cap context lanes
- TradingView chart confirmation is the preferred current-direction owner for `SPX`, `DXY`, `gold`, `oil`, `BTC.D`, `USDT.D`, and `TOTAL3` when a callable chart lane is actually alive
- if a public multi-chart board exists, use it as the preferred visual context lane for the whole section instead of hopping across unrelated single charts
- if you only have relationship context but not current direction, say that plainly instead of turning correlation into a directional call
- do not stop at a label like `mixed_caution`; always explain what that means for Deezoh in plain English
- every final Part 6 write-up must include:
  - `macro_recommendation_explanation`
  - `deezoh_context_now`
  - `plain_english_macro_take`
  - `what_this_means_for_btc`
  - `what_this_means_for_alts`

Economic calendar belongs here.

Earnings do not normally belong here for crypto.

Use earnings in:

- `Part 7: News And Catalysts` for single stocks or stock-sensitive narratives
- or as helper context only for `equity_index_like` setups when a broad earnings week is affecting SPX / NDX behavior

## 7. Catalysts, News, And Event Context

Owner:

- catalyst agent

Objective:

- explain which active catalysts, headlines, scheduled events, and playbooks actually matter for this setup
- separate truly relevant market-moving catalysts from general feed noise
- tell Deezoh whether the move is headline-driven, event-driven, or mostly independent of catalyst flow
- show what is confirmed, what is unresolved, and what still needs monitoring
- expose the persistent catalyst context that spawned agents should inherit

This section should answer:

- is there a real catalyst moving this symbol right now?
- are the latest headlines supportive, harmful, mixed, or mostly noise?
- is the current move being driven by headlines, scheduled events, or by something else?
- which headlines should Deezoh ignore because they are not relevant enough?
- what specific catalyst resolution should Deezoh wait for next?
- what non-macro or symbol-specific event is coming up?
- is a macro event acting like a live headline catalyst right now?
- which previous-event playbook applies here?
- can a spawned catalyst child see enough current context to reason correctly?
- which exact data sources were used for this catalyst read?
- is the persistent catalyst bundle being refreshed independently or only by manual repair?

Fill:

```md
## Catalysts, News, And Event Context

- owner:
- source:
- source_mode:
- observed_at_utc:
- max_age_minutes:
- freshness_state:
- stale_reason:
- section_status:
- asset_focus_profile:

- source_registry:
  - primary_owners:
    - item 1
  - cross_check_only:
    - item 1
  - not_primary_today:
    - item 1

- persistent_context_bundle:
  - status:
  - independent_refresh_state:
  - spawn_context_updated_at:
  - thoughts_updated_at:
  - current_brief_updated_at:
  - state_updated_at:
  - watch_items_updated_at:
  - playbooks_updated_at:
  - bias_state_updated_at:
  - pattern_memory_updated_at:
  - context_quality:

- dominant_narrative:
- narrative_state:
- headline_environment:
- headline_recency_state:
- move_is_news_driven_state:
- current_market_moving_catalyst:
- catalyst_bias_state:
- catalyst_tradeability_state:
- catalyst_resolution_state:
- asset_relevance_filter_state:

- lane_coverage:
  - headline_feed:
    coverage_state:
    source:
  - catalyst_gate:
    coverage_state:
    source:
  - symbol_specific_live_news:
    coverage_state:
    source:
  - economic_calendar:
    coverage_state:
    source:
  - earnings_calendar:
    coverage_state:
    source:
  - earnings_live_lookup:
    coverage_state:
    source:
  - market_implied_policy_path:
    coverage_state:
    source:
  - scheduled_asset_specific:
    coverage_state:
    source:
  - regulatory_policy:
    coverage_state:
    source:
  - geopolitical:
    coverage_state:
    source:
  - company_or_protocol_specific:
    coverage_state:
    source:
  - playbook_memory:
    coverage_state:
    source:
  - persistent_context:
    coverage_state:
    source:
  - macro_policy_headline_helper:
    coverage_state:
    source:

- active_catalysts:
  - catalyst_id:
    title:
    intensity:
    category:
    source_lane:
    why_it_matters:
    likely_directional_effect:
    playbook:

- breaking_headlines_that_matter:
  - title:
    published_at_utc:
    source:
    relevance_to_symbol:
    why_it_matters:
    confirmed_vs_speculative:

- recent_relevant_headlines:
  - title:
    published_at_utc:
    source:
    relevance_to_symbol:
    why_it_matters:
    confirmed_vs_speculative:

- headlines_ignored_as_noise:
  - title:
    reason_ignored:

- scheduled_non_macro_catalysts:
  - event:
    date_or_window_utc:
    relevance_to_symbol:
    likely_impact:

- economic_events_coming_up:
  - event:
    date_or_window_utc:
    country:
    importance:
    relevance_to_symbol:
    why_it_matters:
    linked_playbook:
    what_to_watch_before:
    what_to_watch_after:

- earnings_events_coming_up:
  - event:
    date_or_window_utc:
    relevance_to_symbol:
    why_it_matters:
    linked_playbook:

- event_probability_context:
  - policy_path_signal:
  - next_major_policy_expectation:
  - source:
  - confidence_type:
  - important_unknowns:
  - confidence:

- active_playbooks:
  - playbook:
    why_active_now:
    fit_verdict:
    source_memory_file:

- previous_event_or_pattern_context:
  - precedent:
    why_relevant_now:
    matched_pattern_family:
    confidence:

- bullish_narrative_inputs:
  - item 1
- bearish_narrative_inputs:
  - item 1
- narrative_conflicts:
  - item 1
- confirmed_facts:
  - item 1
- unresolved_or_speculative_items:
  - item 1
- missing_news_lanes_that_matter:
  - item 1

- what_deezoh_should_watch_next:
  - item 1
- what_would_upgrade_news_case:
  - item 1
- what_would_break_news_case:
  - item 1
- asset_specific_search_summary:
  - what_was_searched:
  - what_matched:
  - what_was_missing:

- news_bias:
- free_analysis:
  - plain_english_read:
  - deezoh_should_do_now:
- news_confidence:
- evidence:
  - item 1
  - item 2
```

Allowed values:

- source_mode:
  - report_driven
  - direct_feed
  - mixed_sources
  - helper_only
  - missing

- freshness_state:
  - fresh
  - stale
  - mixed
  - missing
  - not_checked

- section_status:
  - complete_enough
  - partial
  - degraded
  - blocked

- persistent_context_bundle.status:
  - current
  - stale
  - partial
  - missing

- persistent_context_bundle.independent_refresh_state:
  - auto_refreshed
  - manual_refresh_only
  - stale
  - unknown

- asset_focus_profile:
  - btc_like_crypto
  - eth_alt_like_crypto
  - single_stock_like
  - index_like
  - gold_like_macro_metal
  - oil_like_energy
  - fx_like
  - custom

- narrative_state:
  - supportive
  - headwind
  - mixed
  - neutral
  - noisy
  - unclear

- headline_environment:
  - calm
  - elevated
  - breaking
  - chaotic
  - unclear

- headline_recency_state:
  - breaking_last_2h
  - fresh_same_day
  - stale_same_day
  - older_background
  - unclear

- move_is_news_driven_state:
  - yes_active
  - partly
  - no_not_primary
  - unclear

- catalyst_bias_state:
  - bullish
  - bearish
  - mixed
  - wait
  - blocked

- catalyst_tradeability_state:
  - clear_to_trade
  - headline_caution
  - wait_for_resolution
  - blocked_by_breaking_news
  - blocked_by_missing_data

- catalyst_resolution_state:
  - active_unresolved
  - resolving
  - resolved
  - background_only
  - unknown

- asset_relevance_filter_state:
  - clean
  - partial
  - noisy_feed
  - missing

- lane_coverage.*.coverage_state:
  - exact
  - partial
  - helper_only
  - missing
  - not_applicable

- confirmed_vs_speculative:
  - confirmed
  - likely_but_unconfirmed
  - rumor
  - commentary_only

- news_bias:
  - bullish
  - bearish
  - mixed
  - wait
  - blocked

Important:

- do not treat every headline from a crypto source as relevant to BTC
- if a story is broadly interesting but not tradably relevant for the symbol, put it under `headlines_ignored_as_noise`
- macro calendar events belong primarily to Section 6; only repeat them here if they are acting as a headline catalyst the desk is actively trading around
- if `AI_CATALYST.json` or `CATALYST_REPORT.json` is missing, say the catalyst-gate lane is missing instead of pretending it was covered
- `NEWS.json` is a feed source, not the final catalyst owner
- the catalyst agent should combine:
  - `NEWS.json`
  - `AI_CATALYST.json`
  - `CATALYST_REPORT.json`
  - `ECONOMIC_CALENDAR.json`
  - `EARNINGS_CALENDAR.json`
  - persistent catalyst context files
- if the persistent catalyst files are stale, say so explicitly instead of letting spawned agents inherit old context silently

## 8. Structural / Market Intel

Owner:

- market-intel agent

Objective:

- explain the slower structural layer that is not already owned by chart, indicator, macro, news, or derivatives sections
- for crypto, focus on internal crypto structure:
  - stablecoin liquidity and dry powder
  - BTC leadership versus alt breadth
  - DeFi, chain, and network participation
- for stocks, focus on business fundamentals:
  - revenue and profitability trend
  - cash-flow quality
  - balance-sheet strength
  - dilution or buyback behavior
- for commodities or other non-crypto assets, focus on slower supply / inventory / sector structure
- keep exact-vs-proxy boundaries explicit so Deezoh knows what is real, what is helper-only, and what is still missing

This section should answer:

- for crypto:
  - is liquidity building, draining, or just rotating?
  - is BTC still the quality leader or is breadth expanding into alts?
  - are DeFi, chain, and network signals confirming the move?
- for stocks:
  - is the underlying business getting stronger or weaker?
  - is cash flow supportive?
  - is the balance sheet helping or hurting?
  - is share count shrinking, stable, or diluting?
- for any asset:
  - which tracked leaders are currently carrying the tape in crypto, stocks, or commodities?
  - is there a slower fundamental-news or earnings backdrop that materially matters here?
  - do we have any trustworthy big-buyer, insider, or pro-flow helper context?
  - what structural facts are exact right now?
  - what is only proxy or helper-level?
  - what should Deezoh watch next before upgrading confidence?

This section is **not** the main owner for:

- pure macro regime or cross-asset reaction
- scheduled event risk
- one-off news catalysts
- chart structure or indicator timing
- derivatives crowding, funding, or liquidation maps

Use it for medium-horizon internal structure and slower fundamentals.

Fill:

```md
## Structural / Market Intel

- owner:
- source:
- observed_at_utc:
- max_age_minutes:
- freshness_state:
- stale_reason:

- asset_family_focus: crypto_internal_structure / stock_business_fundamentals / commodity_supply_structure / mixed
- section_scope_boundary:
- key_questions_answered:
  - item 1
  - item 2
  - item 3
- market_intel_time_horizon: swing / position / mixed
- source_coverage:
- exact_vs_proxy_boundary:
- exact_structural_signals:
  - item 1
- proxy_structural_signals:
  - item 1
- internal_liquidity_signal:
- stablecoin_supply_trend:
- btc_dominance_signal:
- alt_rotation_signal:
- total3_or_alt_breadth_signal:
- cycle_heat_signal:
- fear_greed_or_risk_appetite_signal:
- defi_participation_signal:
- chain_activity_signal:
- network_health_signal:
- btc_exchange_balance_helper_signal:
- altcoin_season_helper_signal:
- business_fundamentals_signal:
- revenue_and_profitability_signal:
- cash_flow_signal:
- balance_sheet_signal:
- share_change_signal:
- industry_structure_signal:
- commodity_supply_or_inventory_signal:
- leadership_snapshot_scope:
- crypto_leaders_helper_snapshot:
- stock_leaders_helper_snapshot:
- commodity_or_other_market_leaders_helper_snapshot:
- crypto_structural_news_helper:
- stock_structural_news_helper:
- earnings_calendar_helper:
- crypto_pro_flow_helper:
- stock_insider_or_institutional_helper:
- structural_tailwinds:
  - item 1
- structural_headwinds:
  - item 1
- structural_watch_signals:
  - item 1
- what_would_improve_the_structural_case:
  - item 1
- what_would_weaken_the_structural_case:
  - item 1
- structural_bias:
- confidence:
- evidence:
  - item 1
  - item 2
  - item 3
```

Objective:

- explain the slower structural layer underneath price
- show whether broader capital, regime, or ecosystem conditions help or hurt the setup
- separate persistent structural support from one-bar technical noise

This section should answer:

- is the broader structural backdrop helping this trade or quietly fighting it?
- is liquidity expanding, contracting, or just rotating?
- is the market favoring majors, alts, or defensives in a way not already covered by macro or derivatives?
- are on-chain, DeFi, or network signals confirming the price story for crypto?
- for stocks, are business fundamentals strengthening or weakening?
- for commodities, is slower inventory / supply structure helping or hurting the setup?

This section should **not** become the main owner of:

- immediate chart structure
- support / resistance zones
- indicator timing and crossovers
- derivatives crowding and liquidation maps
- headline-by-headline catalyst reporting

Those belong primarily to:

- `Part 2` for structure
- `Part 3` for indicators
- `Part 4` and `Part 5` for derivatives / liquidation
- `Part 6` and `Part 7` for macro and news

Definitions:

- `internal_liquidity_signal`
  - is stablecoin supply expanding, flat, or shrinking?
  - expanding supply usually means sidelined buying power is growing

- `btc_dominance_signal`
  - shows whether BTC is leading the market as the quality bid
  - high or rising dominance usually means BTC-led strength, not broad alt participation

- `alt_rotation_signal`
  - asks whether capital is spreading into alts or staying concentrated in BTC
  - do not confuse one or two strong alts with broad alt breadth

- `cycle_heat_signal`
  - a proxy heat read from dominance, stablecoin growth, breadth, and risk appetite
  - do not pretend this is an exact on-chain cycle model if those exact inputs are unavailable

- `defi_participation_signal`
  - DeFi fees, TVL, stablecoin growth, or yield activity that shows whether on-chain participation is healthy or fading

- `chain_activity_signal`
  - exact network gas/fee/mempool data when available
  - otherwise use cautious chain-participation proxies and label them as proxy

- `network_health_signal`
  - use BTC fees / mempool or ETH gas when they directly matter for the asset or trade
  - do not force this field if the asset is not chain-sensitive

- `btc_exchange_balance_helper_signal`
  - helper-only unless a stronger exact source proves the balance read
  - good for watch-signals, not for sole conviction

- `altcoin_season_helper_signal`
  - helper-only breadth temperature
  - never let this override stronger dominance and TOTAL3 reads

- `business_fundamentals_signal`
  - the broad stock-business quality read
  - should summarize whether the company backdrop is strengthening, stable, or weakening

- `revenue_and_profitability_signal`
  - answers whether revenue and profits are growing, flat, or deteriorating

- `cash_flow_signal`
  - answers whether operating cash flow and free cash flow support the trade

- `balance_sheet_signal`
  - answers whether cash, debt, and net-cash posture support the setup or add structural risk

- `share_change_signal`
  - answers whether dilution or buybacks are helping or hurting shareholders

- `industry_structure_signal`
  - slower sector / industry backdrop that is not just headline noise

- `commodity_supply_or_inventory_signal`
  - slower supply, inventory, or physical-structure backdrop for commodities and similar assets

- `crypto_leaders_helper_snapshot`
  - helper-only read of which liquid crypto majors are leading over the chosen lookback
  - use it to answer whether leadership is broadening or staying concentrated
  - do not treat it as a full-market exact screener unless the source truly covers the whole market

- `stock_leaders_helper_snapshot`
  - helper-only read of which tracked stock leaders are strongest over the chosen lookback
  - use it to answer whether risk is being led by quality megacaps, cyclical names, or weaker speculative pockets
  - do not pretend this is the whole-market strongest-performer list if it comes from a tracked basket

- `commodity_or_other_market_leaders_helper_snapshot`
  - helper-only read of which tracked commodities or other major markets are strongest
  - use it to spot slower cross-market leadership without turning Part 8 into pure macro

- `crypto_structural_news_helper`
  - slower structural crypto stories that matter beyond one headline
  - examples:
    - ETF inflow persistence
    - stablecoin regulation
    - treasury or bank adoption
    - major infrastructure or listing changes
  - this is helper-only; Part 7 still owns the full catalyst lane

- `stock_structural_news_helper`
  - slower business or industry news that changes the structural backdrop
  - examples:
    - capex wave
    - AI demand
    - buyback or dilution announcements
    - major supply-chain or margin-impact stories
  - this is helper-only; Part 7 still owns headline-by-headline news

- `earnings_calendar_helper`
  - helper-only earnings awareness for stocks and equity-risk-sensitive setups
  - use it to answer whether a coming report can materially reshape the structural case
  - do not duplicate the full event calendar here; Part 6 and Part 7 still own the main calendar and catalyst lanes

- `crypto_pro_flow_helper`
  - helper-only read of whether larger crypto derivatives participants are leaning with or against the move
  - use top-position ratios, top-account ratios, taker imbalance, or similar pro-flow proxies
  - do not pretend this is exact whale-wallet truth

- `stock_insider_or_institutional_helper`
  - helper-only read of insider buying or large-holder accumulation if a trustworthy source exists
  - if the source is weak, blocked, delayed, or not runtime-proven, say that plainly instead of forcing a fake whale read

- `structural_tailwinds`
  - the specific structural reasons the medium-horizon case is improving

- `structural_headwinds`
  - the specific structural reasons the medium-horizon case is weaker than the chart alone suggests

- `structural_watch_signals`
  - the next few structural things Deezoh should watch for confirmation or deterioration

- `exact_vs_proxy_boundary`
  - must say which major claims are exact, which are helper-level, and which are still missing
  - never blur exact ETF flows, exact exchange reserves, exact whale wallets, exact token unlocks, or exact stock-fundamental facts with proxy reads if the exact data was not available

Ideal crypto example:

```md
## Structural / Market Intel

- owner: market-intel agent
- source: MARKET_CONTEXT.json + crypto_market.global + defi_analytics + network_status + cross_market_leadership_snapshot + news helpers + derivatives_sentiment + CoinGlass homepage helper
- observed_at_utc: 2026-05-05T16:20:00Z
- max_age_minutes: 180
- freshness_state: fresh
- stale_reason: none

- asset_family_focus: crypto_internal_structure
- section_scope_boundary: crypto internal structure only; macro, news, and derivatives remain in their own sections
- key_questions_answered:
  - is dry powder still supportive?
  - is BTC leadership still stronger than alt breadth?
  - does the structural backdrop help BTC more than broad alt chase?
- market_intel_time_horizon: swing / position
- source_coverage: exact for dominance, stablecoin supply, fear and greed, and DeFi participation; helper-only for exchange-balance, alt-season, leadership, structural-news, and pro-flow reads
- exact_vs_proxy_boundary: exact data supports the dry-powder and dominance read; leadership, ETF/news, and pro-flow helpers do not override the stronger owners
- exact_structural_signals:
  - BTC dominance remains elevated
  - stablecoin supply backdrop remains supportive
  - DeFi participation is not broadly broken
- proxy_structural_signals:
  - exchange-balance, alt-season, leadership, ETF/news, and pro-flow helper reads are useful but secondary
- internal_liquidity_signal: positive
- stablecoin_supply_trend: expanding over the broader month-scale backdrop
- btc_dominance_signal: BTC leadership still stronger than broad alt-rotation proof
- alt_rotation_signal: limited_broad_alt_confirmation
- total3_or_alt_breadth_signal: improving_but_not_full_breadth
- cycle_heat_signal: early_to_mid_reacceleration_not_euphoria
- fear_greed_or_risk_appetite_signal: improving_from_fear_toward_neutral
- defi_participation_signal: mixed_to_positive
- chain_activity_signal: active_but_not_blowoff
- network_health_signal: neutral_to_supportive
- btc_exchange_balance_helper_signal: mild_exchange_balance_drain_helper
- altcoin_season_helper_signal: mixed_not_alt_euphoria
- business_fundamentals_signal: not_applicable
- revenue_and_profitability_signal: not_applicable
- cash_flow_signal: not_applicable
- balance_sheet_signal: not_applicable
- share_change_signal: not_applicable
- industry_structure_signal: not_applicable
- commodity_supply_or_inventory_signal: not_applicable
- leadership_snapshot_scope: tracked liquid majors, not full-market exact screener
- crypto_leaders_helper_snapshot: ZEC and TON are leading the current liquid-major crypto move more aggressively than ETH
- stock_leaders_helper_snapshot: not_applicable
- commodity_or_other_market_leaders_helper_snapshot: gold remains the stronger tracked commodity backdrop than crude
- crypto_structural_news_helper: BTC ETF inflows and institutional-access stories remain supportive helpers but stay outside exact ownership
- stock_structural_news_helper: not_applicable
- earnings_calendar_helper: not_applicable
- crypto_pro_flow_helper: top-position and taker-flow proxies are mixed to slightly supportive, not a clean euphoria read
- stock_insider_or_institutional_helper: not_applicable
- structural_tailwinds:
  - stablecoin backdrop is supportive
  - BTC quality bid remains intact
  - broader crypto structure is not screaming risk-off
- structural_headwinds:
  - broad alt breadth is still less convincing than BTC strength
  - helper-level exchange-balance and alt-season reads should not be over-trusted
- structural_watch_signals:
  - BTC dominance flattening while TOTAL3 improves
  - stablecoin growth continuing
  - broader DeFi and chain breadth improving
- what_would_improve_the_structural_case:
  - stablecoin expansion continues
  - chain and DeFi breadth improve
  - broader risk rotation moves beyond BTC alone
- what_would_weaken_the_structural_case:
  - stablecoin contraction
  - participation deterioration
  - risk rotates away from crypto beta
- structural_bias: bullish
- confidence: 70
- evidence:
  - stablecoin supply backdrop remains large and structurally supportive
  - global crypto structure does not read as broad risk-off
  - rotation still favors BTC leadership more than full alt follow-through
```

Ideal stock example:

```md
## Structural / Market Intel

- owner: market-intel agent
- source: SEC companyfacts + tradfi company profile + cross_market_leadership_snapshot + news helpers + earnings helper
- observed_at_utc: 2026-05-05T16:20:00Z
- max_age_minutes: 240
- freshness_state: fresh
- stale_reason: none

- asset_family_focus: stock_business_fundamentals
- section_scope_boundary: company fundamentals only; earnings dates and one-off headlines stay outside this section
- key_questions_answered:
  - is the business backdrop strengthening or weakening?
  - is cash flow supportive?
  - what would weaken the structural case?
- market_intel_time_horizon: position
- source_coverage: exact for SEC filing facts and basic company profile; helper-only for leadership, earnings, and insider/institutional color
- exact_vs_proxy_boundary: revenue, profit, cash flow, cash, debt, and share count are exact from filings; leadership, earnings, and insider/institutional color are helper-only
- exact_structural_signals:
  - the latest filing still supports positive business strength
  - free cash flow remains positive
- proxy_structural_signals:
  - sector backdrop, leadership, earnings awareness, and insider/institutional color are supportive helpers but not the sole reason for the trade
- internal_liquidity_signal: not_applicable
- stablecoin_supply_trend: not_applicable
- btc_dominance_signal: not_applicable
- alt_rotation_signal: not_applicable
- total3_or_alt_breadth_signal: not_applicable
- cycle_heat_signal: not_applicable
- fear_greed_or_risk_appetite_signal: secondary_only
- defi_participation_signal: not_applicable
- chain_activity_signal: not_applicable
- network_health_signal: not_applicable
- btc_exchange_balance_helper_signal: not_applicable
- altcoin_season_helper_signal: not_applicable
- business_fundamentals_signal: strengthening_business
- revenue_and_profitability_signal: revenue_and_profit_growth_supportive
- cash_flow_signal: free_cash_flow_positive
- balance_sheet_signal: acceptable_balance_sheet
- share_change_signal: buyback_friendly_or_stable
- industry_structure_signal: constructive_industry_backdrop
- commodity_supply_or_inventory_signal: not_applicable
- leadership_snapshot_scope: tracked liquid stock leaders, not a full-market exact screener
- crypto_leaders_helper_snapshot: not_applicable
- stock_leaders_helper_snapshot: NVDA remains one of the stronger tracked leadership names over the medium-horizon basket read
- commodity_or_other_market_leaders_helper_snapshot: not_applicable
- crypto_structural_news_helper: not_applicable
- stock_structural_news_helper: AI demand and capex backdrop remain supportive helpers
- earnings_calendar_helper: next earnings report is close enough to matter, but the detailed event lane stays outside Part 8
- crypto_pro_flow_helper: not_applicable
- stock_insider_or_institutional_helper: no runtime-proven live insider or whale owner in the current free stack, so this stays helper-missing
- structural_tailwinds:
  - business growth remains supportive
  - free cash flow remains positive
  - share count is not diluting the case
- structural_headwinds:
  - valuation and crowd positioning still need separate checking outside this section
- structural_watch_signals:
  - revenue growth slowing sharply
  - free cash flow rolling over
  - debt growing faster than cash
  - dilution reappearing
- what_would_improve_the_structural_case:
  - stronger revenue growth
  - stronger free cash flow
  - continued buyback or tight share-count discipline
- what_would_weaken_the_structural_case:
  - revenue growth stalling
  - margins or free cash flow deteriorating
  - debt pressure or dilution increasing
- structural_bias: bullish
- confidence: 72
- evidence:
  - the latest SEC filing still shows positive business strength
  - cash flow remains supportive
  - share-count behavior is not fighting the thesis
```

## 9. Risk And Invalidation

Owner:

- risk-engine

Objective:

- say what can go wrong before entry
- separate normal reset noise from real thesis damage
- say what downgrades the idea to wait
- say what fully invalidates the current idea
- say what would start making the opposite-side thesis real
- say which missing or stale lanes still limit conviction

This section should answer:

- what should Deezoh ignore as normal noise?
- what is the first real warning that the thesis is degrading?
- what would fully break the current thesis?
- what would make the opposite-side thesis worth watching?
- what missing proof still stops strong conviction?

Fill:

```md
## Risk And Invalidation

- owner:
- source:
  - section synthesis from Part 2 through Part 8
- observed_at_utc:
- max_age_minutes:
- freshness_state:
- stale_reason:

- key_questions_answered:
  - what is only noise, not invalidation?
  - what is the first real warning the thesis is weakening?
  - what fully breaks the thesis?
  - what would make the opposite-side thesis real enough to watch?
  - what missing or stale proof still limits conviction?

- thesis_under_review:
- current_risk_state:
- why_the_thesis_is_not_invalidated_yet:
- what_has_to_hold_for_current_bias:
  - item
- what_counts_as_noise_not_invalidation:
  - item
- active_risks_now:
  - risk:
    why_it_matters:
    current_severity:
- thesis_breakers_now:
  - breaker:
    why_it_matters:
    severity_if_triggered:
- invalidation_ladder:
  - first_warning:
  - thesis_stress:
  - thesis_invalidated:
  - opposite_case_watch:
- what_downgrades_to_wait:
- what_fully_invalidates_the_current_thesis:
- what_would_flip_to_opposite_bias:
- opposite_case_still_missing:
  - item
- stale_or_proxy_lanes_that_limit_confidence:
  - lane:
    problem:
    effect_on_decision:
- missing_confirmation_before_conviction:
  - item
- missing_data_that_matters:
- no_trade_triggers:
  - item
- evidence:
  - field:
    source:
    direct_or_inferred:
```

What belongs here:

- pre-entry thesis risk
- invalidation rules
- downgrade-to-wait rules
- flip-to-opposite-bias rules
- stale or missing proof that weakens confidence

What does not belong here as the main story:

- position sizing details
- stop placement mechanics after entry
- take-profit handling
- scaling plans

Those belong in `Part 11: Execution Plan, Orders, And Risk`.

Definitions:

- `what_counts_as_noise_not_invalidation`
  - normal lower-timeframe shakeout, reset, or sweep that does not break the actual thesis
- `why_the_thesis_is_not_invalidated_yet`
  - the clearest plain-English reason the current idea is still alive despite current risk
- `what_has_to_hold_for_current_bias`
  - the small set of conditions that must remain true for the desk to keep respecting the current side
- `active_risks_now`
  - the real problems already present now, not generic market risks
- `thesis_breakers_now`
  - specific things that would materially damage the current idea if they happen
- `invalidation_ladder`
  - a staged progression:
    - `first_warning`
    - `thesis_stress`
    - `thesis_invalidated`
    - `opposite_case_watch`
- `what_downgrades_to_wait`
  - enough damage to stop acting aggressively, but not enough to flip the whole idea
- `what_would_flip_to_opposite_bias`
  - the evidence set needed before the desk should seriously favor the other side
- `opposite_case_still_missing`
  - what the other side still does not have yet, so Deezoh does not overreact too early
- `stale_or_proxy_lanes_that_limit_confidence`
  - places where the evidence is weaker because it is stale, partial, blocked, or only proxy-grade

Best current source order:

1. `Part 2: Technical Structure`
   - structural invalidation
   - key support and resistance failure logic
2. `Part 3: Indicators And Momentum Signals`
   - timing damage vs true reversal risk
   - trend-filter breakdown
3. `Part 4: Derivatives And Positioning`
   - crowding, positioning, and pressure risk
4. `Part 5: Liquidation Heat Map`
   - sweep-first risk
   - nearby exact-cluster danger when available
5. `Part 6: Macro And Cross-Asset`
   - macro veto or regime risk
6. `Part 7: News And Catalysts`
   - event risk and headline invalidation
7. `Part 8: Structural / Market Intel`
   - deeper market-structure or flow risk

Current ownership rule:

- `risk-engine` owns this section
- `risk-engine` does not invent raw facts
- `risk-engine` synthesizes risk and invalidation from the upstream sections
- `Deezoh` and `trade-judge` consume this section when deciding:
  - act
  - wait
  - no trade
  - opposite-side watch

## 10. Setup Candidates

Owner:

- Deezoh

Objective:

- list the real trade paths for the symbol
- keep long, short, and backup ideas separate
- rank the candidates instead of flattening them into one idea
- show why one path is primary and another is only a watch or backup
- preserve no-trade honesty when no candidate is good enough yet

This section should answer:

- what is the best current setup path?
- what backup path still exists if the primary path fails?
- what opposite-side setup is only a watch and not yet real?
- why does each setup exist?
- why is one candidate stronger than the others right now?

Fill:

```md
## Setup Candidates

- owner:
- source:
  - section synthesis from Part 2 through Part 9
- observed_at_utc:
- max_age_minutes:
- freshness_state:
- stale_reason:

- key_questions_answered:
  - what is the best current setup path?
  - what backup path still exists?
  - what opposite-side path is still only a watch?
  - why is one setup stronger than the others?
  - is no-trade still better than forcing any candidate right now?

- setup_selection_context:
  - current_preferred_direction:
  - current_timing_state:
  - controlling_timeframe:
  - current_best_path:
  - no_trade_still_valid:

- setup_candidates:
  - setup_id:
    direction:
    setup_role: primary / secondary / backup / opposite_watch / no_trade_reference
    timeframe_profile:
      execution_tf:
      confirmation_tf:
      higher_bias_tf:
    thesis_type:
    setup_status: ready_now / wait_for_reset / wait_for_trigger / opposite_watch / invalidated / rejected
    entry_style:
    entry_zone:
    confirmation_needed:
      - item
    invalidation_zone_or_condition:
    target_zone:
    supporting_sections:
      - part_2
      - part_3
    blocked_by:
      - item
    depends_on:
      - item
    conflicts_with:
      - setup_id
    why_it_exists:
    why_it_is_not_the_top_choice_yet:
    promotion_trigger:
    demotion_trigger:
    decision_use_for_deezoh:

- ranking_logic:
  - why_primary_wins_now:
  - why_secondary_is_not_primary:
  - why_opposite_watch_is_not_real_yet:
  - when_no_trade_beats_all_candidates:

- chosen_candidate_now:
- rejected_or_downgraded_candidates:
  - setup_id:
    downgrade_reason:
- evidence:
  - field:
    source:
    direct_or_inferred:
```

Use this when one symbol has:

- both long and short ideas
- different ideas on different timeframes
- a main setup plus backup zones
- a no-trade path that is still better than forcing the available setups

Do not force one symbol into one setup if the real analysis has more than one valid path.

What belongs here:

- candidate trade paths
- candidate ranking
- candidate promotion and demotion rules
- explicit opposite-side watch paths
- explicit no-trade preservation when needed

What does not belong here as the main story:

- detailed stop management after entry
- scale sizing
- post-entry handling

Those belong in `Part 11: Execution Plan, Orders, And Risk`.

Definitions:

- `setup_role`
  - `primary`
    - the best current path
  - `secondary`
    - a real path, but weaker than the primary
  - `backup`
    - a deeper or alternate path if the primary does not trigger
  - `opposite_watch`
    - the other side is worth monitoring but not strong enough yet
  - `no_trade_reference`
    - used when the bundle should preserve a no-trade option explicitly

- `setup_status`
  - `ready_now`
    - all needed confirmations are already present
  - `wait_for_reset`
    - direction is acceptable, timing still needs a better reset
  - `wait_for_trigger`
    - the location is acceptable, but the real trigger is missing
  - `opposite_watch`
    - the other side has warning signs, but not enough proof yet
  - `invalidated`
    - the candidate existed, but the thesis broke
  - `rejected`
    - not good enough to keep active

- `why_it_is_not_the_top_choice_yet`
  - the exact reason the setup is weaker than the current best path

- `promotion_trigger`
  - what must happen for this setup to move up in rank

- `demotion_trigger`
  - what would make this setup weaker or remove it

Best current source order:

1. `Part 2: Technical Structure`
   - setup location
   - zone quality
2. `Part 3: Indicators And Momentum Signals`
   - timing state
   - trigger readiness
3. `Part 4: Derivatives And Positioning`
   - crowding support or conflict
4. `Part 5: Liquidation Heat Map`
   - sweep-first danger
5. `Part 6` through `Part 8`
   - macro, catalysts, and structural filters
6. `Part 9: Risk And Invalidation`
   - why a candidate is alive, degraded, or only a watch

Current ownership rule:

- `Deezoh` owns this section
- `Deezoh` does not invent raw facts
- `Deezoh` converts upstream facts into ranked candidate paths
- `trade-judge` and `Part 11` consume this section after the candidate list is clear

## 11. Execution Plan, Orders, And Risk

Owner:

- position-sizer + entry-watch

Objective:

- define the actual entry plan the desk is waiting for
- separate a good candidate from a tradable order plan
- cap risk across one symbol even when more than one candidate exists
- make trigger, order, stop, target, leverage, and alerts explicit before entry

This section should answer:

- what exact trigger are we waiting for?
- what confirmation would prove the entry is live?
- are we placing a limit, breakout confirmation, or no order yet?
- where are stop loss and take profit?
- how much account and portfolio risk is allowed?
- what leverage and risk/reward are acceptable?
- what alerts should wake the desk up?

Fill:

```md
## Execution Plan, Orders, And Risk

- owner:
- source:
  - Part 10 chosen candidate + Part 9 risk rules + Part 3 trigger logic
- observed_at_utc:
- max_age_minutes:
- freshness_state:
- stale_reason:

- key_questions_answered:
  - what exact trigger are we waiting for?
  - what confirmation would prove the entry is live?
  - what order type should be used?
  - how much account and portfolio risk is allowed?
  - what alerts should wake the desk up?

- chosen_setup_id:
- promoted_setup_contract_state: promoted / not_promoted / blocked
- promotion_dependency:
- execution_blocker_now:
- management_posture:
- execution_readiness: ready_now / wait_for_reset / wait_for_trigger / no_entry
- max_risk_per_idea:
- max_account_risk_pct:
- max_account_risk_amount:
- max_portfolio_heat_pct:
- max_total_symbol_risk:
- correlation_bucket_cap:
- current_book_risk_state:
- confidence_based_risk_sizing:
  - confidence_score:
  - sizing_tier:
  - why:
- min_rr_required_by_trade_class:
- leverage_plan:
- max_effective_leverage:
- leverage_mode:
- liquidation_buffer:
- entry_style: one_shot / scale_in / breakout_confirm / pullback_entry / no_entry / staged_limit_orders
- entry_timing_rule:
- trigger_contract:
  - trigger_type:
  - trigger_tf:
  - level_or_zone:
  - candle_rule:
  - volume_rule:
  - indicator_rule:
  - expires_at:
  - invalid_if:
  - owner:
  - wake_source:
  - on_timeout:
- do_not_chase_rule:
- order_plan:
  - side:
    order_type:
    limit_price:
    stop_price:
    size_pct:
    time_in_force:
    post_only:
    reduce_only:
    activate_when:
    cancel_when:
- no_order_reason:
- alert_plan:
  - owner:
    consumer:
    condition:
    channel:
    expires_at:
    rearm_rule:
- expected_risk_reward:
  - to_tp1:
  - to_tp2:
  - to_final_target:
- stop_loss:
- stop_loss_type:
- scale_plan:
  - tranche_1:
  - tranche_2:
  - tranche_3:
- add_conditions:
  - item
- take_profit_plan:
  - target_price:
    size_pct_to_close:
    stop_move_after_hit:
- stop_plan:
- stop_escalation_or_tightening_rule:
- reduce_plan:
- break_even_rule:
- trailing_or_lock_rule:
- hedge_or_offset_rule:
- symbol_exposure_conflict_rule:
- what_cancels_further_adds:
- when_to_abort_without_entry:
- wake_without_order_rule:
- management_fail_conditions:
  - item
- execution_and_risk_notes:
- evidence:
  - field:
    source:
    direct_or_inferred:
```

Purpose:

- define how the chosen setup would actually be converted into an order plan
- separate the trade idea from the trigger and risk mechanics
- stop vague â€œgood setupâ€ thinking from turning into vague execution

When this section matters most:

- when there are multiple setup candidates
- when the desk is waiting on a precise trigger
- when alerts should be assigned instead of staring at the chart
- when the same symbol could have backup entries or alternate zones
- when risk on one symbol must be capped across more than one idea

What belongs here:

- exact trigger
- confirmation signal
- order type and order ladder
- stop loss and take profit
- leverage
- risk cap
- account risk amount
- total symbol exposure cap
- confidence-based sizing
- risk/reward estimate
- alert assignment
- add rules
- stop and target rules
- reduce / trail / lock rules
- abort rules

What does not belong here as the main story:

- why the setup exists
- why one candidate ranks above another
- pure invalidation analysis
- long-form historical edge research

Those belong mainly to:

- `Part 10` for candidate ranking
- `Part 9` for invalidation and thesis damage
- `Part 12` for strategy and backtest context

Definitions:

- `management_posture`
  - `active_if_triggered`
    - ready to execute if the chosen setup confirms
  - `paper_watch_only`
    - monitor only; do not commit capital yet
  - `capital_preservation`
    - no entry should be taken now

- `promoted_setup_contract_state`
  - `promoted`
    - a real setup contract exists and can feed `trigger_contract` and `order_plan`
  - `not_promoted`
    - the desk has a thesis or screening candidate, but no executable setup contract exists yet
  - `blocked`
    - another veto or missing dependency prevents promotion right now

- `execution_readiness`
  - `ready_now`
    - trigger and confirmation are already satisfied
  - `wait_for_reset`
    - direction is acceptable, but timing must improve first
  - `wait_for_trigger`
    - the setup exists, but the exact trigger is still missing
  - `no_entry`
    - the desk should not place or stage anything now

- `execution_blocker_now`
  - the plain-English reason the desk cannot place or stage a real order yet
  - if `ENTRY_SIGNALS.json` says `NO_PROMOTED_SETUP`, say that plainly here

- `entry_timing_rule`
  - the plain-English trigger for when the desk is allowed to enter

- `exact_entry_trigger`
  - the candle, reclaim, rejection, sweep, breakout, or breakdown condition that wakes the desk up

- `do_not_chase_rule`
  - what makes the desk skip the trade even if the thesis still exists

- `confidence_based_risk_sizing`
  - how confidence affects risk tier
  - do not let high confidence override hard max risk

- `trigger_contract`
  - the exact wake-up contract that `entry-watch` should use
  - must be specific enough that the trigger can be checked without guessing

- `order_plan`
  - structured staged orders, not vague placeholders
  - if no promoted setup exists yet, keep this explicit `none` or empty by design

- `alert_plan`
  - structured wake-up alerts tied to the trigger contract

- `no_order_reason`
  - why the desk is preserving a no-order state right now instead of pretending a valid live ladder exists

- `expected_risk_reward`
  - the estimated reward-to-risk path to each target tier

- `alert_plan`
  - which alerts should be set so `entry-watch` can respond instead of the desk guessing

- `symbol_exposure_conflict_rule`
  - how the desk handles multiple same-symbol candidates so total risk stays capped

- `when_to_abort_without_entry`
  - conditions where the desk cancels the setup before entering

- `wake_without_order_rule`
  - what should still wake the desk up when there is no promoted setup yet
  - this should point to the promotion condition, not a fake order trigger

- `management_fail_conditions`
  - practical handling failures, not just thesis invalidation

Best current source order:

1. `Part 10: Setup Candidates`
   - chosen candidate
   - candidate role
   - candidate triggers
2. `Part 9: Risk And Invalidation`
   - risk caps
   - abort conditions
   - thesis-break rules
3. `reports/auto/ENTRY_SIGNALS.json`
   - whether a real promoted setup contract exists yet
   - current no-entry blocker truth
4. `Part 2` and `Part 3`
   - entry timing, confirmation, and support for no-chase decisions
5. `Part 4` and `Part 5`
   - pressure and sweep risk that may tighten handling

Current ownership rule:

- `position-sizer` owns sizing, risk caps, and order logic
- `entry-watch` owns live trigger/alert confirmation
- neither one invents the thesis
- `execution` consumes this section after Deezoh chooses the candidate and the trigger is explicit

Hard reality rule:

- if `ENTRY_SIGNALS.json` says `NO_PROMOTED_SETUP`, this section must preserve an explicit `no_entry` or `paper_watch_only` posture
- do not invent a live order ladder, live trigger, or executable chosen setup from screening interest alone

## 12. Strategy And Historical Edge

Owner:

- strategy

Objective:

- say which strategy family best fits the current regime and setup
- show what historical or replay evidence supports or weakens that strategy
- separate live trade desirability from longer-run strategic edge

This section should answer:

- what strategy is this trade idea actually using?
- is that strategy favored in the current regime?
- do we have backtest, replay, or playbook evidence for it?
- what strategy is better if this one is weak?
- what should Deezoh learn from past outcomes before acting?

Fill:

```md
## Strategy And Historical Edge

- owner:
- source:
  - strategy agent + replay/backtest surfaces + strategy playbooks
- observed_at_utc:
- max_age_minutes:
- freshness_state:
- stale_reason:

- key_questions_answered:
  - what strategy family fits this setup?
  - is this strategy favored in the current regime?
  - what backtest or replay evidence supports it?
  - what strategy warning matters before entry?
  - what alternative strategy fits better if this one weakens?

- strategy_family:
- strategy_name:
- regime_fit_verdict:
- strategy_role_in_decision:
- setup_to_strategy_mapping:
- historical_edge_summary:
- evidence_type: live_playbook / replay / backtest / mixed / none
- evidence_window:
- key_performance_context:
  - win_rate:
  - profit_factor:
  - sample_size:
  - max_drawdown:
- strategy_confidence:
- strategy_failure_modes:
  - item
- what_improves_strategy_confidence:
  - item
- what_weakens_strategy_confidence:
  - item
- best_alternative_strategy_if_not_this_one:
- strategy_notes_for_deezoh:
- evidence:
  - field:
    source:
    direct_or_inferred:
```

What belongs here:

- strategy family
- regime fit
- replay/backtest/playbook evidence
- alternative strategy ideas

What does not belong here as the main story:

- exact live trigger
- raw chart structure
- optional influencer or transcript learning

Those belong mainly to:

- `Part 11` for execution
- `Part 2` and `Part 3` for structure and indicators
- `Part 14` for optional external learning overlays

Best current source order:

1. `strategy` agent and its persistent context bundle
2. `strategy-backtest-lab`
3. `openclaw-replay-and-backtest`
4. current playbooks and prior strategy reports
5. optional YouTube overlays only if they survive verification

Current ownership rule:

- `strategy` owns this section
- `strategy` does not override live setup facts
- `Deezoh` consumes this section as a confidence and playbook filter, not as sole permission

## 13. Final Decision

Owner:

- Deezoh

Objective:

- collapse the whole bundle into one real desk posture
- preserve long, short, wait, watch, and no-trade honestly
- make the chosen path and immediate next trigger explicit
- stop the bundle from ending as â€œgood information but no clear callâ€

This section should answer:

- what should the desk do now?
- which setup, if any, is actually chosen?
- what is the immediate reason for the posture?
- what missing proof still blocks a stronger action?
- what exact trigger should make the desk recheck?

Fill:

```md
## Final Decision

- owner:
- source:
  - synthesis of Parts 1 through 12
- observed_at_utc:
- max_age_minutes:
- freshness_state:
- stale_reason:

- key_questions_answered:
  - what should the desk do now?
  - what setup, if any, is chosen?
  - why is that posture better than the alternatives?
  - what missing proof still blocks stronger action?
  - what exact trigger should make the desk recheck?

- bull_case_summary:
- bear_case_summary:
- no_trade_case_summary:
- posture_ranking:
  - best_long:
  - best_short:
  - best_no_trade:
- final_posture: activate / watch / wait / reject / no_trade
- chosen_setup_id:
- chosen_setup_role:
- direction: long / short / none / mixed
- confidence: 0-100
- execution_conflict_summary:
- veto_or_restraint_owner:
- immediate_decision_reason:
- why_this_decision:
- why_not_activate_even_if_entry_ready:
- why_not_the_best_alternative:
- what_would_upgrade_the_posture:
- what_would_downgrade_the_posture:
- missing_proof_before_stronger_action:
  - item
- next_trigger_to_recheck:
- consumer_handoff:
  - who_acts_next:
  - what_they_should_do:
  - what_they_should_not_do:
- phase_progression_decision:
  - next_phase: stay_bundle / open_entry_watch / open_active_trade / stop_no_trade / move_to_closeout
  - why_progress_now:
  - why_not_stay_in_current_phase:
  - best_alternative_phase_rejected:
  - expected_owner_of_next_phase:
  - expected_next_document:
- deezoh_decision_trace:
  - decision_trace_id:
  - decision_owner:
  - decision_question:
  - winning_choice:
  - why_this_choice_won:
  - strongest_rejected_alternative:
  - why_that_alternative_lost:
  - counterarguments_considered:
    - item
  - phase_transition_trigger:
- evidence:
  - field:
    source:
    direct_or_inferred:
```

What belongs here:

- the final desk posture
- the chosen setup or explicit no-trade choice
- the immediate reason
- the next trigger to recheck
- the action handoff

What does not belong here as the main story:

- raw structure detail
- raw indicator rows
- full candidate ranking logic
- full management-plan detail

Those belong mainly to:

- `Part 2` through `Part 5` for raw evidence
- `Part 10` for ranking paths
- `Part 11` for handling plan

Definitions:

- `posture_ranking`
  - the best current version of:
    - long
    - short
    - no-trade
  - this forces comparison, not one-sided bias

- `final_posture`
  - `activate`
    - candidate is ready and action should proceed inside the allowed execution policy
  - `watch`
    - a path is favored, but still needs closer observation
  - `wait`
    - a path exists, but patience is still better than action
  - `reject`
    - current trade idea should be dismissed
  - `no_trade`
    - not trading is the best current outcome

- `execution_conflict_summary`
  - the plain-English explanation when one surface looks tradable but another still vetoes or restrains action

- `veto_or_restraint_owner`
  - which section or live report is currently stopping escalation to `activate`
  - examples:
    - `Part 11`
    - `Part 9`
    - `DEEZOH_SCREENER_CONSUMPTION.json`
    - `ACTIVE_SETUPS.json macro alignment`

- `why_not_the_best_alternative`
  - why the second-best posture or candidate still loses

- `why_not_activate_even_if_entry_ready`
  - use this when `ENTRY_SIGNALS.json` says `READY_TO_TRADE` but the broader desk should still stay restrained
  - examples:
    - macro veto still active
    - setup is marked TP-only / counter-trend
    - confidence is too low
    - broader screener workflow is still protection-first

- `what_would_upgrade_the_posture`
  - what would move `wait` to `watch`, `watch` to `activate`, or `no_trade` to a live path

- `consumer_handoff`
  - tells the next owner exactly what to do and not do

Best current source order:

1. `Part 10: Setup Candidates`
   - best current path
   - best alternative path
2. `Part 11: Execution Plan, Orders, And Risk`
   - whether the chosen path is actually tradable now
3. `reports/auto/ENTRY_SIGNALS.json` and `reports/auto/ACTIVE_SETUPS.json`
   - live execution-ready signal versus live restraint truth
4. `Part 12: Strategy And Historical Edge`
   - whether the strategy itself deserves confidence in this regime
5. `Part 9: Risk And Invalidation`
   - no-trade and downgrade logic
6. `reports/auto/DEEZOH_SCREENER_CONSUMPTION.json`
   - screener-selected workflow
   - best no-trade and protection-first posture
7. `Parts 2` through `8`
   - upstream evidence supporting the summaries

Current ownership rule:

- `Deezoh` owns this section
- `Deezoh` makes the final desk posture
- `trade-judge` may challenge or compare the posture
- `execution` should only consume this section after the posture and handoff are explicit

Hard conflict rule:

- if `ENTRY_SIGNALS.json` says `READY_TO_TRADE` but the live bundle still carries a real restraint such as:
  - macro `STAY OUT`
  - `ACTIVE_SETUPS.json` saying `macro_aligned = false`
  - `ACTIVE_SETUPS.json` saying `use_as_tp_target = true`
  - screener workflow still `no_trade_protection`
- then `Deezoh` must explain the conflict and keep `final_posture` at `watch`, `wait`, or `no_trade` unless the restraint is explicitly resolved

## 14. Optional Learning And Idea Overlays

Owner:

- youtube-analyst + strategy

Objective:

- capture optional outside learning that may improve question framing, strategy ideas, or watchlists
- keep those inputs helpful without letting them override fresh market evidence

This section should answer:

- what optional learning is relevant here?
- what came from YouTube or TradingView-style idea lanes?
- did that input survive verification or stay only as a question seed?
- how should Deezoh use it without over-trusting it?

Fill:

```md
## Optional Learning And Idea Overlays

- owner:
- source:
  - youtube overlays + idea system + optional external idea lanes
- observed_at_utc:
- freshness_state:
- stale_reason:
- supplemental_context:
  - used:
  - freshness_state:
  - age_minutes:
  - override_allowed: false
  - consumer_effect:
  - conflict_flags:
    - item
  - summary:
- optionality_state: not_used / used_as_question_seed / verified_and_helpful / stale_only
- key_questions_answered:
  - what optional learning is relevant here?
  - what part is verified versus only a seed?
  - how should Deezoh use it safely?
- youtube_overlay_context:
  - overlay_updated_at:
  - agents_consulted:
    - item
  - analyst_snapshot:
  - narrative_bias_summary:
  - watchlist_hints:
    - item
  - playbook_hints:
    - item
  - relevant_conflict:
- tradingview_or_idea_context:
  - source_file:
  - generated_at:
  - symbols_considered:
    - item
  - idea_id:
  - relevant_findings:
    - symbol:
      direction:
      timeframe:
      confidence:
      entry_zone:
      target_1:
      stop_loss:
      age_days:
      thesis:
  - setup_note:
  - expiry_or_validation_state:
- verified_takeaways:
  - item
- question_seeds_only:
  - item
- do_not_use_as_permission:
  - item
- consumer_use_for_deezoh:
- evidence:
  - field:
    source:
    direct_or_inferred:
```

What belongs here:

- optional learning
- transcript or influencer playbook notes
- TradingView-idea style optional context
- question seeds for Deezoh

What does not belong here as the main story:

- live permission to trade
- fresh market truth
- replacement for Parts 2 through 13

Best current source order:

1. `agents/*/YOUTUBE_OVERLAY.md`
2. `scripts/youtube_analyst/update_agent_overlays.py`
3. `reports/auto/YOUTUBE_INTEL.json` and detailed reports when available
4. `reports/auto/IDEAS` plus `scripts/idea_system/validate_ideas.py`
5. `scripts/idea_system/share_findings.py` when a shared optional-findings surface exists
6. any optional TradingView idea lane only after validation

Current ownership rule:

- `youtube-analyst` owns refresh and overlay generation
- `strategy` consumes it for playbook ideas
- `Deezoh` uses it as optional context only
- it must never override fresh script outputs or live bundle evidence
- it may only:
  - add a question
  - suggest a watchlist candidate
  - lower confidence
  - flag contradiction

## Minimum Quality Rules

Each section must:

- state the bias clearly
- show 2 to 3 concrete evidence points
- state missing data when relevant
- avoid vague words like `looks good` without support

## What To Improve Further

Best next improvements to this template:

1. add a machine-readable JSON twin of the same structure
2. add automated stale-field checks instead of trusting manual writers
3. add per-section source attribution
4. add stock-specific subfields for earnings and fundamentals
5. add a compact replay score block for historical testing

