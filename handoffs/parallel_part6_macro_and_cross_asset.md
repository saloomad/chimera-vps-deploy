# Part 6 Proposal: Macro And Cross-Asset

## Objective

Define the macro backdrop that can help, weaken, or veto the trade thesis for the symbol in this bundle.

This section should answer:

- what the broader macro regime is right now
- whether cross-asset signals support or fight the setup
- whether there is a near-term macro event risk that should slow or block conviction
- whether the symbol is trading with or against its usual macro relationships

This part is not the place for chart structure, indicators, or headline-by-headline news dumping. It is the macro and cross-market context layer.

## Section Owner

- primary owner: `macro-analyst`
- coordination owner: `Deezoh`

Meaning:

- `macro-analyst` fills the section
- `Deezoh` checks whether it is fresh enough, complete enough, and attached to the right symbol/setup before final judgment

## What Belongs Here

- macro regime read
- dollar / yields / rates / liquidity tone when relevant
- equity risk tone when relevant
- volatility / stress tone when relevant
- gold / oil / commodities context when relevant
- cross-asset correlation or divergence that matters for this symbol
- major scheduled macro risks inside the active trading horizon
- regime shift warnings
- macro reason for caution, confirmation, or veto

## What Does Not Belong Here

- support and resistance mapping
- FVG / order block / hotzone logic
- RSI / MACD / indicator detail
- exchange-specific derivatives positioning
- general news recap with no macro significance
- setup entry, stop, targets, or execution plan

## Exact Recommended Fields

```md
## Macro And Cross-Asset

- owner:
- source:
- observed_at_utc:
- max_age_minutes:
- freshness_state:
- stale_reason:

- macro_regime:
- macro_regime_confidence:
- macro_bias:
- macro_bias_strength:
- time_horizon_relevance:

- asset_macro_profile:
- primary_macro_drivers:
  - item

- cross_asset_watchlist:
  - ticker:
    role:
    relevance:

- cross_asset_state:
  - ticker:
    direction_state:
    relationship_to_symbol:
    supports_setup:
    note:

- rates_signal:
- dollar_signal:
- equity_risk_signal:
- volatility_signal:
- liquidity_signal:
- commodity_signal:

- correlation_regime:
- relationship_stability:
- cross_asset_confirmation:
- cross_asset_conflicts:
  - item

- scheduled_macro_events_in_horizon:
  - event_name:
    time_utc:
    importance:
    expected_impact_mode:
    blocking_risk:

- macro_veto_state:
- macro_caution_flags:
  - item

- evidence:
  - item
```

## Allowed Values Where Useful

- `freshness_state`
  - `fresh`
  - `stale`
  - `missing`
  - `not_checked`

- `macro_regime`
  - `risk_on`
  - `mixed`
  - `risk_off`
  - `event_locked`
  - `transition`
  - `unclear`

- `macro_bias`
  - `bullish`
  - `bearish`
  - `mixed`
  - `neutral`
  - `blocked`

- `macro_bias_strength`
  - `strong`
  - `moderate`
  - `weak`
  - `unclear`

- `time_horizon_relevance`
  - `scalp_relevant`
  - `intraday_relevant`
  - `swing_relevant`
  - `position_relevant`
  - `low_relevance`

- `asset_macro_profile`
  - `crypto_beta`
  - `equity_beta`
  - `rate_sensitive`
  - `dollar_sensitive`
  - `commodity_sensitive`
  - `safe_haven`
  - `inflation_sensitive`
  - `mixed_profile`

- `role` in `cross_asset_watchlist`
  - `benchmark`
  - `risk_proxy`
  - `liquidity_proxy`
  - `inflation_proxy`
  - `growth_proxy`
  - `safe_haven_proxy`
  - `volatility_proxy`

- `relevance`
  - `high`
  - `medium`
  - `low`

- `direction_state`
  - `up`
  - `down`
  - `flat`
  - `mixed`
  - `unknown`

- `relationship_to_symbol`
  - `positive_correlation`
  - `negative_correlation`
  - `regime_dependent`
  - `weak_relationship`
  - `unknown`

- `supports_setup`
  - `yes`
  - `no`
  - `mixed`
  - `unclear`

- `rates_signal`
  - `tailwind`
  - `headwind`
  - `mixed`
  - `neutral`
  - `not_applicable`

Use the same allowed values for:

- `dollar_signal`
- `equity_risk_signal`
- `volatility_signal`
- `liquidity_signal`
- `commodity_signal`

- `correlation_regime`
  - `aligned`
  - `diverging`
  - `unstable`
  - `unclear`

- `relationship_stability`
  - `stable`
  - `shifting`
  - `event_distorted`
  - `unclear`

- `cross_asset_confirmation`
  - `supports_long`
  - `supports_short`
  - `mixed`
  - `no_confirmation`
  - `blocked_by_macro`

- `importance`
  - `high`
  - `medium`
  - `low`

- `expected_impact_mode`
  - `volatility_risk`
  - `trend_confirmation`
  - `trend_reversal_risk`
  - `liquidity_shock_risk`
  - `headline_only`
  - `unknown`

- `blocking_risk`
  - `hard_block`
  - `soft_block`
  - `watch_only`
  - `none`

- `macro_veto_state`
  - `none`
  - `soft_veto`
  - `hard_veto`
  - `event_wait`

## Definitions

- `macro_regime`
  - the current broad market backdrop, not the chart pattern
  - example: `risk_on` means macro conditions broadly support risk-taking

- `macro_bias`
  - whether macro context leans for or against the thesis for this symbol
  - this is the verdict, not the raw evidence

- `asset_macro_profile`
  - the main way this asset usually reacts to macro pressure
  - example: BTC often behaves as `crypto_beta` with sensitivity to liquidity, DXY, yields, and risk tone

- `cross_asset_watchlist`
  - the short list of outside markets that matter most for this symbol
  - examples:
    - BTC: `DXY`, `NDX`, `SPX`, `VIX`, `US10Y`, `gold`
    - gold: `DXY`, `US10Y`, `real yields`, `oil`
    - oil: `DXY`, `SPX`, `global growth proxies`, `geopolitical risk`

- `relationship_to_symbol`
  - the expected relationship, not what price did in one candle
  - example: `DXY` is often a `negative_correlation` input for BTC and gold

- `correlation_regime`
  - whether the current cross-asset relationships are behaving normally
  - `diverging` means the setup may be fighting its usual macro map

- `relationship_stability`
  - whether macro relationships are stable enough to trust
  - `event_distorted` means a CPI/FOMC-style event may be overriding normal relationships

- `macro_veto_state`
  - whether macro context should slow, block, or invalidate a trade even if structure looks good

## How Deezoh Knows It Is Filled Enough

Minimum required before using this section in a final decision:

- freshness fields are present
- `macro_regime` is present
- `macro_bias` is present
- at least `2` relevant cross-asset signals are filled for the symbol
- `scheduled_macro_events_in_horizon` is either filled or explicitly `none`
- `macro_veto_state` is present

If those are missing:

- Deezoh should mark the section `incomplete`
- the setup can still stay on watch
- the final judge should not claim strong macro confirmation

Filled enough does not mean perfect.

It means:

- the current regime is stated
- the most relevant outside markets were checked
- near-term event risk was checked
- macro support versus macro conflict is explicit

## Source Order

Use this source order unless a better live source is explicitly proved later:

1. `macro-analyst` skill
   - best current high-level macro and cross-asset synthesis lane
   - useful for macro indicator history, rates/yields context, and cross-asset windows

2. local Chimera macro producers
   - `scripts/macro_bias_builder/macro_bias_builder.py`
   - current macro report surfaces such as `MACRO_BIAS.json` and `MACRO.json`
   - use when current Chimera runtime truth matters more than generic synthesis

3. local Chimera cross-asset and market-context builders
   - `cross_asset_fetcher.py`
   - `market_context_fetcher.py`
   - use for explicit cross-market state snapshots and stamped inputs

4. `macro-calendar` skill
   - use for scheduled event risk and timing

5. `news-briefing` skill
   - use only for macro-significant event context that affects the macro read
   - do not let it replace the macro section

6. `market-intel` skill
   - use as a helper when structural liquidity or broader regime context matters

## Known Proof / Capability Notes

- The current shared template still has a thin placeholder for Part 6, so this proposal intentionally expands it into a real owner-driven section.
- Earlier capability audits already noted that Bitget `macro-analyst` is stronger than a simple headline reader and can cover:
  - macro indicator history
  - rates / yields context
  - BTC cross-asset correlation windows
  - DXY, VIX, SPX, NDX, gold, and oil style snapshots
- Chimera repo research also already identified local cross-asset and market-context builders such as:
  - `cross_asset_fetcher.py`
  - `market_context_fetcher.py`
  - `macro_bias_builder.py`
- Known caution:
  - current runtime-safe local macro surfaces may preserve crypto structure and fear/greed better than full tradfi breadth, so Deezoh should not overclaim full macro coverage if DXY / rates / equity risk fields are missing or stale
- Known live lesson:
  - macro timing fields should prefer exact timing like `hours_away` or exact UTC event fields rather than loose date-only logic
- Practical rule:
  - if event timing is stale or ambiguous, Deezoh should downgrade macro confidence rather than pretending event risk is clear

## Ideal Example Response

```md
## Macro And Cross-Asset

- owner: macro-analyst
- source: macro-analyst + macro_bias_builder.py + macro-calendar
- observed_at_utc: 2026-05-05T09:42:00Z
- max_age_minutes: 30
- freshness_state: fresh
- stale_reason: none

- macro_regime: mixed
- macro_regime_confidence: moderate
- macro_bias: mixed
- macro_bias_strength: moderate
- time_horizon_relevance: swing_relevant

- asset_macro_profile: crypto_beta
- primary_macro_drivers:
  - BTC is still reacting mainly to dollar direction, equity risk tone, and liquidity expectations
  - macro event risk is elevated enough that upside continuation should not be treated as clean trend confirmation

- cross_asset_watchlist:
  - ticker: DXY
    role: benchmark
    relevance: high
  - ticker: NDX
    role: growth_proxy
    relevance: high
  - ticker: VIX
    role: volatility_proxy
    relevance: medium
  - ticker: US10Y
    role: liquidity_proxy
    relevance: high
  - ticker: XAUUSD
    role: safe_haven_proxy
    relevance: medium

- cross_asset_state:
  - ticker: DXY
    direction_state: up
    relationship_to_symbol: negative_correlation
    supports_setup: no
    note: firmer dollar is a headwind for BTC continuation
  - ticker: NDX
    direction_state: up
    relationship_to_symbol: positive_correlation
    supports_setup: yes
    note: equity risk tone still supports a higher-beta bid
  - ticker: VIX
    direction_state: flat
    relationship_to_symbol: negative_correlation
    supports_setup: mixed
    note: no clear stress spike, but no strong calm confirmation either
  - ticker: US10Y
    direction_state: up
    relationship_to_symbol: negative_correlation
    supports_setup: no
    note: higher yields are limiting macro tailwind
  - ticker: XAUUSD
    direction_state: up
    relationship_to_symbol: regime_dependent
    supports_setup: mixed
    note: safe-haven bid suggests macro confidence is not fully clean

- rates_signal: headwind
- dollar_signal: headwind
- equity_risk_signal: tailwind
- volatility_signal: neutral
- liquidity_signal: mixed
- commodity_signal: mixed

- correlation_regime: unstable
- relationship_stability: shifting
- cross_asset_confirmation: mixed
- cross_asset_conflicts:
  - NDX strength supports BTC, but DXY and yields are leaning against a clean risk-on continuation
  - safe-haven demand is not confirming a fully relaxed macro backdrop

- scheduled_macro_events_in_horizon:
  - event_name: US CPI
    time_utc: 2026-05-05T12:30:00Z
    importance: high
    expected_impact_mode: volatility_risk
    blocking_risk: hard_block
  - event_name: Fed speaker cluster
    time_utc: 2026-05-05T15:00:00Z
    importance: medium
    expected_impact_mode: headline_only
    blocking_risk: watch_only

- macro_veto_state: event_wait
- macro_caution_flags:
  - macro relationships are not cleanly aligned
  - major event risk is still inside the active horizon

- evidence:
  - NDX strength is supportive, but DXY and yields are not giving clean confirmation
  - scheduled CPI risk is close enough to distort normal cross-asset behavior
  - macro context does not justify high-conviction continuation before event risk clears
```
