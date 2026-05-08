# Checkpoint - 2026-05-06 - Trade Lifecycle Document Flow And Lobster

## What landed

- created the linked phase-document architecture for Chimera trading
- added:
  - `CHIMERA_ENTRY_WATCH_PACKET_TEMPLATE.md`
  - `CHIMERA_ACTIVE_TRADE_PACKET_TEMPLATE.md`
  - `CHIMERA_TRADE_CLOSEOUT_TEMPLATE.md`
- created:
  - `workflows/codex/chimera-screener-to-trade-document-flow.md`
  - `orchestration/lobster/chimera-trade-lifecycle.lobster`
- updated screener, Deezoh, entry-watch, position-sizer, trade-judge, execution-agent, and workflow-map docs so the phase progression is explicit

## The new answer

Do not use one giant document for every phase.

Use linked packets:

1. screener packet
2. per-symbol research bundle
3. entry-watch packet
4. active-trade packet
5. trade-closeout packet

## Proof

- Windows Codex, Claude, and OpenClaw local skill roots now contain all five Chimera packet templates
- live VPS mirrors now contain the new templates on:
  - `/root/openclawtrading/skills`
  - `/root/.openclaw/kimi-skills`
- live VPS workflow mirrors now contain:
  - `/root/openclawtrading/workflows/codex/chimera-screener-to-trade-document-flow.md`
  - `/root/.openclaw/workspace/workflows/codex/chimera-screener-to-trade-document-flow.md`
- live VPS Lobster mirror now contains:
  - `/root/.openclaw/workspace/orchestration/lobster/chimera-trade-lifecycle.lobster`
- hash-checked:
  - entry-watch packet template
  - active-trade packet template
  - trade-closeout template
  - document-flow workflow
  - Lobster lifecycle file

## Important behavior rule

Use:

- scripts and report pipelines for machine truth
- workflows for owner order and questions
- Task Flow for durable per-symbol lifecycle state
- Lobster for deterministic phase gating

## Still open

- build the durable Task Flow state owner for symbol lifecycle state if we want the full phase machine to persist independently of report inference
- prove one future live cycle actually moves through the new Lobster phase file in practice
