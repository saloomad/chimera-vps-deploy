# CHECKPOINT - screening stack repair and capability upgrade

Date: 2026-05-05
Operator: Codex

## Objective

Continue the screener work by proving how screening is actually done, repairing the broken or misleading paths, and improving the recurring screening flow so Deezoh gets more useful candidate books.

## What changed

Updated:

- `scripts/market_scanner.py`
- `scripts/build_scout_report.py`
- `scripts/tvremix_usage_tracker.py`
- `agents/screener/TOOLS.md`

Created:

- `research/platforms/2026-05-05-screening-stack-capability-audit.md`

## Repairs

### 1. Fixed live VPS `tvremix` helper path

The VPS runtime copy of `tvremix_usage_tracker.py` was stale and still used strict `json.loads(args_json)` parsing.

Mirrored the repaired wrapper to:

- `/root/openclawtrading/scripts/tvremix_usage_tracker.py`
- `/root/.openclaw/workspace/scripts/tvremix_usage_tracker.py`

Proof:

- VPS `run_screener` now returns real rows

### 2. Fixed production scanner report-path drift

`scripts/market_scanner.py` was resolving root incorrectly and could write to `/root/reports/auto` instead of the live repo report surface.

It now uses `runtime_paths.REPORTS_AUTO`.

Proof:

- fresh scanner run wrote to `/root/openclawtrading/reports/auto/OPPORTUNITIES.json`

### 3. Fixed stale scanner contract assumptions

The production scanner now emits richer fields for the screener flow:

- `direction`
- `dominant_timeframe`
- `confirmed_categories`
- `signal_family`
- `bucket`
- `analysis_depth_hint`
- `top_signal`
- `regime_structure`

The `_brief` output now exposes those fields in a useful agent-facing shape instead of stale placeholder fields.

### 4. Fixed scout-builder underuse of live opportunities

`build_scout_report.py` now:

- infers direction from `direction` or `bias`
- reads nested indicator/interpretation fields from the current `OPPORTUNITIES.json` shape
- carries `signal_family`, `analysis_depth_hint`, `bucket`, and dominant-timeframe context
- rebalances market-cap placeholders so they do not automatically outrank every real hit

## Live proof

Verified on VPS:

- `tvremix run_screener` works
- `market_scanner.py --top 12 --workers 4` runs
- `build_scout_report.py` runs
- `OPPORTUNITIES.json` now includes the richer contract fields
- `SCOUT_REPORT.json` now surfaces real candidate sources ahead of placeholders more often

Observed source mix after repair:

- `OPPORTUNITIES.json`
  - primary recurring breadth owner
- `DIVERGENCES.json`
  - still strong in the top long-book entries
- `TOP50_MARKET_CAP_UNIVERSE`
  - still present as filler / fallback, but no longer the only visible source

## Durable doc

See:

- `research/platforms/2026-05-05-screening-stack-capability-audit.md`

It captures:

- the real production screening flow
- best owner by signal family
- what scripts give that chart lanes do not
- what chart lanes still give that scripts do not
- what was repaired today

## Remaining work

- improve DIVERGENCES-to-scout metadata so top divergence hits also carry richer `signal_family` and specialist routing
- run a later Deezoh-consumption proof using the upgraded screener stack
- continue `Part 11: Position Management And Risk`
- continue `Part 12: Final Decision`
