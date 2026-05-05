# Part 4 Proposal: Derivatives And Positioning

## Objective

This section should answer one question:

Is the setup supported by healthy participation, or is it being distorted by crowded leverage, one-sided positioning, liquidation pressure, or squeeze risk?

This part is where Deezoh decides whether the move is:

- confirmed by derivatives participation
- stretched by crowded leverage
- vulnerable to a squeeze
- too noisy or incomplete to trust

It should change trade quality, not replace the chart or replace the final decision.

## Section Owner

- primary owner: `market-maker`
- coordinator and completeness gate: `Deezoh`
- main helper sources:
  - `derivatives_sentiment`
  - `derivatives_fetcher_bitget.py`
  - `coinglass_homepage_scraper.py`
  - CoinGlass scraping lane for liquidation / max-pain support
  - `coinalyze-derivatives` only when a field is still missing after the first two
  - Bitget `sentiment-analyst` only as an extra positioning layer if callable on the active host

Why this owner:

`market-maker` already owns positioning, crowding, trap risk, OI, funding, squeeze risk, and liquidation context. The best tested source mix for this section is:

- `derivatives_sentiment` for long/short, top-trader, taker-ratio, and OI history context
- `derivatives_fetcher_bitget.py` for current Bitget funding/OI/current-price venue truth
- `coinglass_homepage_scraper.py` for `price_change_24h_pct`, `oi_change_1h_pct`, `oi_change_24h_pct`, and liquidation table context
- CoinGlass scraping for liquidation / max-pain support

`bitget-analyst` is too generic to own the whole section by itself.

## What Belongs Here

- open interest level and trend
- price versus OI interpretation
- current funding and funding trend
- predicted funding when available
- long/short crowding
- top-trader or account-position ratios when available
- taker flow bias when available
- liquidation pressure and likely squeeze direction
- venue disagreement or confirmation
- whether derivatives support, weaken, or block the setup

## What Does Not Belong Here

- chart structure, support, resistance, OB, FVG, or patterns
- RSI, MACD, or indicator interpretation as the main story
- macro regime, DXY, yields, oil, gold, or equities context
- news narrative or catalysts
- exact trade execution plan, stop placement, scaling, or take-profit logic

Those belong in other sections.

## Exact Recommended Fields

```md
## Derivatives And Positioning

- owner:
- sources_used:
  - item
- observed_at_utc:
- max_age_minutes:
- freshness_state:
- stale_reason:

- derivatives_market_scope:
- venue_focus:
- primary_contracts:
  - item

- current_price:
- price_change_1h_pct:
- price_change_4h_pct:
- price_change_24h_pct:

- open_interest_state:
- open_interest_change_1h_pct:
- open_interest_change_4h_pct:
- open_interest_change_24h_pct:
- price_vs_oi_read:

- funding_state:
- funding_rate_current_pct:
- funding_trend:
- predicted_funding_pct:
- price_vs_funding_read:

- long_short_account_ratio:
- long_short_position_ratio:
- top_trader_positioning:
- taker_flow_bias:
- taker_buy_sell_ratio:
- taker_buy_volume:
- taker_sell_volume:
- crowding_side:
- taker_vs_price_read:

- liquidation_pressure_state:
- dominant_liquidation_side:
- liquidation_risk_window:
- squeeze_risk:
- max_pain_context:

- cross_venue_agreement:
- derivatives_conflicts:
  - item

- derivatives_support_verdict:
- fakeout_risk:
- positioning_bias:
- confidence:
- evidence:
  - item
  - item
  - item
```

## Field Coverage Rule

Treat these as `required` with the currently tested stack:

- `owner`
- `sources_used`
- `observed_at_utc`
- `max_age_minutes`
- `freshness_state`
- `venue_focus`
- `open_interest_state`
- `current_price`
- `price_change_1h_pct`
- `price_change_4h_pct`
- `price_change_24h_pct`
- `price_vs_oi_read`
- `funding_state`
- `funding_rate_current_pct`
- `price_vs_funding_read`
- `long_short_account_ratio`
- `top_trader_positioning`
- `taker_flow_bias`
- `taker_buy_sell_ratio`
- `taker_buy_volume`
- `taker_sell_volume`
- `crowding_side`
- `taker_vs_price_read`
- `derivatives_support_verdict`
- `fakeout_risk`
- `positioning_bias`
- `evidence`

Treat these as `good if available, but not required`:

- `open_interest_change_1h_pct`
- `open_interest_change_4h_pct`
- `open_interest_change_24h_pct`
- `funding_trend`
- `long_short_position_ratio`
- `liquidation_pressure_state`
- `dominant_liquidation_side`
- `liquidation_risk_window`
- `squeeze_risk`
- `max_pain_context`
- `cross_venue_agreement`

Treat this as `optional gap-fill only`:

- `predicted_funding_pct`
  - use Coinalyze only if the primary stack did not provide it and the symbol works there

## Allowed Values

### `freshness_state`

- `fresh`
- `stale`
- `partial`
- `missing`

### `derivatives_market_scope`

- `single_venue`
- `cross_venue`
- `mixed`

### `venue_focus`

- `bitget`
- `binance`
- `bybit`
- `okx`
- `multi_venue`

### `open_interest_state`

- `rising_fast`
- `rising`
- `flat`
- `falling`
- `falling_fast`
- `unknown`

### `price_vs_oi_read`

- `price_up_oi_up`
- `price_up_oi_down`
- `price_down_oi_up`
- `price_down_oi_down`
- `mixed`
- `unknown`

### `funding_state`

- `positive_light`
- `positive_hot`
- `negative_light`
- `negative_hot`
- `neutral`
- `unknown`

### `funding_trend`

- `rising`
- `falling`
- `flat`
- `mixed`
- `unknown`

### `top_trader_positioning`

- `long_heavy`
- `short_heavy`
- `balanced`
- `unavailable`

### `taker_flow_bias`

- `buyers_aggressive`
- `sellers_aggressive`
- `balanced`
- `unavailable`

### `crowding_side`

- `long_crowded`
- `short_crowded`
- `balanced`
- `unclear`

### `liquidation_pressure_state`

- `longs_vulnerable_below`
- `shorts_vulnerable_above`
- `two_sided`
- `muted`
- `unknown`

### `dominant_liquidation_side`

- `longs`
- `shorts`
- `balanced`
- `unknown`

### `squeeze_risk`

- `short_squeeze_risk`
- `long_squeeze_risk`
- `two_way_squeeze_risk`
- `low`
- `unknown`

### `cross_venue_agreement`

- `agree_bullish`
- `agree_bearish`
- `mixed`
- `single_venue_only`
- `unknown`

### `positioning_bias`

- `supports_long`
- `supports_short`
- `contrarian_long`
- `contrarian_short`
- `mixed`
- `blocks_conviction`
- `unknown`

## Definitions

### Open interest

Total notional value or contract size still open in futures/perps. It matters most when compared with price direction and recent change, not as an isolated number.

### Price versus OI read

This is the core interpretation layer:

- `price_up_oi_up`: new long participation or fresh trend commitment
- `price_up_oi_down`: squeeze or covering, less healthy than it looks
- `price_down_oi_up`: fresh short build or growing downside pressure
- `price_down_oi_down`: deleveraging or long flush

### Funding state

Funding is not an entry signal by itself. It shows whether one side is paying to hold leverage. Extreme positive funding usually means longs are crowded. Extreme negative funding usually means shorts are crowded.

### Crowding side

This is not just the raw long/short ratio. It is the combined crowding read from funding, OI behavior, long/short ratios, top-trader data, and taker flow if available.

### Liquidation pressure state

This should answer where forced unwinds are more likely to happen next:

- below price for overleveraged longs
- above price for overleveraged shorts
- both directions if the book is unstable

### Positioning bias

This is the summary output of the section:

- does derivatives context support the trade
- argue against it
- imply a contrarian trade
- or block confidence entirely

## How Deezoh Knows It Is Filled Enough

This section is `filled enough` when all of these are true:

1. `owner`, `sources_used`, `observed_at_utc`, `max_age_minutes`, and `freshness_state` are present.
2. There is at least one live OI read and one live funding read.
3. `price_change_1h_pct`, `price_change_4h_pct`, or `price_change_24h_pct` is present.
4. `price_vs_oi_read` and `price_vs_funding_read` are explicitly stated.
5. `crowding_side` and `taker_vs_price_read` are explicitly stated.
6. There is an explicit `derivatives_support_verdict`, `fakeout_risk`, and `positioning_bias`.
7. There are at least three concrete evidence bullets.
8. Missing data is named plainly instead of hidden.

If any of these are missing, Deezoh should treat the section as incomplete.

This section is still usable with partial data, but only if it says so clearly. Example:

- single venue only
- no top-trader data
- no predicted funding
- no liquidation map today
- no max-pain scrape on this run

That should reduce confidence, not silently pass as complete.

## Source Order

1. `market-maker`
   - section owner and interpretation layer
   - best current owner for OI, funding, crowding, trap risk, and liquidation logic

2. `derivatives_sentiment`
   - best current working rich derivatives lane for:
     - long/short ratio
     - top-trader account ratio
     - top-trader position ratio
     - OI history
     - taker buy/sell ratio
   - this should be the main non-venue-specific positioning source

3. `derivatives_fetcher_bitget.py`
   - best current working Bitget-native venue lane for:
     - current funding
     - current OI
     - current price
     - current 24h price change
     - Bitget long/short account ratio snapshot
   - use this when venue truth matters because Bitget is Sal's exchange

4. CoinGlass scraping lane
   - `openclawtrading/scripts/coinglass_maxpain_scraper.py`
   - `openclawtrading/scripts/liquidation_heatmap.py`
   - `scripts/market-maker/run_maxpain_scan.py`
   - `scripts/market-maker/run_liquidation_scans.py`
   - use for:
     - max-pain levels
     - liquidation heatmap screenshots
     - liquidation-zone support
   - this should support squeeze / liquidation context, not replace the main numeric derivatives lane

5. `coinalyze-derivatives`
   - optional gap-fill only
   - use when a still-missing field really needs:
     - predicted funding
     - richer liquidation history
     - backup OI/funding on supported symbols
   - do not make it the default primary lane because of rate-limit and symbol-fragility concerns

6. `derivatives`
   - operator-facing wrapper around Coinalyze-style data
   - convenience only, not separate truth

7. Bitget `sentiment-analyst`
   - helpful if callable on the active host
   - likely useful for:
     - long/short
     - top trader
     - taker ratio
     - OI snapshot
   - but the directly tested working lane here is `derivatives_sentiment`

## Field-To-Source Matrix

Use this as the concrete ownership map for the section.

### Best current source

- `current_price`
  - `derivatives_fetcher_bitget.py`
- `price_change_24h_pct`
  - `derivatives_fetcher_bitget.py`
- `open_interest_state`
  - `derivatives_fetcher_bitget.py` + `derivatives_sentiment open_interest`
- `open_interest_change_1h_pct`
  - derive from `derivatives_sentiment open_interest`
- `open_interest_change_4h_pct`
  - derive from `derivatives_sentiment open_interest`
- `open_interest_change_24h_pct`
  - derive from `derivatives_sentiment open_interest`
- `price_vs_oi_read`
  - derived by `market-maker` from price change + OI change
- `funding_rate_current_pct`
  - `derivatives_fetcher_bitget.py`
- `funding_state`
  - `market-maker` from current funding value
- `funding_trend`
  - optional; Bitget fetcher only if repeated snapshots exist, otherwise Coinalyze gap-fill
- `predicted_funding_pct`
  - Coinalyze gap-fill only
- `price_vs_funding_read`
  - derived by `market-maker`
- `long_short_account_ratio`
  - `derivatives_sentiment long_short`
- `top_trader_positioning`
  - `derivatives_sentiment top_ls` + `top_position`
- `taker_flow_bias`
  - `derivatives_sentiment taker_ratio`
- `taker_buy_sell_ratio`
  - `derivatives_sentiment taker_ratio`
- `taker_buy_volume`
  - `derivatives_sentiment taker_ratio`
- `taker_sell_volume`
  - `derivatives_sentiment taker_ratio`
- `crowding_side`
  - derived by `market-maker` from funding + L/S + top trader + taker
- `taker_vs_price_read`
  - derived by `market-maker`
- `liquidation_pressure_state`
  - CoinGlass scraping support + `market-maker`
- `dominant_liquidation_side`
  - CoinGlass scraping support + `market-maker`
- `liquidation_risk_window`
  - CoinGlass scraping support + `market-maker`
- `squeeze_risk`
  - `market-maker` from L/S + top trader + taker + liquidation context
- `max_pain_context`
  - CoinGlass scraping support
- `cross_venue_agreement`
  - optional only if multiple venues are actually queried
- `derivatives_support_verdict`
  - `market-maker`
- `fakeout_risk`
  - `market-maker`
- `positioning_bias`
  - `market-maker`

### Derived interpretation rules

- `price_up_oi_up`
  - move is more likely supported by fresh participation
- `price_up_oi_down`
  - squeeze / covering risk, less healthy than it looks
- `price_down_oi_up`
  - fresh shorts building, downside pressure or squeeze setup
- `price_down_oi_down`
  - deleveraging / long flush

- `price_up + positive_rising_funding + crowded_longs`
  - continuation possible, but fakeout / long-flush risk increases
- `price_up + negative_or_flat_funding + oi_up`
  - cleaner bullish participation
- `price_up + taker_buy_sell_ratio > 1 + oi_up`
  - stronger bullish conviction
- `price_up + taker_buy_sell_ratio < 1`
  - rally is less trustworthy
- `price_down + taker_buy_sell_ratio > 1`
  - sellers are not fully in control; possible trap / reversal attempt
- `price_down + taker_buy_sell_ratio < 1 + oi_up`
  - stronger bearish follow-through

## Known Proof / Capability Notes

- `derivatives_sentiment` was tested live and returned:
  - retail long/short ratio
  - top-trader account ratio
  - top-trader position ratio
  - taker buy/sell ratio
  - OI history
- `derivatives_fetcher_bitget.py` was tested live and returned:
  - current Bitget funding
  - current Bitget OI
  - current Bitget price
  - Bitget long/short snapshot for some symbols
- `openclawtrading/scripts/coinglass_maxpain_scraper.py` was tested locally with Playwright and successfully wrote:
  - `openclawtrading/data/LIQUIDATION_MAXPAIN.json`
  - `openclawtrading/data/MAXPAIN_SIGNAL.json`
- `openclawtrading/scripts/liquidation_heatmap.py` was tested locally with Playwright and successfully wrote:
  - `openclawtrading/reports/heatmaps/HEATMAP_LOG.json`
  - CoinGlass and CoinAnk screenshots for BTC
- `scripts/market-maker/run_maxpain_scan.py` was tested locally after path resolution and successfully wrote:
  - `reports/auto/MAXPAIN_SUMMARY.json`
- `scripts/market-maker/run_liquidation_scans.py` was tested locally after path resolution and successfully wrote:
  - `reports/auto/LIQUIDATION_SUMMARY.json`
- all three Coinalyze keys were tested and work on `BTCUSDT_PERP.A` for:
  - current OI
  - current funding
  - predicted funding
- Coinalyze returned empty for `BTCUSDT_PERP.E` in quick checks, so it should not be treated as a clean Bitget-native venue source
- `market-maker` remains the correct section owner because it is the interpretation layer, not just a fetcher

## Ideal Example Response

```md
## Derivatives And Positioning

- owner: market-maker
- sources_used:
  - coinalyze-derivatives
  - chimera-bitget-derivatives-data
  - Bitget sentiment-analyst
- observed_at_utc: 2026-05-05T11:42:00Z
- max_age_minutes: 20
- freshness_state: fresh
- stale_reason: none

- derivatives_market_scope: mixed
- venue_focus: multi_venue
- primary_contracts:
  - BTCUSDT perpetual
  - BTCUSDT_PERP.A
  - BTCUSDT_PERP.E

- open_interest_state: rising
- open_interest_change_1h_pct: 1.8
- open_interest_change_4h_pct: 4.9
- open_interest_change_24h_pct: 7.6
- price_vs_oi_read: price_up_oi_up

- funding_state: positive_light
- funding_rate_current_pct: 0.012
- funding_trend: rising
- predicted_funding_pct: 0.016

- long_short_account_ratio: 1.41
- long_short_position_ratio: 1.18
- top_trader_positioning: long_heavy
- taker_flow_bias: buyers_aggressive
- crowding_side: long_crowded

- liquidation_pressure_state: longs_vulnerable_below
- dominant_liquidation_side: longs
- liquidation_risk_window: local flush risk if price loses the nearby intraday reclaim zone
- squeeze_risk: long_squeeze_risk
- max_pain_context: no strong max-pain pin available on this pass

- cross_venue_agreement: agree_bullish
- derivatives_conflicts:
  - crowding is building faster than funding extremes suggest

- positioning_bias: mixed
- confidence: 71
- evidence:
  - OI is rising with price, which confirms participation rather than pure short covering.
  - Funding is positive but not yet extreme, so the long side is getting crowded without being fully blown out.
  - Long-short ratios and taker flow both lean long, which supports continuation but raises long-flush risk on any failed breakout.
```

## Practical Rule For Deezoh

Deezoh should read this section as:

- confirmation layer when it agrees with structure
- caution layer when leverage is too one-sided
- block layer when the crowding story is too dangerous or too incomplete

It should never be treated as a standalone trade trigger.
