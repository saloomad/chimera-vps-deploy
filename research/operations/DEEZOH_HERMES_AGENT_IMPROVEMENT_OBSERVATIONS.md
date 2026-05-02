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

## 2026-05-02 Audit Additions

### New Evidence From This Run

- Issue `DHI-014`
  Raw event: live root cron is the active scheduler, while `openclaw cron list` returned `No cron jobs.` and `openclaw tasks flow list` returned `TaskFlows: 0`.
  What happened: the live agents exist under `/root/.openclaw/workspace/agents/`, but recurrence is coming from Linux root cron rather than OpenClaw-native schedulers.
  Why it matters: Deezoh/Hermes audits can overstate or understate automation health if they treat these as one scheduler.
  Recurrence: current live state on 2026-05-02T00:00Z hour.
  Affected agent/workflow/data source/timeframe: Deezoh, Hermes, screener, macro, watchlist, root cron, OpenClaw taskflow.
  Proposed fix: keep audits split into `OpenClaw-native` vs `Linux cron` lanes and do not migrate jobs until each consumer path is proven.
  Owner: `architect-codex + cron-manager`
  Risk: `medium`
  Approval needed: `review before any live scheduler migration`
  Proof test: rerun `openclaw cron list`, `openclaw tasks flow list`, and `crontab -l` in the same audit pass.

- Issue `DHI-015`
  Raw event: `market_scanner.log` shows a successful scan writing `/root/reports/auto/OPPORTUNITIES.json`, then later `ModuleNotFoundError: No module named 'divergence_scanner'`.
  What happened: the scanner lane is intermittently succeeding and then crashing, so fresh reports alone do not prove the lane is stable.
  Why it matters: Deezoh and watchlist consumers can read stale opportunities while the log shows the current scanner pass is broken.
  Recurrence: repeated within the same current log tail.
  Affected agent/workflow/data source/timeframe: screener, strategy, opportunity scan, 30-minute root cron.
  Proposed fix: reproduce the import path under the same cron environment, then patch the smallest import-path guard in the script lane before touching live cron.
  Owner: `screener + Codex`
  Risk: `medium`
  Approval needed: `no for local repro or test; review before live cron/script deployment`
  Proof test: run a bounded import/replay under the same interpreter and confirm no `divergence_scanner` import error.

- Issue `DHI-016`
  Raw event: `derivatives.log` repeatedly ends with `DERIVATIVES.json written: 0 coins`, while `watchlist.log` falls back to `0%` monitor-only candidates and `macro_bias.log` shows `0 articles` with placeholder derivatives context.
  What happened: multiple upstream data lanes are technically running but are producing thin or empty payloads.
  Why it matters: Deezoh can sound active while the underlying catalyst, macro, and derivatives evidence is too weak to support decisions.
  Recurrence: repeated across the latest live log tails.
  Affected agent/workflow/data source/timeframe: derivatives, macro-bias, watchlist, catalyst context, 30-minute and hourly cron.
  Proposed fix: add explicit freshness/coverage downgrades in the human-facing summaries and trace which consumers still treat empty payloads as normal.
  Owner: `pipeline-watchdog + macro-bias + catalyst`
  Risk: `medium`
  Approval needed: `no for summary/test hardening; review before live contract rewrites`
  Proof test: verify summaries flag low-confidence mode whenever derivatives coin count is `0` or news article count is `0`.

### Optimization Queue

- `Q-2026-05-02-01` Extend the runtime-path lint gate beyond Deezoh skill docs to cover shared runtime helpers. Status: done in local mirror via `lint_deezoh_runtime_paths.py` + `runtime_paths.py`.
- `Q-2026-05-02-02` Reproduce the intermittent `divergence_scanner` import failure under the live cron environment without changing cron. Status: narrowed. The active `/root/openclawtrading/scripts/market_scanner.py` imports and runs; the stale workspace copy under `/root/.openclaw/workspace/trading_system/scripts/market_scanner.py` still contains the old `/root/reports/auto` print path.
- `Q-2026-05-02-03` Prove which consumers read `/root/openclawtrading/reports/auto` versus `/root/reports/auto` before any report-path rewrite. Status: done for the repaired lanes. `news_fetcher.py`, `economic_calendar_fetcher.py`, `macro_bias_builder.py`, and `catalyst_agent.py` were verified against `/root/openclawtrading/reports/auto`.
- `Q-2026-05-02-04` Add a low-confidence downgrade contract when derivatives or macro/news inputs are empty. Status: partially done. Macro and catalyst now consume the repaired news/calendar files; derivatives still needs an upstream source fix.

### 2026-05-02 Continuation Results

- Fixed
  `news_fetcher.py`, `economic_calendar_fetcher.py`, `derivatives_fetcher.py`, `catalyst_agent.py`, `macro_calendar_checker.py`, `news_scraper.py`, and `economic_calendar_scraper.py` were updated to use the shared runtime-path helper so they stop writing to retired roots.

- Fixed
  `macro_bias_builder.py` now reads the current `NEWS.json` schema, falls back from missing `MACRO.json` to `ECONOMIC_CALENDAR.json`, and writes `MACRO_BIAS.json` plus the dashboard under `/root/openclawtrading/...`.

- Proved
  Live bounded reruns created:
  - `/root/openclawtrading/reports/auto/NEWS.json`
  - `/root/openclawtrading/reports/auto/ECONOMIC_CALENDAR.json`
  - `/root/openclawtrading/reports/auto/MACRO_BIAS.json`
  - `/root/openclawtrading/dashboard/CHIMERA_MACRO_BIAS.html`
  - live catalyst output with `news=172`, `breaking=15`, and `catalysts=5`

- Still open
  Issue `DHI-017`
  Raw event: `/root/openclawtrading/data/HOMEPAGE_STATS.json` and `HOMEPAGE_TABLE.json` are missing, and live `derivatives_fetcher.py` still writes `DERIVATIVES.json` with `0 coins`.
  What happened: the report-root fix landed, but the upstream Coinglass-style input files the derivatives consolidator depends on are absent in the live repo data directory.
  Why it matters: downstream lanes now read the correct root, but derivatives context remains empty because the source payload is missing, not because of path drift.
  Recurrence: current live proof on 2026-05-02 after the writer fix.
  Affected agent/workflow/data source/timeframe: derivatives, macro-bias, watchlist, screener, 15-minute and 30-minute recurring analysis.
  Proposed fix: trace which upstream collector is supposed to materialize `HOMEPAGE_STATS.json` and `HOMEPAGE_TABLE.json`, then restore or replace that collector before changing scoring logic.
  Owner: `pipeline-watchdog + derivatives`
  Risk: `medium`
  Approval needed: `no for bounded source tracing; review before swapping data vendors or changing recurring live collection`
  Proof test: rerun the upstream collector and confirm both data files exist with non-empty payloads before rerunning `derivatives_fetcher.py`.

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

## 2026-05-02 Live Observation Loop Additions

### New Evidence From The 15-Minute Observation Buildout

- Issue `DHI-017`
  Raw event: live Deezoh breakout replay selected `breakout_acceptance`, rejected the chase, and then upgraded from `WATCH` to `READY` after a same-session retest/cooldown follow-up.
  What happened: the new workflow selector is influencing the live answer and the follow-up state transition, not just changing wording.
  Why it matters: this is proof that Deezoh can now change its ranking and next step when the evidence improves instead of repeating the same pushback forever.
  Recurrence: observed in session `deezoh-observe-breakout` on 2026-05-02.
  Affected agent/workflow/data source/timeframe: Deezoh, breakout acceptance, 4H permission with 15M timing.
  Proposed fix: keep this as the baseline replay for future regressions and require the same-session follow-up check in recurring audits.
  Owner: `architect-codex`
  Risk: `low`
  Approval needed: `no`
  Proof test: compare first and second `DEEZOH_THOUGHTS_LIVE.json` writes in the same session and confirm state moves from `WATCH` to `READY`.

- Issue `DHI-018`
  Raw event: live Deezoh named `chart-analyzer`, `market-maker`, `indicator-analyst`, `strategy`, and `macro-bias`, but the session traces show `sessions_spawn = 0`.
  What happened: Deezoh is still mostly simulating agent-to-agent interaction in prose instead of actually delegating to specialist agents.
  Why it matters: the system can sound like a desk while still behaving like one big solo agent, which weakens both evidence quality and monitoring truth.
  Recurrence: observed in `deezoh-observe-breakout` and `deezoh-observe-news-v2`.
  Affected agent/workflow/data source/timeframe: Deezoh, council/advisory routing, all trade workflows.
  Proposed fix: add a real delegation contract for at least one specialist follow-up branch in the recurring replay suite and flag any case where named specialists were not actually spawned or their reports not read.
  Owner: `architect-codex + orchestrator`
  Risk: `medium`
  Approval needed: `review before changing live delegation policy`
  Proof test: future replay must show either `sessions_spawn > 0` or explicit fresh specialist report reads for the named lanes.

- Issue `DHI-019`
  Raw event: live Deezoh attempted to read missing local files such as `OBSERVATIONS.md`, `EXECUTION_POLICY.md`, `DESK_CONTRACT.md`, and `EXPERT_COUNCIL.md`.
  What happened: the live workspace was missing expected local bootstrap surfaces, which created read errors and likely wasted reasoning cycles.
  Why it matters: missing local bootstrap files make the live agent slower, noisier, and less reliable before it even reaches the market logic.
  Recurrence: observed in the first breakout replay session.
  Affected agent/workflow/data source/timeframe: Deezoh bootstrap, all live trading loops.
  Proposed fix: create and sync local Deezoh bootstrap support files, then re-run the live observation suite.
  Owner: `Codex`
  Risk: `low`
  Approval needed: `no`
  Proof test: confirm the files exist on `/root/.openclaw/workspace/agents/deezoh/` and future sessions read `OBSERVATIONS.md` without ENOENT.
  Status: `fixed and verified`

- Issue `DHI-020`
  Raw event: Deezoh shared docs still surfaced retired `/home/open-claw/...` and Windows-local `C:\\Users\\becke\\...` paths during live runs.
  What happened: the agent is still being handed stale path truth from large shared reference files even when the live runtime is correct.
  Why it matters: path drift causes bad reads, wasted retries, and false assumptions about what files are available.
  Recurrence: observed in `TRADINGVIEW_GUIDE.md`, `OPENCLAW_AGENTS.md`, and `WORKFLOW.md` during live sessions.
  Affected agent/workflow/data source/timeframe: Deezoh runtime pathing, TradingView/chart workflow, capability inventory interpretation.
  Proposed fix: add explicit runtime-truth banners to old shared docs and keep extending the runtime-path lint/audit pass.
  Owner: `Codex`
  Risk: `medium`
  Approval needed: `no for doc/runtime-truth fixes`
  Proof test: future sessions should stop surfacing stale `/home/open-claw` examples as active instructions.
  Status: `partially fixed`

- Issue `DHI-021`
  Raw event: post-fix news-event replay succeeded, but Deezoh attempted crypto pricing through `kimi_finance`, hit stock-style ticker errors, then fell back to web fetch/search.
  What happened: the live reasoning improved enough to finish, but the data-source routing is still suboptimal for crypto because the wrong finance tool path is being attempted first.
  Why it matters: wasted tool calls make event-mode answers slower and can hide better native routes like Bitget or TradingView-derived surfaces.
  Recurrence: observed in session `deezoh-observe-news-v2`.
  Affected agent/workflow/data source/timeframe: Deezoh, news-event control, crypto price routing.
  Proposed fix: prefer Bitget/TradingView/report surfaces for crypto quotes before generic Kimi finance, and treat generic finance ticker errors as a routing bug.
  Owner: `data-source router + Codex`
  Risk: `medium`
  Approval needed: `no for routing preference changes`
  Proof test: the next crypto replay should not call `kimi_finance` with `ETHUSDT` or `BTCUSDT`.

- Issue `DHI-022`
  Raw event: live Deezoh looked for `/root/.openclaw/workspace/agents/deezoh/reports/auto/OPPORTUNITIES.json` and failed before the shared report root was linked.
  What happened: the agent expected a local agent-relative report surface while the real reports live under `/root/openclawtrading/reports/auto`.
  Why it matters: even when the reports exist, the agent can behave as if they are missing and downgrade itself unnecessarily.
  Recurrence: observed in `deezoh-observe-news-v2`.
  Affected agent/workflow/data source/timeframe: Deezoh, report-consumption workflow, shared report access.
  Proposed fix: create agent-local `reports/auto` symlinks to `/root/openclawtrading/reports/auto` for Deezoh, screener, and macro-bias.
  Owner: `Codex`
  Risk: `low`
  Approval needed: `no`
  Proof test: future sessions should stop emitting ENOENT for local `reports/auto` reads.
  Status: `fixed and pending replay confirmation`

- Issue `DHI-023`
  Raw event: screener direct replay repeatedly aborted its own reads and timed out, while macro-bias direct replay failed without leaving a normal session artifact.
  What happened: the specialist lanes are still less stable than the main Deezoh lane under direct live prompting.
  Why it matters: Deezoh cannot rely on specialist delegation if the specialist lanes time out or fail before producing usable outputs.
  Recurrence: observed in `screener-observe-accumulation` and `macro-observe-pre-event`.
  Affected agent/workflow/data source/timeframe: screener accumulation workflow, macro pre-event workflow.
  Proposed fix: slim specialist bootstrap/read order, add missing local support surfaces where needed, and test specialist lanes one by one with shorter deterministic prompts.
  Owner: `architect-codex + screener + macro-bias`
  Risk: `medium`
  Approval needed: `no for bounded prompt/bootstrap fixes`
  Proof test: a direct screener replay and a direct macro replay should complete successfully without aborted read storms.

- Issue `DHI-024`
  Raw event: pre-event smoke replay asked for `FOMC.md` and failed until a local event-policy stub was added.
  What happened: Deezoh has an event-control instinct, but the live workspace lacked one of the expected event reference files.
  Why it matters: event workflows should not lose time or confidence because a basic event policy note is missing.
  Recurrence: observed in `deezoh-observe-smoke-v3`.
  Affected agent/workflow/data source/timeframe: Deezoh, pre-event/news-event control workflows.
  Proposed fix: keep the new `FOMC.md` stub synced and expand it only if future event replays still hit missing policy gaps.
  Owner: `Codex`
  Risk: `low`
  Approval needed: `no`
  Proof test: future pre-event replays should read `FOMC.md` successfully.
  Status: `fixed and pending replay confirmation`

### Observation Loop Results

- The strongest live improvement is that Deezoh now names a workflow and can change state when the evidence changes.
- The biggest remaining weakness is that named specialist lanes are still mostly rhetorical; real specialist delegation and direct specialist stability are not proven.
- The second major weakness is runtime truth drift: Deezoh still inherits too many stale path assumptions and imperfect crypto data-source routing.

### Optimization Queue Updates

- `Q-2026-05-02-05` Add missing local Deezoh bootstrap support files (`OBSERVATIONS.md`, `EXECUTION_POLICY.md`, `FOMC.md`) and sync the missing contract/council files. Status: done.
- `Q-2026-05-02-06` Add agent-local `reports/auto` symlinks for Deezoh, screener, and macro-bias to the shared `/root/openclawtrading/reports/auto` root. Status: done, pending replay confirmation.
- `Q-2026-05-02-07` Stop crypto event-mode replays from using stock-style `kimi_finance` routes for `ETHUSDT` and `BTCUSDT`. Status: queued.
- `Q-2026-05-02-08` Prove real specialist delegation or fresh specialist-report consumption in live Deezoh replays. Status: queued.
- `Q-2026-05-02-09` Slim screener and macro-bias direct live bootstrap enough that direct replays stop timing out or aborting reads. Status: queued.

## 2026-05-02 Follow-On Audit Additions

### New Evidence From The Current Run

- Issue `DHI-026`
  Raw event: live `openclaw cron list` and `openclaw tasks flow list` both hung until a 6-second timeout, while `crontab -l` returned the real active schedule immediately.
  What happened: the OpenClaw-native scheduler commands are not currently a fast trustworthy truth surface on this VPS, even though Linux root cron is readable.
  Why it matters: an audit can wrongly conclude "no jobs" when the real problem is "the scheduler command hangs."
  Recurrence: reproduced on 2026-05-02 during this pass.
  Affected agent/workflow/data source/timeframe: scheduler proof, cron audit, OpenClaw taskflow, recurring data lanes.
  Proposed fix: record `timeout or failed` as a separate state from `empty`, and prefer root cron plus report freshness while the OpenClaw scheduler surface is hanging.
  Owner: `architect-codex + cron-manager`
  Risk: `medium`
  Approval needed: `no for audit/reporting fixes; review before changing live scheduler configuration`
  Proof test: rerun `timeout 6s openclaw cron list`, `timeout 6s openclaw tasks flow list`, and `crontab -l` in the same pass and keep the states separate.

- Issue `DHI-027`
  Raw event: live breakout replay `deezoh-observe-breakout-v3` ignored the direct "best long / best short / best no-trade" ask and drifted into a generic desk briefing after reading large reference files and stale inventory surfaces.
  What happened: Deezoh still answers like a broad morning report too easily when the prompt is a focused chart-side observation question.
  Why it matters: Sal asked for a direct decision comparison, and the live response shape drift makes the desk feel less trader-like and less useful in the moment.
  Recurrence: observed in the current breakout replay; earlier observation runs already showed rhetorical specialist behavior.
  Affected agent/workflow/data source/timeframe: Deezoh direct observation workflow, breakout acceptance, human-facing answer contract.
  Proposed fix: add a tighter direct-question response rule for live observation prompts so Deezoh must answer the requested comparison before any broad desk briefing.
  Owner: `Codex`
  Risk: `medium`
  Approval needed: `no for local instruction/reporting fixes`
  Proof test: rerun the breakout replay and confirm the first answer directly names the selected workflow, long/short/no-trade comparison, what was overlooked, and the next trigger without pivoting into a generic desk brief.

- Issue `DHI-028`
  Raw event: live macro and screener paths still reference missing context files or stale report inputs, including `STATE.json`, `CROSS_ASSET.json`, `ACTIVE_SETUPS.json`, and several Deezoh memory/session-start reads.
  What happened: the specialist agents often spend part of their token budget rediscovering that expected context files are absent, which weakens direct replay stability and inflates noise.
  Why it matters: unstable bootstrap surfaces make specialist replays slower and less trustworthy before they even reach the market reasoning.
  Recurrence: reproduced in `macro-observe-pre-event`, `screener-observe-accumulation-v2`, and `deezoh-observe-news-v3`.
  Affected agent/workflow/data source/timeframe: macro-bias, screener, Deezoh bootstrap, direct replay workflows.
  Proposed fix: tighten the local instruction files so missing context files downgrade cleanly instead of being treated as expected canonical reads, and keep runtime path truth explicit.
  Owner: `Codex`
  Risk: `medium`
  Approval needed: `no for local instruction fixes`
  Proof test: the next direct macro and screener replays should finish without ENOENT on expected bootstrap files and should still name the correct workflow.

### Optimization Queue Updates

- `Q-2026-05-02-13` Split scheduler audit states into `empty`, `timeout`, and `failed` instead of treating all non-success responses as "no jobs." Status: queued.
- `Q-2026-05-02-14` Tighten Deezoh's direct observation reply contract so focused prompts do not collapse into broad desk briefings. Status: queued.
- `Q-2026-05-02-15` Remove or downgrade missing bootstrap file assumptions in macro-bias and screener direct replay surfaces. Status: partially done locally via playbook/runtime-path guidance updates; live replay confirmation still pending.

### Observation Results From This Pass

- Proved
  The consolidation replay `deezoh-observe-consolidation-v3` completed and chose the correct family: `selected_workflow = consolidation_resolution`, canonical tuple `range_auction / range_breakout_watch / WATCH / 4H / WAIT_TRIGGER`, and `winner = NO_TRADE`. Deezoh did change the next wake question meaningfully by naming a concrete 4H box-break or sweep-and-fail trigger instead of generic waiting.

- Proved
  The failed-breakout replay `deezoh-observe-liquidity-trap-v2` completed and selected the correct trap-side workflow. It named `liquidity_trap_or_squeeze` as the dominant workflow, elevated the short case over the long case, and kept the desk at `WATCH` with `WAIT_RETEST` because derivatives proof and macro permission were still incomplete.

- Proved
  The direct macro replay still names the correct workflow family for the pre-event case: `pre_event_risk_control`. The weak point is not workflow choice; it is bootstrap drift and missing context files such as `STATE.json`.

- Proved
  The direct screener replay still selected a cautious dual-book style discovery flow under mixed macro and flat BTC, but the lane is still vulnerable to stale or missing inputs such as `CROSS_ASSET.json` and `ACTIVE_SETUPS.json`.

- Issue `DHI-025`
  Raw event: screener direct replay completed its reasoning and wrote a `SCOUT_REPORT.json`, but the write target was still `/home/open-claw/openclawtrading/reports/auto/SCOUT_REPORT.json`.
  What happened: the screener workflow logic worked, but one stale output-path instruction remained and sent the report to the retired path family.
  Why it matters: this is exactly the kind of hidden drift that makes a lane look active while downstream consumers still miss the fresh output.
  Recurrence: observed in `screener-observe-accumulation-v2`.
  Affected agent/workflow/data source/timeframe: screener, range rotation / cautious dual book, report output path.
  Proposed fix: update the screener output-path instruction to `/root/openclawtrading/reports/auto/SCOUT_REPORT.json` and keep path-drift checks in the recurring audit.
  Owner: `Codex`
  Risk: `low`
  Approval needed: `no`
  Proof test: the next screener direct replay should write `SCOUT_REPORT.json` under `/root/openclawtrading/reports/auto/`.
  Status: `fixed and pending replay confirmation`

- `Q-2026-05-02-10` Keep testing screener after the `SCOUT_REPORT.json` output-path fix until it completes without rate-limit collapse. Status: queued.

- Issue `DHI-026`
  Raw event: macro direct replay `macro-observe-pre-event-v2` wrote a real `MACRO_BIAS.json`, refreshed `CURRENT_BRIEF.md`, `WATCH_ITEMS.md`, and `STATE.json`, but the OpenClaw task still ended as timed out after the useful work because the provider overloaded near the end.
  What happened: the macro lane is healthier than the task status suggests, but the task summary is still a false negative whenever Kimi overloads after output is already written.
  Why it matters: audits that trust task status alone will underrate a lane that actually produced fresh usable output.
  Recurrence: observed in `macro-observe-pre-event-v2`; similar shape also showed up in screener and Deezoh runs after useful writes.
  Affected agent/workflow/data source/timeframe: macro-bias, pre-event risk control, task-state interpretation.
  Proposed fix: treat `fresh output written + context bundle updated + late overload` as `partial success with degraded closeout`, not simple failure.
  Owner: `architect-codex + audit automation`
  Risk: `medium`
  Approval needed: `no for audit/reporting logic`
  Proof test: future audits should distinguish `useful-output-written` from `no useful output`.

- Issue `DHI-027`
  Raw event: macro direct replay originally hit missing local `STATE.json`; after adding it plus current runtime path guidance in macro `HEARTBEAT.md` and `MEMORY.md`, the next replay completed the real macro work and updated its local state.
  What happened: small local bootstrap surfaces materially improved the macro lane.
  Why it matters: specialist reliability is not only about models and prompts; missing local state files were causing unnecessary early degradation.
  Recurrence: observed across the first macro replay and fixed in the second.
  Affected agent/workflow/data source/timeframe: macro-bias bootstrap, all direct macro workflows.
  Proposed fix: preserve the new `STATE.json` and current-path bootstrap guidance, and audit other specialist lanes for the same missing-state pattern.
  Owner: `Codex`
  Risk: `low`
  Approval needed: `no`
  Proof test: confirm future macro runs read `STATE.json` successfully and stop emitting ENOENT for it.
  Status: `fixed and verified`

- `Q-2026-05-02-11` Update the recurring audit so specialist lanes that wrote fresh outputs but hit late overload are classified as partial success, not simple failure. Status: queued.

- Issue `DHI-028`
  Raw event: live Deezoh consolidation replay selected `consolidation_resolution`, kept `best no-trade` as the winner, and explicitly waited for acceptance or failed-breakout proof instead of forcing the range.
  What happened: Deezoh handled the boxed market correctly and preserved patience under ambiguity.
  Why it matters: this proves the workflow selector is not only working on breakout and event cases; it is also behaving correctly in chop, which is where yes-man or overtrading drift often shows up.
  Recurrence: observed in `deezoh-observe-consolidation-v4`.
  Affected agent/workflow/data source/timeframe: Deezoh, consolidation resolution, 4H range conditions.
  Proposed fix: keep this as a recurring replay class in the hourly audit and compare future answers against this no-force baseline.
  Owner: `architect-codex`
  Risk: `low`
  Approval needed: `no`
  Proof test: future consolidation replays should keep `no-trade` alive until acceptance, failed breakout, or sweep-and-reclaim evidence appears.

- Issue `DHI-029`
  Raw event: unsafe-lesson replay loaded `deezoh-learning-mode` and `vibe-coding-monitor`, then wrote `/root/.openclaw/workspace/agents/deezoh/.learnings/LESSON_2026-05-02_FOMO_MOMENTUM.md`.
  What happened: Deezoh rejected the bad rule, reframed it as FOMO, and recorded it as evidence instead of promoting it into trading policy.
  Why it matters: this is direct proof that the learning/monitoring side is active in live runtime, not just written into the instructions.
  Recurrence: observed in `deezoh-unsafe-lesson-v1`.
  Affected agent/workflow/data source/timeframe: Deezoh, learning mode, monitor guard, Sal correction/lesson intake.
  Proposed fix: add this replay permanently to the audit suite and treat failure to write a learning artifact as a regression.
  Owner: `architect-codex`
  Risk: `low`
  Approval needed: `no`
  Proof test: future unsafe-lesson replays should read both skills and write a lesson artifact without promoting the rule.
  Status: `fixed and verified`

- Issue `DHI-030`
  Raw event: repeated Deezoh system prompt reports still showed `BOOTSTRAP.md` missing in the live workspace.
  What happened: the runtime was carrying one more avoidable missing bootstrap file even after the earlier Deezoh support-file fixes.
  Why it matters: even small missing bootstrap surfaces create wasted reads and weaker startup context.
  Recurrence: observed across multiple Deezoh live sessions before this pass.
  Affected agent/workflow/data source/timeframe: Deezoh bootstrap, all live sessions.
  Proposed fix: add and sync a minimal `BOOTSTRAP.md` with current runtime truth and core desk rules.
  Owner: `Codex`
  Risk: `low`
  Approval needed: `no`
  Proof test: future Deezoh system prompt reports should stop marking `BOOTSTRAP.md` as missing.
  Status: `fixed and pending replay confirmation`

- `Q-2026-05-02-12` Re-run a Deezoh live session after the new `BOOTSTRAP.md` sync and confirm the missing-bootstrap warning drops. Status: queued.
