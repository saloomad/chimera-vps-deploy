---
name: chimera-vps-4h-monitor
description: Windows-owned 4-hour monitor for the live Chimera VPS. Refreshes bounded audit surfaces, reads Deezoh/diary/trading reports, classifies issues, and writes a detailed local report with next fixes.
---

# Chimera VPS 4-Hour Monitor

Use this skill when the goal is:

- monitor what the live VPS is doing from the Windows machine
- keep a recurring detailed report every 4 hours
- surface issues, owners, and next fixes instead of only saying "it looks okay"
- distinguish host reachability problems from true runtime regressions

## Owner Model

This loop has two owners:

1. VPS producer, every 15 minutes
   - `/root/openclawtrading/scripts/run_chimera_trade_lifecycle_cycle.sh`
   - writes lifecycle, Deezoh, diary, journal, and learning artifacts

2. Windows consumer, every 4 hours
   - `C:\Users\becke\claudecowork\scripts\build_chimera_vps_4h_monitor.py`
   - registered by `scripts/register_chimera_vps_4h_monitor_task.ps1`
   - writes local reports under `reports/auto/CHIMERA_VPS_4H_MONITOR/`

## What This Monitor Must Check

- root cron still owns the VPS producer loop
- review/debug still passes or clearly names the failures
- post-build monitor still passes or clearly names the failures
- pipeline observability, Deezoh round state, diary, journal, and learning queue still exist and are fresh enough
- Deezoh still exposes the current phase, focus, and next-best-question path
- diary feedback still surfaces weak agents or weak process contracts
- Hermes consultation (`HERMES_CONSULTATION.md`) is fresh (within 5 hours)
- remaining risks stay visible

## The Hermes Trading Analyst (Consultation Producer)

Windows also runs a standalone Hermes trading analyst every 4 hours as a consultant subagent:

**Script:** `C:\Users\becke\.hermes\scripts\chimera_trading_analyst.py`

**Output:** `C:\Users\becke\claudecowork\consultation\HERMES_CONSULTATION.md`

The analyst produces:
- Per-symbol (BTC, ETH, SOL) analysis across 6 timeframes (1W, 3D, 1D, 4H, 1H, 15M)
- RSI, MACD, EMA trend, support/resistance, ATR
- Order block entries, FVG gaps, divergence alerts
- Cross-symbol summary and bias consensus

This is separate from the VPS producer loop. It is a read-only consultant deliverable, not a trade executor. It analyzes what the market is doing and surfaces the consultation for Deezoh to consume.

## Outputs

- `reports/auto/CHIMERA_VPS_4H_MONITOR/CHIMERA_VPS_4H_MONITOR_LATEST.json`
- `reports/auto/CHIMERA_VPS_4H_MONITOR/CHIMERA_VPS_4H_MONITOR_LATEST.md`
- `reports/auto/CHIMERA_VPS_4H_MONITOR/CHIMERA_VPS_4H_MONITOR_HISTORY.jsonl`
- `logs/chimera-vps-4h-monitor.log`
- `consultation/HERMES_CONSULTATION.md` (Hermes analyst output)

## Rules

- Evidence first.
- Refresh bounded remote audit surfaces before summarizing.
- Separate `host unreachable` from `runtime broken`.
- If a weak agent contract appears in diary feedback, keep it in the next-action list until it is repaired.
- Do not place or modify live trades.
- If the local 4-hour task is missing, the orchestration owner is incomplete.
