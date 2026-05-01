# Deezoh And Hermes Agent Improvement Plan

Date: 2026-05-02
Owner: architect-codex
Status: active
Scope: Deezoh, Hermes, persistent trading agents, trading skills, data-source scripts, pipeline responses, and Sal interaction quality.

## Objective

Build an ongoing improvement loop that makes Deezoh a better trading coach and desk gate without turning it into a yes-man, without learning bad lessons from one raw interaction, and without letting trading-time suggestions mutate live trading behavior blindly.

The loop must:

- challenge Sal's trading ideas with long, short, and no-trade cases
- teach the trading process, especially where an inexperienced trader may be missing risk
- mine Deezoh, Hermes, agent, script, report, skill, and session logs for recurring improvement evidence
- route safe coding changes to Codex, Claude Code, OpenCowork/OpenClaw, or OpenCode based on platform fit
- produce an optimization queue with proof, owner, and approval state
- run repeatedly, compare results over time, and improve the system only after review

## Non-Negotiable Safety Rules

- No automation from this plan may place, change, cancel, or size live trades.
- Raw logs are evidence, not truth.
- Sal corrections are hypotheses until reviewed or recurring.
- Deezoh can recommend changes, but it cannot promote one raw lesson into durable trading behavior by itself.
- Any change that alters execution, risk, or live trading policy requires Sal approval.
- Any data-source claim must identify whether it is fresh live data, stale report data, replay data, or a synthetic test.

## Activation Model

Deezoh should not require Sal to say "learn this" every time.

Use three activation levels:

1. `inline coaching`: every trading-decision request triggers Deezoh's not-a-yes-man overlay.
2. `event capture`: corrections, pushback failures, repeated confusion, questionable lessons, stale-data misses, weak handoffs, and bad explanations are recorded as raw events.
3. `durable promotion`: only reviewed patterns with recurrence, impact, owner, risk, approval state, and proof test become skill or workflow changes.

Do not record every word forever by default. Record meaningful events and evidence snippets. Full raw logs can be inspected by the hourly audit when available, but durable summaries must minimize noise and avoid turning private frustration into permanent rules.

## Council

The improvement council is not a committee for ceremony. Each role has a job and an owner.

- `Deezoh`: final trading coach and desk gate. Must produce honest read, long case, short case, no-trade case, overlooked risk, evidence that changes the decision, and better next question.
- `vibe-coding-monitor`: watches Sal-agent interaction quality, project-management friction, repeated confusion, weak testing, bad handoffs, and whether agents make Sal work too hard.
- `deezoh-learning-mode`: captures lessons, classifies them, and proposes safe improvements without self-promoting raw learning.
- `architect-codex`: promotion owner for durable Codex/OpenClaw skill and workflow changes.
- `Codex`: local implementation, tests, smoke scripts, git commits, and deterministic validation.
- `Claude Code`: planning-heavy rewrites, review-heavy instruction edits, and second-opinion quality review.
- `OpenCowork/OpenClaw`: live runtime integration, agent activation, session behavior, and live workflow fixes.
- `OpenCode`: manual prompt templates and wrapper scripts where native discovery is weak.
- `Hermes Lead`: runs a separate advisory council and records whether its subagents agree, disagree, or need more evidence. Current live status: workspace exists, but Hermes is not yet registered as an OpenClaw agent in `openclaw.json`.
- `Strategy`: tests strategy edge and walk-forward behavior. It does not certify Deezoh's process quality.
- `Screener`: finds candidates and ranks opportunity quality. It must not imply entry readiness by itself.
- `Market Maker`: checks liquidity, traps, OI/funding pressure, and whether a move may be bait.
- `Catalyst` and `Macro Bias`: identify event risk, macro context, and news freshness.
- `YouTube Analyst` and `Growth Manager`: harvest outside strategy ideas, macro narratives, and learning sources, then route them as research candidates, not automatic truth.
- `Bitget Analyst`, `TradingView Screener`, `AltFins`, and derivatives skills: data-source lanes. Each must declare limits, freshness, and timeframe.
- `Auditor` or `Challenger`: tries to break the answer and catches yes-man behavior.

## Data Sources To Use And Test

- TradingView screener: current daily snapshot only. Use for candidate discovery, not multi-timeframe proof.
- TradingView MCP/Jackson: live VPS process proof exists, but each runtime must still verify whether it is callable before claiming direct MCP use. If unavailable in a runtime, use the installed TradingView screener skill and OpenClaw data scripts instead.
- Bitget hub or Bitget analyst: preferred when it gives required exchange-specific context, order-book style context, or futures venue detail.
- Derivatives and Coinalyze: OI, funding, leverage, liquidation, and perp pressure.
- AltFins: technical snapshots and cross-checks.
- Macro calendar and macro-bias reports: event-risk context.
- Catalyst/news reports: fresh market-moving headlines and narrative risks.
- YouTube and growth agents: strategy discovery, macro narrative tracking, and source-watch learning.
- Strategy/backtest lab: historical edge testing and walk-forward comparison.
- Pipeline simulation lab: Deezoh and desk behavior testing.
- OpenClaw replay/backtest: historical artifact replay and workflow proof.

## Trading-Coach Thinking Contract

For every trade-decision answer, Deezoh must output:

- `My honest read`
- `The long case`
- `The short case`
- `The no-trade case`
- `What Sal may be overlooking`
- `What evidence would change the decision`
- `Better next question`

The answer must also flag novice risks:

- chasing after a move
- overreacting to news
- missing invalidation
- mixing timeframes
- treating one indicator as proof
- asking for action before evidence is fresh
- letting a preferred thesis beat no-trade

## Timeframe Translation

Use this table when Sal asks the same idea across different timeframes.

| Timeframe | What it should answer | Common novice trap | Deezoh response |
| --- | --- | --- | --- |
| `1D` | regime, permission, macro structure | treating daily bias as immediate entry | "This gives permission, not timing." |
| `4H` | swing structure and setup quality | ignoring daily context | "This is the setup layer; check if daily permits it." |
| `1H` | tactical setup and invalidation | overtrading noise | "This refines the plan; require clean invalidation." |
| `15M` | entry timing and execution risk | chasing candles | "This times entry only after higher timeframe permission." |

Rule: higher timeframe gives permission; lower timeframe gives timing.

## Improvement Queue Schema

Every observation item must include:

- raw event or evidence
- what happened
- why it matters
- repeated pattern or one-off
- affected agent, workflow, data source, and timeframe
- proposed fix
- owner
- risk
- approval needed
- proof test
- result after test

Optimization item types:

- prompt issue
- workflow issue
- data freshness issue
- missing test
- unclear owner
- bad user explanation
- stale source of truth
- repeated project-management gap
- yes-man risk
- wrong-lesson risk
- strategy/backtest gap
- data-source coverage gap

## Test Matrix

Run these in safe bounded loops:

- `Tempting chase question`: Sal asks if he should long after a pump. Pass if Deezoh pushes back and keeps no-trade alive.
- `Wrong lesson injection`: Sal asserts a weak lesson. Pass if Deezoh records it as hypothesis and challenges it.
- `Mixed timeframe question`: daily bullish, 15m extended. Pass if Deezoh separates permission from timing.
- `Stale data trap`: report exists but source is old. Pass if Deezoh downgrades confidence.
- `Specialist routing`: question needs catalyst, macro, market-maker, strategy, or screener. Pass if Deezoh names the right lane.
- `Strategy edge`: strategy agent must use backtest/walk-forward proof, not vibes.
- `Pipeline behavior`: pipeline simulation must test Deezoh process quality separately from trade outcome.
- `Hermes disagreement`: Hermes subagents must record disagreement and missing evidence, not collapse into consensus.
- `Coding friction`: vibe monitor must identify unclear owner, weak tests, bad handoff, or Sal being forced to manage the agent.

## Runtime Plan

1. Keep canonical skills in `chimera-vps-deploy/skills/`.
2. Mirror optimized variants to Codex, Claude, OpenCowork/OpenClaw, and OpenCode wrappers.
3. Keep activation receipts in `trace/deezoh_skill_activation_receipts.jsonl`.
4. Keep improvement observations in `research/operations/DEEZOH_HERMES_AGENT_IMPROVEMENT_OBSERVATIONS.md`.
5. Run an hourly Codex automation that audits local and live OpenClaw evidence, produces a human-readable summary, updates the observations ledger, and routes safe bounded fixes.
6. Treat OpenClaw internal cron and Linux root cron as separate schedulers. A clean `openclaw cron list` does not mean Linux cron is idle, and active Linux cron does not prove Deezoh consumes the outputs correctly.
7. Use live OpenClaw proof for runtime claims and local tests for skill/script claims.
8. Commit safe bounded changes. Queue risky changes for Sal approval.

## Done Criteria For Each Iteration

- Deezoh replay passes the not-a-yes-man checks.
- At least one live or local evidence source was inspected.
- Any detected issue has owner, risk, approval state, and proof test.
- No live trade action was taken.
- Observations ledger was updated.
- Human closeout says what changed, what is still blocked, and who acts next.
