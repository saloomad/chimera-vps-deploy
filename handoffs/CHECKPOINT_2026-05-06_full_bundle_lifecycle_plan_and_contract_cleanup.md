# CHECKPOINT - full bundle lifecycle plan and contract cleanup

Date: 2026-05-06
Operator: Codex

## Objective

Continue the full Chimera bundle orchestration objective with prompt-upgrade, expert council, contract cleanup, and a durable implementation plan.

## What changed

Updated:

- `chimera-vps-deploy/skills/CHIMERA_RESEARCH_BUNDLE_TEMPLATE.md`
- `agents/entry-watch/TOOLS.md`
- `agents/youtube-analyst/TOOLS.md`
- `agents/execution/AGENTS.md`
- `agents/strategy/strategy_signal_generator.py`

Created:

- `chimera-vps-deploy/handoffs/PLAN_2026-05-06_full_chimera_bundle_lifecycle_orchestration.md`

## Council used

Five expert council roles inspected the system:

- bundle document architect
- data-source and script verification lead
- OpenClaw workflow / Lobster / hooks architect
- Deezoh behavior and agent architecture reviewer
- strategy and backtest lead

## Main decisions

- Keep the per-symbol `Chimera Research Bundle` as the parent decision packet.
- Do not overload it with all post-entry trade state.
- Add or link companion surfaces:
  - `Screener Packet`
  - `Entry / Active Trade State`
  - `Strategy Evidence Ledger`
  - `Learning / Review Ledger`
- Use Task Flow for durable lifecycle state.
- Use Lobster for bounded subflows.
- Use hooks for event receipts.
- Keep cron as a wake-up source only.
- Keep live trading disabled unless separately approved.

## Cleanup completed

- Removed the obsolete duplicate `## 12. Final Decision` block from the research bundle template.
- Verified the template now has exactly Parts 1 through 14.
- Fixed stale Part 11 references from `Position Management And Risk` to `Execution Plan, Orders, And Risk`.
- Fixed Part 14 source-list numbering.
- Replaced active stale `/home/open-claw` paths in:
  - `entry-watch/TOOLS.md`
  - `youtube-analyst/TOOLS.md`
  - `execution/AGENTS.md`
  - `strategy/strategy_signal_generator.py`
- `strategy_signal_generator.py` compiles locally and on the VPS.

## Live VPS sync

Synced to:

- `/root/openclawtrading/skills/CHIMERA_RESEARCH_BUNDLE_TEMPLATE.md`
- `/root/.openclaw/kimi-skills/CHIMERA_RESEARCH_BUNDLE_TEMPLATE.md`
- `/root/.openclaw/workspace/agents/entry-watch/TOOLS.md`
- `/root/.openclaw/workspace/agents/youtube-analyst/TOOLS.md`
- `/root/.openclaw/workspace/agents/execution/AGENTS.md`
- `/root/openclawtrading/agents/strategy/strategy_signal_generator.py`
- `/root/.openclaw/workspace/PLAN_2026-05-06_full_chimera_bundle_lifecycle_orchestration.md`

## Remaining first implementation slice

The next bounded implementation slice should be:

1. restore the VPS strategy backtest lane
2. generate real `combo_results.json`
3. split rough watch signals from proven strategy alerts
4. upgrade `STRATEGY_REPORT.json` into a stronger Part 12 evidence source
5. run BTC strategy matrix and then a full bundle-consumer simulation

## Known blockers

- strategy evidence is currently weak on VPS
- account/portfolio risk source is not yet proven
- optional YouTube/idea overlays are not live-proven
- old `trade-investigation.lobster` is not bundle-aware
- `taskflow.json` still points the routine market cycle at the old thin investigation flow
