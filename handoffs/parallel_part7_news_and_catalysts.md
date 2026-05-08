# Part 7 Proposal: News And Catalysts

## Objective

- explain what news or scheduled events could move the symbol now
- separate active narrative from scheduled event risk
- tell Deezoh whether this is a normal environment, an event setup, or a stand-aside window
- make catalyst risk visible early enough that a good chart does not get mistaken for a safe trade

## Section Owner

- primary owner: `catalyst writer`
- coordinator: `Deezoh`

Deezoh does not invent this section. Deezoh checks whether the required fields are present, fresh enough, and coherent with the rest of the bundle.

## What Belongs Here

- recent market-moving headlines for the symbol, sector, or asset class
- macro or geopolitical news that could move the setup
- scheduled event risk:
  - FOMC
  - CPI
  - NFP
  - GDP
  - rate decisions
  - major earnings
  - ETF/regulatory deadlines when available
- whether the story is active now, background only, or upcoming
- whether the news supports, fights, or overrides the setup
- event-window guidance:
  - normal
  - caution
  - event
  - lockdown

## What Does Not Belong Here

- full macro regime interpretation
  - that belongs in `Macro And Cross-Asset`
- chart structure, support/resistance, OB/FVG, hot zones
  - that belongs in `Technical Structure`
- indicator state, RSI/MACD/divergence
  - that belongs in `Indicators And Momentum Signals`
- derivatives crowding and liquidation map detail
  - those belong in their own sections
- position sizing and stop placement
  - that belongs in `Position Management And Risk`

## Recommended Fill

```md
## News And Catalysts

- owner:
- source:
  - primary:
  - secondary:
  - tertiary:
- observed_at_utc:
- max_age_minutes:
- freshness_state:
- stale_reason:

- symbol_relevance:
- asset_scope:
- current_news_state:
- dominant_narrative:
- dominant_narrative_strength:
- current_headline_set:
  - headline:
    source:
    published_at_utc:
    hours_ago:
    relevance:
    directional_impact:
    confidence:
    note:

- scheduled_event_window:
  - next_24h:
  - next_48h:
  - next_7d:
- key_upcoming_events:
  - event_name:
    category:
    scheduled_at_utc:
    hours_away:
    importance:
    expected_volatility_impact:
    directional_bias_if_any:
    affected_assets:
    status:

- earnings_or_sector_event_risk:
- geopolitical_or_regulatory_risk:
- catalyst_alignment_with_setup:
- catalyst_override_risk:
- recommended_catalyst_mode:
- no_trade_until_condition:
- missing_or_uncertain_items:
  - item
- confidence:
- evidence:
  - item 1
  - item 2
  - item 3
```

## Allowed Values

- `freshness_state`
  - `fresh`
  - `aging`
  - `stale`
  - `missing`

- `symbol_relevance`
  - `direct`
  - `sector`
  - `market_wide`
  - `background_only`

- `asset_scope`
  - `single_symbol`
  - `sector_theme`
  - `cross_market`

- `current_news_state`
  - `quiet`
  - `active`
  - `crowded`
  - `unclear`

- `dominant_narrative_strength`
  - `low`
  - `medium`
  - `high`

- `relevance`
  - `critical`
  - `high`
  - `medium`
  - `low`

- `directional_impact`
  - `bullish`
  - `bearish`
  - `mixed`
  - `event_only`
  - `unclear`

- `category`
  - `macro`
  - `earnings`
  - `regulation`
  - `etf`
  - `geopolitical`
  - `protocol`
  - `exchange`
  - `sector`
  - `other`

- `importance`
  - `critical`
  - `high`
  - `medium`
  - `low`

- `status`
  - `upcoming`
  - `active`
  - `passed_recently`
  - `delayed`
  - `uncertain`

- `catalyst_alignment_with_setup`
  - `supports_long`
  - `supports_short`
  - `supports_volatility_only`
  - `fights_setup`
  - `neutral`
  - `unclear`

- `catalyst_override_risk`
  - `none`
  - `low`
  - `medium`
  - `high`
  - `critical`

- `recommended_catalyst_mode`
  - `normal`
  - `caution`
  - `event`
  - `lockdown`

## Definitions

- `current_news_state`
  - `quiet`: no meaningful fresh driver is dominating the tape
  - `active`: one or more fresh stories are clearly affecting sentiment or positioning
  - `crowded`: too many overlapping stories or reactions are competing, which lowers clarity
  - `unclear`: sources disagree, are too stale, or coverage is too thin

- `dominant_narrative`
  - the single clearest story Deezoh should keep in mind first
  - examples:
    - `Fed risk repricing`
    - `ETF optimism cooling`
    - `geopolitical escalation`
    - `NVDA earnings sympathy risk`

- `scheduled_event_window`
  - this is the timing view, not the opinion
  - it should tell Deezoh whether a major event is inside the next:
    - `24h`
    - `48h`
    - `7d`

- `catalyst_alignment_with_setup`
  - whether the catalyst environment helps the current long/short idea
  - this is not the same as macro bias
  - it is setup-specific

- `catalyst_override_risk`
  - whether catalyst conditions are strong enough to downgrade or override a technically good setup
  - high or critical means Deezoh should slow down, wait, or branch into event logic

- `recommended_catalyst_mode`
  - `normal`: no major catalyst obstruction
  - `caution`: news risk exists, but trading may still be possible with care
  - `event`: setup must be treated as event-driven; fast conditions may matter more than normal structure logic
  - `lockdown`: do not open new trades until the event or uncertainty clears

- `no_trade_until_condition`
  - the plain-English unblock condition
  - examples:
    - `wait until CPI release is out and first reaction settles`
    - `wait until the ETF rumor is confirmed or denied`
    - `wait until post-earnings gap direction is clear`

## How Deezoh Knows It Is Filled Enough

This section is `complete enough` when all of the following are true:

- freshness fields are present
- at least one recent-news source has been checked or explicitly marked unavailable
- scheduled-event window is filled from a calendar source or explicitly marked unavailable
- there is one plain dominant narrative or an explicit statement that there is no dominant narrative
- catalyst mode is set:
  - `normal`
  - `caution`
  - `event`
  - or `lockdown`
- missing items are listed honestly instead of being silently skipped

This section is `not filled enough` when any of these happen:

- news is present but there is no timestamp
- scheduled event risk is omitted
- old news is treated like fresh news
- the section says `bullish` or `bearish` without naming the actual catalyst
- there is no event-window view for known macro/earnings-sensitive assets

## Source Order

1. `macro-calendar`
   - best first source for scheduled macro events
   - use for `next_24h`, `next_48h`, `next_7d`, and macro-risk timing

2. `earnings-calendar`
   - best first source for big-tech earnings risk that can bleed into crypto or risk assets
   - especially important for BTC, ETH, NASDAQ-correlated names, AI trades, and risk-on setups

3. `news-reader`
   - best local report-reader for fresh crypto, macro, and geopolitical headlines
   - good for `market_impact`, `critical_alerts`, `trending_coins`, and article timestamps

4. Bitget `news-briefing`
   - use for recent narrative, keyword-filtered recent stories, KOL/social pulse, and China-social context
   - good analyst layer for `what is moving markets now`

5. `tvremix` news / economic-calendar path
   - use only when it is callable and budget-appropriate
   - good as a supporting check, not the primary owner

6. `historical-market-context`
   - only for replay/backtest branches when point-in-time catalyst context is needed
   - do not use it to fake live freshness

## Known Proof / Capability Notes

- `news-reader`
  - reads `NEWS.json`
  - useful for:
    - recent crypto headlines
    - macro headlines
    - geopolitical headlines
    - timestamps
    - critical alerts
    - market impact labels
  - caution:
    - report-driven, not a direct archive
    - stale file means stale conclusions

- `macro-calendar`
  - reads `MACRO.json`
  - useful for:
    - FOMC
    - CPI
    - NFP
    - GDP
    - rate decisions
    - event windows and days/hours until event
  - caution:
    - report-driven
    - must respect freshness and exact `hours_away` style timing if available

- `earnings-calendar`
  - also reads `MACRO.json`
  - useful for:
    - NVDA/AAPL/MSFT/AMZN/GOOGL/META/TSLA style earnings risk
    - crypto-correlation framing
  - caution:
    - exact pre-market/post-market timing may still need verification elsewhere

- Bitget `news-briefing`
  - proven useful for:
    - recent narrative
    - keyword-filtered recent stories
    - macro/geopolitical headlines
    - KOL/social pulse
    - China-social trend surface
  - caution:
    - freshness-first, not a true historical archive
    - weak fit for arbitrary date-range event-study work

- `tvremix`
  - docs say it can help with news and economic-calendar style checks
  - treat as augment-only here unless the exact lane is freshly proven in the current host/runtime

- Catalyst operating rule from earlier Chimera design:
  - catalyst can recommend `event` or `lockdown`
  - catalyst does not impose it by itself
  - Deezoh still decides whether to trade, wait, or stand aside

## Ideal Example Response

```md
## News And Catalysts

- owner: catalyst writer
- source:
  - primary: macro-calendar + news-reader
  - secondary: Bitget news-briefing
  - tertiary: earnings-calendar
- observed_at_utc: 2026-05-05T09:20:00Z
- max_age_minutes: 30
- freshness_state: fresh
- stale_reason: none

- symbol_relevance: direct
- asset_scope: cross_market
- current_news_state: active
- dominant_narrative: Fed risk repricing plus NVDA earnings sympathy risk
- dominant_narrative_strength: high
- current_headline_set:
  - headline: Fed speakers pushed back on fast-cut expectations
    source: news-reader
    published_at_utc: 2026-05-05T07:50:00Z
    hours_ago: 1.5
    relevance: high
    directional_impact: bearish
    confidence: medium
    note: stronger dollar / yields risk can pressure BTC and risk assets
  - headline: NVDA earnings due inside the next 48 hours
    source: earnings-calendar
    published_at_utc: 2026-05-05T09:00:00Z
    hours_ago: 0.3
    relevance: high
    directional_impact: event_only
    confidence: high
    note: important for BTC and AI-beta names even without direct coin-specific news
  - headline: ETF optimism faded after no new approval signal
    source: Bitget news-briefing
    published_at_utc: 2026-05-05T08:10:00Z
    hours_ago: 1.2
    relevance: medium
    directional_impact: mixed
    confidence: medium
    note: weakens easy upside narrative but does not create a clean short by itself

- scheduled_event_window:
  - next_24h: no top-tier macro release
  - next_48h: NVDA earnings inside window
  - next_7d: CPI in 3.5 days
- key_upcoming_events:
  - event_name: NVDA earnings
    category: earnings
    scheduled_at_utc: 2026-05-06T20:15:00Z
    hours_away: 35
    importance: high
    expected_volatility_impact: risk-on / risk-off sympathy move for BTC and tech beta
    directional_bias_if_any: unclear
    affected_assets:
      - BTC
      - ETH
      - SOL
      - NASDAQ
    status: upcoming
  - event_name: CPI release
    category: macro
    scheduled_at_utc: 2026-05-08T12:30:00Z
    hours_away: 87
    importance: critical
    expected_volatility_impact: major repricing risk for yields, DXY, and crypto
    directional_bias_if_any: unclear
    affected_assets:
      - BTC
      - ETH
      - gold
      - oil
      - stocks
    status: upcoming

- earnings_or_sector_event_risk: elevated
- geopolitical_or_regulatory_risk: low
- catalyst_alignment_with_setup: fights_setup
- catalyst_override_risk: high
- recommended_catalyst_mode: caution
- no_trade_until_condition: wait for either a cleaner post-NVDA reaction or a lower-risk intraday setup away from earnings sympathy noise
- missing_or_uncertain_items:
  - exact ETF deadline relevance not confirmed in current sources
- confidence: 72
- evidence:
  - fresh news source shows hawkish-rate narrative pressure today
  - earnings calendar puts NVDA inside the next 48h risk window
  - no direct bullish catalyst is strong enough yet to override the event risk
```
