# Part 5 Liquidation Heat Map Build And Test

Date: 2026-05-05
Owner: Codex
Thread scope: Part 5 only

## What was built

- Hardened exact extractor:
  - `C:\Users\becke\claudecowork\trading_system\scripts\coinglass_heatmap_exact.py`
- Repaired legacy screenshot capture path:
  - `C:\Users\becke\claudecowork\trading_system\scripts\liquidation_heatmap.py`

## What is now proven

### CoinGlass exact status

- `24h` works as a real exact extraction path.
- `12h`, `48h`, `3d`, and `1w` do not return a successful heatmap response in the current unauthenticated local path.
- Those locked windows now write honest blocker JSON instead of fake exact cluster output.
- Cross-coin truth on the current direct route is not uniform:
  - `BTC 24h` works
  - `ETH 24h` returns API code `40000`
  - `SOL 24h` does not render a heatmap chart on the direct route and now writes `chart_not_rendered`

### Exact extractor proof

Command run:

```powershell
python C:\Users\becke\claudecowork\trading_system\scripts\coinglass_heatmap_exact.py --coin BTC --timeframes 12h 24h 48h 3d 1w
```

Observed result:

- `BTC 24h` -> `exact_heatmap_extracted`
- `BTC 12h` -> `timeframe_locked_or_unavailable`
- `BTC 48h` -> `timeframe_locked_or_unavailable`
- `BTC 3d` -> `timeframe_locked_or_unavailable`
- `BTC 1w` -> `timeframe_locked_or_unavailable`

Fresh outputs:

- `C:\Users\becke\claudecowork\reports\auto\LIQUIDATION_DATA\BTC_24h.json`
- `C:\Users\becke\claudecowork\reports\auto\LIQUIDATION_DATA\BTC_12h.json`
- `C:\Users\becke\claudecowork\reports\auto\LIQUIDATION_DATA\BTC_48h.json`
- `C:\Users\becke\claudecowork\reports\auto\LIQUIDATION_DATA\BTC_3d.json`
- `C:\Users\becke\claudecowork\reports\auto\LIQUIDATION_DATA\BTC_1w.json`
- `C:\Users\becke\claudecowork\reports\auto\LIQUIDATION_DATA\ETH_24h.json`
- `C:\Users\becke\claudecowork\reports\auto\LIQUIDATION_DATA\SOL_24h.json`

Important blocker truth from fresh JSON:

- non-24h windows return API response code `40000`
- `selected_window_label` still changes in the UI
- the extractor now records that as a locked/unavailable window instead of pretending the chart changed

### Legacy screenshot path proof

Command run:

```powershell
python C:\Users\becke\claudecowork\trading_system\scripts\liquidation_heatmap.py --coin BTC --force
```

Observed result:

- CoinGlass screenshot now uses the real heatmap page:
  - `https://www.coinglass.com/pro/futures/LiquidationHeatMap?coin=BTC`
- fresh usable capture:
  - `C:\Users\becke\claudecowork\reports\heatmaps\BTC_coinglass_maxpain_2026-05-05.png`
- CoinAnk still hits a login wall and remains unusable as a direct screenshot source in the current local path

## Practical Part 5 owner truth

- Exact working local source today:
  - CoinGlass `24h`
- Honest blocked local source today:
  - CoinGlass `12h`, `48h`, `3d`, `1w`
- Proof/capture helper:
  - repaired `liquidation_heatmap.py`
- Not usable today without login:
  - CoinAnk screenshot path

## Recommended merge truth for Part 5

- keep `market-maker` as owner
- allow exact local CoinGlass `24h`
- treat other CoinGlass windows as blocked until authenticated or replaced by another exact source
- keep screenshot capture as proof, not as permission to fake exact clusters

## Live VPS extension

- VPS reachability was re-proved during the follow-up pass.
- Playwright is installed on the VPS.
- `run_maxpain_scan.py` works live on the VPS and writes:
  - `/root/openclawtrading/reports/auto/MAXPAIN_SUMMARY.json`
- `run_liquidation_scans.py` was patched to resolve the exact-extractor Python separately from the system Python.
- exact-extractor live dependency fix:
  - created `/root/openclawtrading/.venv-coinglass`
  - installed `rapidocr_onnxruntime`, `numpy`, `pillow`, and `playwright` there
- exact live truth after rerun:
  - the current unauthenticated VPS path still blocks exact CoinGlass heatmap extraction
  - screenshot and max-pain browser lanes still work
  - live Part 5 should therefore treat VPS as `screenshot/max-pain + proxy` unless a later authenticated route is added

## Final tested truth after integration pass

- Windows local:
  - exact `BTC 24h` structured extraction works
  - `LIQUIDATION_SUMMARY.json` can carry real exact BTC 24h clusters when the exact extractor is run
- Live VPS:
  - max-pain browser scrape works
  - screenshot lane works
  - exact CoinGlass heatmap lane is still blocked without authentication

## Integration landed

- shared template upgraded:
  - `C:\Users\becke\claudecowork\chimera-vps-deploy\skills\CHIMERA_RESEARCH_BUNDLE_TEMPLATE.md`
- Part 5 draft updated with the stronger source order and capability truth:
  - `C:\Users\becke\claudecowork\chimera-vps-deploy\handoffs\parallel_part5_liquidation_heat_map.md`
- liquidation runner patched so the exact extractor uses the right Python when a dedicated OCR venv exists:
  - `C:\Users\becke\claudecowork\scripts\market-maker\run_liquidation_scans.py`
