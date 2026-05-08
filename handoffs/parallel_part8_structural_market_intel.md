# Part 8 Proposal: Structural / Market Intel

## Objective

Define the `Structural / Market Intel` section of the Chimera research bundle so Deezoh can capture the deeper market-structure context that sits beneath price action.

This section should answer:

- where capital is flowing
- whether the broader market structure supports or fights the setup
- which signals are direct structural data versus proxy-only
- whether the current setup is happening in a healthy, weak, crowded, late, early, or mixed backdrop

This is not the chart section and not the macro calendar section.

---

## Section Owner

- primary owner: `market-intel writer`
- coordinator: `Deezoh`

The owner of this section is the part of the pipeline that gathers structural market context from trusted market-intel sources and writes it into the document.

Deezoh's role here:

- make sure the section exists
- make sure required fields are filled or explicitly marked unknown
- make sure proxy-only fields are labeled as proxy
- make sure stale or missing structural context is visible before final judgment

---

## What Belongs Here

- crypto market structure context
- stablecoin supply / dry-powder context
- DeFi TVL and chain/protocol strength
- protocol fee / activity context
- network health when it changes the structural read
- market-cap structure and dominance-style context
- institutional / ETF / whale / exchange-flow narratives only when clearly marked as:
  - direct
  - proxy
  - unavailable
- cycle-position clues when they are source-supported
- structural liquidity context that helps explain whether the setup is happening in a healthy or fragile environment

This section is for the layer beneath price, not the candle-by-candle trade setup.

---

## What Does Not Belong Here

- support / resistance mapping
- FVG / OB / fib / VWAP zone work
- RSI / MACD / indicator interpretation
- pure macro-event timing like CPI/FOMC schedules
- recent news headline summaries
- trade entry / stop / TP planning
- liquidation heat map specifics
- derivatives positioning specifics like funding / OI / long-short ratios

Those belong in their own sections.

---

## Exact Recommended Fields

```md
## Structural / Market Intel

- owner:
- source:
- observed_at_utc:
- max_age_minutes:
- freshness_state:
- stale_reason:

- asset_class_scope:
- structural_data_scope:
- structural_read_quality:
- structural_bias:
- confidence:

- market_structure_regime:
- capital_rotation_state:
- liquidity_backdrop:
- market_breadth_state:
- cycle_context:

- stablecoin_supply_signal:
- stablecoin_supply_trend:
- stablecoin_signal_type:

- defi_tvl_state:
- defi_leadership:
- protocol_activity_state:
- chain_strength_notes:

- network_health_state:
- network_health_relevance:

- institutional_flow_state:
- institutional_flow_signal_type:
- whale_or_exchange_flow_state:
- whale_or_exchange_signal_type:

- structural_supports_setup:
- structural_risks:
  - item
- structural_tailwinds:
  - item
- structural_headwinds:
  - item

- direct_signals_used:
  - item
- proxy_signals_used:
  - item
- unavailable_signals:
  - item

- evidence:
  - item
```

---

## Allowed Values Where Useful

### `freshness_state`

- `fresh`
- `aging`
- `stale`
- `unknown`

### `asset_class_scope`

- `crypto`
- `equity`
- `commodity`
- `fx`
- `index`
- `mixed`

### `structural_read_quality`

- `strong`
- `usable`
- `weak`
- `proxy_heavy`
- `insufficient`

### `structural_bias`

- `bullish`
- `bearish`
- `mixed`
- `neutral`
- `unknown`

### `market_structure_regime`

- `risk_on`
- `risk_off`
- `rotation`
- `defensive`
- `euphoria`
- `distribution`
- `accumulation`
- `mixed`
- `unknown`

### `capital_rotation_state`

- `btc_led`
- `eth_led`
- `alt_rotation`
- `large_cap_led`
- `defi_led`
- `stablecoin_building`
- `defensive_rotation`
- `mixed`
- `unknown`

### `liquidity_backdrop`

- `improving`
- `ample`
- `neutral`
- `tightening`
- `fragile`
- `unknown`

### `market_breadth_state`

- `broad_participation`
- `narrow_leadership`
- `fragmented`
- `weakening`
- `unknown`

### `cycle_context`

- `early_cycle`
- `mid_cycle`
- `late_cycle`
- `post_euphoria`
- `reset_or_reaccumulation`
- `unclear`
- `unknown`

### `stablecoin_signal_type`

- `direct_structural`
- `proxy_structural`
- `unavailable`

### `defi_tvl_state`

- `expanding`
- `stable`
- `contracting`
- `mixed`
- `unknown`

### `protocol_activity_state`

- `strong`
- `healthy`
- `soft`
- `weak`
- `mixed`
- `unknown`

### `network_health_state`

- `healthy`
- `active`
- `congested`
- `stressed`
- `quiet`
- `mixed`
- `unknown`

### `network_health_relevance`

- `high`
- `medium`
- `low`
- `none`

### `institutional_flow_signal_type`

- `direct`
- `proxy`
- `narrative_only`
- `unavailable`

### `whale_or_exchange_signal_type`

- `direct`
- `proxy`
- `narrative_only`
- `unavailable`

### `structural_supports_setup`

- `supports_long`
- `supports_short`
- `supports_neither`
- `mixed`
- `unknown`

---

## Definitions

### `Structural / Market Intel`

The non-chart market layer that explains whether capital, participation, network use, and structural liquidity are helping or hurting the setup.

### `structural_read_quality`

How trustworthy this whole section is.

- `strong`: mostly direct structural data and clear conclusions
- `usable`: enough real data to matter, even if some fields are missing
- `weak`: too thin to lean on strongly
- `proxy_heavy`: many conclusions rely on indirect clues rather than direct structural data
- `insufficient`: not enough truth to use this section meaningfully

### `market_structure_regime`

The broad condition of the market underneath price.

Examples:

- `risk_on`: capital is participating and not hiding
- `risk_off`: capital is defensive and selective
- `rotation`: money is moving between market segments rather than lifting everything
- `distribution`: leadership is tiring and participation is weakening
- `accumulation`: quiet strengthening under the surface

### `capital_rotation_state`

Which part of the market is attracting capital right now.

### `liquidity_backdrop`

Whether the environment looks supportive for continuation or fragile enough that setups can fail easily.

### `stablecoin_supply_signal`

Whether stablecoin supply trends imply new dry powder, flat demand, or shrinking risk appetite.

### `institutional_flow_state`

What we honestly know about institutional participation.

Important:

- if this is inferred from news or indirect data, it must not be written like direct ETF ledger truth

### `whale_or_exchange_flow_state`

What we honestly know about large-holder or exchange-flow behavior.

Important:

- if it is only inferred from positioning proxies or narratives, it must be labeled that way

---

## How Deezoh Knows It Is Filled Enough

This section is `filled enough` when all of the following are true:

1. freshness fields are present
   - `observed_at_utc`
   - `max_age_minutes`
   - `freshness_state`

2. section ownership and source are present
   - `owner`
   - `source`

3. the section has a usable structural verdict
   - `structural_read_quality`
   - `structural_bias`
   - `structural_supports_setup`

4. at least one real structural lane is filled
   - stablecoins
   - DeFi / TVL / protocol activity
   - market structure / breadth / regime

5. proxy-only fields are labeled honestly
   - institutional flow
   - whale / exchange flow
   - cycle clues

6. missing truth is visible
   - `unavailable_signals` is filled when needed

If the section only has vague prose and no signal labeling, Deezoh should treat it as incomplete.

If the section is mostly proxy-only, Deezoh can still use it, but the section should be marked:

- `structural_read_quality: proxy_heavy`

---

## Source Order

Use this source order for the section.

1. Bitget `market-intel`
   - best current structural source for DeFi TVL, chain rankings, protocol fees, stablecoin supply, network status, and broad market-structure context

2. Bitget `macro-analyst`
   - use when cross-asset or macro-linked structural context matters, especially for gold, oil, indexes, or crypto regime framing

3. Bitget `news-briefing`
   - use only to support institutional/ETF/whale narratives when direct structural data is not available
   - never promote this above direct structural sources

4. local report readers if already populated
   - `news-reader`
   - `macro-calendar`
   - `earnings-calendar`
   - use these as support lanes, not primary Part 8 owners

5. TradingView / chart lanes
   - low priority here
   - only use if needed for context confirmation, not as the main source for Part 8

---

## Known Proof / Capability Notes

- Bitget `market-intel` is the strongest current source for this section.
- Prior capability audit already proved its strongest lanes are:
  - DeFi TVL
  - chain rankings
  - protocol fees
  - stablecoin supply
  - network status
  - global crypto market structure

- Bitget `market-intel` is weaker on:
  - direct ETF flows
  - true whale wallet tracking
  - direct exchange reserve data
  - exact cycle indicators such as AHR999, Pi Cycle, or Coinbase Premium

- The workspace capability matrix already records that several of the attractive "institutional" and "on-chain" answers are proxy-based rather than direct raw feeds.

- `market-intel` should therefore be trusted most for:
  - structural crypto backdrop
  - DeFi health
  - stablecoin context
  - network usage and protocol activity

- It should not be allowed to overstate:
  - exact ETF ledger truth
  - exact whale-flow truth
  - exact exchange-flow truth

- For commodities like gold and oil, this section can still exist, but the likely owner shifts more toward:
  - Bitget `macro-analyst`
  - macro/calendar/news support lanes
  - and the section should usually be thinner than the crypto version

- This section is mostly a `chartless` section.
  - Agents can answer most of it without seeing a chart.
  - A chart is not required for Part 8 to be useful.
  - The bigger risk here is false confidence from proxy-only data, not missing visuals.

---

## Ideal Example Response

```md
## Structural / Market Intel

- owner: market-intel writer
- source: Bitget market-intel + Bitget macro-analyst
- observed_at_utc: 2026-05-05T16:40:00Z
- max_age_minutes: 30
- freshness_state: fresh
- stale_reason: none

- asset_class_scope: crypto
- structural_data_scope: stablecoins, DeFi TVL, protocol activity, network status, broad market structure
- structural_read_quality: usable
- structural_bias: bullish
- confidence: 71

- market_structure_regime: risk_on
- capital_rotation_state: btc_led
- liquidity_backdrop: improving
- market_breadth_state: narrow_leadership
- cycle_context: mid_cycle

- stablecoin_supply_signal: stablecoin base is still expanding, which suggests dry powder remains available
- stablecoin_supply_trend: rising
- stablecoin_signal_type: direct_structural

- defi_tvl_state: expanding
- defi_leadership: Ethereum and major DeFi chains remain structurally healthy
- protocol_activity_state: healthy
- chain_strength_notes:
  - DeFi participation is not collapsing
  - fee and activity trends still support a constructive backdrop

- network_health_state: active
- network_health_relevance: medium

- institutional_flow_state: ETF and institutional participation looks supportive in narrative terms, but this source does not provide exact daily ETF ledger figures
- institutional_flow_signal_type: proxy
- whale_or_exchange_flow_state: no direct whale or reserve-flow proof from this section; only indirect structural hints
- whale_or_exchange_signal_type: unavailable

- structural_supports_setup: supports_long
- structural_risks:
  - leadership is still somewhat narrow
  - institutional flow read is proxy-heavy, not direct
- structural_tailwinds:
  - stablecoin supply is constructive
  - DeFi TVL and protocol activity are still healthy
  - overall crypto market structure still looks supportive
- structural_headwinds:
  - breadth is not fully broad yet
  - whale/exchange-flow truth is missing

- direct_signals_used:
  - stablecoin supply
  - DeFi TVL
  - protocol activity / fees
  - network status
- proxy_signals_used:
  - institutional participation narrative
  - cycle framing
- unavailable_signals:
  - direct ETF daily flow ledger
  - direct whale wallet tracking
  - direct exchange reserve data

- evidence:
  - stablecoin supply and DeFi activity both lean supportive rather than defensive
  - structural participation is healthy enough to support upside continuation
  - the main weakness is that some high-interest institutional/whale conclusions are still indirect
```
