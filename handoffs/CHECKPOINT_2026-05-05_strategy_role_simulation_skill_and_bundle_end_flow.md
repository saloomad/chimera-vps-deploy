# CHECKPOINT - strategy role, simulation skill, and bundle-end flow

Date: 2026-05-05
Operator: Codex

## Objective

Finish the missing operational layer around the upgraded bundle-end sections by:

- fixing stale strategy owner docs
- defining how the persistent strategy lane feeds Part 12
- creating a reusable bundle-consumer simulation skill
- documenting how Parts 11 through 14 should work together

## What changed

Updated:

- `agents/strategy/AGENTS.md`
- `agents/strategy/TOOLS.md`
- `agents/strategy/references/WORKFLOW.md`
- `agents/entry-watch/AGENTS.md`

Created:

- `agents/strategy/BUNDLE_ROLE_AND_BACKTEST_PLAN.md`
- `chimera-vps-deploy/skills/chimera-bundle-consumer-simulation/SKILL.md`
- `research/platforms/2026-05-05-bundle-end-orchestration-plan.md`
- `research/platforms/2026-05-05-btc-parts11-14-explained.md`

## Main outcome

The bundle-end contract is now clearer:

- `Part 11` is where entries, triggers, orders, leverage, stop loss, take profit, alerts, and account-risk limits live
- `Part 12` is where persistent strategy, replay, tracker, and backtest evidence raise or lower confidence
- `Part 13` is where Deezoh makes the final desk call
- `Part 14` is where YouTube and idea overlays stay optional and non-overriding

## Runtime and skill work

- mirrored the new `chimera-bundle-consumer-simulation` skill to:
  - `C:\Users\becke\.codex\skills`
  - `C:\Users\becke\.claude\skills`
  - `C:\Users\becke\.openclaw\skills`
  - `/root/openclawtrading/skills`
  - `/root/.openclaw/kimi-skills`
- mirrored the updated strategy and entry-watch docs to the live VPS runtime surfaces
- removed the stray mistaken file:
  - `/root/.openclaw/workspace/agents/entry-watch.AGENTS.md`

## Important live truth

Current VPS strategy runtime still shows a weak strategy artifact:

- `/root/openclawtrading/reports/auto/STRATEGY_REPORT.json`
  - `passing_strategies: 0`
  - `matching_strategy: false`
  - `win_rate: 0`
  - `profit_factor: 0`

That means `Part 12` should currently treat the runtime strategy lane as useful but not strong enough by itself.

## Remaining work

- optionally tighten `STRATEGY_REPORT.json` itself so runtime strategy evidence maps more directly into Part 12
- run a real Deezoh or pipeline consumer simulation using the new skill
- optionally attach hard replay/backtest proof to the BTC Part 12 example instead of leaving it as partial evidence
