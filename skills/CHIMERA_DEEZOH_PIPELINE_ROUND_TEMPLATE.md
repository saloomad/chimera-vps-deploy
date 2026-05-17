# Chimera Deezoh Pipeline Round Template

This is Deezoh's current-round reasoning document.

It should grow every cycle as new data arrives, specialists answer, the phase
changes, or the desk learns from a trade or thesis stop.

## Purpose

Answer:

- what am I looking for right now?
- what is my bias and why?
- what are the mandatory boards saying?
- which charts were actually checked this round?
- what are my best long, best short, and no-trade paths?
- which trade ideas are alive versus only interesting?
- what am I waiting for?
- should I pass to the next phase or stay here?
- what do I need to ask my agents?
- where will new answers be added?
- what did I learn from the last result?

## Required Fields

```json
{
  "current_phase": "entry_watch",
  "primary_document": "CHIMERA_ENTRY_WATCH_PACKET_TEMPLATE.md",
  "focus_symbol": "SOLUSDT",
  "focus_direction": "LONG",
  "bias_now": {
    "selected_workflow": "trend_auction",
    "winner": "wait",
    "final_posture": "wait",
    "macro_bias": "risk_on",
    "why": "waiting for trigger confirmation"
  },
  "current_strategy": {
    "posture": "wait",
    "should_pass_to_next_phase": false,
    "pass_or_wait_reason": "entry trigger is not live",
    "wait_type": "WAIT_TRIGGER",
    "wake_trigger": "1h reclaim with volume",
    "expires_or_recheck": "next lifecycle cycle"
  },
  "mandatory_market_boards": {
    "crypto_majors": ["BTCUSDT", "ETHUSDT", "SOLUSDT"],
    "macro_board": ["SPX", "QQQ", "DXY", "gold", "oil", "BTC.D", "USDT.D", "TOTAL3"],
    "stock_leaders": ["NVDA", "AAPL", "GOOGL", "MSFT", "AMZN", "TSLA", "PLTR", "MSTR", "COIN"],
    "coverage_status": "active"
  },
  "chart_reference_registry": {
    "saved_chart_boards": [],
    "active_chart_lane": "tradingview_direct / screenshot_only / report_only",
    "chart_lane_notes": "Which charts were actually checked this round and which are only saved references."
  },
  "active_trade_ideas": {
    "best_continuation_long": {},
    "best_reset_long": {},
    "best_reaction_short": {},
    "best_failed_move_reversal": {},
    "best_no_trade": {}
  },
  "watchlists": {},
  "needed_info": {},
  "where_new_info_gets_added": {},
  "agent_capability_map": {},
  "architect_feedback_items": [],
  "learning_and_review": {}
}
```

## Pass / Wait / Reject Loop

Every round Deezoh asks:

1. Is the current phase still correct?
2. Did new data change the best long, best short, or no-trade?
3. Is there enough confirmation to pass to the next phase?
4. If not, what exact typed wait is active?
5. Which one agent question would most improve the next decision?
6. What answer would force a phase switch?
7. What should be remembered for the next similar setup?

## Where New Information Goes

- market data goes to its source report and the observability source inventory
- agent answers go to `DEEZOH_ROUND_DISPATCH.json`, `DESK_INTERACTION_BUS.json`, and that agent's report
- phase decisions go to the current phase packet, lifecycle context, symbol lifecycle state, and this round document
- trade results go to closeout or thesis-stop packets plus the learning queue
- mistakes and patterns go to the learning queue and future Deezoh thoughts

## Agent Menu

Deezoh can ask:

- `screener`: opportunity ranking and market-wide shortlist
- `chart-analyzer`: price action, zones, breakouts, rejects, visual confirmation
- `indicator-analyst`: timing, divergence, reset, crossover, timeframe stretch
- `macro-bias`: broad risk, events, cross-asset context
- `catalyst`: news, events, earnings, narrative changes
- `market-maker`: liquidations, max pain, OI, funding, trap risk
- `entry-watch`: exact wake trigger and entry readiness
- `execution`: open trade and ledger truth
- `trade-judge`: closeout, mistakes, lessons, memory patterns
- `review-debug`: issues, replay, scenario failure, instruction repair

## Good Round Close

A good round ends with:

- one current phase
- one current strategy
- one typed wait or phase promotion
- one next agent question
- one wake trigger
- one issue list
- one learning state
