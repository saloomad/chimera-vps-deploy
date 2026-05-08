# Checkpoint - 2026-05-05 - VPS TradingView Jackson tvremix Repair

## Session Info
- **Ended by**: Codex / Windows
- **Ended at**: 2026-05-05T09:30:00+03:00
- **Platform**: Windows Codex + live VPS
- **Session focus**: stop diagnosing dead/stale chart paths and actually repair the live VPS TradingView/Jackson/tvremix route

## Original Goal

Fix the live VPS Linux OpenClaw chart/runtime path, prove Jackson on the real saved TradingView chart, prove tvremix and Bitget on the same runtime, and remove the stale Windows helper defaults that were still pointing at old hosts.

## Completed Work
- [x] Fixed stale Windows helper defaults:
  - `scripts/connect_openclaw_linux.ps1`
  - `scripts/open_linux_paperclip_tunnel.ps1`
- [x] Proved the fixed Windows SSH helper reaches:
  - `root@100.67.172.114`
  - `/root`
- [x] Added a clean VPS browser-launch helper source:
  - `projects/tradingview-mcp-jackson/scripts/launch_tv_browser_debug_linux.sh`
- [x] Synced the browser-launch helper to:
  - `/root/.openclaw/workspace/projects/tradingview-mcp-jackson/scripts/launch_tv_browser_debug_linux.sh`
- [x] Hardened `projects/tradingview-mcp-jackson/src/connection.js`
  - multi-target scoring
  - bad-target skipping
  - optional `Page.enable` / `DOM.enable`
- [x] Synced the Jackson connection fix to:
  - `/root/.openclaw/workspace/projects/tradingview-mcp-jackson/src/connection.js`
- [x] Repaired the VPS chart browser path so `9333` is the live truth surface
- [x] Proved Jackson on the saved BTC chart:
  - symbol `BINANCE:BTCUSDT`
  - timeframe `240`
  - chart type `Candles`
  - API available `true`
- [x] Proved Jackson can see loaded custom studies on the saved chart
- [x] Proved remote `tvremix` on VPS by importing the tracker in Python and calling `get_full_technicals`
- [x] Proved remote Bitget technical-analysis on VPS with saved BTC `4h` volume-profile artifact

## Partially Done
- [~] VPS chart-side screenshot / Playwright proof was not promoted; Jackson CLI is now the stronger proof lane on this runtime

## Not Done
- [ ] The remaining research-bundle sections still need the same owner-proof treatment

## Decisions Made
- **Decision**: Trust the VPS web-chart Chrome path on `9333`, not desktop TradingView on `9222` | **Why**: `9333` has the real chart target and live chart API; `9222` still does not
- **Decision**: Keep Jackson as the chart-backed proof lane and loaded-study truth lane | **Why**: after the repair it can read the saved BTC chart and its attached custom studies
- **Decision**: Keep tvremix and Bitget as support lanes for chartless or deterministic output | **Why**: they answer different parts of the document cleanly and survive when chart extraction is too thin

## Files Changed / Created
| File | Platform | What Changed |
|------|----------|-------------|
| `scripts/connect_openclaw_linux.ps1` | Windows | fixed live host/user defaults |
| `scripts/open_linux_paperclip_tunnel.ps1` | Windows | fixed live host/user defaults |
| `projects/tradingview-mcp-jackson/src/connection.js` | Windows + VPS | hardened CDP target selection and optional-domain behavior |
| `projects/tradingview-mcp-jackson/scripts/launch_tv_browser_debug_linux.sh` | Windows + VPS | new clean launch + tab-pruning helper for VPS browser CDP |
| `research/platforms/2026-05-05-vps-tradingview-jackson-tvremix-repair.md` | Windows | durable proof note |
| `chimera-vps-deploy/handoffs/CHECKPOINT_2026-05-05_vps_tradingview_jackson_tvremix_repair.md` | Windows | this handoff |

## Sync Status
- **GitHub status**: local only
- **Other platforms that should pull this**: Windows Claude, shared repo consumers
- **What still needs sync**: shared repo push if you want these repairs pullable everywhere

## Routing Used
- **Task lane**: mixed
- **Model used**: gpt-5.5
- **Reasoning used**: high
- **Result quality**: strong
- **Rerun needed**: no
- **Better route next time**: same

## Next Actions (for next agent)
1. **[PRIORITY]** Continue the same proof discipline for the next bundle section instead of falling back to chat-only design
2. **[MEDIUM]** If needed, add a small Jackson CLI proof wrapper that records `status`, `state`, and `values` into one artifact for Deezoh / chart-analyzer / indicator-analyst
3. **[LOW]** Push the shared repo changes if cross-platform pullability matters now

## Live System State (if applicable)
- **VPS TradingView chart lane**: healthy on `127.0.0.1:9333`
- **VPS Jackson CLI**: healthy on the saved BTC chart
- **VPS tvremix**: healthy via tracker import path
- **VPS Bitget technical-analysis**: healthy and saving artifacts

## Reading List for Next Agent
- `research/platforms/2026-05-05-vps-tradingview-jackson-tvremix-repair.md`
- `/root/.openclaw/workspace/reports/auto/TECHNICAL_ANALYSIS/btcusdt_4h_vp_latest.json`
- `/root/.openclaw/workspace/projects/tradingview-mcp-jackson/src/connection.js`
