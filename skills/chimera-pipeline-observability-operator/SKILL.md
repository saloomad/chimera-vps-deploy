---
name: chimera-pipeline-observability-operator
description: Use this when Sal asks how to monitor the Chimera/OpenClaw trading pipeline, trace Deezoh decisions, inspect data source freshness, audit agent interactions, schedule reports, or improve the process from issues and outcomes.
---

# Chimera Pipeline Observability Operator

Use this skill when the task is to make the trade pipeline visible,
traceable, and improvable.

## Read First

1. `C:\Users\becke\claudecowork\chimera-vps-deploy\skills\CHIMERA_PIPELINE_OBSERVABILITY_TEMPLATE.md`
2. `C:\Users\becke\claudecowork\chimera-vps-deploy\skills\CHIMERA_DEEZOH_PIPELINE_ROUND_TEMPLATE.md`
3. `C:\Users\becke\claudecowork\agents\deezoh\WORKFLOW.md`
4. `C:\Users\becke\claudecowork\workflows\codex\chimera-screener-to-trade-document-flow.md`
5. `C:\Users\becke\claudecowork\orchestration\lobster\chimera-trade-lifecycle.lobster`
6. `C:\Users\becke\claudecowork\scripts\build_chimera_pipeline_observability.py`
7. `C:\Users\becke\claudecowork\scripts\run_chimera_trade_lifecycle_cycle.sh`
8. `C:\Users\becke\claudecowork\scripts\run_chimera_review_debug_orchestration.py`
9. `C:\Users\becke\claudecowork\chimera-vps-deploy\skills\prompt-upgrade-engineer\SKILL.md`

## What This Skill Owns

It explains and enforces the monitor layer over:

- data sources
- report freshness
- scripts that produced reports
- agent questions and answers
- Deezoh thoughts and bias
- phase progression
- wait states and wake triggers
- trade closeout learning
- Deezoh diary entries
- actual trading journal entries
- review/debug findings
- cron reporting

## Main Runtime Reports

Primary observability output:

- `reports/auto/CHIMERA_PIPELINE_OBSERVABILITY.json`
- `reports/auto/CHIMERA_PIPELINE_OBSERVABILITY.md`

Primary Deezoh round document:

- `reports/auto/DEEZOH_PIPELINE_ROUND_STATE.json`

Diary and journal surfaces:

- `reports/auto/DEEZOH_DIARY.json`
- `reports/auto/DEEZOH_DIARY.md`
- `reports/auto/DEEZOH_DIARY.jsonl`
- `reports/auto/TRADING_JOURNAL.json`
- `reports/auto/TRADING_JOURNAL.jsonl`
- `reports/auto/DEEZOH_JOURNAL_FEEDBACK.json`

Related reasoning and interaction reports:

- `reports/auto/DEEZOH_THOUGHTS.json`
- `reports/auto/DEEZOH_ROUND_DISPATCH.json`
- `reports/auto/DESK_INTERACTION_BUS.json`
- `reports/auto/DEEZOH_SLEEP_STATE.json`
- `reports/auto/ORCHESTRATOR_ACTIVITY.json`

Local 4-hour consumer-side monitor:

- `reports/auto/CHIMERA_VPS_4H_MONITOR/CHIMERA_VPS_4H_MONITOR_LATEST.json`
- `reports/auto/CHIMERA_VPS_4H_MONITOR/CHIMERA_VPS_4H_MONITOR_LATEST.md`
- `logs/chimera-vps-4h-monitor.log`

## How To Run

Local:

```bash
python scripts/build_chimera_pipeline_observability.py --reports-dir reports/auto
python scripts/tests/chimera_pipeline_observability_smoke.py
```

Live VPS:

```bash
bash /root/openclawtrading/scripts/run_chimera_trade_lifecycle_cycle.sh
python3 /root/openclawtrading/scripts/build_chimera_pipeline_observability.py --reports-dir /root/openclawtrading/reports/auto
```

Windows local consumer:

```powershell
python scripts/build_chimera_vps_4h_monitor.py
powershell -File scripts/run_chimera_vps_4h_monitor.ps1
```

## Cron Recommendation

Run the lifecycle cycle every 15 minutes:

```cron
*/15 * * * * cd /root/openclawtrading && /bin/bash scripts/run_chimera_trade_lifecycle_cycle.sh >> logs/chimera-lifecycle-observability.log 2>&1
```

Why:

- keeps source reports fresh
- refreshes Deezoh thoughts
- dispatches and reads agent questions
- rebuilds lifecycle phase context
- writes observability and round-state reports
- writes Deezoh diary and trading journal reports
- feeds diary issues into the lifecycle learning queue
- preserves issues for the next improvement loop

Then keep the Windows consumer-side audit every 4 hours:

- owner: Windows Scheduled Task `ChimeraVpsFourHourMonitor`
- purpose: verify the VPS producer is still alive, classify issues, and keep a detailed local report/history

## Deezoh Round Loop

Each round Deezoh must ask:

1. what market condition are we in?
2. what is my bias and why?
3. what is the best long, best short, and no-trade?
4. should this pass to the next phase or wait?
5. what exact event wakes the desk?
6. what one missing input would most improve the decision?
7. which agent should answer that?
8. where will the answer be added?
9. what did the last trade, thesis stop, or simulation teach?
10. what should we change before the next similar case?
11. what diary or trading-journal item should feed the next learning cycle?

## Monitoring Questions

Every observability review should ask:

- is a critical report missing or stale?
- did a source exist but no consumer used it?
- did Deezoh ask the right next question?
- did a specialist answer actually change anything?
- is the phase owner logical?
- does the wait have a real trigger?
- is the learning queue growing with useful lessons or noise?
- do simulation results agree with natural outcomes?

## Prompt Engineer Use

For messy or broad requests, apply `prompt-upgrade-engineer` first.

Convert the request into:

- objective
- data/report surfaces to inspect
- owners to involve
- proof path
- monitoring need
- done criteria

Then execute the observability pass.

## Good Closeout

A good run leaves:

- a fresh observability JSON report
- a fresh markdown summary
- a fresh Deezoh round-state document
- a fresh Deezoh diary entry
- a fresh trading journal summary
- one issue list with owners
- one next agent question
- one improvement target
- proof that the report ran locally or on the VPS
