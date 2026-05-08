# Checkpoint - 2026-05-05 - Live VPS Jackson Part 2 Source Finalization

## Objective

Finalize which live data sources `chart-analyzer` should use for `Part 2: Technical Structure`, with live VPS proof first.

## Completed in this pass

- proved live VPS `tradingview-jackson` is working on a real chart target
- proved live VPS Jackson can:
  - switch symbol and timeframe
  - read state
  - read quote
  - read values
  - take screenshots
- proved live VPS Jackson also worked on `OANDA:XAUUSD`
- proved local and VPS `scripts/bitget_technical_analysis.py` match on `BTCUSDT 4h`
- proved `tvremix` works on local and VPS through direct probe wrappers
- promoted the local script probe into:
  - `scripts/technical_structure_probe.py`
- promoted the tvremix probe into:
  - `scripts/tvremix_probe.py`
- synced the new probe scripts to:
  - `/root/openclawtrading/scripts`
  - `/root/.openclaw/workspace/scripts`
- synced updated `chart-analyzer` instructions to:
  - `/root/openclawtrading/agents/chart-analyzer`
  - `/root/.openclaw/workspace/agents/chart-analyzer`
- synced and proved the newer deterministic foundation files on VPS:
  - `anchored_vwap.py`
  - `range_levels.py`
  - `create_anchored_volume_profile.py`
- captured the final proof note:
  - `research/platforms/2026-05-05-live-vps-jackson-source-stack-finalization.md`

## Final source order for Part 2

1. `tradingview-jackson`
   - live chart proof
   - screenshots
   - chart-side values
   - visible labels
2. `scripts/technical_structure_probe.py`
   - deterministic document fields
3. `tvremix.analyze_smc_tool` / `analyze_swing_tool`
   - no-chart structure helper
4. `scripts/bitget_technical_analysis.py`
   - indicator-series support
5. `multi_timeframe_analyzer.py`
   - alignment helper only

## Important current limits

- Jackson `data boxes` for ICT OB/FVG still returned empty
- Jackson `data lines --study 'Auto Fib Retracement'` still did not isolate fib-only lines cleanly
- do not use `tvremix.analyze_multi_timeframe` as sole truth
- no safe script deletion landed yet beyond temporary probe cleanup

## Safe cleanup that did land

- removed temp-only probes:
  - `tmp/jackson_probe.py`
  - `tmp/part2_source_probe.py`
  - `tmp/tvremix_probe.py`

## Still open

- if Sal approves demo-path cleanup later, the first prune chain is:
  - `phase2_demo.py`
  - `phase2_simple_demo.py`
  - then `indicators/divergence_detector.py`
- remaining document sections after Part 2 still need the same source-proof closeout
