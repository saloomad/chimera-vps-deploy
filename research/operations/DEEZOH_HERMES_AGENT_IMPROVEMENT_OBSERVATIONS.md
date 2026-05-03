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

## 2026-05-03 Audit Additions

### New Evidence From This Run

- Issue `DHI-029`
  Raw event: live SSH to `root@100.67.172.114` succeeded again, the agent workspace inventory loaded, root cron was readable, and live report/log reads completed in the same pass.
  What happened: the previous "SSH stalled" blocker is no longer the active issue, so the loop can return to live runtime proof instead of local-only inference.
  Why it matters: the improvement loop can stop treating SSH reachability as the main blocker and focus on real report-contract and data-quality problems.
  Recurrence: cleared on 2026-05-03 during this pass.
  Affected agent/workflow/data source/timeframe: live OpenClaw audit path, Deezoh/Hermes verification loop.
  Proposed fix: close the old SSH-stall narrative in future handoffs unless the direct `ssh.exe` path fails again.
  Owner: `architect-codex`
  Risk: `low`
  Approval needed: `no`
  Proof test: rerun direct `ssh.exe` checks for reports, logs, and root cron in the same pass.
  Status: `resolved this run`

- Issue `DHI-030`
  Raw event: live `MACRO_BIAS.json` now says `verdict=MIXED`, `selected_workflow=data_degraded_mode`, and `action_recommendation=WAIT`, while the fresh live `ENTRY_SIGNALS.json` still says `effective_entry_state=READY_TO_TRADE`, `recommendation=READY`, and `macro_veto_active=false`.
  What happened: the report contract exposes the macro fields, but data-degraded macro mode still does not downgrade execution readiness unless the verdict is a hard veto like `STAY OUT`.
  Why it matters: the desk can sound execution-ready while key upstream sources are stale or empty, which is a real trading-policy and risk-boundary issue rather than a cosmetic label problem.
  Recurrence: reproduced live on 2026-05-03 after the latest desk rebuild.
  Affected agent/workflow/data source/timeframe: entry-watch, desk contract bridge, macro gate, paper execution lane.
  Proposed fix: decide whether `data_degraded_mode` should force `WAIT` or a separate degraded gate state before changing live behavior.
  Owner: `Sal approval + architect-codex + entry-watch`
  Risk: `high`
  Approval needed: `yes before live policy/execution change`
  Proof test: after approval, rebuild `ENTRY_SIGNALS.json` under a degraded macro scenario and confirm `effective_entry_state` no longer stays `READY_TO_TRADE`.

- Issue `DHI-031`
  Raw event: deterministic screener audits showed `infer_screener_workflow()` labeling broad-hunt and continuation cases as `range_rotation`, and a generic `rotation` phrase in catalyst text could mislabel ordinary range tape as `post_news_rotation`.
  What happened: the screener workflow classifier was too eager to jump into range/post-news labels even when the contract should stay on `accumulation_hunt` or `continuation`.
  Why it matters: this weakens workflow audits and makes Deezoh/Hermes consume noisier screener context than the desk actually intends.
  Recurrence: reproduced locally on 2026-05-03 with deterministic scenario cases.
  Affected agent/workflow/data source/timeframe: screener workflow selection, accumulation, continuation, range rotation, post-news rotation.
  Proposed fix: tighten the classifier so continuation wins when the book is clearly imbalanced, range rotation only wins when both sides are genuinely balanced or the mode is explicitly dual-book, and post-news rotation requires stronger event wording.
  Owner: `Codex`
  Risk: `low`
  Approval needed: `no`
  Proof test: `scripts/tests/workflow_contract_surfaces_smoke.py` plus targeted case replays for accumulation, continuation, range rotation, and post-news rotation.
  Status: `fixed locally, synced live to /root/openclawtrading/scripts/build_scout_report.py, and verified`

- Issue `DHI-032`
  Raw event: deterministic macro workflow audits showed a high-impact `STAY OUT` scenario with a near-term next event still resolving to `pre_event_control` before `post_event_digest` can ever win.
  What happened: the current macro workflow order makes `post_event_digest` effectively unreachable in some realistic event-digest cases because near-event checks fire first.
  Why it matters: macro workflow audits can overstate pre-event control and under-report genuine post-event digestion, which weakens both macro replay coverage and Deezoh's event-context explanation.
  Recurrence: reproduced locally on 2026-05-03 with deterministic audit inputs.
  Affected agent/workflow/data source/timeframe: macro workflow selection, pre-event control, post-event digest.
  Proposed fix: add a clearer event-phase signal or a safer precedence rule before changing live macro labeling.
  Owner: `architect-codex + macro-bias`
  Risk: `medium`
  Approval needed: `review before live heuristic change`
  Proof test: a deterministic macro case with high-impact post-event digestion should resolve to `post_event_digest` without breaking pre-event control cases.

### This Run's Observation Suite

- Deezoh direct observation smoke re-ran locally across the required chart-style families:
  - breakout -> `selected_workflow=breakout_acceptance`, `winner=short`, `wait=WAIT_ACCEPTANCE`
  - consolidation -> `selected_workflow=consolidation_resolution`, `winner=short`, `wait=NONE`
  - news event -> `selected_workflow=news_event_control`, `winner=no_trade`, `wait=WAIT_ACCEPTANCE`
  - failed breakout / liquidity trap -> `selected_workflow=liquidity_trap`, `winner=no_trade`, `wait=WAIT_SWEEP`
- The answer contract still changes the next question and wait state by scenario, which is the right behavior shape.
- The specialist interaction proof is still mostly planning-grade rather than execution-grade in this deterministic lane: the next-question payload names specialist branches and expected outputs, but not real spawned sub-sessions. Treat that as reaffirmed support for existing issue `DHI-018`, not as fresh delegation proof.

### Live Runtime Proof Snapshot

- Live report freshness on 2026-05-03 showed:
  - `DEEZOH_THOUGHTS.json`, `SCOUT_REPORT.json`, and `ENTRY_SIGNALS.json` updating within about 16 minutes
  - `MACRO_BIAS.json` and `DERIVATIVES.json` updating within about 21 minutes
  - `HERMES_DECISION_TRACE.json` aging to about 92 minutes
  - `NEWS.json` and `CATALYST_REPORT.json` still stale at roughly 343 minutes
- Live root cron remains the active scheduler:
  - `market_scanner.py`, `candle_analyzer.py`, `derivatives_fetcher.py`, and `macro_bias_builder.py` every 30 minutes
  - `watchlist_generator.py` hourly
  - desk observability chain at `5,35 * * * *`
- Live logs still show the same weak-input pattern:
  - `derivatives.log`: repeated `DERIVATIVES.json written: 0 coins`
  - `watchlist.log`: monitor-only `0%` candidates
  - `macro_bias.log`: `MIXED 30%` with placeholder derivatives context

### Optimization Queue Updates

- `Q-2026-05-03-01` Tighten screener workflow inference so accumulation and continuation are not relabeled as range/post-news by default. Status: done locally, synced to live repo, and covered by smoke tests.
- `Q-2026-05-03-02` Decide whether `data_degraded_mode` must downgrade `ENTRY_SIGNALS.json` readiness. Status: queued for approval because it crosses the trading-policy/risk boundary.
- `Q-2026-05-03-03` Add a cleaner macro event-phase signal so `post_event_digest` can be selected without breaking pre-event control. Status: queued for design review.
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

## 2026-05-02 Direct-Answer And Hermes Path Audit

### What Actually Ran

- Live OpenClaw re-check on `root@100.67.172.114`:
  - verified `/root/.openclaw/workspace/agents/`
  - verified `/root/openclawtrading/reports/auto/`
  - verified root `crontab -l`
  - re-tested `openclaw cron list` and `openclaw tasks flow list` under timeout
- Fresh live Deezoh observation suite:
  - `deezoh-observe-breakout-v4`
  - same-session breakout follow-up in `deezoh-observe-breakout-v4`
  - `deezoh-observe-consolidation-v4`
  - `deezoh-observe-news-v4`
  - `deezoh-observe-liquidity-trap-v3`
- Fresh live workflow audits:
  - `screener-workflow-audit-v1`
  - `macro-workflow-audit-v2`
- Live bounded Hermes inspection:
  - read `run_hermes_lead.sh`
  - read `run_hermes_pm_heartbeat.sh`
  - checked expected Hermes reports and `cron.log`

### New Evidence From This Run

- Proved
  The Deezoh direct-answer patch worked. `deezoh-observe-breakout-v4` no longer opened with a broad morning briefing. It answered the requested comparison first, then explained the block.

- Proved
  Same-session breakout follow-up changed Deezoh's state handling: the winner stayed `NO_TRADE`, but the wait moved from `WAIT_COOLDOWN` to `WAIT_ACCEPTANCE`, and the next question narrowed to 1H timing instead of a generic desk recap.

- Proved
  `screener-workflow-audit-v1` now picks the intended workflow family cleanly across the six requested discovery situations:
  - quiet builders -> `accumulation_hunt`
  - accepted trend -> `trend_continuation_hunt`
  - second-order rotation -> `post_news_rotation_hunt`
  - failed acceptance -> `failed_breakout_short_hunt`
  - balanced range -> `range_rotation_hunt`
  - degraded or distorted tape -> `no_trade_protection`

- Proved
  `macro-workflow-audit-v2` now picks the intended workflow family cleanly across the requested macro situations:
  - pre-release control -> `pre_event_risk_control`
  - post-release reaction -> `post_event_digest`
  - cross-market divergence -> `cross_asset_divergence`
  - broken-playbook capture -> `unusual_behavior_precedent`
  - thin or stale inputs -> `data_degraded_macro`

- Issue `DHI-029`
  Raw event: `deezoh-observe-breakout-v4` answered in the improved direct format, but still labeled the dominant workflow `news_event_control` instead of a structure-first breakout workflow.
  What happened: the answer contract improved, but the workflow selector still lets stale macro vetoes overwrite the setup-family label itself.
  Why it matters: Deezoh can now speak more clearly while still classifying the setup incorrectly, which weakens replay truth and makes it harder to compare breakout behavior across runs.
  Recurrence: observed in `deezoh-observe-breakout-v4` on 2026-05-02 after the direct-answer patch.
  Affected agent/workflow/data source/timeframe: Deezoh, breakout observation workflow, workflow selector, 4H/15M breakout review.
  Proposed fix: keep `selected_workflow` structure-first (`breakout_acceptance` here), and let macro/event pressure decide `winner`, `typed_wait`, or veto status separately.
  Owner: `Codex`
  Risk: `medium`
  Approval needed: `no for instruction or replay-contract fixes`
  Proof test: rerun the breakout scenario and confirm `selected_workflow = breakout_acceptance` while `winner` may still remain `NO_TRADE`.

- Issue `DHI-030`
  Raw event: `deezoh-observe-consolidation-v4` still attempted `kimi_finance` with `BTCUSDT`, hit stock-style ticker errors, then fell back to search/report reading.
  What happened: the crypto price-routing bug is still active in direct observation mode.
  Why it matters: even when Deezoh answers eventually, it wastes time on the wrong finance lane and pollutes the replay with irrelevant tool failures.
  Recurrence: reproduced in `deezoh-observe-consolidation-v4` on 2026-05-02.
  Affected agent/workflow/data source/timeframe: Deezoh, consolidation observation workflow, crypto quote routing.
  Proposed fix: explicitly forbid stock-style generic finance routing for crypto symbols and prefer fresh report, Bitget, or TradingView-derived lanes first.
  Owner: `Codex + data-source router`
  Risk: `medium`
  Approval needed: `no for routing preference and prompt-surface fixes`
  Proof test: the next BTC or ETH observation replay should not call `kimi_finance` with `BTCUSDT`, `ETHUSDT`, or stock-shaped fallback symbols.

- Issue `DHI-031`
  Raw event: `deezoh-observe-news-v4` answered honestly from stale files only, spawned no specialists, and explicitly depended on 8-9 hour old reports with empty derivatives.
  What happened: the news-event lane is still better at admitting degraded truth than at recovering from it.
  Why it matters: this is safer than hallucinating freshness, but it still means live event-mode guidance remains too weak for real chart-side use unless a fresh headline or fresher inputs are provided.
  Recurrence: observed in `deezoh-observe-news-v4` on 2026-05-02.
  Affected agent/workflow/data source/timeframe: Deezoh, news-event control, live event digest, freshness handling.
  Proposed fix: for direct news-event prompts, require the current headline or symbol in the first question and prefer a fresh price/report refresh before ranking long vs short.
  Owner: `Codex`
  Risk: `low`
  Approval needed: `no`
  Proof test: future news-event replays should either fetch a fresh lane or explicitly ask for the missing live headline before ranking setups.

- Issue `DHI-032`
  Raw event: live Hermes runner files under `/root/.openclaw/workspace/agents/hermes-lead/` still hardcode `/home/open-claw/openclawtrading`, while `/root/openclawtrading/reports/auto/HERMES_LANE_THESIS.json`, `HERMES_ADVISOR_REVIEW.json`, `HERMES_RUNTIME_INPUT.json`, and `cron.log` were all missing on the current VPS truth path.
  What happened: Hermes artifacts are not currently wired to the active `/root/...` runtime, and Hermes is absent from the current root cron proof.
  Why it matters: Hermes exists as files, but on this VPS it is not proven active, current, or path-correct. This is exactly the `exists` versus `wired` versus `used` gap the loop is supposed to catch.
  Recurrence: observed in the live bounded Hermes inspection on 2026-05-02.
  Affected agent/workflow/data source/timeframe: Hermes lead, PM heartbeat, runtime bridge outputs, VPS path truth.
  Proposed fix: audit Hermes end-to-end on the `/root/...` runtime before any re-enable attempt: update path constants, run `bash -n`, then do one bounded manual Hermes refresh and confirm fresh reports under `/root/openclawtrading/reports/auto/`.
  Owner: `architect-codex + Hermes Lead`
  Risk: `medium`
  Approval needed: `review before any live Hermes cron re-enable or policy change`
  Proof test: Hermes scripts should point at `/root/openclawtrading`, a bounded manual run should finish, and fresh Hermes reports should appear under the current `/root/...` report root.

### Safe Changes Applied This Run

- Local and live Deezoh direct-answer contract tightened in:
  - `agents/deezoh/QUESTION_ENGINE.md`
- Local and live macro bundle-grace behavior tightened in:
  - `agents/macro-bias/AGENTS.md`
- Local and live screener workflow-grace and selector guidance tightened in:
  - `agents/screener/WORKFLOW.md`

### Optimization Queue Updates

- `Q-2026-05-02-16` Keep the direct-answer contract, but separate workflow labeling from macro veto logic in Deezoh. Status: queued.
- `Q-2026-05-02-17` Remove stock-style generic finance calls from crypto observation workflows. Status: queued.
- `Q-2026-05-02-18` Require fresh headline or symbol capture before Deezoh ranks live news-event scenarios. Status: queued.
- `Q-2026-05-02-19` Audit Hermes against `/root/...` truth and prove whether it is active, inactive, or only staged. Status: queued.

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

## 2026-05-02 SSH-Stalled Continuation Pass

### What Actually Ran

- Re-read the current bootstrap, runtime-router, orchestration loop, automation memory hints, and latest same-day handoff.
- Re-inspected the local Deezoh instruction surfaces and local Hermes runner mirrors under `C:\Users\becke\claudecowork`.
- Verified network reachability to the current VPS target with Windows `Test-NetConnection`.
- Attempted multiple bounded `ssh.exe` probes to `root@100.67.172.114` for scheduler truth, report freshness, session inventory, Hermes runner reads, and log tails.

### New Evidence From This Run

- Issue `DHI-SSH-2026-05-02`
  Raw event: `Test-NetConnection 100.67.172.114 -Port 22` returned `TcpTestSucceeded = True`, but every bounded `ssh.exe` probe to `root@100.67.172.114` stalled until the local timeout without returning command output.
  What happened: the host is reachable at the TCP layer, but this pass could not obtain a usable remote shell or remote command output.
  Why it matters: live OpenClaw truth could not be freshly re-verified, so this pass cannot honestly claim new live Deezoh/Hermes behavior proof or live sync completion.
  Recurrence: reproduced across multiple command shapes on 2026-05-02, including explicit key-based `BatchMode` probes.
  Affected agent/workflow/data source/timeframe: live VPS verification, Deezoh observation suite, Hermes path audit, root-cron truth, report freshness.
  Proposed fix: resolve the current SSH stall or auth/startup-shell hang first, then rerun the blocked live observation suite before judging the local fixes as verified.
  Owner: `system-access + architect-codex`
  Risk: `medium`
  Approval needed: `no for connectivity diagnosis; review before changing live access or shell startup policy`
  Proof test: a bounded `ssh.exe root@100.67.172.114 "echo ok"` must return output within the timeout, then the normal live probes can resume.

- Proved
  The local Deezoh contract still needed a stronger separation between workflow naming and macro veto logic, so this pass tightened `QUESTION_ENGINE.md` to keep `selected_workflow` structure-first and to keep crypto quote routing away from stock-style generic finance surfaces.

- Proved
  The local Hermes runner mirrors were still hardcoded to retired `/home/open-claw/...` paths. This pass updated the local `run_hermes_lead.sh` and `run_hermes_pm_heartbeat.sh` mirrors to `/root/...` truth so the next live sync can use current path defaults.

### Safe Changes Applied This Run

- Local Deezoh instruction update in:
  - `agents/deezoh/QUESTION_ENGINE.md`
- Local Hermes path-truth updates in:
  - `agents/hermes-lead/run_hermes_lead.sh`
  - `agents/hermes-lead/run_hermes_pm_heartbeat.sh`

### Optimization Queue Updates

- `Q-2026-05-02-20` Restore bounded SSH command execution to `root@100.67.172.114` before the next Deezoh/Hermes live improvement pass. Status: queued.
- `Q-2026-05-02-21` After SSH is healthy again, live-sync the repaired local Hermes runner mirrors and prove fresh Hermes outputs under `/root/openclawtrading/reports/auto/`. Status: queued.

## 2026-05-02 Local Path-Truth Repair Pass

### What Actually Ran

- Re-read the current bootstrap, runtime router, automation memory, and latest same-day handoff.
- Re-checked Windows-to-VPS reachability with `Test-NetConnection 100.67.172.114 -Port 22`.
- Re-attempted bounded `ssh.exe` probes to `root@100.67.172.114`, which still stalled until timeout and returned no remote command output.
- Inspected active local Deezoh/Hermes runner and orchestrator scripts under `scripts/`.
- Ran bounded local verification:
  - `python scripts/simulator/test_deezoh_question_engine.py`
  - `python scripts/simulator/test_deezoh_council_runtime_visibility.py`
  - `python scripts/tests/hermes_dual_lane_contract_smoke.py`
  - `python scripts/tests/hermes_learning_store_smoke.py`
  - `python -m py_compile` on the touched runner/orchestrator files

### New Evidence From This Run

- Issue `DHI-033`
  Raw event: active local runner and orchestrator files still defaulted to retired `/home/open-claw/...` roots, including `scripts/runtime_paths.py`, `scripts/hermes_runtime_bridge.py`, `scripts/hermes_progress_status.py`, `scripts/build_dual_lane_experiment.py`, `scripts/build_trade_judge_cycle.py`, `scripts/deezoh_round_orchestrator.py`, `scripts/deezoh_orchestrator.py`, and `scripts/simulator/tradingview_style_replay.py`.
  What happened: the current local mirrors had drifted behind the already-proven VPS path truth and would have misled the next live sync or bounded manual replay.
  Why it matters: this is a real `truth surface` regression. Even if the live VPS is correct, stale local defaults create bad handoffs, false negatives, and unnecessary `/home/open-claw` fallbacks in the next pass.
  Recurrence: observed in the local active script set on 2026-05-02.
  Affected agent/workflow/data source/timeframe: Deezoh orchestrator, Hermes runtime bridge, Hermes progress/judge lane, strategy replay, runtime path helper.
  Proposed fix: keep `/root/openclawtrading` and `/root/.openclaw` as the primary defaults in active scripts, leave only explicit legacy compatibility where it is deliberate, and verify with `py_compile` plus local smoke tests before any live sync.
  Owner: `Codex`
  Risk: `medium`
  Approval needed: `no for local runner/path fixes`
  Proof test: the touched files should compile cleanly, the Deezoh/Hermes smokes should pass, and no active default should still point at `/home/open-claw/...` except an intentional legacy fallback line.

- Proved
  The local Deezoh and Hermes path-truth repair did not break the current bounded test harnesses. All four local smokes passed after the path-default changes, and the touched files compiled cleanly.

- Proved
  The live blocker is still access, not market logic. `Test-NetConnection` still shows TCP/22 reachable on the Tailscale path, but bounded `ssh.exe` command probes still hang and return no usable shell output.

### Safe Changes Applied This Run

- Local path-truth repairs in:
  - `scripts/runtime_paths.py`
  - `scripts/hermes_runtime_bridge.py`
  - `scripts/hermes_progress_status.py`
  - `scripts/build_dual_lane_experiment.py`
  - `scripts/build_trade_judge_cycle.py`
  - `scripts/deezoh_round_orchestrator.py`
  - `scripts/deezoh_orchestrator.py`
  - `scripts/simulator/tradingview_style_replay.py`

### Optimization Queue Updates

- `Q-2026-05-02-22` Recover usable SSH command execution to the Kimi VPS so the blocked live observation suite and Hermes proof can resume. Status: queued.
- `Q-2026-05-02-23` After SSH recovery, live-sync the repaired local script defaults and prove Hermes/Deezoh artifacts write under `/root/openclawtrading/reports/auto/`. Status: queued.

## 2026-05-02 Scenario Harness Path-Truth Pass

### What Actually Ran

- Re-checked bounded SSH access with `Test-NetConnection 100.67.172.114 -Port 22` and another timed `ssh.exe` probe; TCP/22 stayed reachable but the remote command still hung until timeout.
- Inspected the local simulator and replay harnesses under `scripts/simulator/`.
- Repaired the retired `/home/open-claw/openclawtrading` default in `scripts/simulator/agent_scenario_tester.py`.
- Ran bounded local verification:
  - `python -m py_compile scripts/simulator/agent_scenario_tester.py`
  - `python scripts/simulator/agent_scenario_tester.py --capture-current deezoh-hermes-local-pass-2026-05-02 --description "Local bounded snapshot after scenario harness path-truth fix"`
  - `python scripts/simulator/agent_scenario_tester.py --snapshot deezoh-hermes-local-pass-2026-05-02`
  - `python scripts/simulator/test_deezoh_question_engine.py`
  - `python scripts/simulator/test_deezoh_council_runtime_visibility.py`
  - `python scripts/tests/hermes_dual_lane_contract_smoke.py`
  - `python scripts/tests/hermes_learning_store_smoke.py`

### New Evidence From This Run

- Issue `DHI-034`
  Raw event: `scripts/simulator/agent_scenario_tester.py` still hardcoded `BASE = Path('/home/open-claw/openclawtrading')` even after the rest of the active local Deezoh/Hermes runner layer had been moved to current `/root/...` truth.
  What happened: the local scenario harness had drifted behind the newer path-truth repairs, so bounded snapshot capture and snapshot replay depended on a retired Linux root by default.
  Why it matters: this harness is part of the safe replay surface for Deezoh/Hermes quality checks. Leaving it on the old root would keep producing false negatives or force the next agent to rediscover the same path bug before running local scenario audits.
  Recurrence: observed in the current Windows workspace on 2026-05-02.
  Affected agent/workflow/data source/timeframe: local Deezoh/Hermes scenario harness, snapshot capture, snapshot replay, simulator path truth.
  Proposed fix: resolve `CHIMERA_BASE_DIR` first, otherwise prefer the current workspace root, then `/root/openclawtrading`, and only keep `/home/open-claw/openclawtrading` as an explicit legacy fallback.
  Owner: `Codex`
  Risk: `low`
  Approval needed: `no for local harness/path fixes`
  Proof test: `agent_scenario_tester.py --capture-current ...` and `--snapshot ...` should both run from the current workspace without needing the retired Linux root.

- Proved
  The repaired scenario harness now captures and replays snapshots from the current workspace successfully. It wrote a new snapshot under `scripts/simulator/snapshots/deezoh-hermes-local-pass-2026-05-02` and produced `reports/auto/SCENARIO_TEST_REPORT.json` plus `SCENARIO_TEST_REPORT.md`.

- Proved
  The captured local snapshot fail-closed to `PAUSE` instead of pretending the desk was tradable. The report marked core files like `CATALYST_REPORT.json`, `MACRO_BIAS.json`, `SCOUT_REPORT.json`, `CHART_ANALYSIS.json`, `INDICATOR_REPORT.json`, and `STRATEGY_REPORT.json` as missing and kept execution skipped.

- Proved
  The broader bounded verification set still passed after the harness repair: Deezoh question-engine tests passed `16/16`, runtime council visibility passed, and both Hermes smoke tests passed.

### Safe Changes Applied This Run

- Local simulator path-truth repair in:
  - `scripts/simulator/agent_scenario_tester.py`

### Optimization Queue Updates

- `Q-2026-05-02-24` Keep the simulator and replay harness set aligned to current `/root/openclawtrading` truth whenever runner-path repairs land elsewhere first. Status: queued.

## 2026-05-02 Tailscale SSH Daily Prompt Fix

### What Actually Ran

- Re-tested live SSH access to `root@100.67.172.114`.
- Captured the behavior difference between the earlier stalled Tailscale SSH path and the current recovered session.
- Inspected the live VPS SSH stack:
  - `systemctl is-active ssh`
  - `systemctl is-enabled ssh`
  - `sshd -T`
  - `/root/.ssh/authorized_keys`
  - `ss -ltnp`
- Enabled normal `sshd` permanently with `systemctl enable ssh`.
- Disabled Tailscale SSH on the VPS with `tailscale set --ssh=false --accept-risk=lose-ssh`.
- Re-verified non-intercepted SSH command execution from Windows to the VPS after the cutover.

### New Evidence From This Run

- Issue `DHI-035`
  Raw event: earlier SSH debug showed the remote software version as `Tailscale` and required a browser-based extra check; later debug after the fix authenticated with `publickey` and learned standard OpenSSH host keys instead.
  What happened: the daily access friction was caused by Tailscale SSH intercepting port `22` on the Tailscale IP and applying check-mode approval, not by broken Tailscale connectivity or a dead VPS.
  Why it matters: this was the real root cause behind the recurring daily browser approval that blocked non-interactive Codex automation.
  Recurrence: reproduced and then resolved on 2026-05-02.
  Affected agent/workflow/data source/timeframe: all live Codex-to-VPS automation, Deezoh/Hermes live verification, remote command execution.
  Proposed fix: keep standard `sshd` enabled on the VPS and keep Tailscale SSH disabled for this node so SSH runs over the Tailscale network without the extra Tailscale SSH approval layer.
  Owner: `Codex`
  Risk: `low`
  Approval needed: `no`
  Proof test: `ssh root@100.67.172.114 "echo post_disable_ok"` should authenticate with `publickey` and complete without the Tailscale SSH browser check.
  Status: `fixed and verified`

- Proved
  Normal `sshd` was already healthy on the VPS, but it was not enabled at boot. This pass enabled it permanently so a reboot should not silently re-break the non-Tailscale SSH fallback.

- Proved
  The root authorized key for this Windows machine was already present on the VPS, so the cutover away from Tailscale SSH did not need any risky auth rewiring first.

### Safe Changes Applied This Run

- Live VPS:
  - enabled standard SSH service at boot with `systemctl enable ssh`
  - disabled Tailscale SSH with `tailscale set --ssh=false --accept-risk=lose-ssh`

### Optimization Queue Updates

- `Q-2026-05-02-25` If SSH approval friction returns, check whether Tailscale SSH was re-enabled on the VPS before touching Deezoh/Hermes again. Status: queued.

## 2026-05-02 Chimera Desk Observability Audit

### What Actually Ran

- Re-verified live SSH command execution to `root@100.67.172.114`.
- Ran `openclaw cron list`, `openclaw tasks flow list`, and root `crontab -l` in the same pass.
- Verified that the active root crontab entries point at current `/root/openclawtrading/...` paths and that the referenced paths exist.
- Audited report freshness under `/root/openclawtrading/reports/auto/`.
- Audited Deezoh and Hermes trace surfaces under `/root/.openclaw/workspace/agents/`.
- Audited live log freshness and error signatures under `/root/.openclaw/logs/`.
- Checked whether review and critic surfaces exist and whether they are current enough to debug today's desk cycle.

### New Evidence From This Run

- Issue `DHI-036`
  Raw event: collector files like `CANDLES.json`, `MACRO_BIAS.json`, `WATCHLISTS.json`, and `OPPORTUNITIES.json` refreshed within minutes, while `DEEZOH_THOUGHTS.json`, `DEEZOH_THOUGHTS_LIVE.json`, `SCOUT_REPORT.json`, and `CATALYST_REPORT.json` were still about 13 to 15 hours old.
  What happened: the live desk is collecting fresh inputs faster than it is refreshing its visible reasoning trail.
  Why it matters: a human or audit loop can falsely read the desk as current because the raw inputs are fresh even when the actual decision narrative is stale.
  Recurrence: observed in the live audit on 2026-05-02.
  Affected agent/workflow/data source/timeframe: Deezoh, scout, catalyst, desk operator trust, same-cycle observability.
  Proposed fix: tie one bounded desk trace bundle to the recurring collector cycle so Deezoh thought, scout, catalyst, and operator surfaces either refresh together or degrade together.
  Owner: `architect-codex`
  Risk: `high`
  Approval needed: `review before broad recurring loop rewiring`
  Proof test: one bounded live cycle should show collector outputs and the desk trace bundle refreshing in the same cycle window.

- Issue `DHI-037`
  Raw event: live review and critic surfaces such as `REASONING_AUDIT_LATEST.md`, `critic-findings-*`, `reviewer-findings-*`, `review-log.md`, and the monitor review exports were present but around 145 hours old.
  What happened: the review layer currently exists mostly as stale archive material instead of a live debug surface for today's desk state.
  Why it matters: when the desk behaves oddly, there is no current-cycle critic or reviewer trail to explain whether the reasoning actually degraded or only the raw inputs did.
  Recurrence: observed in the live audit on 2026-05-02.
  Affected agent/workflow/data source/timeframe: review freshness, critic freshness, human debug path, operator trust.
  Proposed fix: either wire one current-cycle review artifact into the recurring desk loop or retire the stale review surfaces from any user-facing trust claims.
  Owner: `architect-codex + cron-manager`
  Risk: `medium`
  Approval needed: `review before changing recurring review policy`
  Proof test: the next bounded desk cycle should either write one fresh review artifact or clearly mark review as unavailable.

- Issue `DHI-038`
  Raw event: `candle_analyzer.log` still shows repeated fetch and data errors for stock-style symbols like `MSFTUSDT`, `NVDAUSDT`, `TSLAUSDT`, `AMZNUSDT`, and `XAGUSDT`, while `DERIVATIVES.json` refreshed with empty `coins` and `market` payloads.
  What happened: at least two upstream collector lanes are producing fresh files but degraded analytical value.
  Why it matters: timestamp freshness alone is currently enough to make weak candle and derivatives lanes look healthy, which can contaminate Deezoh, watchlist, and macro confidence.
  Recurrence: observed in the live audit on 2026-05-02.
  Affected agent/workflow/data source/timeframe: candle lane, derivatives lane, watchlist confidence, macro confidence, same-cycle desk observability.
  Proposed fix: remove unsupported stock-style `*USDT` names from the active candle universe and add an explicit low-confidence downgrade whenever derivatives refresh with empty payloads.
  Owner: `codex + pipeline-watchdog`
  Risk: `medium`
  Approval needed: `no for bounded input-scope and downgrade repairs`
  Proof test: a fresh candle cycle should stop logging those unsupported symbols, and a fresh derivatives cycle should either produce non-empty payloads or visibly downgrade downstream confidence.

- Proved
  Active recurrence on the current VPS still comes from Linux root cron, not OpenClaw-native cron or Task Flow. `openclaw cron list` returned `No cron jobs.`, `openclaw tasks flow list` returned `TaskFlows: 0`, and root `crontab -l` carried the current market scripts.

- Proved
  The active root crontab entries now point at current `/root/openclawtrading/...` paths and the referenced script/log paths exist. This audit did not find active crontab entries still pointing at retired `/home/open-claw/...` roots.

- Proved
  Hermes is still not visible as a fresh live desk lane under the current report root. The current desk audit found runner files in the Hermes workspace, but no fresh Hermes runtime artifacts under `/root/openclawtrading/reports/auto/`.

### Optimization Queue Updates

- `Q-2026-05-02-26` Build one same-cycle desk trace bundle so collector freshness cannot be mistaken for fresh Deezoh reasoning. Status: queued.
- `Q-2026-05-02-27` Reintroduce one live current-cycle review artifact or retire stale review surfaces from trust claims. Status: queued.
- `Q-2026-05-02-28` Remove unsupported stock-style `*USDT` symbols from the active candle universe and make empty derivatives payloads degrade downstream confidence visibly. Status: queued.

## 2026-05-02 Hermes Live Sync And Runtime Gap Pass

### What Actually Ran

- Re-verified bounded SSH command execution to `root@100.67.172.114`.
- Re-read the latest Deezoh/Hermes handoffs, live report inventory, root cron truth, and current Hermes runner state under `/root/.openclaw/workspace/agents/hermes-lead/`.
- Re-ran bounded local verification:
  - `python scripts/simulator/test_deezoh_question_engine.py`
  - `python scripts/simulator/test_deezoh_council_runtime_visibility.py`
  - `python scripts/tests/hermes_dual_lane_contract_smoke.py`
  - `python scripts/tests/hermes_learning_store_smoke.py`
- Live-synced the already-repaired local Hermes runner scripts into:
  - `/root/.openclaw/workspace/agents/hermes-lead/run_hermes_lead.sh`
  - `/root/.openclaw/workspace/agents/hermes-lead/run_hermes_pm_heartbeat.sh`
- Fixed the first live sync failure by republishing those files with clean Unix `LF` endings.
- Verified both live Hermes runner scripts with `bash -n`.
- Ran one bounded live manual Hermes refresh:
  - `timeout 120s bash /root/.openclaw/workspace/agents/hermes-lead/run_hermes_lead.sh`
- Re-checked the current derivatives payload at `/root/openclawtrading/reports/auto/DERIVATIVES.json`.

### New Evidence From This Run

- Issue `DHI-039`
  Raw event: after the live Hermes runner scripts were republished to current `/root/...` path truth and passed `bash -n`, a bounded manual Hermes lead run exited with `2` and logged `python3: can't open file '/root/openclawtrading/scripts/hermes_runtime_bridge.py': [Errno 2] No such file or directory`.
  What happened: Hermes advanced past the old path bug and immediately exposed the next real live blocker: the current VPS repo does not contain the runtime bridge script the runner depends on.
  Why it matters: Hermes is still not honestly `wired` on the current VPS. The problem is no longer just stale `/home/open-claw/...` paths; at least one required runtime script is absent from `/root/openclawtrading/scripts`, so a one-off manual refresh cannot complete.
  Recurrence: reproduced in the bounded live manual run on 2026-05-02 after the path-truth sync.
  Affected agent/workflow/data source/timeframe: Hermes lead, dual-lane bridge, runtime refresh, manual proof path, `/root/openclawtrading/reports/auto/`.
  Proposed fix: audit the full Hermes script dependency set from the repaired local mirror, compare it to the live `/root/openclawtrading/scripts` inventory, and route a bounded live script sync plan for review before attempting another Hermes refresh.
  Owner: `architect-codex + Hermes Lead`
  Risk: `medium`
  Approval needed: `review before mirroring missing Hermes runtime scripts into the live repo`
  Proof test: the next bounded Hermes manual run should find `hermes_runtime_bridge.py`, complete without `Errno 2`, and write fresh Hermes artifacts under `/root/openclawtrading/reports/auto/`.

- Proved
  The live Hermes runner scripts under `/root/.openclaw/workspace/agents/hermes-lead/` were still stale before this pass. They now point at `/root/openclawtrading`, source `/root/.chimera.env` and `/root/.hermes/.env`, and pass `bash -n` after a binary-safe republish with Unix line endings.

- Proved
  `DERIVATIVES.json` is still refreshing with an empty structure rather than a useful market payload. Current live proof shows:
  - `"coins": {}`
  - `"market": {}`
  - `_brief.signals = []`
  This keeps the derivatives lane in a fresh-but-thin state even when the timestamp is current.

- Proved
  The bounded local Deezoh/Hermes regression suite still passes after the Hermes path-truth work:
  - Deezoh question-engine tests passed `16/16`
  - Deezoh runtime council visibility passed
  - Hermes dual-lane contract smoke passed
  - Hermes learning-store smoke passed

### Safe Changes Applied This Run

- Live Hermes runner path-truth sync in:
  - `/root/.openclaw/workspace/agents/hermes-lead/run_hermes_lead.sh`
  - `/root/.openclaw/workspace/agents/hermes-lead/run_hermes_pm_heartbeat.sh`

### Optimization Queue Updates

- `Q-2026-05-02-29` Compare the live `/root/openclawtrading/scripts` Hermes dependency inventory against the repaired local mirror and produce the smallest safe live sync set before retrying Hermes. Status: queued.
- `Q-2026-05-02-30` Treat empty-object `DERIVATIVES.json` payloads as an explicit degraded-confidence signal, not just a fresh timestamp. Status: queued.

## 2026-05-02 Desk Observability Repair Verification Pass

### What Actually Ran

- Added a shared local/live helper `refresh_desk_observability_bundle.py` under the current `/root/openclawtrading/scripts/` path.
- Wired that helper into the maintained macro and watchlist builders so one bounded collector cycle can also refresh the human-facing desk trace bundle.
- Removed unsupported stock-style `MSFTUSDT`, `NVDAUSDT`, `TSLAUSDT`, `AMZNUSDT`, and `XAGUSDT` names from the active candle default universe while keeping current crypto symbols plus `XAUUSDT`.
- Added a visible derivatives downgrade contract to `WATCHLISTS.json` whenever `DERIVATIVES.json` refreshes with empty `coins` and `market` objects.
- Synced the changed scripts to the live VPS and ran bounded live verification against the current `/root/openclawtrading` runtime.

### New Evidence From This Run

- Issue `DHI-040`
  Raw event: the first bounded live `watchlist_generator.py` run after the observability-helper wiring wrote `WATCHLISTS.json` to `/root/reports/auto/` instead of the active `/root/openclawtrading/reports/auto/` root.
  What happened: the maintained watchlist builder still had a wrong default base path that climbed too far up the repo tree, so a repair intended to improve observability initially refreshed the wrong report root.
  Why it matters: wrong-root writes can create false confidence because a manual test appears successful while the live consumers keep reading the stale current root.
  Recurrence: reproduced once during the bounded live repair pass on 2026-05-02 and fixed in the same pass by switching the default base path to `runtime_paths.ROOT`.
  Affected agent/workflow/data source/timeframe: watchlist builder, observability bundle, active report-root truth, same-cycle operator trust.
  Proposed fix: keep the root-aware default and verify every rebuilt artifact against `/root/openclawtrading/reports/auto/` rather than only checking for file creation.
  Owner: `codex-main-thread`
  Risk: `medium`
  Approval needed: `no for bounded path-truth repair`
  Proof test: a fresh live watchlist run should update `/root/openclawtrading/reports/auto/WATCHLISTS.json` and trigger same-cycle refreshes for the connected observability bundle in that same root.

- Proved
  After the root-aware watchlist fix, one bounded live cycle refreshed `WATCHLISTS.json`, `DEEZOH_THOUGHTS.json`, `ORCHESTRATOR_ACTIVITY.json`, `PAPER_DESK_OPERATOR_SNAPSHOT.json`, `PAPER_DESK_PIPELINE_BRIEF.md`, and `PAPER_DESK_INTERACTION_TRACE.md` within the same minute under `/root/openclawtrading/reports/auto/`.

- Proved
  The active saved `WATCHLISTS.json` now carries a visible derivatives downgrade object when the derivatives lane is structurally thin: `status = degraded`, `coins_count = 0`, `market_fields = 0`, and a warning that leverage context should be treated as low confidence.

- Proved
  The active candle default universe no longer includes the unsupported stock-style `*USDT` names seen in the earlier live log pollution. Final bounded live verification returned `False` for `MSFTUSDT`, `NVDAUSDT`, `TSLAUSDT`, `AMZNUSDT`, and `XAGUSDT`, while keeping `XAUUSDT = True`.

### Safe Changes Applied This Run

- Local + live `openclawtrading/scripts/refresh_desk_observability_bundle.py`
- Local + live `openclawtrading/scripts/watchlist_generator.py`
- Local + live `openclawtrading/scripts/macro_bias_builder.py`
- Local + live `openclawtrading/scripts/candle_analyzer.py`
- Local + live copies of:
  - `build_deezoh_thoughts.py`
  - `build_orchestrator_activity.py`
  - `build_paper_desk_operator_report.py`

### Optimization Queue Updates

- `Q-2026-05-02-31` Prove the repaired observability bundle lands from natural root cron rather than only a bounded manual run. Status: queued.

## 2026-05-02 Natural Cron Proof And Manager Contract Repair

### What Actually Ran

- Re-checked live root cron, `desk_observability.log`, and active report mtimes after the repaired chain had time to run naturally.
- Confirmed the scheduled `19:35` local root-cron cycle refreshed the active `/root/openclawtrading/reports/auto/` desk bundle without a manual trigger.
- Traced the remaining fake warning in the rebuilt operator surface and found that the live scheduled runner never invoked `manager_agent.py`, so `MANAGER_STATUS.json` could not exist.
- Synced the current path-aware manager implementation into `/root/openclawtrading/scripts/manager_agent.py`.
- Added `python3 manager_agent.py || true` back into `run_desk_observability_chain.sh`, then ran one bounded live verification cycle.

### New Evidence From This Run

- Issue `DHI-041`
  Raw event: after natural cron proof showed the desk observability bundle landing correctly, `PAPER_LOOP_AUDIT.json` still warned `Manager status is missing or stale.` and the live repo had no `/root/openclawtrading/scripts/manager_agent.py`.
  What happened: the restored observability chain had recovered the desk trace bundle, but it had not recovered the manager-health producer that the watchdog and operator snapshot still depend on.
  Why it matters: this was a fake infrastructure warning layered on top of real upstream warnings. Without `MANAGER_STATUS.json`, the operator brief could not distinguish “manager contract missing” from genuine unhealthy lanes.
  Recurrence: reproduced in the natural `19:35` root-cron cycle on 2026-05-02 and fixed in the same follow-up pass.
  Affected agent/workflow/data source/timeframe: manager health, paper watchdog, operator snapshot, scheduled desk observability chain.
  Proposed fix: keep the current manager implementation in `/root/openclawtrading/scripts/`, keep it wired into the scheduled chain, and treat any future missing `MANAGER_STATUS.json` as a real broken-contract regression.
  Owner: `codex-main-thread`
  Risk: `medium`
  Approval needed: `no for bounded contract restoration`
  Proof test: a fresh live chain should write `MANAGER_STATUS.json`, let the watchdog read real manager alerts, and stop reporting a fake missing-manager condition.

- Proved
  Natural root cron proof now exists for the repaired desk chain. The live `desk_observability.log` shows a scheduled `2026-05-02T16:35Z` cycle writing `DEEZOH_THOUGHTS.json`, `ORCHESTRATOR_ACTIVITY.json`, `PAPER_DESK_OPERATOR_SNAPSHOT.json`, `CRITIC_REPORTS.json`, and `REASONING_AUDIT_LATEST.md`, and the matching report mtimes line up with that natural cycle instead of a manual trigger.

- Proved
  After the manager contract repair, a fresh bounded live rerun now writes `MANAGER_STATUS.json`, `PAPER_LOOP_AUDIT.json`, and `PAPER_DESK_OPERATOR_SNAPSHOT.json` in the same minute, and the rebuilt operator snapshot now reports `same_cycle_confirmed = true` with reason `Critical reports are within 4.95 minutes of each other.`

- Proved
  The stale-review problem from the original audit is no longer the current truth on the restored chain. Current live `CRITIC_REPORTS.json` and `REASONING_AUDIT_LATEST.md` are fresh same-cycle outputs under the active report root.

- Proved
  Hermes is still not visible as a current-cycle runtime lane under `/root/openclawtrading/reports/auto/`. The repair improved Deezoh/operator visibility but did not produce any fresh Hermes-named report artifacts in the active root.

### Optimization Queue Updates

- `Q-2026-05-02-32` Repair or intentionally retire the upstream context/report lanes that still keep the now-working desk chain in `WARN`: `MARKET_CONTEXT.json`, `NEWS.json`, `ALTFINS.json`, `DIVERGENCES.json`, and `CATALYST_REPORT.json`. Status: queued.

## 2026-05-03 Deezoh Workflow-Label Retry Pass

### What Actually Ran

- Re-verified bounded SSH access to `root@100.67.172.114` after the earlier blocked pass.
- Restored the thread heartbeat `deezoh-15-minute-observation-loop` at a 15 minute cadence.
- Inspected the latest live Deezoh, screener, and macro session traces plus the current shared report root.
- Verified that the prior screener and macro direct runs had written useful output even when later provider behavior made the task look worse than the written artifact.
- Ran a fresh live Deezoh chart-side replay with explicit session id `deezoh-observe-breakout-v5`.
- Patched the Deezoh instruction layer locally and then live in:
  - `agents/deezoh/QUESTION_ENGINE.md`
  - `agents/deezoh/WORKFLOW.md`
  - `agents/deezoh/HEARTBEAT.md`
- Re-ran the same live Deezoh chart-side replay with explicit session id `deezoh-observe-breakout-v6`.

### New Evidence From This Run

- Issue `DHI-041`
  Raw event: the first fresh retry replay `deezoh-observe-breakout-v5` pushed back correctly and kept `no_trade` alive, but returned `selected_workflow = deezoh-trading-coach three-case comparison workflow` instead of a canonical market workflow id.
  What happened: the reasoning quality was materially good, but the workflow label contract was still too weak, so Deezoh answered with a meta coaching label instead of the actual structural workflow.
  Why it matters: this breaks downstream monitoring and makes workflow analytics noisy, because the system cannot reliably tell whether the desk thought the market was a breakout, consolidation, trap, or event-control case.
  Recurrence: reproduced once in the fresh live retry pass on 2026-05-03 and fixed in the same pass by tightening the direct-observation workflow contract.
  Affected agent/workflow/data source/timeframe: Deezoh direct observation replies, workflow analytics, monitor ledger quality, 15 minute desk loop.
  Proposed fix: require `selected_workflow` to be a canonical market workflow id, require a direct read of `WORKFLOW.md` when the prompt asks for the workflow label, and forbid skill names or prose labels as the workflow output.
  Owner: `codex-main-thread`
  Risk: `low`
  Approval needed: `no for bounded instruction repair`
  Proof test: a fresh replay of the same chart-side prompt should output a canonical workflow id such as `consolidation_resolution` rather than a coaching label.

- Proved
  After the live instruction repair, the immediate rerun `deezoh-observe-breakout-v6` returned `selected_workflow = consolidation_resolution` and still kept `winner = no_trade`, `typed_wait = WAIT_ACCEPTANCE`, and strong pushback against front-running the breakout.

- Proved
  The retry pass confirmed the higher-value behavioral contract is now working together:
  - Deezoh pushed back instead of yes-manning.
  - Deezoh named what Sal may be overlooking.
  - Deezoh exposed stale and missing evidence clearly.
  - Deezoh listed what it actually read.

- Proved
  Specialist delegation is still not honestly live in this path. Both fresh retry replays returned `actually_spawned = None`, so the desk is still behaving as a single-session report consumer rather than a genuinely delegated specialist round.

- Proved
  Freshness remains a real blocker on judgment quality even when the answer format improved. The repaired replay still reported roughly 8 to 24 hour report age, empty `DERIVATIVES.json`, and no structured chart-analyzer payload.

### Safe Changes Applied This Run

- Local + live `agents/deezoh/QUESTION_ENGINE.md`
- Local + live `agents/deezoh/WORKFLOW.md`
- Local + live `agents/deezoh/HEARTBEAT.md`

### Optimization Queue Updates

- `Q-2026-05-03-01` Force canonical workflow ids in all direct observation outputs and validate them in replay tests. Status: done.
- `Q-2026-05-03-02` Add one explicit freshness-first branch so Deezoh asks for a refresh before deep thesis ranking when the core desk reports are 8+ hours stale. Status: queued.
- `Q-2026-05-03-03` Prove one real delegated specialist round or explicitly downgrade the desk contract to report-consumption mode until delegation is honest. Status: queued.

## 2026-05-02 Deezoh Root-Cause Council And Delegation/Freshness Repair

### What Actually Ran

- Spawned a three-agent council to isolate the root cause instead of guessing:
  - Delegation root cause: why Deezoh did not honestly spawn specialists.
  - Data freshness root cause: why Deezoh still saw degraded or stale report state.
  - Instruction/workflow root cause: why old path and precedence guidance still polluted behavior.
- Patched the live OpenClaw agent policy so Deezoh can spawn approved trading specialists instead of only itself.
- Split Deezoh freshness into a critical-report contract and optional-lane health, so missing optional lanes no longer falsely break same-cycle proof.
- Replaced stale Deezoh workspace-local thought copies with symlinks to the active shared report root.
- Added Deezoh front-door guards so old Linux paths and older helper docs are treated as background unless translated to current `/root/...` runtime truth.

### New Evidence From This Run

- Issue `DHI-042`
  Raw event: Deezoh direct replay sessions kept returning no honest delegated specialist round, even when the behavior contract expected chart, indicator, macro, screener, or risk specialists.
  What happened: OpenClaw's `sessions_spawn` policy defaulted to only the requesting agent unless `subagents.allowAgents` was explicitly configured. Deezoh therefore could only spawn `deezoh`, not `chart-analyzer` or the trading specialist council.
  Why it matters: Deezoh looked like it was doing a multi-agent desk process, but it was actually operating as a single-session report consumer. That makes “agent-to-agent reasoning” claims unsafe unless spawn proof exists.
  Recurrence: reproduced in live session `deezoh-spawn-proof-v1` with `status = forbidden` and error `agentId is not allowed for sessions_spawn (allowed: deezoh)`.
  Affected agent/workflow/data source/timeframe: Deezoh, chart-analyzer, indicator-analyst, macro-bias, catalyst, screener, strategy, entry-watch, risk-engine, trade-judge, bitget-analyst.
  Proposed fix: add an explicit Deezoh specialist allowlist in `/root/.openclaw/openclaw.json` and keep future delegation tests proof-based.
  Owner: `codex-main-thread`
  Risk: `medium`
  Approval needed: `no for bounded runtime policy repair`
  Proof test: `deezoh-spawn-proof-v2` returned `sessions_spawn.status = accepted`, produced a `childSessionKey`, and wrote a real child `chart-analyzer` session that read active chart/candle reports.

- Issue `DHI-043`
  Raw event: live `DEEZOH_THOUGHTS.json` reported `same_cycle_confirmed = false` because nonexistent `INDICATOR_REPORT.json` and `STRATEGY_REPORT.json` were treated as required core reports.
  What happened: the builder mixed critical report freshness with optional specialist lane completeness.
  Why it matters: Deezoh was being told the core desk cycle was invalid even when the actual core reports were fresh, which pushed it toward noisy stale-data warnings and weaker next-question behavior.
  Recurrence: reproduced in the live shared report root before the builder patch.
  Affected agent/workflow/data source/timeframe: Deezoh thought bundle, question engine, same-cycle proof, 15 minute observation loop.
  Proposed fix: define a smaller critical contract and emit optional-lane health separately.
  Owner: `codex-main-thread`
  Risk: `low`
  Approval needed: `no for bounded report-contract repair`
  Proof test: a fresh live rebuild returned `same_cycle_confirmed = true`, reason `Critical reports are within 5.41 minutes of each other.`, plus `optional_lane_health.status = degraded` for missing/thin optional lanes.

- Issue `DHI-044`
  Raw event: Deezoh had workspace-local `DEEZOH_THOUGHTS.json` files that could lag behind `/root/openclawtrading/reports/auto/DEEZOH_THOUGHTS.json`, and some older helper docs still contained old Linux paths or ambiguous precedence.
  What happened: runtime truth, workspace-local convenience files, and older docs were not clearly separated.
  Why it matters: Deezoh and agents can accidentally read stale local context or treat old `/home/open-claw` examples as current, causing wrong diagnosis and repeated path drift.
  Recurrence: seen during the live council pass while comparing workspace-local thought files against the active shared report root.
  Affected agent/workflow/data source/timeframe: Deezoh startup, Deezoh bootstrap, workspace-local context, shared report reads.
  Proposed fix: point workspace-local thought files to the active report-root file and add front-door instruction guards for current path and precedence truth.
  Owner: `codex-main-thread`
  Risk: `low`
  Approval needed: `no for bounded stale-context repair`
  Proof test: `/root/.openclaw/workspace/agents/deezoh/DEEZOH_THOUGHTS.json` and `DEEZOH_THOUGHTS_LIVE.json` now resolve to `/root/openclawtrading/reports/auto/DEEZOH_THOUGHTS.json`.

### Proved

- Live specialist delegation is now allowed and executable. The fixed Deezoh spawn proof accepted `chart-analyzer`, created a child session, and the child actually read `/root/openclawtrading/reports/auto/CHART_ANALYSIS.json` plus `/root/openclawtrading/reports/auto/CANDLES.json`.
- Deezoh can consume the completed child result in a follow-up answer. The `deezoh-spawn-proof-v2` continuation used the chart-analyzer finding, selected `data_unreliable`, kept the best no-trade case as the winner, named what Sal may be overlooking, and recorded the missing chart payload as a monitor issue instead of inventing usable chart structure.
- Core same-cycle freshness is now separated from optional-lane degradation. Deezoh can say “core reports are fresh” while still warning that chart, derivatives, indicator, strategy, or catalyst lanes are thin/missing/stale.
- Deezoh's local thought surface no longer has to be manually refreshed separately because it now resolves to the active shared report file.

### Safe Changes Applied This Run

- Local + live `agents/deezoh/AGENTS.md`
- Local + live `agents/deezoh/BOOTSTRAP.md`
- Local + live `scripts/build_deezoh_thoughts.py`
- Local + live `scripts/deezoh_question_engine.py`
- Local + live `openclawtrading/scripts/build_deezoh_thoughts.py`
- Live `/root/.openclaw/openclaw.json` Deezoh `subagents.allowAgents` policy
- Live Deezoh workspace thought symlinks

### Optimization Queue Updates

- `Q-2026-05-02-33` Add a natural follow-up test proving Deezoh resumes after a child specialist completes and incorporates the child finding into its final trade-coach answer. Status: done.
- `Q-2026-05-02-34` Repair or replace the chart payload producer because `CHART_ANALYSIS.json` is fresh but still reports `data_quality = MISSING`. Status: queued.
- `Q-2026-05-02-35` Repair derivatives payload quality because `DERIVATIVES.json` is timestamp-fresh but structurally empty. Status: queued.
- `Q-2026-05-02-36` Deprecate or rewrite older helper docs that still show old Linux paths or outdated spawn examples after the live behavior is stable. Status: queued.

## 2026-05-02 Chart Analysis Producer Repair

### What Actually Ran

- Traced the active writer of `CHART_ANALYSIS.json` and confirmed it is `scripts/desk_contract_bridge.py`, not the child-agent prose itself.
- Found that the bridge expects `/root/openclawtrading/reports/auto/CHART_ANALYSIS_latest.json`, but the live chart runner still pointed at retired `/home/open-claw/openclawtrading` paths and the expected generator was missing from the new VPS runtime.
- Restored a deterministic chart generator under `/root/openclawtrading/scripts/generate_chart_analysis.py`.
- Rewired `/root/.openclaw/workspace/agents/chart-analyzer/run_chart_analyzer.sh` to current `/root/openclawtrading` paths, current OpenClaw workspace agent path, and the real `mcporter` location when available.
- Tightened `desk_contract_bridge.py` so fallback OHLCV analysis is labeled `PARTIAL` and cannot mark `zone_confirmed = true` unless a real entry signal or verified/full chart specialist result exists.
- Rebuilt Deezoh and operator surfaces after the chart repair.

### New Evidence From This Run

- Issue `DHI-045`
  Raw event: `CHART_ANALYSIS.json` was fresh but had `data_quality = MISSING`, reason `No structured CHART_ANALYSIS_latest payload was available to bridge.`
  What happened: the bridge was refreshing the final report, but the upstream latest-payload producer was not running on the new VPS path. The chart runner still used `/home/open-claw/openclawtrading`, looked for a nonexistent generator under the old report root, and therefore never created the structured latest payload.
  Why it matters: Deezoh saw a fresh chart file and could count it as current-cycle evidence, but the file contained no usable chart structure. This made monitoring noisy and forced Deezoh to treat the chart lane as unavailable.
  Recurrence: reproduced on 2026-05-02 from live `/root/openclawtrading/reports/auto/CHART_ANALYSIS.json`.
  Affected agent/workflow/data source/timeframe: chart-analyzer, TradingView MCP, desk-contract bridge, Deezoh chart-side workflow, 15 minute observation loop.
  Proposed fix: keep the chart runner on `/root/...`, restore the deterministic fallback generator, and keep fallback output explicitly partial unless TradingView/visual specialist proof succeeds.
  Owner: `codex-main-thread`
  Risk: `medium`
  Approval needed: `no for bounded runtime path/generator repair`
  Proof test: live chart run now writes `CHART_ANALYSIS_latest.json`, `HOT_ZONES.json`, `CHART_ANALYZER_EXECUTION.json`, and a bridged `CHART_ANALYSIS.json` with `data_quality = PARTIAL`, `source_mode = binance_ohlcv_fallback`, `specialist_verified = false`, and `zone_confirmed = false`.

### Proved

- `CHART_ANALYSIS_latest.json` now exists and contains 16 structured deterministic analyses for the supported Binance symbols in the current universe.
- `HOT_ZONES.json` now exists and carries generated support/resistance levels from the fallback lane.
- `CHART_ANALYSIS.json` no longer says the latest payload is missing. Current BTC chart state is fallback/partial, bearish-biased on the mechanical 4H read, but not zone-confirmed.
- Deezoh read the corrected files and correctly said the chart lane should not justify a trade by itself because it is deterministic OHLCV fallback, not visual TradingView confirmation.

### Remaining Issues

- TradingView Desktop CDP is reachable on port `9222`, but `/json/list` returns no page targets and `/json/new` returns HTTP 500, so Jackson cannot attach to a live chart page yet.
- The fallback generator cannot fetch `HYPEUSDT` and `XAUUSDT` from the Binance spot kline endpoint, so those symbols either need a Bitget/futures fallback or should be filtered from this specific generator.
- Deezoh's proof reply incorrectly described the freshly generated UTC timestamp as about 8 hours stale, which is a timezone interpretation bug in the answer layer rather than the chart file itself.

### Optimization Queue Updates

- `Q-2026-05-02-34` Repair or replace the chart payload producer because `CHART_ANALYSIS.json` is fresh but still reports `data_quality = MISSING`. Status: done.
- `Q-2026-05-02-37` Repair TradingView Desktop/CDP target exposure so Jackson sees a real `tradingview.com/chart` page target instead of only a browser endpoint with empty `/json/list`. Status: queued.
- `Q-2026-05-02-38` Add Bitget or futures fallback for chart symbols that Binance spot rejects, including `HYPEUSDT` and `XAUUSDT`. Status: queued.
- `Q-2026-05-02-39` Add a Deezoh UTC freshness sanity rule so it does not call same-minute UTC artifacts stale just because the runtime prompt is in GMT+8. Status: queued.

## 2026-05-02 Heartbeat Observation After Chart Repair

### What Actually Ran

- Ran live Deezoh replay `deezoh-observe-after-chart-fix-v1` as if Sal was looking at BTCUSDT after the chart-analysis producer repair.
- Prompt required Deezoh to read the current chart, thoughts, screener, macro, and derivatives reports and to answer with workflow, winner, pushback, next question, monitor issue, and unsafe-learning guard.

### Proved

- Deezoh selected `range_or_mixed` and kept `winner = no_trade`.
- Deezoh pushed back clearly instead of yes-manning the short setup.
- Deezoh treated `PARTIAL` Binance OHLCV chart output as context only, not TradingView visual confirmation.
- Deezoh named the unsafe lesson to avoid: do not learn that a mechanical 4H bearish fallback label plus bullish EMA/MACD is a valid short pattern.
- Deezoh updated the next question based on evidence: reframe BTCUSDT through macro-bias first, then require a fresh visual chart-analyzer run.

### New Issues Confirmed

- `TradingView CDP port 9222` remains reachable at `/json/version`, but `/json/list` has no chart page targets and `/json/new` returns HTTP 500.
- `DERIVATIVES.json` is still structurally empty, so Deezoh has no OI/funding/liquidation context.
- `INDICATOR_REPORT.json` and `STRATEGY_REPORT.json` are still missing.
- The council remains incomplete because the critic lane is missing from the current round.

### Optimization Queue Updates

- `Q-2026-05-02-40` Add a replay assertion that Deezoh must reject activating trades from `CHART_ANALYSIS.data_quality = PARTIAL` unless independent trigger evidence exists. Status: queued.

## 2026-05-03 Deezoh Reporting Compatibility And Hermes Runtime Retry

### What Actually Ran

- Read the current Codex bootstrap, runtime router, latest shared handoff, and the automation memory before changing anything.
- Re-verified live OpenClaw truth on `root@100.67.172.114`, including active report mtimes, root cron, Deezoh/Hermes agent homes, and recent desk logs.
- Patched `scripts/deezoh_question_engine.py` locally so `DEEZOH_THOUGHTS.json` exposes:
  - `selected_workflow`
  - `question_plan`
  - `next_question`
  - `best_long`
  - `best_short`
  - `best_no_trade`
  - `long_vs_short_vs_no_trade`
- Added a deterministic local smoke suite `scripts/tests/deezoh_observation_suite_smoke.py` and proved the real question engine chooses the expected workflows for:
  - breakout watch
  - consolidation / range mean reversion
  - live news event
  - failed breakout / liquidity trap
  - pre-event control
  - post-event digest
  - data-degraded mode
- Synced the reporting fix live and rebuilt `DEEZOH_THOUGHTS.json` from the live scripts directory to confirm the fields are now present in the active shared report root.
- Re-tested the Hermes paper lane with one bounded manual `run_hermes_lead.sh` pass after confirming the bridge exists again.
- Synced the missing paper-lane helpers `build_dual_lane_experiment.py`, `build_trade_judge_cycle.py`, and `hermes_progress_status.py` to the live repo and retried Hermes once more.

### New Evidence From This Run

- Issue `DHI-045`
  Raw event: the live `DEEZOH_THOUGHTS.json` that Deezoh consumers read had the deeper workflow guidance and comparison payload internally, but it did not expose simple top-level fields for the chosen workflow, next question, or long-vs-short-vs-no-trade ranking.
  What happened: the core Deezoh logic was already computing the useful evidence, but the report contract was too weak for the observation loop and monitor surfaces that need direct fields instead of deep nested parsing.
  Why it matters: without those fields, the improvement loop cannot cheaply prove whether Deezoh named the workflow it chose, what question comes next, or whether the ranking changed after evidence shifts.
  Recurrence: current live proof before the repair on 2026-05-03.
  Affected agent/workflow/data source/timeframe: Deezoh thought bundle, desk observability reports, workflow analytics, recurring observation loop.
  Proposed fix: keep the new top-level compatibility fields in `DEEZOH_THOUGHTS.json` and guard them with the scenario suite so future refactors do not silently remove them.
  Owner: `codex-main-thread`
  Risk: `low`
  Approval needed: `no for bounded reporting/test repair`
  Proof test: `python scripts/tests/deezoh_observation_suite_smoke.py` passes locally and a fresh live rebuild now shows `selected_workflow`, `question_plan`, `next_question`, and the three-way comparison fields in `/root/openclawtrading/reports/auto/DEEZOH_THOUGHTS.json`.

- Issue `DHI-046`
  Raw event: the first bounded live Hermes retry no longer failed on a missing bridge, but it still produced no Hermes runtime artifacts because the lead runner first lacked `build_dual_lane_experiment.py`, then after syncing the missing helpers it failed again because `/root/.hermes/hermes-agent/venv/bin/hermes` does not exist on the VPS.
  What happened: Hermes moved past the older bridge-path failure and is now blocked by an executable-path/install gap in the actual Hermes CLI lane.
  Why it matters: this proves Hermes is still not an active paper runtime despite the repaired wrapper scripts, so Deezoh/Hermes closeouts must not overclaim live dual-lane behavior yet.
  Recurrence: reproduced in the bounded live retry on 2026-05-03 after helper sync.
  Affected agent/workflow/data source/timeframe: Hermes lead runner, Hermes runtime bridge, dual-lane experiment artifacts, paper-only lane activation.
  Proposed fix: verify the intended Hermes CLI install path or update `CHIMERA_HERMES_BIN` / `hermes_runtime_bridge.py` to the real installed executable only after proving the correct binary and invocation contract.
  Owner: `hermes-lead + codex-main-thread`
  Risk: `medium`
  Approval needed: `review before changing the Hermes executable contract or installing a missing runtime`
  Proof test: a bounded `run_hermes_lead.sh` pass should write `HERMES_RUNTIME_STATUS.json`, `HERMES_DECISION_TRACE.json`, and `HERMES_PROGRESS_STATUS.json` without `FileNotFoundError` for the Hermes binary.

### Proved

- Local deterministic Deezoh scenario coverage now exists for the exact observation cases this loop needs most often. Current pass results:
  - `breakout_watch -> range_breakout_watch | wait=WAIT_ACCEPTANCE | winner=short`
  - `consolidation -> range_mean_reversion | wait=NONE | winner=short`
  - `news_event -> live_event | wait=WAIT_ACCEPTANCE | winner=no_trade`
  - `failed_breakout -> liquidity_trap_or_squeeze | wait=WAIT_SWEEP | winner=no_trade`
  - `pre_event_control -> pre_event | wait=WAIT_EVENT | winner=no_trade`
  - `post_event_digest -> post_event_digest | wait=WAIT_ACCEPTANCE | winner=no_trade`
  - `data_degraded -> data_degraded | wait=WAIT_REFRESH | winner=no_trade`
- The active live `DEEZOH_THOUGHTS.json` now exposes a direct workflow/ranking/question contract again. After the rebuild from `/root/openclawtrading/scripts/`, the live file shows:
  - `selected_workflow = range_or_mixed`
  - `next_question.agent = macro-bias`
  - `winner = no_trade`
- The current live three-way ranking still prefers caution:
  - `best_long.score = 23.0`
  - `best_short.score = 55.0`
  - `best_no_trade.score = 63.0`
- Hermes helper-script drift was partially repaired live:
  - `DUAL_LANE_EVIDENCE_PACK.json` now writes again
  - `HERMES_LANE_THESIS.json` now writes again
  - the remaining failure is the missing Hermes CLI executable, not the older missing bridge or missing builder scripts

### Safe Changes Applied This Run

- Local + live `scripts/deezoh_question_engine.py`
- Local `scripts/tests/deezoh_observation_suite_smoke.py`
- Live `scripts/build_dual_lane_experiment.py`
- Live `scripts/build_trade_judge_cycle.py`
- Live `scripts/hermes_progress_status.py`

### Optimization Queue Updates

- `Q-2026-05-03-04` Keep the Deezoh top-level workflow/ranking/question compatibility contract under smoke-test coverage. Status: done.
- `Q-2026-05-03-05` Prove the real Hermes executable path or install state before any further live dual-lane claims. Status: queued.

## 2026-05-03 Hermes Runtime Activation Proof

### What Actually Ran

- Proved the live Hermes CLI install state on `root@100.67.172.114` instead of guessing:
  - `command -v hermes` returned `/usr/local/bin/hermes`
  - the package venv entrypoint exists at `/usr/local/lib/hermes-agent/venv/bin/hermes`
  - the old bridge default `/root/.hermes/hermes-agent/venv/bin/hermes` does not exist
- Patched `scripts/hermes_runtime_bridge.py` locally and live so it:
  - resolves the real Hermes binary automatically
  - reads the current Hermes config for provider/model
  - injects the configured provider API key into the subprocess env when needed
- Proved the provider fix with a bounded direct Hermes CLI test before changing the bridge:
  - forcing `provider=minimax` plus the stored MiniMax key returns a valid one-shot response
- Re-ran one bounded live `run_hermes_lead.sh` cycle after the bridge fix.

### New Evidence From This Run

- Issue `DHI-046`
  Raw event: Hermes initially failed because the bridge pointed to `/root/.hermes/hermes-agent/venv/bin/hermes`, but the actual installed CLI lives at `/usr/local/bin/hermes` and `/usr/local/lib/hermes-agent/venv/bin/hermes`.
  What happened: the runtime bridge was carrying an outdated executable-path assumption from an older install shape.
  Why it matters: the paper lane could not even start, so prior Hermes closeouts were blocked on infrastructure rather than reasoning quality.
  Recurrence: reproduced on the live retry and fixed in this pass.
  Affected agent/workflow/data source/timeframe: Hermes runtime bridge, Hermes lead runner, dual-lane paper experiment.
  Proposed fix: keep the new binary auto-resolution logic and preserve `CHIMERA_HERMES_BIN` as an explicit override when needed.
  Owner: `codex-main-thread`
  Risk: `low`
  Approval needed: `no for bounded runtime-path repair`
  Proof test: bounded `run_hermes_lead.sh` now writes `HERMES_RUNTIME_STATUS.json` with `status = ready` and `hermes_bin = /usr/local/bin/hermes`.
  Status: `fixed and verified`

- Issue `DHI-047`
  Raw event: once Hermes actually ran, it independently agreed with Deezoh on `no_trade` and then flagged a concrete pipeline contradiction: `ENTRY_SIGNALS` was effectively marking the setup as ready while macro/catalyst still said `STAY OUT`.
  What happened: the system is still letting directional score/readiness surfaces overstate execution readiness when macro gates are closed.
  Why it matters: this is the kind of contradiction that can erode trust or produce false positives if a later lane consumes the signal blindly.
  Recurrence: observed in the first clean live Hermes cycle on 2026-05-03.
  Affected agent/workflow/data source/timeframe: entry-signals, macro gate, setup confidence classification, Deezoh/Hermes dual-lane comparison, paper decision loop.
  Proposed fix: add a pipeline-integrity check that blocks `READY_TO_TRADE` or similar entry-ready states whenever macro gate is `STAY OUT`, and flag zone-alignment/confidence contradictions in the same pass.
  Owner: `pipeline-watchdog + entry-watch + catalyst + codex-main-thread`
  Risk: `medium`
  Approval needed: `no for bounded audit/test/reporting hardening; review before live execution-gate policy changes`
  Proof test: on the next bounded cycle, no entry-ready state should survive when macro verdict is `STAY OUT`, and the contradiction should either be suppressed upstream or emitted as an explicit defect instead of a trade-ready suggestion.

### Proved

- Hermes runtime is now live enough for the paper lane contract:
  - `HERMES_RUNTIME_STATUS.json` => `status = ready`
  - `HERMES_RUNTIME_INPUT.json` exists
  - `HERMES_DECISION_TRACE.json` exists
  - `HERMES_PROGRESS_STATUS.json` exists
  - `HERMES_LANE_THESIS.json` exists
  - `HERMES_ADVISOR_REVIEW.json` exists
  - `JUDGE_DECISION.json` exists
  - `TRADE_DECISION_SCORECARD.json` exists
  - `LEARNING_FEEDBACK.json` exists
- The first clean live Hermes lane agreed with Deezoh on caution, not bravado:
  - Hermes decision: `no_trade`
  - Hermes direction: `SHORT`
  - Hermes summary: directional short bias exists, but macro gate blocked by named critical events and timing trigger still missing
  - Judge decision: `selected_lane = merge`, `selected_action = no_trade`, `send_to_execution = false`
- The new live Hermes cycle created useful reviewed learning candidates instead of only a success banner. The strongest one is the macro-gate vs ready-to-trade contradiction.

### Safe Changes Applied This Run

- Local + live `scripts/hermes_runtime_bridge.py`

### Optimization Queue Updates

- `Q-2026-05-03-05` Prove the real Hermes executable path or install state before any further live dual-lane claims. Status: done.
- `Q-2026-05-03-06` Add a pipeline-integrity guard for macro-gate vs entry-ready contradictions before any later execution-facing lane trusts those signals. Status: queued.

## 2026-05-03 Live Workflow Contract Repair And Hermes Trace Compatibility

### What Actually Ran

- Re-ran the deterministic local Deezoh observation suite after patching the reporting layer so the four core observation cases now map to canonical workflow ids instead of internal situation labels:
  - breakout -> `breakout_acceptance`
  - consolidation -> `consolidation_resolution`
  - news / event control -> `news_event_control`
  - failed-breakout / liquidity-trap -> `liquidity_trap`
- Repaired the Windows-local `scripts/runtime_paths.py` helper so local mirrors stop resolving `REPORTS_AUTO` to the retired `\\home\\open-claw\\...` root when Deezoh reports are rebuilt on Windows.
- Synced the bounded Deezoh reporting fixes to both live repo and live OpenClaw workspace copies:
  - `/root/openclawtrading/scripts/deezoh_question_engine.py`
  - `/root/openclawtrading/scripts/runtime_paths.py`
  - `/root/.openclaw/workspace/scripts/deezoh_question_engine.py`
  - `/root/.openclaw/workspace/scripts/runtime_paths.py`
- Rebuilt the live desk artifacts and proved the active `DEEZOH_THOUGHTS.json` now exposes canonical workflow fields plus the workflow rationale/switch contract.
- Patched the manager compatibility layer so macro verdict `STAY OUT` is treated as the valid `OUT` alias instead of a fake schema error.
- Synced the manager fix to:
  - `/root/openclawtrading/scripts/manager_agent.py`
  - `/root/.openclaw/workspace/scripts/manager_agent/manager_agent.py`
  - `/root/.openclaw/workspace/trading_system/scripts/manager_agent.py`
- Ran the live manager again and confirmed the false macro-bias alert dropped out of `MANAGER_STATUS.json` (7 unhealthy -> 6 unhealthy).
- Patched `scripts/hermes_runtime_bridge.py` so `HERMES_DECISION_TRACE.json` carries the same top-level `symbol`, `direction`, `decision`, `summary`, and `confidence` that Hermes already computed deeper in the lane thesis.
- Synced the Hermes trace fix to both the repo and workspace bridge copies, then ran a bounded live paper-only Hermes bridge cycle directly from `/root/openclawtrading/scripts/hermes_runtime_bridge.py --timeout-seconds 180 --quiet`.

### New Evidence From This Run

- Issue `DHI-048`
  Raw event: the live `DEEZOH_THOUGHTS.json` was still emitting `selected_workflow = range_or_mixed`, which violates the Deezoh contract that requires canonical market workflow ids.
  What happened: the question engine was already deriving a canonical `situation_pack`, but it still wrote the raw internal situation label into `selected_workflow`.
  Why it matters: the observation loop could not prove whether Deezoh chose the right workflow family because the report exposed an internal label instead of the operator-facing workflow contract.
  Recurrence: reproduced on the live VPS before the repair on May 3, 2026.
  Affected agent/workflow/data source/timeframe: Deezoh reporting layer, observation suite, workflow analytics, all chart-side desk loops.
  Proposed fix: keep `selected_workflow` bound to the canonical market workflow id, and preserve `situation` / `situation_pack` separately for deeper internal context.
  Owner: `codex-main-thread`
  Risk: `low`
  Approval needed: `no for bounded reporting-contract repair`
  Proof test: fresh live `DEEZOH_THOUGHTS.json` now shows `selected_workflow = accumulation_hunt` plus `why_this_workflow`, `why_not_the_next_two_alternatives`, and `what_evidence_would_force_a_workflow_switch`.
  Status: `fixed and verified`

- Issue `DHI-049`
  Raw event: `MANAGER_STATUS.json` was flagging `macro_bias_agent: CONTENT INVALID — bias='STAY OUT' — invalid value (expected LONG/SHORT/MIXED/OUT)` even though `STAY OUT` is a real macro contract value in the live desk.
  What happened: the manager validator only accepted the legacy alias `OUT` and treated `STAY OUT` as a bad payload instead of a compatible macro veto.
  Why it matters: the operator surface was overstating desk breakage by counting one real policy output as a schema defect.
  Recurrence: reproduced on the live VPS before the repair on May 3, 2026.
  Affected agent/workflow/data source/timeframe: manager health monitor, macro-bias compatibility layer, operator brief.
  Proposed fix: keep `STAY OUT` normalized to the valid `OUT` alias inside the manager validator and preserve the human-facing summary text as `STAY OUT`.
  Owner: `codex-main-thread`
  Risk: `low`
  Approval needed: `no for bounded compatibility fix`
  Proof test: after the live rerun, the false macro-bias alert disappeared and the live unhealthy count dropped from `7` to `6`.
  Status: `fixed and verified`

- Issue `DHI-050`
  Raw event: `SCOUT_REPORT.json` and `MACRO_BIAS.json` still do not expose explicit workflow ids for accumulation, continuation, post-news rotation, failed-breakout short, range rotation, pre-event control, post-event digest, cross-asset divergence, unusual-behavior precedent capture, or data-degraded mode.
  What happened: Deezoh now has a stronger workflow contract, but the screener and macro surfaces still expose verdicts/summaries without a first-class workflow-selection field.
  Why it matters: the improvement loop can only infer those workflow choices indirectly from text and verdicts, so the screener/macro audit is still weaker than the Deezoh observation audit.
  Recurrence: current live proof on May 3, 2026 after inspecting `SCOUT_REPORT.json` keys and `MACRO_BIAS.json` top-level shape.
  Affected agent/workflow/data source/timeframe: screener workflow audit, macro workflow audit, recurring improvement loop.
  Proposed fix: add explicit `selected_workflow`-style fields to the screener and macro report contracts so accumulation/continuation/post-news/data-degraded paths can be tested directly instead of inferred.
  Owner: `screener + macro-bias + architect-codex`
  Risk: `medium`
  Approval needed: `no for bounded reporting-contract additions; review before policy-level routing changes`
  Proof test: future `SCOUT_REPORT.json` and `MACRO_BIAS.json` should each expose a single workflow id plus the reason it was selected.
  Status: `open`

- Issue `DHI-051`
  Raw event: `HERMES_LANE_THESIS.json` held the real Hermes decision, but `HERMES_DECISION_TRACE.json` still left top-level `decision`, `direction`, and `summary` empty.
  What happened: the runtime bridge was writing the parsed Hermes output under `parsed_output` only, leaving the operator-facing top-level trace fields blank.
  Why it matters: Hermes could be functioning while the improvement loop still sees a half-empty trace surface, which slows every audit and makes the lane look weaker than it is.
  Recurrence: reproduced on the live VPS before the repair on May 3, 2026.
  Affected agent/workflow/data source/timeframe: Hermes runtime bridge, dual-lane trace contract, recurring Hermes audit.
  Proposed fix: keep the top-level Hermes trace fields populated from the normalized lead thesis on every successful runtime pass.
  Owner: `codex-main-thread`
  Risk: `low`
  Approval needed: `no for bounded reporting-contract repair`
  Proof test: bounded direct live bridge run now writes `HERMES_DECISION_TRACE.json` with `symbol = BTCUSDT`, `direction = SHORT`, `decision = no_trade`, the Hermes summary, and `confidence = 0`.
  Status: `fixed and verified`

### Proved

- The local Deezoh observation suite now proves canonical workflow ids for the core chart-side cases instead of internal situation labels.
- The Windows-local report builder path helper now resolves to `C:\Users\becke\claudecowork\reports\auto` instead of the retired Linux mirror path.
- The active live `DEEZOH_THOUGHTS.json` now exposes a clearer operator contract:
  - `selected_workflow = accumulation_hunt`
  - `winner = no_trade`
  - `why_this_workflow` is present
  - `why_not_the_next_two_alternatives` is present
  - `what_evidence_would_force_a_workflow_switch` is present
- The live council truth is now aligned across Deezoh-side reasoning and the derived control artifact:
  - `COUNCIL_REVIEW.json status = partially_visible`
  - `COUNCIL_REVIEW.json actually_ran = false`
  - Deezoh no longer claims a fully-ran council when the critic lane is still missing
- The manager still reports real upstream degradation, but one false alert is gone:
  - remaining live blockers are stale `NEWS.json`, stale `MACRO.json`, stale `CATALYST_REPORT.json`, stale/missing divergence coverage, missing `ALTFINS.json`, and empty `DERIVATIVES.json`
  - the old false `STAY OUT` schema alert is gone
- Hermes is still paper-safe and cautious after the bounded direct rerun:
  - `HERMES_LANE_THESIS.json decision = no_trade`
  - `JUDGE_DECISION.json selected_lane = merge`
  - `JUDGE_DECISION.json selected_action = no_trade`
  - `send_to_execution = false`
- The macro-gate versus ready-to-trade contradiction remains live:
  - `ENTRY_SIGNALS.json` still promotes `READY_TO_TRADE`
  - Hermes advisor still explicitly objects that this should be macro-gated before any later execution-facing lane trusts it

### Safe Changes Applied This Run

- Local + live `scripts/deezoh_question_engine.py`
- Local + live `scripts/runtime_paths.py`
- Local `scripts/tests/deezoh_observation_suite_smoke.py`
- Local + live `scripts/manager_agent.py` / local mirror `scripts/manager_agent/manager_agent.py`
- Live workspace mirrors:
  - `/root/.openclaw/workspace/scripts/deezoh_question_engine.py`
  - `/root/.openclaw/workspace/scripts/runtime_paths.py`
  - `/root/.openclaw/workspace/scripts/manager_agent/manager_agent.py`
  - `/root/.openclaw/workspace/trading_system/scripts/manager_agent.py`
- Local + live `scripts/hermes_runtime_bridge.py`

### Remaining Issues

- `NEWS.json`, `CATALYST_REPORT.json`, and `MACRO.json` are still stale in the live root reports on May 3, 2026, so event-sensitive answers remain partly degraded.
- `DERIVATIVES.json` still writes `0 coins`, so Deezoh, Hermes, screener, and macro remain weak on positioning context.
- `SCOUT_REPORT.json` and `MACRO_BIAS.json` still lack explicit workflow ids, so screener and macro workflow audits remain inference-based.
- The execution-facing contradiction still needs a real pipeline guard:
  - macro says `STAY OUT`
  - `ENTRY_SIGNALS.json` still says `READY_TO_TRADE`
  - Hermes explicitly calls this a system design flaw rather than a judgment difference

### Optimization Queue Updates

- `Q-2026-05-03-07` Keep Deezoh canonical workflow ids and workflow-rationale fields under deterministic smoke coverage. Status: done.
- `Q-2026-05-03-08` Add explicit workflow-id fields to `SCOUT_REPORT.json` and `MACRO_BIAS.json` so the improvement loop can audit screener and macro routing directly. Status: queued.
- `Q-2026-05-03-09` Add a macro-veto gate to suppress `READY_TO_TRADE` when macro remains `STAY OUT`. Status: queued.
- `Q-2026-05-03-10` Keep Hermes trace top-level fields populated from the normalized lead thesis so audits do not have to parse nested payloads first. Status: done.

## 2026-05-03 Workflow Contract Fields And Macro Builder Root Repair

### What Actually Ran

- Re-ran the deterministic local Deezoh observation suite for the four required chart-side cases plus pre-event, post-event, and data-degraded control cases:
  - `breakout_watch -> breakout_acceptance`
  - `consolidation -> consolidation_resolution`
  - `news_event -> news_event_control`
  - `failed_breakout -> liquidity_trap`
- Patched the report-source builders instead of layering more monitor-only logic on top:
  - local + live `scripts/build_scout_report.py`
  - local + live `scripts/desk_contract_bridge.py`
  - local + live `scripts/macro_bias_builder.py`
- Added bounded local proof for the new contract surfaces:
  - `python scripts/simulator/test_desk_contract_bridge_entry_signals.py`
  - `python scripts/tests/workflow_contract_surfaces_smoke.py`
- Ran a bounded live rebuild on `root@100.67.172.114` for:
  - `python3 scripts/macro_bias_builder.py`
  - `python3 scripts/build_scout_report.py`
  - `python3 scripts/desk_contract_bridge.py --target entry`
- Read back the live `MACRO_BIAS.json`, `SCOUT_REPORT.json`, `ENTRY_SIGNALS.json`, `DEEZOH_THOUGHTS.json`, and `HERMES_DECISION_TRACE.json` from `/root/openclawtrading/reports/auto/`.

### New Evidence From This Run

- Issue `DHI-050` status update
  Raw event: fresh live `SCOUT_REPORT.json` now exposes `selected_workflow = no_trade_protection`, and fresh live `MACRO_BIAS.json` now exposes `selected_workflow = data_degraded_mode`.
  What happened: the screener and macro report contracts now carry first-class workflow ids plus workflow reasons, so the improvement loop no longer has to infer those lanes from summary text alone.
  Why it matters: this closes the weakest blind spot in the screener/macro audit and makes workflow-selection regressions testable.
  Recurrence: verified live on May 3, 2026 after the bounded rebuild.
  Affected agent/workflow/data source/timeframe: screener workflow audit, macro workflow audit, recurring improvement loop.
  Proposed fix: keep the new workflow fields under smoke coverage and preserve them in future report-builder refactors.
  Owner: `codex-main-thread`
  Risk: `low`
  Approval needed: `no`
  Proof test: live `SCOUT_REPORT.json` and `MACRO_BIAS.json` now each expose `selected_workflow` plus `workflow_reason`.
  Status: `fixed and verified`

- Issue `DHI-052`
  Raw event: the live VPS copy of `scripts/macro_bias_builder.py` wrote `MACRO_BIAS.json` to `/root/reports/auto` instead of `/root/openclawtrading/reports/auto` because its base-dir math assumed the nested local file layout.
  What happened: the local nested script layout and the live flat script layout were both using the same `parent.parent.parent` rule, which resolves to the workspace root locally but the wrong `/root` directory live.
  Why it matters: the macro lane could appear repaired locally while the live active report root stayed stale, which undermines every downstream audit.
  Recurrence: reproduced live at the start of this run and fixed in the same pass.
  Affected agent/workflow/data source/timeframe: macro-bias builder, live report-root truth, desk-chain downstream consumers.
  Proposed fix: keep the new ancestor search that resolves the first directory containing both `reports/auto` and `scripts`.
  Owner: `codex-main-thread`
  Risk: `low`
  Approval needed: `no`
  Proof test: fresh live `python3 scripts/macro_bias_builder.py` now writes `/root/openclawtrading/reports/auto/MACRO_BIAS.json`.
  Status: `fixed and verified`

- Issue `DHI-053`
  Raw event: after the fresh macro rebuild produced `MACRO_BIAS.json verdict = MIXED` and `selected_workflow = data_degraded_mode`, the rebuilt `ENTRY_SIGNALS.json` still carried `macro_verdict = STAY OUT` and `macro_gate = BLOCKED_BY_MACRO`.
  What happened: the entry bridge now exposes the contradiction clearly through `effective_entry_state`, `recommendation`, and macro-gate fields, but the upstream entry layer still embeds an older macro verdict than the fresh macro report.
  Why it matters: the contradiction is now visible instead of hidden, but the system still needs a real source-of-truth decision about whether entry readiness should follow the latest macro report or an embedded upstream lane snapshot.
  Recurrence: verified live on May 3, 2026 after the bounded rebuild.
  Affected agent/workflow/data source/timeframe: entry-signals bridge, macro gate contract, execution-facing desk outputs, Hermes/Deezoh contradiction audit.
  Proposed fix: trace where the stale embedded macro verdict enters the entry pipeline, then choose one canonical source for the gate before suppressing or promoting `READY_TO_TRADE`.
  Owner: `entry-watch + pipeline-watchdog + codex-main-thread`
  Risk: `medium`
  Approval needed: `review before changing the execution-facing gate policy`
  Proof test: a fresh cycle should either align `ENTRY_SIGNALS.json macro_verdict` with the active `MACRO_BIAS.json` verdict or emit an explicit cross-layer mismatch field instead of silently disagreeing.
  Status: `open`

### Proved

- The Deezoh observation suite still covers the exact chart-style scenarios this loop requires most often, and all local cases passed after the contract changes.
- The live screener lane now declares its workflow directly:
  - `SCOUT_REPORT.json selected_workflow = no_trade_protection`
  - `SCOUT_REPORT.json workflow_reason` explains the freshness/protection stance
- The live macro lane now declares its workflow directly and writes to the correct report root:
  - `MACRO_BIAS.json selected_workflow = data_degraded_mode`
  - `MACRO_BIAS.json workflow_reason` explains why missing/empty macro inputs force degraded mode
  - `MACRO_BIAS.json` now writes under `/root/openclawtrading/reports/auto/`
- The live entry bridge now exposes the contradiction more honestly even though the upstream mismatch remains:
  - `ENTRY_SIGNALS.json entry_state = READY_TO_TRADE`
  - `ENTRY_SIGNALS.json effective_entry_state = BLOCKED_BY_MACRO`
  - `ENTRY_SIGNALS.json recommendation = NO_TRADE`
  - `ENTRY_SIGNALS.json macro_gate_workflow = data_degraded_mode`
- Hermes still remains cautious in the latest readable trace:
  - `HERMES_DECISION_TRACE.json decision = no_trade`
  - `direction = SHORT`
  - summary still calls out the macro-gate versus ready-to-trade contradiction

### Safe Changes Applied This Run

- Local + live `scripts/build_scout_report.py`
- Local + live `scripts/desk_contract_bridge.py`
- Local + live `scripts/macro_bias_builder.py`
- Local `scripts/simulator/test_desk_contract_bridge_entry_signals.py`
- Local `scripts/tests/workflow_contract_surfaces_smoke.py`

### Remaining Issues

- `NEWS.json` and `CATALYST_REPORT.json` are still stale by roughly 4.7 hours in the live root reports, so event-sensitive answers remain degraded.
- `MACRO_BIAS.json` is now fresh at the correct root, but it is still in `data_degraded_mode` because the macro/news inputs are thin.
- `ENTRY_SIGNALS.json` still disagrees with the fresh macro report and needs a canonical gate-source decision before a true macro-veto policy change lands.
- `DERIVATIVES.json` still writes `0 coins`, so positioning context remains weak for Deezoh, Hermes, screener, and macro.

### Optimization Queue Updates

- `Q-2026-05-03-08` Add explicit workflow-id fields to `SCOUT_REPORT.json` and `MACRO_BIAS.json` so the improvement loop can audit screener and macro routing directly. Status: done.
- `Q-2026-05-03-09` Add a macro-veto gate to suppress `READY_TO_TRADE` when macro remains `STAY OUT`. Status: narrowed. The bridge now exposes `effective_entry_state`, but the upstream macro-verdict source mismatch must be resolved before a policy-level suppression is safe.
- `Q-2026-05-03-11` Resolve the entry-layer macro source mismatch so `ENTRY_SIGNALS.json` and the fresh `MACRO_BIAS.json` stop disagreeing silently. Status: queued.

## 2026-05-03 Hermes Publish Order Repair And Macro Workflow Selector Audit

### What Actually Ran

- Re-ran the deterministic local Deezoh observation suite for the required chart-style scenarios:
  - `breakout_watch -> breakout_acceptance`
  - `consolidation -> consolidation_resolution`
  - `news_event -> news_event_control`
  - `failed_breakout -> liquidity_trap`
- Re-ran the bounded local contract tests:
  - `python scripts/tests/workflow_contract_surfaces_smoke.py`
  - `python scripts/simulator/test_desk_contract_bridge_entry_signals.py`
- Ran a targeted local workflow audit for the screener families:
  - `accumulation_hunt`
  - `continuation`
  - `post_news_rotation`
  - `failed_breakout_short`
  - `range_rotation`
  - `no_trade_protection`
- Ran a targeted local workflow audit for the macro families:
  - `pre_event_control`
  - `post_event_digest`
  - `cross_asset_divergence`
  - `unusual_behavior_precedent_capture`
  - `data_degraded_mode`
- Pulled fresh live proof from `root@100.67.172.114` for:
  - `/root/openclawtrading/reports/auto/DEEZOH_THOUGHTS.json`
  - `/root/openclawtrading/reports/auto/SCOUT_REPORT.json`
  - `/root/openclawtrading/reports/auto/MACRO_BIAS.json`
  - `/root/openclawtrading/reports/auto/ENTRY_SIGNALS.json`
  - `/root/openclawtrading/reports/auto/HERMES_DECISION_TRACE.json`
  - `/root/openclawtrading/reports/auto/HERMES_LANE_THESIS.json`
- Read bounded live evidence from:
  - root crontab
  - `/root/.openclaw/logs/desk_observability.log`
  - `/root/.openclaw/logs/macro_bias.log`
  - `/root/.openclaw/logs/derivatives.log`
  - `/root/.openclaw/logs/openclaw.log`
- Ran a bounded live paper-only Hermes cycle:
  - `python3 scripts/hermes_runtime_bridge.py --timeout-seconds 180 --quiet`
- Ran a bounded live macro rebuild after the selector fix:
  - `python3 scripts/macro_bias_builder.py`

### New Evidence From This Run

- Issue `DHI-054`
  Raw event: a bounded live Hermes rerun refreshed `HERMES_DECISION_TRACE.json`, but `HERMES_LANE_THESIS.json` still stayed `invalid_runtime_input` with the stale summary `Hermes runtime input is stale ... evidence_pack_id does not match ...`.
  What happened: `scripts/hermes_runtime_bridge.py` rebuilt the dual-lane experiment before Hermes wrote fresh `HERMES_RUNTIME_INPUT.json`, so the thesis artifact was published from the previous cycle while the trace artifact reflected the new cycle.
  Why it matters: the Hermes lane could look both fresh and invalid at the same time, which weakens every recurring audit and makes the advisor lane look more broken than it is.
  Recurrence: reproduced live on May 3, 2026 before the repair.
  Affected agent/workflow/data source/timeframe: Hermes runtime bridge, dual-lane experiment publish contract, recurring Hermes audit.
  Proposed fix: republish the dual-lane builder after the bridge writes fresh `HERMES_RUNTIME_INPUT.json` so the thesis and advisor review stay on the same frozen runtime pack as the trace.
  Owner: `codex-main-thread`
  Risk: `low`
  Approval needed: `no`
  Proof test: after syncing the patched bridge and rerunning `python3 scripts/hermes_runtime_bridge.py --timeout-seconds 180 --quiet`, live `HERMES_LANE_THESIS.json`, `HERMES_ADVISOR_REVIEW.json`, and `HERMES_DECISION_TRACE.json` all refreshed to the same `generated_at = 2026-05-02T23:57:36Z`, share `evidence_pack_id = 6f935bb142e313be`, and show `status = ready`.
  Status: `fixed and verified`

- Issue `DHI-055`
  Raw event: the deterministic macro audit routed both `post_event_digest` and `unusual_behavior_precedent_capture` scenarios to `cross_asset_divergence`.
  What happened: `scripts/macro_bias_builder/macro_bias_builder.py` let the generic `verdict == MIXED` branch fire before checking post-event or unusual-behavior signals, so two required workflow families were effectively unreachable under mixed conditions.
  Why it matters: the improvement loop would over-credit cross-asset divergence and under-detect post-event digestion or anomaly capture, which directly weakens macro workflow quality grading.
  Recurrence: reproduced locally on May 3, 2026 with deterministic selector inputs before the repair.
  Affected agent/workflow/data source/timeframe: macro workflow selector, workflow-quality audit, recurring Deezoh/Hermes improvement loop.
  Proposed fix: prioritize explicit `POST_EVENT` / post-event summary signals and unusual-behavior flags before the generic mixed fallback, then pin those cases in smoke coverage.
  Owner: `codex-main-thread`
  Risk: `low`
  Approval needed: `no`
  Proof test: local audit now returns `post_event_digest` for a post-event mixed case and `unusual_behavior_precedent_capture` for an anomaly-flagged mixed case; `python scripts/tests/workflow_contract_surfaces_smoke.py` passes with the new assertions.
  Status: `fixed and verified`

### Proved

- The required Deezoh observation suite still passes locally for breakout, consolidation, news-event, and failed-breakout/liquidity-trap scenarios.
- The screener selector now returns the expected workflow ids for the audited families:
  - `accumulation_hunt`
  - `continuation`
  - `post_news_rotation`
  - `failed_breakout_short`
  - `range_rotation`
  - `no_trade_protection`
- The macro selector now returns the expected workflow ids for the audited families:
  - `pre_event_control`
  - `post_event_digest`
  - `cross_asset_divergence`
  - `unusual_behavior_precedent_capture`
  - `data_degraded_mode`
- Current live Deezoh-side truth at read time:
  - `DEEZOH_THOUGHTS.json selected_workflow = accumulation_hunt`
  - `winner = no_trade`
  - `next_question.agent = macro-bias`
  - `wait_state.wait_type = WAIT_TRIGGER`
- Current live screener and macro truth at read time:
  - `SCOUT_REPORT.json selected_workflow = no_trade_protection`
  - `MACRO_BIAS.json selected_workflow = data_degraded_mode`
  - `ENTRY_SIGNALS.json macro_verdict = MIXED`
  - `ENTRY_SIGNALS.json effective_entry_state = READY_TO_TRADE`
- Current live Hermes truth after the bounded rerun:
  - `HERMES_LANE_THESIS.json status = ready`
  - `HERMES_LANE_THESIS.json decision = no_trade`
  - `HERMES_ADVISOR_REVIEW.json status = ready`
  - `HERMES_DECISION_TRACE.json status = ready`
- Current live blockers remain upstream rather than selector-only:
  - `NEWS.json` stale by about 403 minutes at read time
  - `CATALYST_REPORT.json` stale by about 403 minutes at read time
  - `MACRO.json` still stale in manager output
  - `DERIVATIVES.json` still writes `0 coins`
  - `DIVERGENCES.json` missing
  - `ALTFINS.json` missing
- Current live cron still refreshes collectors and the desk observability chain, but it does not directly schedule Hermes:
  - collectors every 30 minutes
  - desk observability chain at minute `5,35`
  - no separate live Hermes cron entry present in root crontab

### Safe Changes Applied This Run

- Local + live `scripts/hermes_runtime_bridge.py`
- Local + live `scripts/macro_bias_builder/macro_bias_builder.py`
- Local `scripts/tests/workflow_contract_surfaces_smoke.py`

### Remaining Issues

- Hermes is now internally consistent when run, but it is still not part of the live root cron schedule, so Hermes can go stale again unless the desk triggers it explicitly or Sal approves scheduler ownership.
- `NEWS.json`, `CATALYST_REPORT.json`, and `MACRO.json` are still stale, so event-sensitive Deezoh and Hermes judgments remain degraded.
- `DERIVATIVES.json` still writes `0 coins`, and `DIVERGENCES.json` / `ALTFINS.json` are still missing, so positioning and rotation context are still weak.
- `ENTRY_SIGNALS.json` still says `effective_entry_state = READY_TO_TRADE` while the desk is otherwise caution-heavy and Hermes still resolves to `no_trade`; this remains an approval-sensitive execution-facing design question, not a safe reporting-only change.

### Optimization Queue Updates

- `Q-2026-05-03-10` Keep Hermes trace top-level fields populated from the normalized lead thesis so audits do not have to parse nested payloads first. Status: done.
- `Q-2026-05-03-12` Keep Hermes dual-lane artifacts republished from the same fresh runtime input that produced the trace. Status: done.
- `Q-2026-05-03-13` Keep post-event and unusual-behavior macro workflows pinned ahead of the generic mixed fallback. Status: done.
- `Q-2026-05-03-14` Decide whether Hermes should get explicit cron ownership or stay a bounded on-demand audit lane. Status: queued for Sal approval.

## 2026-05-03 Macro News Count Repair And Manager Status Contract Update

### What Actually Ran

- Re-ran the deterministic local Deezoh observation suite:
  - `python scripts/tests/deezoh_observation_suite_smoke.py`
- Re-ran the bounded local contract tests:
  - `python scripts/tests/workflow_contract_surfaces_smoke.py`
  - `python scripts/simulator/test_desk_contract_bridge_entry_signals.py`
  - `python scripts/tests/hermes_dual_lane_contract_smoke.py`
- Pulled fresh live truth from `root@100.67.172.114` for:
  - root crontab
  - `/root/.openclaw/logs/desk_observability.log`
  - `/root/.openclaw/logs/macro_bias.log`
  - `/root/.openclaw/logs/derivatives.log`
  - `/root/.openclaw/logs/openclaw.log`
  - `/root/openclawtrading/reports/auto/DEEZOH_THOUGHTS.json`
  - `/root/openclawtrading/reports/auto/SCOUT_REPORT.json`
  - `/root/openclawtrading/reports/auto/MACRO_BIAS.json`
  - `/root/openclawtrading/reports/auto/ENTRY_SIGNALS.json`
  - `/root/openclawtrading/reports/auto/HERMES_DECISION_TRACE.json`
  - `/root/openclawtrading/reports/auto/HERMES_LANE_THESIS.json`
  - `/root/openclawtrading/reports/auto/NEWS.json`
  - `/root/openclawtrading/reports/auto/CATALYST_REPORT.json`
  - `/root/openclawtrading/reports/auto/DERIVATIVES.json`
  - `/root/openclawtrading/reports/auto/MANAGER_STATUS.json`
- Ran a bounded live paper-only Hermes cycle:
  - `python3 scripts/hermes_runtime_bridge.py --timeout-seconds 180 --quiet`
- Synced safe reporting-contract repairs to the live repo runtime paths and re-ran:
  - `python3 scripts/macro_bias_builder.py`
  - `python3 scripts/manager_agent.py`

### New Evidence From This Run

- Issue `DHI-056`
  Raw event: live `NEWS.json` and `CATALYST_REPORT.json` were no longer multi-hour stale; `NEWS.json` carried `_meta.total_articles = 172` with a fresh `fetched_at`, and `CATALYST_REPORT.json timestamp = 2026-05-03T00:13:39.781768+00:00`.
  What happened: the earlier stale-news diagnosis is no longer the main blocker for this cycle.
  Why it matters: the remaining macro degradation is now better explained by empty derivatives plus stale `MACRO.json`, not by a dead news/catalyst fetch lane.
  Recurrence: verified live on May 3, 2026 in this run.
  Affected agent/workflow/data source/timeframe: macro, catalyst, Deezoh event-mode, Hermes paper lane, current desk cycle.
  Proposed fix: reframe the next debugging slice around derivatives coverage and macro-calendar freshness, not generic news freshness.
  Owner: `pipeline-watchdog + macro-bias`
  Risk: `low`
  Approval needed: `no`
  Proof test: re-read `NEWS.json`, `CATALYST_REPORT.json`, and the corresponding log timestamps in the same live pass.
  Status: `verified`

- Issue `DHI-057`
  Raw event: live `DEEZOH_THOUGHTS.json` still shows `next_question.dispatch_state = planned`, `selected_agents = ["macro-bias"]`, and a `dispatch_proof` string that says the row is planning only until a specialist run proves execution.
  What happened: Deezoh still names the next specialist lane and changes its wait/question framing, but the specialist interaction is still mostly declarative rather than visibly executed in the same cycle.
  Why it matters: Sal asked for real chart-desk behavior, and this is still short of fully visible agent-to-agent execution proof.
  Recurrence: verified live again on May 3, 2026.
  Affected agent/workflow/data source/timeframe: Deezoh observation loop, macro follow-up lane, execution-visibility audit.
  Proposed fix: keep one recurring audit case that requires either a fresh specialist artifact read or an explicit spawned/delegated proof row before Deezoh can claim the interaction happened.
  Owner: `architect-codex + orchestrator`
  Risk: `medium`
  Approval needed: `review before changing live delegation policy`
  Proof test: future live replay should show either a fresh macro specialist artifact consumed in-cycle or an executed delegation receipt instead of `dispatch_state = planned`.
  Status: `open`

- Issue `DHI-058`
  Raw event: the Windows flat mirror under `openclawtrading/scripts/` had older `macro_bias_builder.py` and `manager_agent.py` copies than the canonical tested scripts under `scripts/macro_bias_builder/` and `scripts/manager_agent/`.
  What happened: syncing the stale flat mirror to the VPS temporarily regressed live workflow/status fields until the tested canonical copies were mirrored back over the flat runtime paths.
  Why it matters: this is a real cross-platform continuity hazard; a well-intentioned sync can silently undo live improvements if the wrong local source is treated as canonical.
  Recurrence: reproduced in this run and fixed immediately.
  Affected agent/workflow/data source/timeframe: Windows mirror sync, live macro report contract, live manager status contract, future Codex repair passes.
  Proposed fix: treat the tested canonical scripts under `scripts/...` as the source for these lanes, and either remove drift or add an explicit mirror-check before future VPS syncs.
  Owner: `codex-main-thread`
  Risk: `medium`
  Approval needed: `no`
  Proof test: compare the flat mirror against the tested canonical copy before syncing and confirm the live rerun still exposes workflow/status fields afterward.
  Status: `fixed and verified`

- Issue `DHI-059`
  Raw event: live macro builder console output previously printed `News: 0 articles` even when `NEWS.json` contained populated nested article categories, and `MACRO_BIAS.json data_sources.news_articles` followed the same stale assumption.
  What happened: the runtime output was still reading the old `total_articles` field instead of counting the current nested `articles` schema.
  Why it matters: the macro lane looked more data-starved than it really was, which can mislead operator audits and future debugging.
  Recurrence: reproduced and fixed on May 3, 2026.
  Affected agent/workflow/data source/timeframe: macro-bias builder, operator logs, `MACRO_BIAS.json`, recurring improvement loop.
  Proposed fix: use the same nested-article counting logic for runtime logging and `data_sources.news_articles` that the workflow selector already uses.
  Owner: `codex-main-thread`
  Risk: `low`
  Approval needed: `no`
  Proof test: fresh live `python3 scripts/macro_bias_builder.py` must print `News: 172 articles`, and `MACRO_BIAS.json data_sources.news_articles` must match `172`.
  Status: `fixed and verified`

- Issue `DHI-060`
  Raw event: `MANAGER_STATUS.json` required inference from nested summary fields to answer a simple question like "is the manager degraded right now?" because it lacked top-level `status`, `overall_status`, and `generated_at`.
  What happened: the manager contract was usable but slower to consume in downstream desk summaries and quick audits.
  Why it matters: this loop repeatedly needs a fast machine-readable manager health line, and contract ambiguity wastes time.
  Recurrence: verified in this run and fixed in the same pass.
  Affected agent/workflow/data source/timeframe: manager agent, operator snapshot builders, paper watchdog summaries, recurring Deezoh/Hermes audit loop.
  Proposed fix: emit top-level `status`, `overall_status`, `health`, and `generated_at` aliases alongside the existing summary payload.
  Owner: `codex-main-thread`
  Risk: `low`
  Approval needed: `no`
  Proof test: fresh live `MANAGER_STATUS.json` must expose `status = DEGRADED`, `overall_status = DEGRADED`, and a top-level `generated_at` timestamp.
  Status: `fixed and verified`

### Proved

- The required local Deezoh/Hermes safety suite still passes:
  - `deezoh_observation_suite_smoke`
  - `workflow_contract_surfaces_smoke`
  - `test_desk_contract_bridge_entry_signals`
  - `hermes_dual_lane_contract_smoke`
- Live Deezoh still changes the desk framing, but not via visible same-cycle specialist execution:
  - `DEEZOH_THOUGHTS.json selected_workflow = accumulation_hunt`
  - `winner = short`
  - `next_question.agent = macro-bias`
  - `next_question.dispatch_state = planned`
  - `wait_state.wait_type = WAIT_TRIGGER`
- Live screener and macro remain intentionally cautious for different reasons:
  - `SCOUT_REPORT.json selected_workflow = range_rotation`
  - `MACRO_BIAS.json selected_workflow = data_degraded_mode`
  - `MACRO_BIAS.json verdict = MIXED`
  - `MACRO_BIAS.json data_sources.news_articles = 172`
- Live entry and Hermes still disagree on whether "ready" should become action:
  - `ENTRY_SIGNALS.json effective_entry_state = READY_TO_TRADE`
  - `ENTRY_SIGNALS.json macro_gate = CLEAR`
  - `ENTRY_SIGNALS.json macro_gate_workflow = data_degraded_mode`
  - `HERMES_DECISION_TRACE.json decision = no_trade`
- The remaining live blockers are narrower than the last stale-news framing suggested:
  - `MACRO.json` is still stale by about 24 hours
  - `DERIVATIVES.json` still writes `0 coins`
  - `DIVERGENCES.json` is still missing/stale
  - `ALTFINS.json` is still missing
  - `ACTIVE_TRADES.json` is stale in the manager lane

### Safe Changes Applied This Run

- Local canonical + flat mirror `scripts/macro_bias_builder/macro_bias_builder.py` and `openclawtrading/scripts/macro_bias_builder.py`
- Local canonical + flat mirror `scripts/manager_agent/manager_agent.py` and `openclawtrading/scripts/manager_agent.py`
- Live repo sync:
  - `/root/openclawtrading/scripts/macro_bias_builder.py`
  - `/root/openclawtrading/scripts/manager_agent.py`

### Remaining Issues

- The biggest live data weakness is still derivatives and macro-calendar freshness, not the raw news fetcher.
- Deezoh still plans a macro follow-up without clear same-cycle specialist execution proof.
- Hermes remains paper-safe and cautious, but it still is not directly scheduled by root cron.
- The local `openclawtrading/scripts/` mirror cannot be trusted blindly for these lanes unless its drift from `scripts/...` is removed or checked first.

### Optimization Queue Updates

- `Q-2026-05-03-15` Add or enforce a mirror-consistency check before syncing `openclawtrading/scripts/*` runtime copies to the live VPS. Status: queued.
- `Q-2026-05-03-16` Require at least one visibly executed specialist follow-up proof in the recurring Deezoh observation suite instead of accepting `dispatch_state = planned`. Status: queued.
- `Q-2026-05-03-17` Keep macro runtime logging and `data_sources` aligned with the current nested `NEWS.json` schema. Status: done.
- `Q-2026-05-03-18` Keep top-level manager status aliases present so desk summaries do not need nested inference. Status: done.

## 2026-05-03 Heartbeat Derivatives And Chart Freshness Repair

### Trigger

- Heartbeat: `deezoh-15-minute-observation-loop`
- Objective: retest Deezoh, screener, macro, and related agent interactions as if Sal is looking at charts; verify Deezoh names the right workflow, pushes back instead of yes-manning, updates the next question from evidence, and records unsafe lessons as monitor issues.

### What Ran

- Rechecked live report freshness and quality for chart, derivatives, macro, scout, and Deezoh thought surfaces.
- Patched the live desk observability chain so chart analysis is regenerated before `desk_contract_bridge.py` publishes the bridge-facing `CHART_ANALYSIS.json`.
- Patched the derivatives fetcher so an empty Coinglass payload no longer leaves `DERIVATIVES.json` with zero usable coins; it now fills a degraded Binance Futures fallback from market scanner and scan-history data.
- Rebuilt the live desk observability chain and replayed a Deezoh-style chart question against the fresh outputs.

### Issues Captured

- Issue `DHI-061`
  Raw event: `run_desk_observability_chain.sh` refreshed `CHART_ANALYSIS.json` through the bridge while the underlying `CHART_ANALYSIS_latest.json` could still be stale.
  What happened: downstream consumers saw a fresh bridge mtime even though the producer output was from an older cycle.
  Why it matters: this can make Deezoh think chart evidence is fresher than it really is.
  Recurrence: reproduced on the May 3 heartbeat and fixed in the same pass.
  Affected agent/workflow/data source/timeframe: chart analyzer, desk contract bridge, Deezoh chart workflow, 15-minute observation loop.
  Proposed fix: run the chart analyzer/generator inside the desk observability chain before the bridge step.
  Owner: `codex-main-thread`
  Risk: `low`
  Approval needed: `no`
  Proof test: fresh live chain run must update `CHART_ANALYSIS_latest.json`, `CHART_ANALYZER_EXECUTION.json`, and `CHART_ANALYSIS.json` in the same cycle.
  Status: `fixed and verified`

- Issue `DHI-062`
  Raw event: `DERIVATIVES.json` reported `source = coinglass` but had empty `coins` and no clear top-level quality/status fields.
  What happened: the derivatives lane looked present but provided no usable per-coin funding/OI context.
  Why it matters: Deezoh, screener, and manager can overtrust a lane that exists but is effectively empty.
  Recurrence: reproduced on the May 3 heartbeat and fixed with degraded fallback behavior.
  Affected agent/workflow/data source/timeframe: derivatives fetcher, manager agent, Deezoh evidence quality, screener follow-up context.
  Proposed fix: when Coinglass files are empty, fill partial per-coin funding/OI context from Binance Futures scanner and scan-history outputs, and mark the result degraded.
  Owner: `codex-main-thread`
  Risk: `low`
  Approval needed: `no`
  Proof test: fresh live `DERIVATIVES.json` must expose `status`, `data_quality`, `coins_count`, market fallback fields, and non-empty BTC/ETH/SOL records when scanner context exists.
  Status: `fixed and verified`

- Issue `DHI-063`
  Raw event: after chart and derivatives fixes, Deezoh still selected `winner = short` from the current thought surface while chart evidence was partial, trend labels conflicted with bullish EMA/MACD, and the entry signal was null.
  What happened: Deezoh's replay pushed back correctly, but the scoring output still needs a confidence discount for internal contradiction.
  Why it matters: this is exactly the kind of beginner-trader trap Sal warned about: copying a preferred side from weak or contradictory evidence.
  Recurrence: observed in this heartbeat; not fixed yet.
  Affected agent/workflow/data source/timeframe: Deezoh scoring, chart-analysis consumer, trading-coach overlay, 15-minute chart workflow.
  Proposed fix: add an explicit contradiction discount when side selection conflicts with trigger readiness, EMA/MACD evidence, or partial chart quality.
  Owner: `architect-codex`
  Risk: `needs_review`
  Approval needed: `no for queue capture; review before durable scoring change`
  Proof test: replay a weak tempting short question and verify Deezoh keeps `WATCH/NO_TRADE` primary unless trigger, invalidation, and fresh confirmation line up.
  Status: `queued`

### Proved

- Chart freshness is no longer hidden by the bridge:
  - `CHART_ANALYSIS_latest.json`, `CHART_ANALYZER_EXECUTION.json`, and `CHART_ANALYSIS.json` were all refreshed in the same live chain cycle.
  - `CHART_ANALYSIS.json data_quality = PARTIAL`
  - `CHART_ANALYSIS.json zone_confirmed = false`
  - `CHART_ANALYSIS.json specialist_verified = false`
- Derivatives are no longer empty:
  - `DERIVATIVES.json source = coinglass+market_scanner_binance_futures_fallback`
  - `DERIVATIVES.json status = degraded_fallback`
  - `DERIVATIVES.json data_quality = PARTIAL`
  - `DERIVATIVES.json coins_count = 30`
  - Manager derivatives alert cleared; overall manager unhealthy count dropped from 6 to 5.
- Deezoh replay passed the not-a-yes-man behavior check:
  - It kept the practical posture at `WATCH`.
  - It explicitly vetoed activation from partial chart evidence.
  - It named the contradiction between the short label, bullish EMA/MACD, null entry signal, low volume, FOMC timing, and weekend Asia liquidity.
  - It recorded unsafe-learning concerns instead of treating the current `short` winner as a durable lesson.

### Remaining Issues

- TradingView CDP is still not giving a usable chart target: `/json/version` works on port `9222`, but `/json/list` is empty and `/json/new` returns HTTP 500.
- Indicator and strategy reports are still missing from the same-cycle desk bundle.
- Catalyst, news, divergence, and macro-calendar freshness still need repair or clearer degraded-mode handling.
- Council output still needs a visible critic lane.
- The derivatives fallback is intentionally partial; it does not replace Coinglass long/short ratios, liquidation heatmaps, or full liquidation context.
- BTC open-interest units from the fallback need a sanity check before being used as high-confidence evidence.

### Optimization Queue Updates

- `Q-2026-05-03-19` Run chart producer before bridge publishing in the desk observability chain. Status: done.
- `Q-2026-05-03-20` Fill empty derivatives lane with explicit degraded Binance Futures fallback and quality fields. Status: done.
- `Q-2026-05-03-21` Add Deezoh scoring contradiction discount for partial chart evidence, null trigger, and indicator-side conflict. Status: queued.
- `Q-2026-05-03-22` Repair TradingView CDP chart target discovery or route chart visual inspection through a different verified surface. Status: queued.
- `Q-2026-05-03-23` Restore same-cycle indicator, strategy, catalyst, divergence, and critic-lane proof for the Deezoh observation bundle. Status: queued.
