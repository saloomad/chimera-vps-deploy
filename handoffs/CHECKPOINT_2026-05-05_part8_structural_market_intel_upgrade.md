# CHECKPOINT - Part 8 structural / market intel upgrade

Date: 2026-05-05
Operator: Codex

## Objective

Upgrade `Part 8: Structural / Market Intel` so it becomes:

- decision-useful for Deezoh
- honest about exact versus proxy data
- wired to a real owner
- backed by tested current sources

## What changed

Updated:

- `chimera-vps-deploy/skills/CHIMERA_RESEARCH_BUNDLE_TEMPLATE.md`

Created:

- `agents/market-intel/AGENTS.md`
- `agents/market-intel/TOOLS.md`
- `research/platforms/2026-05-05-structural-market-intel-source-matrix.md`
- `research/platforms/2026-05-05-btc-part8-deezoh-example.md`

## Source truth

Strongest current Section 8 sources:

1. `reports/auto/MARKET_CONTEXT.json`
   - BTC dominance
   - TOTAL3 proxy
   - fear and greed
   - total crypto market-cap context
2. `mcp__market_data__.defi_analytics`
   - exact stablecoin supply
   - DeFi fee activity
3. `mcp__market_data__.news_feed`
   - institutional and ETF narrative
4. `mcp__market_data__.tradfi_news`
   - second institutional-news lane
5. `mcp__market_data__.derivatives_sentiment`
   - smart-money positioning proxy

## Main design correction

Part 8 now explicitly separates:

- exact structural signals
- proxy structural signals

That prevents Deezoh from treating:

- exact dominance
- exact stablecoin supply
- exact participation metrics

the same way as:

- ETF-flow narratives
- smart-money derivatives proxies
- whale-behavior inference

## BTC example verdict

Current BTC structural read:

- `structural_bias: bullish_with_btc_led_caution`
- dry powder still supportive
- BTC still the quality bid leader
- risk appetite improving from fear toward neutral
- DeFi participation improving
- broad alt confirmation still limited

## Remaining work

- later test how Deezoh consumes Part 8 together with the other upgraded sections in a full bundle

## VPS proof

Mirrored and verified:

- `/root/openclawtrading/skills/CHIMERA_RESEARCH_BUNDLE_TEMPLATE.md`
- `/root/.openclaw/kimi-skills/CHIMERA_RESEARCH_BUNDLE_TEMPLATE.md`
- `/root/openclawtrading/agents/market-intel/AGENTS.md`
- `/root/.openclaw/workspace/agents/market-intel/AGENTS.md`
- `/root/openclawtrading/agents/market-intel/TOOLS.md`
- `/root/.openclaw/workspace/agents/market-intel/TOOLS.md`
- `/root/.openclaw/workspace/research/platforms/2026-05-05-structural-market-intel-source-matrix.md`
- `/root/.openclaw/workspace/research/platforms/2026-05-05-btc-part8-deezoh-example.md`

Remote grep proved the live copies contain:

- `exact_vs_proxy_boundary`
- `stablecoin_dry_powder_signal`
- `institutional_or_allocation_signal`
- `structural_watch_signals`
- BTC example `structural_bias: bullish_with_btc_led_caution`
