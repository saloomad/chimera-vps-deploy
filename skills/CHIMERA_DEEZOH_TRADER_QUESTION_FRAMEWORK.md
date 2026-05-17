# Chimera Deezoh Trader Question Framework

Purpose: shared runtime mirror of `agents/deezoh/TRADER_QUESTION_FRAMEWORK.md`.

Use this document whenever Deezoh is expected to reason like a trader, generate specialist questions, compare long/short/no-trade, or decide whether to wait, prepare, activate, manage, or stand down.

## Non-Negotiable Rule

Scripts provide the minimum question floor. Deezoh must add freeform follow-up questions when the chart, agents, events, or contradictions reveal a better question.

## Required Idea Ledger

Every meaningful cycle keeps these ideas alive until evidence kills them:

- continuation long
- pullback or reset long
- reaction short
- failed-move reversal
- explicit no-trade

Each idea must name the owning timeframe, key zone, supporting evidence, missing evidence, trigger, invalidation, target path, and counter-case.

## Required Question Fields

Every question routed to an agent should include:

- `trade_idea_role`
- `timeframe_owner`
- `zone_contract`
- `indicator_contract`
- `context_contract`
- `decision_delta`
- `agent_report_memory_contract`

These fields make the answer auditable: Deezoh can see which idea the answer changes and whether the answer was specific enough to matter.

## Agent Capabilities

- `screener`: candidates, long/short/watch books, narratives, no-trade deferrals
- `chart-analyzer`: structure, zones, fibs, VWAP/AVWAP, MAs, OB/FVG/profile/sweeps, trend lines
- `indicator-analyst`: RSI, MACD, stochastic, divergence, reset/cross/exhaustion, timeframe timing
- `macro-bias`: SPX/QQQ, DXY, gold, oil, BTC.D, USDT.D, TOTAL3, rates when available
- `catalyst`: news, events, calendars, earnings, coin-specific drivers
- `market-maker`: OI, funding, liquidations, pain paths, crowding, trap/squeeze risk
- `strategy`: playbook, historical edge, entry/exit logic, invalidation
- `entry-watch`: exact lower-timeframe trigger and wake condition
- `risk-engine`: size class, book risk, correlation, permission to add risk
- `execution`: fills, active trade state, trail/reduce/exit, paper-safe execution
- `challenger`: strongest counter-thesis and no-trade case
- `youtube-analyst`: optional transcript and TradingView community-idea context only
- `Hermes`: paper-safe competitor and same-symbol challenger when fresh

## Hourly Delta Rule

Every active persistent specialist should refresh roughly every hour and compare against its last report:

- what changed
- what stayed the same
- bullish/bearish/mixed/stale impact
- sources used and freshness
- next question Deezoh should ask

## Chart-First Reasoning

Deezoh should reason in this order:

1. higher-timeframe permission
2. hot-zone map
3. indicator story by timeframe
4. liquidity and positioning path
5. macro/catalyst/YouTube/TradingView-idea/Hermes context
6. long vs short vs no-trade decision

For BTC, ETH, SOL, and other majors, Deezoh should translate the chart into trader questions, not generic labels:

- Which weekly and daily zones are price trading between now?
- Is the move a continuation, a recovery into resistance, a reset bounce, or a trap?
- Does `4H` support another push, or does it mainly support a short-term reaction?
- Is divergence missing, forming, or confirmed by timeframe?
- Is the long idea a tactical move into resistance, or a true trend continuation?
- Is the short idea active now, or only a watch once a higher zone is tagged and rejected?

Mixed timeframes must stay mixed in the answer.

Examples:

- `1H overbought` does not kill a valid `4H` continuation by itself
- `4H reset complete` does not prove a `1D` breakout if price is still under the major daily resistance cluster
- `daily divergence almost there` means watch for one more push or one more dump, not force the trade early

## TradingView Idea Rule

TradingView community ideas are outside-context only. Deezoh may use them to ask sharper questions about public levels, crowding, narratives, and author theses, but every idea must be verified by chart, indicator, derivatives, strategy, and risk evidence before it can affect a trade plan.

Each TradingView idea must answer:

- is the public idea pointing at a real zone on our chart?
- does it name timeframe, level, invalidation, and target path?
- is it fresh enough to matter or only background memory?
- is the crowd leaning too hard one way?
- which specialist must verify it next?

## Activation Rule

Before `READY` or activation, Deezoh needs structure, timing, positioning, playbook, invalidation, reward/risk, and a clear reason no-trade lost.

If any are missing, stay `WATCH`, `PREPARE`, or `NO_TRADE`.

## Alert And Wake Rule

When Deezoh waits for price or indicator confirmation, it should publish an alert request with symbol, timeframe, trigger condition, invalidation, and what Deezoh should do when it fires.

TradingView price alerts can be created from the live TradingView MCP when the symbol and price are known. Indicator alerts require the chart study to expose a Pine `alert()` or `alertcondition()` condition. Alerts wake Deezoh; they do not authorize a trade by themselves.
