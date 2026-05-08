# CHECKPOINT - screener packet and coin selection flow

Date: 2026-05-05
Operator: Codex

## Objective

Implement the screener packet architecture so market-wide discovery selects which symbols deserve deeper analysis before per-coin research bundles are created.

## What changed

Created:

- `chimera-vps-deploy/skills/CHIMERA_SCREENER_PACKET_TEMPLATE.md`
- `research/platforms/2026-05-05-screener-packet-source-matrix.md`
- `research/platforms/2026-05-05-screener-packet-live-example.md`

Updated:

- `chimera-vps-deploy/skills/CHIMERA_RESEARCH_BUNDLE_TEMPLATE.md`
- `agents/screener/AGENTS.md`
- `agents/screener/WORKFLOW.md`
- `agents/screener/TOOLS.md`
- `agents/deezoh/WORKFLOW.md`
- `agents/deezoh/SETUP_CANDIDATES.md`

## Design decision

The screener is not `Part 13` of the research bundle.

The new flow is:

1. one `Screener Packet` per scan cycle
2. one normal `Chimera Research Bundle` per selected symbol
3. `Part 1: Instrument And Context` links the selected symbol back to the screener packet

## New Part 1 intake fields

Added `screener_intake` with:

- `screener_packet_id`
- `screener_observed_at_utc`
- `screener_rank`
- `screener_book`
- `screener_reason`
- `analysis_depth_decision`
- `specialist_questions_from_screener`
- `screener_intake_status`

## Live proof

The live VPS `SCOUT_REPORT.json` at `2026-05-05T19:10:17Z` was used for the worked example.

It showed:

- `selected_workflow: no_trade_protection`
- `top_opportunities`: 50
- `chart_review_queue`: 10
- `long_book`: 50 review-only candidates
- `short_book`: 50 review-only candidates
- active no-trade protection because the report warned against blind promotion

The example therefore correctly produced:

- BTC and ETH as `chart_first`
- XRP as `watch_only`
- `coins_selected_for_full_bundle: []`

That proves the packet can stop automatic full-bundle creation when no-trade protection is stronger.

## Mirrors

Mirrored and verified:

- `/root/openclawtrading/skills/CHIMERA_SCREENER_PACKET_TEMPLATE.md`
- `/root/.openclaw/kimi-skills/CHIMERA_SCREENER_PACKET_TEMPLATE.md`
- `/root/openclawtrading/skills/CHIMERA_RESEARCH_BUNDLE_TEMPLATE.md`
- `/root/.openclaw/kimi-skills/CHIMERA_RESEARCH_BUNDLE_TEMPLATE.md`
- `/root/.openclaw/workspace/agents/screener/AGENTS.md`
- `/root/.openclaw/workspace/agents/screener/WORKFLOW.md`
- `/root/.openclaw/workspace/agents/screener/TOOLS.md`
- `/root/.openclaw/workspace/agents/deezoh/WORKFLOW.md`
- `/root/.openclaw/workspace/research/platforms/2026-05-05-screener-packet-source-matrix.md`
- `/root/.openclaw/workspace/research/platforms/2026-05-05-screener-packet-live-example.md`

Also placed the screener packet template on Windows skill surfaces:

- `C:\Users\becke\.codex\skills\CHIMERA_SCREENER_PACKET_TEMPLATE.md`
- `C:\Users\becke\.claude\skills\CHIMERA_SCREENER_PACKET_TEMPLATE.md`
- `C:\Users\becke\.openclaw\skills\CHIMERA_SCREENER_PACKET_TEMPLATE.md`

## Remaining work

- run a later Deezoh consumption test where Deezoh reads the screener packet and chooses which per-coin bundles to request
- continue `Part 11: Position Management And Risk`
- continue `Part 12: Final Decision`
