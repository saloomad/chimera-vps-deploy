# CHECKPOINT - 2026-05-06 - Part 8 Leadership, News, Earnings, And Flow Helpers

## Objective

Expand `Part 8: Structural / Market Intel` so it can also carry:

- strongest tracked leaders across crypto, stocks, and commodities
- slower structural-news helpers for crypto and stocks
- earnings-awareness helpers
- crypto whale-style pro-flow helpers
- honest stock insider / institutional helper reality

without collapsing back into macro or headline clutter.

## What Changed

### Template and skill contract

Updated:

- `chimera-vps-deploy/skills/CHIMERA_RESEARCH_BUNDLE_TEMPLATE.md`
- `chimera-vps-deploy/skills/market-intel/SKILL.md`
- `agents/market-intel/AGENTS.md`
- `agents/market-intel/TOOLS.md`
- `research/platforms/2026-05-05-structural-market-intel-source-matrix.md`

New Part 8 helper fields now include:

- `leadership_snapshot_scope`
- `crypto_leaders_helper_snapshot`
- `stock_leaders_helper_snapshot`
- `commodity_or_other_market_leaders_helper_snapshot`
- `crypto_structural_news_helper`
- `stock_structural_news_helper`
- `earnings_calendar_helper`
- `crypto_pro_flow_helper`
- `stock_insider_or_institutional_helper`

### New runtime helper script

Added:

- `scripts/cross_market_leadership_snapshot.py`

Purpose:

- build a tracked-basket leadership snapshot for:
  - crypto majors
  - tracked stock leaders
  - tracked commodities

Outputs:

- `reports/auto/CROSS_MARKET_LEADERSHIP_SNAPSHOT.json`

### New audit note

Added:

- `research/platforms/2026-05-06-part8-leadership-news-earnings-and-flow-helper-audit.md`

## Source Verdicts

### Best new helper owners

- leadership:
  - `scripts/cross_market_leadership_snapshot.py`
- crypto structural news:
  - `mcp__market_data__.news_feed`
  - cross-check: `tradfi_news(action="crypto_news")`
- earnings awareness:
  - `tradfi_news(action="earnings")`
- crypto pro-flow:
  - `derivatives_sentiment(top_position/top_ls/taker_ratio)`

### Demoted or weak

- `tradfi_news(action="news", symbol=...)`
  - noisy in latest test
- Binance plugin top-trader / taker endpoints
  - latest calls failed output validation
- OpenInsider
  - direct host scraping blocked in latest test
- WhaleWisdom
  - pages reachable, but structured live stock-specific extraction not yet proven
- WhaleTrades
  - public data-hub still showed placeholder-style values in latest host scrape

## Proof

### Local proof

- `python -m py_compile scripts/cross_market_leadership_snapshot.py`
  - passed
- `python scripts/cross_market_leadership_snapshot.py`
  - succeeded
  - wrote `reports/auto/CROSS_MARKET_LEADERSHIP_SNAPSHOT.json`
- `tradfi_news(action="earnings")`
  - returned upcoming names including `NVDA`
- `news_feed(action="latest", feeds="cointelegraph,coindesk,decrypt,blockworks", keyword="ETF")`
  - returned usable ETF / institutional crypto helper stories
- `derivatives_sentiment(top_position/top_ls/taker_ratio)`
  - returned usable BTC futures-participant lean and taker-flow helpers

### VPS proof

- mirrored to:
  - `/root/openclawtrading/skills`
  - `/root/.openclaw/kimi-skills`
  - `/root/openclawtrading/agents/market-intel`
  - `/root/.openclaw/workspace/agents/market-intel`
  - `/root/openclawtrading/scripts/cross_market_leadership_snapshot.py`
  - `/root/.openclaw/workspace/scripts/cross_market_leadership_snapshot.py`
  - `/root/openclawtrading/research/platforms/...`
  - `/root/.openclaw/workspace/research/platforms/...`
- SHA256 matched for:
  - market-intel skill
  - bundle template
  - market-intel AGENTS
  - market-intel TOOLS
  - cross_market_leadership_snapshot.py
- `python3 /root/openclawtrading/scripts/cross_market_leadership_snapshot.py`
  - succeeded
  - wrote `/root/openclawtrading/reports/auto/CROSS_MARKET_LEADERSHIP_SNAPSHOT.json`

## Important Next Work

1. Build one refreshed `Part 8` BTC example using the new helper fields.
2. Build one stock `Part 8` example that uses:
   - SEC fundamentals
   - leadership helper
   - earnings-awareness helper
3. If stock insider / institutional accumulation becomes important, prove a live owner before promoting it.
4. If CoinGlass or another exact ETF / reserve / whale lane is later added, keep it helper-only until cross-checked against stronger owners.
