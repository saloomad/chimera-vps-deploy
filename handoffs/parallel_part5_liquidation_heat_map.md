# Part 5 Proposal: Liquidation Heat Map

## Objective

Show where liquidation pressure is concentrated, which side is vulnerable, whether price is likely to get pulled into a sweep, and whether the liquidation picture supports or fights the current setup.

This section exists to answer:

- where are the nearest meaningful liquidation clusters above and below price
- which side is more exposed right now
- is there a likely sweep path before the real move
- does the heat map improve confidence, reduce confidence, or force patience
- which windows are exact, screenshot-only, or proxy-only right now

## Section Owner

- primary owner: `market-maker`
- coordinator/consumer: `Deezoh`

Why:

- the existing pipeline already treats `market-maker` as the lane for OI, funding, crowding, trap risk, liquidation, and max-pain context
- Deezoh should coordinate this section, but should not invent liquidation truth itself

## What Belongs Here

- liquidation clusters above and below current price
- max-pain or strongest magnet zone when real evidence exists
- long-liquidation pressure vs short-liquidation pressure
- nearest sweep targets
- whether the setup is vulnerable to a stop hunt first
- timeframe-window truth for `12h`, `24h`, `48h`, `3d`, `1w`
- whether the liquidation picture supports long, supports short, or argues for waiting
- a separate agent-analysis pass that confirms the OCR/structured levels or adds extra levels that matter
- explicit blocker/caveat when the section is only proxy-grade

## What Does Not Belong Here

- generic OI/funding commentary by itself
- chart structure mapping like support, resistance, OB, FVG, VWAP, POC, fib
- indicator commentary like RSI/MACD
- macro or news interpretation
- position sizing and stop placement
- fake precision from derivatives proxy data when no real heatmap evidence exists

## Exact Recommended Fields

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

- window_truth_map:
  - window:
    state:
    blocker_state:
    notes:

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
  - item
```

## Allowed Values

- `source_mode`
  - `exact_heatmap_vision`
  - `exact_heatmap_structured`
  - `exact_heatmap_structured_plus_agent_review`
  - `screenshot_only_needs_vision`
  - `derivatives_proxy_only`
  - `missing`

- `freshness_state`
  - `fresh`
  - `stale`
  - `missing`
  - `not_checked`

- `applicability`
  - `required`
  - `useful_optional`
  - `not_applicable`

- `blocker_state`
  - `none`
  - `coinglass_window_locked`
  - `login_missing`
  - `playwright_missing`
  - `chart_capture_failed`
  - `symbol_unsupported`
  - `vision_not_run`
  - `proxy_only`
  - `unknown`

- `vulnerable_side`
  - `longs`
  - `shorts`
  - `both`
  - `unclear`

- `heatmap_balance_state`
  - `long_heavy`
  - `short_heavy`
  - `two_sided`
  - `thin`
  - `unclear`

- `sweep_bias`
  - `up_first`
  - `down_first`
  - `two_sided_squeeze`
  - `no_clear_sweep`
  - `unclear`

- `intensity`
  - `low`
  - `medium`
  - `high`
  - `extreme`

- `cluster_type`
  - `long_liquidation`
  - `short_liquidation`
  - `mixed`

- `cluster_role`
  - `nearest_magnet`
  - `primary_magnet`
  - `secondary_magnet`
  - `sweep_then_reverse`
  - `invalidates_if_hit`

- `squeeze_or_trap_state`
  - `none`
  - `long_squeeze_risk`
  - `short_squeeze_risk`
  - `two_sided_squeeze_risk`
  - `stop_hunt_risk`
  - `unclear`

- `setup_interaction`
  - `supports_long`
  - `supports_short`
  - `supports_wait`
  - `mixed`
  - `not_applicable`

- `image_analysis_mode`
  - `chart_agent_review`
  - `screenshot_vision_review`
  - `not_run`

- `analysis_status`
  - `complete`
  - `partial`
  - `blocked`
  - `not_run`

- `zone_confirmation_state`
  - `confirms_core_levels`
  - `confirms_with_additions`
  - `partially_confirms`
  - `disagrees_with_structured_read`
  - `not_run`

- `invalidates_or_delays_setup`
  - `none`
  - `delays_long`
  - `delays_short`
  - `invalidates_long`
  - `invalidates_short`
  - `forces_wait`

## Definitions

- `applicability`
  - `required` for crypto perpetual/futures setups where liquidation behavior matters directly
  - `useful_optional` when futures context exists but the trade can still be judged without it
  - `not_applicable` for assets/setups with no meaningful liquidation-map surface

- `exact_heatmap_vision`
  - a real heatmap screenshot exists and the section was filled from visual extraction of actual clusters

- `exact_heatmap_structured`
  - a real structured liquidation report exists with actual cluster/zone outputs, not just proxy derivatives summary

- `exact_heatmap_structured_plus_agent_review`
  - structured extraction returned exact zones and a separate agent/screenshot review confirmed or extended them

- `screenshot_only_needs_vision`
  - a real screenshot exists for the requested window, but the structured exact extraction did not succeed
  - use this as visual proof only, not as exact cluster truth

- `derivatives_proxy_only`
  - only fallback OI/funding/ratio context exists; exact heatmap clusters are not available
  - this is still useful pressure context, but it is not enough to claim exact sweep targets

- `heatmap_balance_state`
  - `long_heavy`: more meaningful long liquidation pressure sits below price
  - `short_heavy`: more meaningful short liquidation pressure sits above price
  - `two_sided`: meaningful pressure exists on both sides, raising squeeze risk
  - `thin`: no meaningful nearby clusters

- `sweep_bias`
  - the most likely first draw if price is hunting liquidity before the cleaner move

- `max_pain_zone`
  - the strongest concentration or most likely pain magnet
  - leave as `missing` or `unclear` if only proxy data exists

- `setup_interaction`
  - how the liquidation picture changes the trade judgment, not what the whole trade plan is

- `agent_heatmap_analysis`
  - this is the second-pass read
  - it should confirm the OCR/structured zones when they look right
  - it may add extra levels or visual caveats when the chart clearly shows more than the extractor captured
  - it should not replace the structured extractor when exact numeric zones already exist

## How Deezoh Knows It Is Filled Enough

This section is `complete enough` only when all of these are true:

- `owner` is present
- `source_mode` is present
- `observed_at_utc` is present
- `freshness_state` is present
- `applicability` is present
- one of these is true:
  - both `nearest_above_cluster` and `nearest_below_cluster` are filled from exact evidence
  - or the section explicitly says `source_mode = derivatives_proxy_only` and carries `blocker_state` plus `blocker_detail`
- `setup_interaction` is present
- if exact structured extraction succeeded, `agent_heatmap_analysis` should also be present unless explicitly marked `not_run` with a reason
- if exact structured extraction is missing but screenshot review still ran, the section may use `SCREENSHOT_PLUS_AGENT_REVIEW` and must say it is screenshot-led, not exact-cluster-led

Deezoh should treat the section as `not filled enough` when:

- it claims exact clusters without an exact source
- it has only generic funding/OI pressure but no blocker explanation
- it has exact zones but no separate confirmation/analysis pass and no reason for skipping it
- it hides that the section is proxy-only
- it omits freshness and current price reference

For non-applicable assets:

- if `applicability = not_applicable`, the section is filled enough only when that is stated plainly and the reason is given

## Source Order

1. `trading_system/scripts/coinglass_heatmap_exact.py`
   - best current exact structured path when it returns real clusters
2. fresh screenshot capture from `trading_system/scripts/liquidation_heatmap.py`
   - helper for obtaining the image input
   - not the final analyst by itself
3. `trading_system/scripts/coinglass_maxpain_scraper.py` plus `MAXPAIN_SUMMARY.json`
   - good for max-pain and magnet context
   - not enough to replace exact cluster extraction
4. `liquidation-vision-analyzer`
   - fallback exact-reading path from screenshots when structured extraction is unavailable
5. market-maker derivatives fallback reports
   - use only as `derivatives_proxy_only`
   - useful for pressure, not enough for exact sweep targets

## Known Proof / Capability Notes

- `agents/market-maker/AGENTS.md` already makes `market-maker` the existing lane for liquidation and max-pain context
- `trading_system/scripts/coinglass_heatmap_exact.py` is now the strongest exact path for this section
  - Windows local proof:
    - `BTC 24h` -> exact structured clusters worked
    - `ETH 24h` -> exact structured clusters now work in the authenticated local route
    - `SOL 24h` -> exact structured clusters now work in the authenticated local route
    - `12h`, `48h`, `3d`, `1w` -> honest blocked-window JSON
- `trading_system/scripts/liquidation_heatmap.py` can capture screenshots on both Windows and the live VPS, but it is still a capture utility, not the section owner
- `trading_system/scripts/coinglass_maxpain_scraper.py` works on both Windows and the live VPS and gives real max-pain targets
- live VPS truth is still weaker than Windows local for exact heatmap extraction:
  - Playwright and max-pain scrape work on VPS
  - the exact CoinGlass heatmap route is still blocked in the current unauthenticated VPS path
- `trading_system/scripts/indicators/liquidation_scorer.py` is still a stub and is not trustworthy as a section owner
- `coinglass_screenshots/SOL_full_analysis.json` is not trustworthy as exact evidence because it is mostly nulls and empty cluster arrays

Practical trust split:

- trusted for exact cluster truth:
  - `coinglass_heatmap_exact.py` when `data_extracted = true`
  - current best exact windows: `BTC 24h`, `ETH 24h`, `SOL 24h`
- trusted for exact-ish magnet support:
  - `MAXPAIN_SUMMARY.json` from the browser scrape lane
- helper-only:
  - `liquidation_heatmap.py`
- not trustworthy as exact owner right now:
  - `liquidation_scorer.py` stub
  - null/empty legacy analysis JSON
  - proxy-only derivatives summaries pretending to be heatmap truth

Generic searchable-symbol rule:

- do **not** collapse `CoinAnk unsupported` into `symbol unsupported`
- if CoinGlass search can resolve the contract, the maintained lane still supports the symbol
- proven ad hoc examples now include:
  - `HYPE`
    - CoinGlass screenshot works
    - exact `24h` structured extraction works
    - agent screenshot review can be merged into the summary lane
  - `DOGE`
    - ad hoc `--coin DOGE` run works through the same path

## Ideal Example Response

```md
## Liquidation Heat Map

- owner: market-maker
- source: CoinGlass 24h exact structured extraction + CoinGlass max-pain browser scrape
- source_mode: exact_heatmap_structured
- observed_at_utc: 2026-05-05T18:42:00Z
- max_age_minutes: 20
- freshness_state: fresh
- stale_reason: none
- applicability: required
- blocker_state: none
- blocker_detail: none

- window_truth_map:
  - window: 24h
    state: exact_heatmap_structured
    blocker_state: none
    notes: exact clusters extracted from the live CoinGlass 24h heatmap
  - window: 48h
    state: screenshot_only_needs_vision
    blocker_state: coinglass_window_locked
    notes: screenshot may exist, but the current structured extractor did not get a successful CoinGlass response

- current_price_reference: 64210
- current_price_reference_observed_at_utc: 2026-05-05T18:42:00Z

- vulnerable_side: longs
- heatmap_balance_state: long_heavy
- sweep_bias: down_first
- confidence: 78

- nearest_above_cluster:
  - price_zone: 64680 to 64820
  - window: 24h
  - intensity: medium
  - cluster_type: short_liquidation
  - distance_pct: 0.92
  - evidence_source: CoinGlass 24h exact structured extract

- nearest_below_cluster:
  - price_zone: 63740 to 63910
  - window: 24h
  - intensity: high
  - cluster_type: long_liquidation
  - distance_pct: -0.63
  - evidence_source: CoinGlass 24h exact structured extract

- strongest_clusters:
  - window: 24h
    side: longs
    price_zone: 63740 to 63910
    intensity: high
    distance_pct: -0.63
    cluster_role: primary_magnet
    evidence_source: CoinGlass 24h exact structured extract

- max_pain_zone:
  - price_zone: 63800 to 63900
  - window: 24h
  - confidence: medium
  - evidence_source: CoinGlass browser scrape

- squeeze_or_trap_state: stop_hunt_risk
- liquidity_path_scenario: price is more likely to sweep the heavy long cluster below first, then reassess for reversal if structure still holds
- setup_interaction: supports_wait
- invalidates_or_delays_setup: delays_long
- evidence:
  - the heaviest nearby cluster sits below price, not above
  - the nearest short cluster is smaller and farther away
  - this liquidation map argues against chasing an immediate long before the lower sweep risk is resolved
```
