# Agent Session Handoff - Chimera Ecosystem

## Session Info
- **Ended by**: Codex
- **Ended at**: 2026-05-05T20:00:00Z
- **Platform**: Windows Codex + Kimi VPS
- **Session focus**: Generalize the CoinGlass liquidation heatmap path so it works by in-page symbol search instead of hardcoded coin routes, then prove it locally and on the VPS.

## Original Goal
Make the CoinGlass heatmap flow behave like a real generalized tool: search the symbol on the page, switch timeframes, capture valid screenshots, and extract clusters without pretending only BTC/ETH/SOL are supported.

## Completed Work
- [x] Reworked CoinGlass contract selection in [browser_auth.py](/C:/Users/becke/claudecowork/trading_system/scripts/browser_auth.py) to use the on-page combobox search and choose the best exchange/quote match with `USDT` preference.
- [x] Repaired [liquidation_heatmap.py](/C:/Users/becke/claudecowork/trading_system/scripts/liquidation_heatmap.py) so CoinGlass is booted from a known-good BTC page, then switched to the requested symbol and timeframe.
- [x] Repaired [coinglass_heatmap_exact.py](/C:/Users/becke/claudecowork/trading_system/scripts/coinglass_heatmap_exact.py) so login-wall captures are rejected instead of saved as fake screenshots, stale screenshots are removed before recapture, and timeframe selection is more robust.
- [x] Repaired [run_liquidation_scans.py](/C:/Users/becke/claudecowork/scripts/market-maker/run_liquidation_scans.py) so the exact extractor uses the generalized watchlist instead of the old hardcoded subset and runs both maintained capture windows.
- [x] Mirrored the repaired files to `/root/openclawtrading/...` and `/root/.openclaw/workspace/...`.
- [x] Proved local CoinGlass screenshot capture on multi-coin multi-timeframe samples: `DOGE`, `HYPE`, `SOL`, `XRP`, `BNB`, `ADA`, `AVAX`, `PEPE` across `24h` and `1w`.
- [x] Proved local exact extraction on the same generalized path for the tested symbols and timeframes.
- [x] Proved VPS CoinGlass screenshot capture on `ADA`, `PEPE`, and `HYPE` across `24h` and `1w`.
- [x] Proved VPS exact extraction using `/root/openclawtrading/.venv-coinglass/bin/python` on `HYPE`, `PEPE`, and `SOL`.
- [x] Re-ran the full VPS liquidation runner successfully with log capture; it wrote `/root/openclawtrading/reports/auto/LIQUIDATION_SUMMARY.json`.

## Partially Done
- [~] Universal-coin support is strongly improved and now driven by page search, but it is still proven by sampled symbols rather than literally every market CoinGlass lists.

## Not Done
- [ ] Broader automation around arbitrary user-supplied symbols in every higher-level document section was not expanded in this pass.

## Decisions Made
- **Decision**: CoinGlass should be treated as the real Part 5 owner, and symbol routing should come from the page search box instead of hardcoded `?coin=` assumptions. | **Why**: live probing showed the page exposes the contract search directly, and that route generalizes cleanly.
- **Decision**: Login-wall screenshots are invalid and must never be saved as truth. | **Why**: one BNB exact pass saved a CoinGlass login page as a fake heatmap until this was repaired.
- **Decision**: The VPS exact extractor should use `/root/openclawtrading/.venv-coinglass/bin/python` when OCR is needed. | **Why**: the OCR package is installed there, not in system `python3`.

## Files Changed / Created
| File | Platform | What Changed |
|------|----------|-------------|
| `C:/Users/becke/claudecowork/trading_system/scripts/browser_auth.py` | Windows + VPS mirror | Added generalized CoinGlass symbol-search selection and smarter contract scoring. |
| `C:/Users/becke/claudecowork/trading_system/scripts/liquidation_heatmap.py` | Windows + VPS mirror | Uses generalized CoinGlass symbol search and safer timeframe selection. |
| `C:/Users/becke/claudecowork/trading_system/scripts/coinglass_heatmap_exact.py` | Windows + VPS mirror | Rejects login-wall captures, clears stale screenshots, and uses safer timeframe clicks. |
| `C:/Users/becke/claudecowork/scripts/market-maker/run_liquidation_scans.py` | Windows + VPS mirror | Uses generalized exact extraction for the configured watchlist and both maintained timeframes. |
| `C:/Users/becke/claudecowork/chimera-vps-deploy/handoffs/CHECKPOINT_2026-05-05_coinglass_general_symbol_search_and_vps_proof.md` | Windows | Captures the proof and remaining boundary for this repair slice. |

## Skills Created / Updated
- [ ] none

## Other Durable Outputs Created
- [x] This handoff - shared in repo

## Sync Status
- **GitHub status**: local only
- **Other platforms that should pull this**: Windows Claude, Kimi VPS
- **What still needs sync**: Git commit/push if the repo mirror should become pullable elsewhere.

## Routing Used
- **Task lane**: mixed
- **Model used**: gpt-5.5
- **Reasoning used**: high
- **Result quality**: strong
- **Rerun needed**: no
- **Better route next time**: same, but start with symbol-search routing immediately instead of subset-by-subset assumptions.

## Next Actions (for next agent)
1. **[PRIORITY]** If Sal wants broader proof, test a few more random symbols through the same CoinGlass search path instead of assuming universality.
2. **[MEDIUM]** If higher-level document sections still hardcode old liquidation assumptions, update them to say the path is now `page search -> timeframe -> screenshot -> exact extraction`.
3. **[LOW]** Commit and push the repaired files if this local-only state should become the shared repo truth.

## Skills to Read Before Starting
- [x] `codex-runtime-router`
- [x] `objective-orchestration-loop`
- [ ] `chimera-research-bundle-section-upgrader` if continuing the document section work

## Live System State (if applicable)
- **OpenClaw Gateway**: not checked in this slice
- **TradingView Desktop**: not checked in this slice
- **Discord Bot**: not checked in this slice
- **Last data update**: `/root/openclawtrading/reports/auto/LIQUIDATION_SUMMARY.json` refreshed successfully during this run

## Reading List for Next Agent
- [browser_auth.py](/C:/Users/becke/claudecowork/trading_system/scripts/browser_auth.py)
- [liquidation_heatmap.py](/C:/Users/becke/claudecowork/trading_system/scripts/liquidation_heatmap.py)
- [coinglass_heatmap_exact.py](/C:/Users/becke/claudecowork/trading_system/scripts/coinglass_heatmap_exact.py)
- [run_liquidation_scans.py](/C:/Users/becke/claudecowork/scripts/market-maker/run_liquidation_scans.py)

---

> The hardcoded-coin path is no longer the main owner. The real path is now CoinGlass page search plus timeframe switching, and that has live local and VPS proof.
