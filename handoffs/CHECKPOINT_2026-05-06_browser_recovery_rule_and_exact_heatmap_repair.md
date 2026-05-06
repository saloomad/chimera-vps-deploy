# Browser Recovery Rule And Exact Heatmap Repair Checkpoint

Date: 2026-05-06
Owner: Codex
Scope: finish the CoinGlass exact-heatmap recovery loop instead of stopping at the first failed ETH/SOL state, then harden orchestration so the same mistake is less likely again

## Objective

Stop treating browser-backed data lanes as failed before exhausting the obvious recovery path, and prove the exact `24h` CoinGlass lane plus Deezoh focused bundle truth after the fix.

## What changed

- strengthened `trading_system/scripts/coinglass_heatmap_exact.py`
  - added auth-refresh retry when the page-side response is weak but the browser lane is still usable
  - fixed the ETH axis parser so valid 4-digit labels like `2491` are not rejected
  - fixed the SOL axis parser so decimal labels like `89.325` and `80.745` stay numeric instead of becoming fake `89325` / `80745`

- strengthened `scripts/market-maker/run_liquidation_scans.py`
  - exact extractor now runs through `python -B` so stale bytecode does not keep old parser behavior alive

- added regression coverage
  - `scripts/tests/coinglass_axis_value_smoke.py`
  - this guards the ETH 4-digit and SOL decimal OCR-value cases directly

- hardened the orchestration layer
  - `handoffs/ORCHESTRATION_ISSUES.md` now records the browser-data recovery miss
  - `skills/objective-orchestration-loop/SKILL.md` now forces the browser-data recovery ladder before a scrape/OCR lane can honestly be called failed or blocked

## Fresh proof

Passed:
- `python scripts/tests/coinglass_axis_value_smoke.py`
- `python scripts/tests/liquidation_summary_contract_smoke.py`
- `python scripts/tests/deezoh_derivatives_context_smoke.py`
- `python scripts/market-maker/run_liquidation_scans.py`
- `python -B scripts/build_deezoh_thoughts.py`

Fresh exact local outputs:
- `reports/auto/LIQUIDATION_DATA/BTC_24h.json`
- `reports/auto/LIQUIDATION_DATA/ETH_24h.json`
- `reports/auto/LIQUIDATION_DATA/SOL_24h.json`
- `reports/auto/DEEZOH_THOUGHTS_FOCUS/INDEX.json`

## Current truth

- exact CoinGlass `24h` heatmap extraction now works locally for:
  - `BTC`
  - `ETH`
  - `SOL`
- focused Deezoh bundles now show:
  - `BTCUSDT -> exact_both`
  - `ETHUSDT -> exact_both`
  - `SOLUSDT -> exact_both`
- exact max-pain browser scrape is still working
- `HYPE` remains proxy-only because it is unsupported by the maintained screenshot/extractor lane

## Prevention rule that landed

For browser-backed data lanes, do not stop at the first weak artifact state.

Required recovery order now is:
1. rerun and inspect the fresh artifact
2. verify or refresh auth/session if credentials exist
3. inspect raw screenshot/OCR/parser assumptions
4. patch parser/crop/runtime assumptions
5. rerun with `python -B` if stale runtime behavior is plausible
6. only then call the lane `iterate` or `blocked`

## Remaining gap

- `HYPE` still needs either:
  - a maintained screenshot/extractor path
  - or an honest permanent proxy-only classification in the document/runtime surfaces
