# Checkpoint: Pipeline Observability And Deezoh Round State

Date: 2026-05-08

## Objective

Create an architecture to monitor the Chimera/OpenClaw trading pipeline end to
end:

- data sources read
- reports produced
- agent questions and answers
- Deezoh reasoning and bias
- phase progression
- wait triggers
- missing information
- learning from closeout, thesis stop, simulation, and future natural outcomes

## Built

- `scripts/build_chimera_pipeline_observability.py`
- `scripts/tests/chimera_pipeline_observability_smoke.py`
- `chimera-vps-deploy/skills/CHIMERA_PIPELINE_OBSERVABILITY_TEMPLATE.md`
- `chimera-vps-deploy/skills/CHIMERA_DEEZOH_PIPELINE_ROUND_TEMPLATE.md`
- `chimera-vps-deploy/skills/chimera-pipeline-observability-operator/SKILL.md`
- `research/platforms/2026-05-08-chimera-pipeline-observability-and-deezoh-round-architecture.md`

## Updated

- `scripts/run_chimera_trade_lifecycle_cycle.sh`
- `scripts/tests/current_focus_full_lifecycle_smoke.py`
- `scripts/run_chimera_review_debug_orchestration.py`
- `agents/deezoh/WORKFLOW.md`
- `workflows/codex/chimera-screener-to-trade-document-flow.md`
- `orchestration/lobster/chimera-trade-lifecycle.lobster`
- `operations/cron/CRON_REGISTRY.md`

## Live Outputs

- `/root/openclawtrading/reports/auto/CHIMERA_PIPELINE_OBSERVABILITY.json`
- `/root/openclawtrading/reports/auto/CHIMERA_PIPELINE_OBSERVABILITY.md`
- `/root/openclawtrading/reports/auto/DEEZOH_PIPELINE_ROUND_STATE.json`

## Proof

Local:

- `python scripts/tests/chimera_pipeline_observability_smoke.py` passed.
- Python compile passed for the new builder and smoke.

Live VPS:

- `python3 scripts/tests/chimera_pipeline_observability_smoke.py` passed.
- `bash scripts/run_chimera_trade_lifecycle_cycle.sh` passed.
- `python3 scripts/run_chimera_review_debug_orchestration.py --skip-replay` passed.
- observability report status: `PASS`
- observability issues: `0`
- agent questions traced: `11`
- agent answers traced: `7`
- current phase: `entry_watch`
- focus symbol: `BTCUSDT`
- Deezoh next question: `For BTCUSDT, what side has cleaner odds right now, and what invalidates that lane first?`

## Cron

Installed on root crontab:

```cron
*/15 * * * * cd /root/openclawtrading && /bin/bash scripts/run_chimera_trade_lifecycle_cycle.sh >> logs/chimera-lifecycle-observability.log 2>&1
```

## Bugs Found And Fixed

- The accelerated lifecycle smoke failed after the new review/debug check because isolated workspaces did not build observability first.
- Fixed by building `DEEZOH_THOUGHTS.json`, `CHIMERA_PIPELINE_OBSERVABILITY.json`, and `DEEZOH_PIPELINE_ROUND_STATE.json` inside the isolated smoke before review/debug runs.
- The live monitor first reported no agent round because `deezoh_round_orchestrator.py` was not mirrored to the VPS.
- Fixed by syncing the script to `/root/openclawtrading/scripts`.
- The observability parser did not understand the current `DEEZOH_ROUND_DISPATCH.json` and `DEEZOH_SLEEP_STATE.json` shape.
- Fixed parser to count `round_1_dispatched_count`, `round_2_followup_count`, `asked_this_round`, and `answers_received`.

## Remaining Work

- Let cron run naturally and inspect the first scheduled result/log.
- Keep comparing synthetic lessons to real paper-trade outcomes.
- If the observability issue list starts repeating, patch the named owner rather than only clearing the report.
