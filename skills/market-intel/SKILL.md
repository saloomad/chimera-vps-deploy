---
name: market-intel
description: >
  Internal crypto structure and slower stock fundamentals beneath price. Use this
  skill whenever the user asks about stablecoin supply, BTC dominance, alt breadth,
  DeFi participation, BTC/ETH network demand, stock revenue/profitability/cash-flow
  structure, balance-sheet quality, dilution or buybacks, strongest tracked leaders,
  structural-news helpers, earnings awareness, or slower structural backdrop
  questions that are not already owned by chart, indicators, macro, news, or
  derivatives.
---

# Market Intelligence Skill

Use this skill for `Part 8: Structural / Market Intel`.

Purpose:

- for crypto: answer internal crypto structure questions
- for stocks: answer slower business-fundamental questions
- for commodities: answer slower supply / inventory questions when a real source exists

Do not let this skill drift into:

- macro event timing
- chart structure
- indicator timing
- derivatives crowding
- headline-by-headline catalyst reporting

## Quick Decision Tree

| User asks about | Go to section |
|---|---|
| Stablecoins, BTC.D, alt breadth | `Crypto Internal Structure` |
| Revenue, cash flow, debt, dilution | `Stock Fundamentals` |
| Strongest leaders across crypto/stocks/commodities | `Leadership Helpers` |
| Structural crypto or stock news that matters beyond one headline | `Structural News And Earnings Helpers` |
| Earnings timing that can reshape the structural case | `Structural News And Earnings Helpers` |
| ETF flows, institutional buying | `ETF & Institutional Helpers` |
| Crypto pro-flow / whale-style futures proxies | `Crypto Pro Flow Helpers` |
| Stock insider or institutional accumulation | `Stock Insider And Institutional Helpers` |
| Whale moves, exchange reserves | `On-chain Flow Helpers` |
| Market cycle heat | `Cycle Heat` |
| DeFi TVL, chains, fees | `DeFi Structure` |
| BTC fees, mempool, ETH gas | `Network Health` |

## Crypto Internal Structure

Use the strongest exact owners first:

```
crypto_market(action="global")
defi_analytics(action="stablecoins")
defi_analytics(action="fees")
defi_analytics(action="chains", limit=15)
network_status(action="btc_fees")
network_status(action="btc_mempool")
network_status(action="eth_gas")
```

Use this section to answer:

- is dry powder building or draining?
- is BTC leading or is breadth spreading into alts?
- are DeFi and network signals confirming the move?

Helper only:

- local `coinglass_homepage_scraper.py`
  - BTC exchange-balance helper
  - altcoin season helper
  - average RSI heat helper

Do not let CoinGlass helpers override stronger owners.

## Leadership Helpers

Use:

```
python scripts/cross_market_leadership_snapshot.py
crypto_market(action="markets", vs_currency="usd", per_page=50, page=1)
global_assets(action="ohlcv", symbol="{ticker_or_future}", interval="1d", period="3mo")
```

Use this section to answer:

- which tracked leaders are carrying the current move?
- is leadership concentrated in quality majors or broadening?
- are commodities or other tracked markets confirming a slower structural risk-on or defensive tone?

Rule:

- leadership is helper-only unless the source truly covers the whole market
- tracked-basket leaders are useful, but do not call them whole-market exact winners

## Stock Fundamentals

Use:

```
tradfi_news(action="company", symbol="{ticker}")
python scripts/sec_company_fundamentals.py --symbol {ticker}
```

Use this section to answer:

- is the business strengthening or weakening?
- is free cash flow supportive?
- is the balance sheet helping or hurting?
- is share count shrinking, stable, or diluting?

Interpretation:

- rising revenue + rising profits + positive free cash flow = structurally supportive
- strong business but weakening cash flow = supportive but softening
- negative cash flow, leverage pressure, or rising dilution = structural headwind

## Structural News And Earnings Helpers

Use:

```
news_feed(action="latest", feeds="cointelegraph,coindesk,decrypt,blockworks", keyword="ETF", limit=5)
news_feed(action="latest", feeds="cnbc", keyword="{company_or_sector}", limit=5)
tradfi_news(action="crypto_news", limit=10)
tradfi_news(action="earnings", from_date="{today}", to_date="{future_date}", limit=20)
```

Use this section to answer:

- is there a slower fundamental story backing the move?
- is there an earnings window that can materially reshape the structural case?
- is the story persistent enough to matter, or just a one-off catalyst that belongs in Part 7?

Rules:

- treat earnings here as helper awareness only; Part 6 and Part 7 still own the full event and catalyst lanes
- in the current tested stack, `tradfi_news(action="news", symbol=...)` is noisy and should not be the primary stock-news owner

## ETF & Institutional Helpers

Direct ETF flow tables are not available in the current proven free stack.

Use:

```
news_feed(action="latest", feeds="cointelegraph,coindesk,decrypt,blockworks", keyword="ETF", limit=10)
news_feed(action="latest", feeds="cointelegraph,coindesk,decrypt,blockworks", keyword="institutional", limit=5)
tradfi_news(action="crypto_news", limit=10)
```

Rule:

- treat this as helper context only
- do not present it as exact flow truth

## Crypto Pro Flow Helpers

Use:

```
derivatives_sentiment(action="top_position", symbol="BTCUSDT", period="4h", limit=5)
derivatives_sentiment(action="top_ls", symbol="BTCUSDT", period="4h", limit=5)
derivatives_sentiment(action="taker_ratio", symbol="BTCUSDT", period="4h", limit=5)
```

Use this section to answer:

- are larger futures participants leaning with or against the move?
- is taker flow confirming the latest impulse?
- is pro-flow stretched enough that Deezoh should watch for a reset?

Rules:

- this is a pro-flow helper, not exact whale-wallet truth
- if these proxies conflict with stronger structure signals, call the section mixed instead of forcing conviction

## Stock Insider And Institutional Helpers

Best current reality:

- direct stock-insider or large-holder ownership is not yet runtime-proven as a clean exact owner
- OpenInsider search pages were discoverable on the web but direct host scraping was blocked in this run
- WhaleWisdom pages are reachable, but structured stock-specific holdings extraction is not yet proven as a reliable live owner

Use:

- SEC share-count change from `sec_company_fundamentals.py`
- company buyback or dilution announcements from the news helpers above

Rule:

- if no runtime-proven live insider or institutional lane exists, say `helper_missing` or `unavailable` plainly

## On-chain Flow Helpers

Exact whale wallets, exchange reserves, and token unlock tables are not available in the current proven free stack.

If needed, say that plainly and fall back to the best helper context:

- stablecoin supply
- breadth / dominance
- CoinGlass exchange-balance helper

## Cycle Heat

Exact branded cycle models like `AHR999`, `Pi Cycle`, `MVRV`, and `NVT` are not available in the current proven free stack.

Use proxy heat instead:

```
crypto_market(action="global")
defi_analytics(action="stablecoins")
```

Interpretation:

- BTC dominance high and rising = BTC-led / earlier-cycle quality preference
- BTC dominance falling while breadth improves = broader risk spread
- stablecoin growth = more potential buying power

## DeFi Structure

```
defi_analytics(action="stablecoins")
defi_analytics(action="fees")
defi_analytics(action="chains", limit=15)
defi_analytics(action="tvl_rank", limit=20)
```

Best use:

- exact stablecoin supply
- DeFi participation
- filtered chain context

## Network Health

```
network_status(action="eth_gas")
network_status(action="btc_fees")
network_status(action="btc_mempool")
```

Best use:

- Ethereum activity pressure
- Bitcoin fee and mempool demand

## Output Rules

- state exact vs helper vs missing plainly
- prefer exact owners first
- keep macro and news ownership in their own sections
- for stocks, filings beat headlines
- for crypto, stablecoins / dominance / DeFi / network data beat vague sentiment

## Notes

- CoinAnk is not a clean free default; it is trial / API-key gated
- WhaleTrades public pages are not strong enough to trust as a core owner today
- CoinGlass homepage scraping is useful but helper-grade
