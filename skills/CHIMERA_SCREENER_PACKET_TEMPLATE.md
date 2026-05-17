# Chimera Screener Packet Template

Purpose:

- decide which symbols deserve deeper analysis
- explain why those symbols were selected over alternatives
- keep broad-market discovery separate from one-symbol research bundles
- give Deezoh a clean queue for chart, indicator, positioning, liquidation, macro, catalyst, and entry-watch follow-up

This document is upstream of the normal `CHIMERA_RESEARCH_BUNDLE_TEMPLATE.md`.

One screener cycle should produce one screener packet.
Each selected symbol can then receive its own normal Chimera research bundle.

Do not create one huge 12-part research bundle containing every screened coin.

This packet answers market-wide discovery questions such as:

- what is the macro and majors backdrop?
- are we in trend, range, trap, event, or no-trade conditions?
- which symbols deserve deeper work right now?
- which symbols only deserve chart review, indicator timing review, or watch status?
- why should the desk ignore other symbols for now?

## Ownership

Owner:

- `screener`

Consumers:

- `Deezoh`
- `chart-analyzer`
- `indicator-analyst`
- `market-maker`
- `entry-watch`
- per-symbol research-bundle builders

Machine source:

- `/root/openclawtrading/reports/auto/SCOUT_REPORT.json`

Decision-facing output:

- screener packet

## Screener Packet

Fill:

```md
# Screener Packet

- packet_id:
- observed_at_utc:
- packet_owner: screener
- linked_previous_documents:
  - document_type:
    document_id:
    why_it_matters_now:
- linked_next_documents:
  - document_type:
    document_id:
    owner:
    status: planned / opened / waiting / not_needed
- source:
  - SCOUT_REPORT.json
  - OPPORTUNITIES.json
  - WATCHLISTS.json
  - MARKET_CONTEXT.json
  - MACRO_BIAS.json
  - NEWS.json
  - CANDLES.json
  - DIVERGENCES.json
  - DERIVATIVES.json
- scan_mode: broad_hunt / directed_review / watchlist_refresh / event_scan
- universe: crypto_majors / full_crypto_universe / watchlist / commodities / equities / mixed_market
- market_state: trend / range / event / transition / data_unreliable
- desk_phase: broad_hunt / shortlist_refine / no_trade_protection / active_trade_monitor / review_only
- selected_workflow:
- workflow_reason:
- major_market_board:
  - btc:
    structure_read:
    momentum_read:
    why_it_matters:
  - eth:
    structure_read:
    momentum_read:
    why_it_matters:
  - sol:
    structure_read:
    momentum_read:
    why_it_matters:
  - btc_d:
    read:
    why_it_matters:
  - usdt_d:
    read:
    why_it_matters:
  - dxy:
    read:
    why_it_matters:
  - spx_ndx:
    read:
    why_it_matters:
  - gold_oil_rates:
    read:
    why_it_matters:
- source_freshness:
  - source:
    status: fresh / stale / missing / proxy
    observed_at_utc:
    effect_on_selection:

- discovery_lenses:
  - trend_continuation:
    status:
    notes:
  - breakout_or_acceptance:
    status:
    notes:
  - failed_breakout_or_trap:
    status:
    notes:
  - accumulation_or_stealth_strength:
    status:
    notes:
  - distribution_or_crowded_weakness:
    status:
    notes:
  - mean_reversion_or_reset:
    status:
    notes:

- selection_criteria:
  - signal_strength:
  - multi_timeframe_agreement:
  - location_quality:
  - indicator_timing_quality:
  - derivatives_and_liquidation_risk:
  - volume_liquidity_quality:
  - catalyst_or_macro_support:
  - structural_market_intel_support:
  - freshness_and_data_confidence:
  - risk_reward_readiness:

- long_book:
  - symbol:
    rank:
    score:
    status:
    why_selected:
    analysis_depth_decision: auto_bundle / chart_first / indicator_first / positioning_first / watch_only / reject_now
    next_specialist_questions:
      - lane:
        question:

- short_book:
  - symbol:
    rank:
    score:
    status:
    why_selected:
    analysis_depth_decision:
    next_specialist_questions:
      - lane:
        question:

- watch_book:
  - symbol:
    rank:
    reason_to_watch:
    wake_trigger:
    analysis_depth_decision:

- no_trade_case:
  - summary:
  - reasons:
  - what_would_change_it:

- analysis_queue:
  - symbol:
    direction:
    rank:
    analysis_depth_decision:
    reason:
    specialist_handoffs:
      - lane:
        question:

- rejected_or_deferred:
  - symbol:
    reason:
    recheck_trigger:

- specialist_handoffs:
  - chart_analyzer:
    - symbol:
      direction:
      question:
  - indicator_analyst:
    - symbol:
      direction:
      question:
  - market_maker:
    - symbol:
      direction:
      question:
  - entry_watch:
    - symbol:
      direction:
      question:

- coins_selected_for_full_bundle:
  - symbol:
    direction:
    screener_rank:
    screener_book:
    screener_reason:
    analysis_depth_decision: auto_bundle
    specialist_questions_from_screener:
      - lane:
        question:

- why_these_coins_over_others:
  - item
- what_would_change_the_shortlist:
  - item
- next_phase_routes:
  - symbol:
    next_document:
    next_owner:
    why_now:
- transition_receipts:
  - symbol:
    promoted_to_phase:
    promoted_document_type:
    promotion_owner:
    why_progress_now:
    why_not_stay_in_screener:
    best_alternative_rejected:
    required_follow_up_question:
- deezoh_shortlist_reasoning:
  - best_long_now:
    why:
  - best_short_now:
    why:
  - best_no_trade_now:
    why:
  - why_promoted_coins_won_over_others:
  - why_some_good_coins_still_did_not_advance:
- packet_decision_summary:
```

## Analysis Depth Rules

Use these values:

- `auto_bundle`
  - create a full per-symbol research bundle now
- `chart_first`
  - send to `chart-analyzer` before deciding whether to create a full bundle
- `indicator_first`
  - send to `indicator-analyst` before a full bundle
- `positioning_first`
  - send to derivatives, liquidation, or market-maker lanes before a full bundle
- `watch_only`
  - keep in the screener packet and watch list; no full bundle yet
- `reject_now`
  - do not analyze further unless conditions change

## Selection Rules

Default full-bundle budget:

- top `1` to `3` names per cycle

Promote to `auto_bundle` when:

- the symbol is top-ranked in a real long or short book
- the signal is fresh enough to matter
- the location and timing questions are answerable
- the next specialist questions are clear
- the symbol can change Deezoh's best long, best short, or no-trade decision

Do not promote to `auto_bundle` when:

- the symbol is only a market-cap placeholder
- the report says review-only
- the no-trade case dominates
- the next needed work is only chart, indicator, or positioning confirmation
- source freshness is too weak for deeper synthesis

## Coin Bundle Link

When a selected symbol gets a normal Chimera research bundle, `Part 1: Instrument And Context` must include:

- `trigger_source: screener_hit`
- `screener_packet_id`
- `screener_rank`
- `screener_book`
- `screener_reason`
- `analysis_depth_decision`
- `specialist_questions_from_screener`

This keeps the per-symbol bundle traceable to the market-wide selection decision.

## Minimum Quality Rules

The screener packet is not complete unless it states:

- what BTC, ETH, SOL, BTC.D, and USDT.D are saying about the board
- why the selected symbols deserve attention
- why other symbols were deferred or rejected
- whether no-trade is stronger than forcing a setup
- why a symbol was promoted to the next phase instead of staying in screener
- which specialist questions should run next
- which symbols receive full bundles and which do not
- what would change the shortlist
