# Deezoh And Hermes Agent Improvement Observations

Owner: architect-codex
Status: active ledger
Purpose: track recurring evidence, test results, improvement proposals, and approval boundaries for Deezoh, Hermes, persistent trading agents, skills, scripts, and Sal-agent interaction quality.

## Current Control State

- The Deezoh coach suite exists as canonical skills under `chimera-vps-deploy/skills/`.
- The suite has been mirrored to Codex, Claude, local `.agents`, OpenClaw skill homes, and OpenCode prompt/wrapper form.
- Deezoh's instruction layer now requires a not-a-yes-man trading response and routes questionable lessons to learning/monitoring instead of blindly adopting them.
- Live OpenClaw currently exposes the relevant persistent agents under `/root/.openclaw/workspace/agents/`.
- OpenClaw internal cron currently reports no OpenClaw-native jobs, but Linux root cron is active and running market scripts.
- One failed OpenClaw background task exists because `thinking medium` is not supported for `kimi/k2.6`; future live tests must use `--thinking on` or `--thinking off`.

## Immediate Observations

| ID | Observation | Type | Evidence | Impact | Owner | Risk | Approval | Proof Test | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DHI-001 | Deezoh needs the trading coach and learning monitor together, not isolated. The coach catches the bad trade question; learning mode decides whether it is a lesson; monitor catches repeated friction or wrong-lesson risk. | workflow issue | Deezoh coach suite runtime and live replay receipts | Prevents yes-man behavior and prevents bad self-training | architect-codex | Low | No approval for skill text; approval required for trading-policy changes | Replay tempting chase and wrong-lesson scenarios | In progress |
| DHI-002 | TradingView screener is installed on OpenClaw, but it is daily snapshot data, not multi-timeframe historical proof. | data-source coverage gap | `chimera-tradingview-screener` skill listing and local skill docs | Prevents treating a screener hit as an entry | strategy + screener | Low | No | Ask Deezoh to explain TradingView limits in a setup question | Open |
| DHI-003 | OpenClaw's internal cron list has no jobs, but Linux root cron is active. The improvement loop must treat those as separate schedulers. | workflow issue | `openclaw cron list` returned no jobs; root `crontab -l` shows market scripts | Prevents false "no automation" or false "everything is wired" conclusions | architect-codex + cron-manager | Medium | No for Codex automation; review before OpenClaw-native cron mutation | Create hourly Codex automation, then test whether Deezoh consumes Linux cron outputs | In progress |
| DHI-004 | Kimi K2.6 rejects `thinking medium`; live tests must use `thinking on/off`. | prompt issue | `openclaw tasks list` failed task summary | Avoids recurring failed test tasks | architect-codex | Low | No | Rerun live replay with `--thinking on` | Open |
| DHI-005 | Reports surface on live OpenClaw is currently sparse (`reports/auto/WATCHLISTS.json` visible), so audit must distinguish missing reports from agent absence. | stale source-of-truth | live `find reports` inventory | Prevents false claims that agents are active just because they exist | auditor + pipeline-watchdog | Medium | Review before deleting or rewriting report contracts | Audit recent reports, agent logs, and tasks separately | Open |
| DHI-006 | Combined trade-and-learning prompts originally selected only `deezoh-trading-coach`; the dispatcher now selects trading coach, learning mode, and vibe monitor together for wrong-lesson risk. | prompt issue | local dispatcher test on "Learn that momentum means buy fast" | Prevents Deezoh from challenging the trade but failing to protect the learning loop | Codex | Low | No | `run_deezoh_coach_suite_smoke.py` must fail if expected skills are missing | Verified |
| DHI-007 | Live TradingView data script can return absurd microcap values and crashed formatting a `None` RSI in its built-in demo path. | data-source coverage gap | `python3 scripts/data/tradingview_api.py --help` executed demo and hit `TypeError: unsupported format string passed to NoneType.__format__` | Deezoh must not treat raw screener output as clean trade evidence without quality filters | screener + Codex | Medium | Review before script change | Add screener quality filters/null handling or route to screener issue queue | Open |
| DHI-008 | Live market scanner completed but Coinalyze keys were rate-limited and outputs went to `/root/reports/auto/OPPORTUNITIES.json`, while `/root/openclawtrading/reports/auto` only showed `WATCHLISTS.json`. | stale source-of-truth | `python3 scripts/market_scanner.py --help` executed scan and printed output paths | Consumers may read the wrong report root or miss fresh scanner output | pipeline-watchdog + architect | Medium | Review before path rewrite | Verify current consumer paths before editing scripts | Open |
| DHI-009 | Live macro builder completed with MIXED 30% confidence but had 0 news articles and placeholder macro/funding/OI context. | data freshness issue | `python3 scripts/macro_bias_builder.py --help` executed build | Macro advice should be downgraded when inputs are sparse | macro-bias + catalyst | Low | No | Deezoh must label macro confidence low when source counts are weak | Open |
| DHI-010 | Hermes has live workspace files but is not registered in `/root/.openclaw/openclaw.json`, so OpenClaw routing may not reach Hermes as a first-class agent. | workflow issue | live council audit of `/root/.openclaw/workspace/agents/hermes-*` and `openclaw.json` | Hermes may exist but fail activation in normal routing | architect + Hermes Lead | Medium | Review before live registry edit | Test Hermes invocation path, then register only if route is confirmed safe | Open |
| DHI-011 | Linux candle analyzer cron is failing with `ModuleNotFoundError: No module named 'indicators.calculator'`. | missing test | live `/root/.openclaw/logs/candle_analyzer.log` tail | Candle/indicator freshness may be stale even while cron service is active | indicator-analyst + Codex | Medium | Review before live dependency/path fix | Reproduce command manually, locate import path, patch smallest safe path/dependency issue | Open |
| DHI-012 | TradingView MCP/Jackson is running as a Node process on the VPS, but this Codex runtime does not currently expose a direct TradingView MCP tool. | data-source coverage gap | live process `/root/.openclaw/workspace/projects/tradingview-mcp-jackson/src/server.js`; current Codex tool list has no TradingView MCP callable | Prevents overclaiming direct chart-control ability from this session | chart-analyzer + architect-codex | Low | No | Use OpenClaw route for TradingView MCP tests; use screener skill locally unless connector is exposed | Open |
| DHI-013 | Several local mirror scripts still carry retired `/home/open-claw` defaults. | stale source-of-truth | local council audit of Hermes, market-maker, YouTube, strategy bridge, Bitget, screener/catalyst paths | Local mirrors can mislead agents or generate stale handoffs | Codex | Medium | Review before broad migration | Add or extend runtime-path lint gate for active lanes | Open |

## Hourly Audit Output Requirements

Each hourly run must include:

- top plain-English summary Sal can read without opening files
- what agents, skills, scripts, reports, and logs were actually inspected
- Deezoh/Hermes behavior test result
- data-source freshness result
- optimization queue changes
- safe fixes applied
- risky changes waiting for review or Sal approval
- next owner

## Open Questions For Council

- Is TradingView MCP/Jackson actually callable in OpenClaw, or only represented by TradingView screener scripts/skills?
- Which persistent agents are actively scheduled versus only installed?
- Which strategy/backtest scripts are current source of truth, and do they have walk-forward proof?
- Should Hermes get OpenClaw-native cron via `cron-manager`, or should the first recurrence stay in Codex until the live job shape is proven?
- Are Bitget hub outputs richer than current derivatives/AltFins/TradingView lanes for Sal's preferred trading questions?
