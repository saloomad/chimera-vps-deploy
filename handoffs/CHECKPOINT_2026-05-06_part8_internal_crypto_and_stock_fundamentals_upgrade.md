# CHECKPOINT - 2026-05-06 - Part 8 Internal Crypto And Stock Fundamentals Upgrade

## Objective

Tighten `Part 8: Structural / Market Intel` so it stops overlapping with macro/news and becomes:

- crypto-internal structure for crypto assets
- slower business fundamentals for stocks
- slower supply / inventory structure for commodities when a real source exists

## What Changed

### Boundary cleanup

- `Part 8` template was rewritten to focus on:
  - internal liquidity
  - BTC leadership versus alt breadth
  - DeFi / chain / network participation
  - stock business fundamentals
  - stock cash flow / balance sheet / share-count behavior
- macro-style overlap was reduced
- `Part 6` now explicitly treats `BTC.D`, `USDT.D`, and `TOTAL3` as `Part 8` ownership, not primary macro ownership

### New real source lane

- added `scripts/sec_company_fundamentals.py`
- source uses:
  - SEC ticker map
  - SEC companyfacts
- output artifact:
  - `reports/auto/SEC_FUNDAMENTALS_<TICKER>.json`

### Owner docs updated

- `chimera-vps-deploy/skills/CHIMERA_RESEARCH_BUNDLE_TEMPLATE.md`
- `chimera-vps-deploy/skills/market-intel/SKILL.md`
- `agents/market-intel/AGENTS.md`
- `agents/market-intel/TOOLS.md`
- `research/platforms/2026-05-05-structural-market-intel-source-matrix.md`
- `research/platforms/2026-05-05-macro-and-cross-asset-source-matrix.md`

## Source Verdicts

### Strong exact owners

- `MARKET_CONTEXT.json`
  - BTC.D
  - USDT.D
  - TOTAL3 proxy
  - fear and greed
- `mcp__market_data__.crypto_market(action="global")`
  - crypto global market-cap mix cross-check
- `mcp__market_data__.defi_analytics(action="stablecoins")`
  - stablecoin supply snapshots
- `mcp__market_data__.defi_analytics(action="fees")`
  - DeFi participation
- `mcp__market_data__.network_status`
  - BTC fees / mempool
  - ETH gas
- `scripts/sec_company_fundamentals.py`
  - stock revenue / profit / cash flow / debt / share-count structure

### Helper-only

- `trading_system/scripts/coinglass_homepage_scraper.py`
  - helper-only for:
    - BTC exchange balance hint
    - altcoin season helper
    - average RSI heat helper
  - tested live in `--test`
  - do not let it override stronger owners

### Not good core owners today

- CoinAnk
  - trial / API-key gated
- WhaleTrades
  - public page not strong enough to promote as a core owner

## Proof

### Local proof

- `python scripts/sec_company_fundamentals.py --symbol NVDA`
  - wrote `reports/auto/SEC_FUNDAMENTALS_NVDA.json`
- `python scripts/sec_company_fundamentals.py --symbol AAPL`
  - wrote `reports/auto/SEC_FUNDAMENTALS_AAPL.json`
- `python trading_system/scripts/coinglass_homepage_scraper.py --test`
  - succeeded twice in this run

### VPS proof

- mirrored to:
  - `/root/openclawtrading/skills`
  - `/root/.openclaw/kimi-skills`
  - `/root/openclawtrading/agents/market-intel`
  - `/root/.openclaw/workspace/agents/market-intel`
  - `/root/openclawtrading/scripts/sec_company_fundamentals.py`
  - `/root/.openclaw/workspace/scripts/sec_company_fundamentals.py`
- remote script smoke:
  - `python3 /root/openclawtrading/scripts/sec_company_fundamentals.py --symbol NVDA`
  - `python3 /root/openclawtrading/scripts/sec_company_fundamentals.py --symbol AAPL`
  - both succeeded

## Important Next Work

1. Build one new `Part 8` BTC example from the updated crypto-internal field set.
2. Build one stock `Part 8` example using the new SEC lane.
3. If exact ETF flows or exact reserve / whale lanes become important later, add a better owner instead of re-expanding macro/news overlap.
