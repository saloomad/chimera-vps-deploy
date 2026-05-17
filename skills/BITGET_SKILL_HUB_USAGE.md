# Bitget Skill Hub Usage

This is the practical guide for how Chimera should use the Bitget Skill Hub.

## What This Should Become

This document should not stay a loose explanation file.

It should become:

- the operator guide for Bitget skill usage
- the ownership map for which agent fills which section
- the section-by-section analysis template reference
- the truth boundary for what Bitget can do versus what Chimera scripts still own
- the ownership map for freshness, stale detection, and multi-setup handling

## What It Is

The Bitget Skill Hub is a curated set of plug-and-play AI skills bundled with Bitget Agent Hub.

Each skill is a structured prompt that tells an AI agent:

- what data to fetch
- how to interpret it
- how to present it
- how to handle missing data safely

In practice, this means the skills turn raw market-data tool calls into analyst-style outputs instead of making the agent improvise the whole workflow each time.

Important:

- Bitget skills do not magically know the full analysis context
- they only know the symbol, timeframe, mode, and inputs they are actually given
- freshness must come from fetch metadata or bundle stamps, not from confident prose

## How The Skill Pattern Works

A skill normally includes:

- trigger language in `SKILL.md`
- the data calls to make
- the interpretation logic
- output templates
- error-handling rules

For Bitget, most of the skills depend on the `market-data` MCP server.

Important exception:

- `technical-analysis` does not depend on the Bitget `market-data` MCP server
- it fetches candle data directly from Bitget APIs
- it calculates indicators locally with Python

## The Five Main Skills

### `macro-analyst`

Use this for macro and cross-asset context.

What it does:

- reads the rate environment
- checks the yield curve
- looks at inflation and jobs data
- compares BTC with assets like DXY, gold, Nasdaq, S&P, VIX, and yields
- brings in China and global market context
- ends with a risk-on / mixed / risk-off style verdict

Best use:

- macro backdrop
- is the environment helping or hurting crypto
- cross-asset context before a trade

### `market-intel`

Use this for structural market context beyond the chart.

What it does:

- looks at ETF and institutional narratives
- approximates whale and exchange-flow style context
- checks market-cycle style signals and stablecoin supply
- reads DeFi structure
- reads DEX trend activity
- checks network health like ETH gas and BTC mempool/fees

Best use:

- structural context
- DeFi and market-cap regime
- what is happening beneath price

Important caveat:

- some of this is proxy-based, not true deep on-chain or direct ETF flow truth

### `news-briefing`

Use this for recent market narrative.

What it does:

- aggregates crypto, macro, tech, and geopolitical feeds
- creates a market briefing
- supports keyword filtering on recent stories
- looks at social pulse and KOL/research views
- summarizes the dominant narrative

Best use:

- what is moving markets now
- morning briefing
- recent catalyst scan

Important caveat:

- this is not a full historical news archive

### `sentiment-analyst`

Use this for crowding and positioning.

What it does:

- reads Fear & Greed
- compares retail long/short with top-trader long/short
- checks open interest
- checks taker buy/sell pressure
- looks at Reddit-style community buzz
- highlights positioning divergence

Best use:

- are longs crowded
- is smart money disagreeing with retail
- is leverage building or being unwound

Important caveat:

- useful, but still not a full replacement for Chimera’s richer custom derivatives pipelines

### `technical-analysis`

Use this for direct chart and indicator work.

What it does:

- computes 23 technical indicators across trend, volatility, oscillator, volume, momentum, and support/resistance groups
- returns time-series data, not just one current value
- supports scenario-based defaults
- can export CSV

Best use:

- indicator-heavy analysis
- multi-timeframe technical review
- divergence-style follow-up logic

Important caveat:

- divergence is not a built-in labeled feature
- the data is strong enough to compute it on top

## Missing But Required Chimera Lane: Liquidation Heat Maps

Bitget's five main skills do not give Chimera a full liquidation-heatmap lane.

Chimera should keep a separate liquidation-heatmap section in the research flow.

What this lane is for:

- visible liquidation clusters above and below price
- squeeze-risk zones
- likely magnet levels
- whether the market is moving into a dense liquidation pocket
- whether a breakout is clean or likely to be a liquidation sweep

What it should contribute to the bundle:

- nearest major long liquidation cluster
- nearest major short liquidation cluster
- distance from current price
- whether the path of least resistance points into a cluster
- whether the heatmap confirms or fights the current chart thesis

What Bitget currently does not replace here:

- external liquidation heatmap assets
- custom heatmap image generation
- visual liquidation-cluster interpretation

Recommended Chimera ownership:

- scripts or external heatmap tools generate the raw truth
- a dedicated market-maker or liquidation analyst agent summarizes it
- the result goes into the shared research bundle

## Using Skills Together

These skills work best as a pack, not as isolated one-offs.

Good combinations:

- full market assessment:
  - `macro-analyst` + `sentiment-analyst` + `technical-analysis`
- should I buy BTC now:
  - `market-intel` + `sentiment-analyst` + `technical-analysis`
- what is moving markets today:
  - `news-briefing` + `macro-analyst`
- is this altcoin worth looking at:
  - `market-intel` + `technical-analysis` + `sentiment-analyst`

For full Chimera use, also add:

- liquidation heatmap lane
- existing execution/risk lane

## Required Data Surface

Most of the Bitget skills depend on:

- `market-data`
- URL: `https://datahub.noxiaohao.com/mcp`

That server exposes tool families like:

- `crypto_market`
- `defi_analytics`
- `dex_market`
- `sentiment_index`
- `derivatives_sentiment`
- `news_feed`
- `social_trending`
- `tradfi_news`
- `network_status`
- `rates_yields`
- `macro_indicators`
- `cross_asset`
- `global_assets`
- `global_data`
- `cn_market`

## Chimera Usage Rule

Use Bitget skills as the analyst layer, not the raw truth layer.

That means:

- scripts still collect and store deterministic truth
- Bitget skills interpret and summarize
- Chimera’s shared decision logic combines Bitget output with its own cached state
- execution stays in the existing paper/runtime path

## Recommended Document Structure

## Real Ownership Model

Use concrete owners, not vague "the agent knows" language.

- `request source`
  - user request, screener hit, automation, replay runner
- `symbol classifier`
  - determines asset type and market family
- `data fetcher`
  - owns fetched timestamps and stale state
- `section writer`
  - writes one lane using the latest available data
- `final judge`
  - chooses posture or setup, but should not invent missing upstream facts

## Freshness Rule

Every lane should carry its own freshness stamp.

At minimum, each section should expose:

- source
- observed_at_utc
- max_age_minutes
- freshness_state
- stale_reason

If the section is older than its allowed age:

- mark it `stale`
- do not let later lanes silently treat it as current

## Multi-Setup Rule

One symbol can have more than one valid setup in the same bundle.

Examples:

- a 5m long scalp and a 4h short fade can both exist
- a primary breakout setup and a backup pullback setup can both exist
- a long and short thesis can both stay alive until one invalidates

So Chimera should keep:

- one bundle per symbol per pass
- multiple `setup candidates` inside that bundle when needed

The final judge picks:

- one chosen setup
- or `wait`
- or `watch`
- or `mixed / unresolved`

If multiple agents are filling one shared research document, the document should be organized by lane, not by tool.

Recommended top-level sections:

1. instrument and context
2. technical structure
3. indicators and momentum signals
4. derivatives and positioning
5. liquidation heat map
6. macro and cross-asset
7. news and catalysts
8. structural / market-intel
9. risk and invalidation
10. final decision

This is better than a loose note because each agent can own one section and write into a stable shape.

## Templates

Yes. The Bitget skills already include partial templates inside their own references.

Examples:

- macro:
  - output templates for macro reports
- news:
  - output templates for briefings and topic summaries
- sentiment:
  - output templates for snapshots, full reports, and squeeze/divergence alerts
- market-intel:
  - output templates for institutional flow, cycle, network health, and DEX intelligence

What was missing was a single Chimera-wide template that combines all lanes into one normalized packet.

Use this shared Chimera template:

- `C:\Users\becke\claudecowork\chimera-vps-deploy\skills\CHIMERA_RESEARCH_BUNDLE_TEMPLATE.md`

## How To Improve This Document Further

The next good improvements are structural, not just explanatory.

### 1. Split the guide into three layers

- capability map
- analysis template
- install and verification guide

### 2. Add ownership labels everywhere

Every section should say:

- owner agent
- required inputs
- optional inputs
- output shape

### 3. Add stock-specific notes

The current guide is still crypto-heavier than it should be.

Add:

- earnings lane
- fundamentals lane
- analyst revision lane
- stock-news lane

### 4. Add freshness rules

Each analysis section should say how stale is too stale.

### 5. Add a JSON twin

The markdown template is good for humans.
The same shape should also exist as machine-readable JSON for replay and decision engines.

## Install Reminder

The real skill-load paths in this ecosystem are:

- Windows Claude:
  - `C:\Users\becke\.claude\skills`
- Windows Codex:
  - `C:\Users\becke\.codex\skills`
- Windows OpenClaw local:
  - `C:\Users\becke\.openclaw\skills`
- shared repo mirror:
  - `C:\Users\becke\claudecowork\chimera-vps-deploy\skills`
- live VPS OpenClaw repo mirror:
  - `/root/openclawtrading/skills`
- live VPS OpenClaw runtime extra skills:
  - `/root/.openclaw/kimi-skills`

Important:

- for the live VPS, `kimi-skills` is the runtime-critical extra skill directory
- copying only into `/root/.openclaw/skills` is not enough unless the live config proves it is being loaded

## Verification

Use this shared verifier when you need to confirm the Bitget pack is really staged in the right places:

- `C:\Users\becke\claudecowork\chimera-vps-deploy\scripts\verify_bitget_skill_install_surfaces.ps1`

It checks:

- Windows Claude skill directory
- Windows Codex skill directory
- Windows OpenClaw local skill directory
- shared repo mirror
- VPS repo mirror
- VPS `kimi-skills`
- local `market-data` MCP registration
- VPS `market-data` MCP registration
