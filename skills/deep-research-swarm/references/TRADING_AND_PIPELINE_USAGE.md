# Trading And Pipeline Usage

## Use In Trading Like This

### Good Fits

- weekly BTC thesis
- weekly sector rotation memo
- event-driven setup review after CPI, FOMC, ETF news, or major on-chain shock
- post-trade review when the desk made a weak or surprising decision
- large comparison such as best AI tokens, best L1 setups, or best risk-off hedges

### Bad Fits

- every routine monitor cycle
- every entry-watch wake
- every active-trade management pass
- every signal filter

## Live Trading Loop Stays Lean

The live loop should remain:

1. monitor inputs
2. detect setup
3. gather only needed specialists
4. validate freshness, conflicts, and risk
5. decide `execute`, `watch`, or `reject`
6. manage position or state
7. review and update state

## Example Split

### Example A: Weekly BTC Thesis

- use `deep-research-swarm`
- fan out by timeframe, on-chain, derivatives, macro, ETF flow, and alt rotation
- cross-verify before writing the memo

### Example B: Live BTC Setup Watcher

- do not use full swarm
- use the lean pipeline loop
- if the watcher hits deep ambiguity, open a separate swarm-backed review objective

### Example C: Post-Trade Failure Analysis

- use `deep-research-swarm`
- dimensions can include chart state, specialist recommendations, data freshness, execution timing, and risk handling
- use targeted validation only on the dimensions that disagreed
