# Agent Session Handoff - TradingView Browser Lane And Volume Profile

## Session Info
- **Ended by**: Windows Codex
- **Ended at**: 2026-05-05
- **Platform**: Windows Codex + live VPS
- **Session focus**: replace the broken VPS TradingView Desktop chart lane with a persistent browser-backed CDP lane, test Jackson/browser feasibility, tighten source truth for structure indicators, and upgrade the weakest truthful local profile script

## Original Goal
Find truthful sources for divergence / structure work, test TradingView alternatives to Jackson Desktop, and move Chimera toward one real chart lane instead of duplicated weak scripts and broken page-target assumptions.

## Completed Work
- [x] Proved the key Windows vs VPS difference:
  - Windows TradingView/CDP has real page targets on `localhost:9222`
  - VPS TradingView Desktop had CDP on `9222` but zero page targets
- [x] Cloned `tradingview-mcp-jackson` locally to:
  - `C:\Users\becke\claudecowork\vendor_imports\tradingview-mcp-jackson`
- [x] Installed the local Jackson repo with `npm install`
- [x] Added local Codex MCP config for Jackson:
  - `C:\Users\becke\.codex\config.toml`
- [x] Proved local Windows Jackson quote path works against the current TradingView target
- [x] Built a browser-backed VPS chart lane on port `9333` using:
  - `google-chrome`
  - persistent profile dir `/root/.config/google-chrome/chimera-tv-profile`
  - CDP endpoint `http://127.0.0.1:9333`
- [x] Logged TradingView into that persistent VPS browser profile
- [x] Proved the VPS profile persisted enough to reopen TradingView chart targets
- [x] Patched Jackson connection code locally and on the VPS project to accept `CDP_PORT` / `CDP_HOST` from env
- [x] Switched live OpenClaw Jackson config to the browser-wrapper path in:
  - `/root/.openclaw/openclaw.json`
- [x] Added live wrapper script:
  - `/root/.openclaw/workspace/projects/tradingview-mcp-jackson/scripts/run_tv_jackson_browser.sh`
- [x] Added live persistent browser service:
  - `/etc/systemd/system/tradingview-browser-cdp.service`
  - launcher script:
    `/root/.openclaw/workspace/projects/tradingview-mcp-jackson/scripts/launch_tv_browser_debug_linux.sh`
- [x] Rewrote the old local `volume_profile.py` logic so it now:
  - spreads candle volume across overlapping bins
  - builds VAH/VAL outward from POC
  - stops using the old one-bin typical-price shortcut
- [x] Re-tested the rewritten local profile script on live BTC 4h data and confirmed it now produces a sane POC / VAH / VAL ordering
- [x] Completed a deeper tvremix tool audit and Pine/source-pattern research via subagents

## Partially Done
- [~] The VPS browser lane is alive, logged in, persistent, and exposes real TradingView page targets on `9333`, but the full Jackson toolchain was not yet cleanly re-proved end-to-end through a direct MCP tool call in this session.
- [~] The browser launch script still needs a small cleanup to avoid reopening duplicate chart tabs on repeated restarts.

## Not Done
- [ ] Rewrite `market_structure.py` as the new core structure owner.
- [ ] Rewrite `fvg_detector.py`.
- [ ] Rewrite `order_block_detector.py`.
- [ ] Collapse duplicated divergence paths into one screening layer on top of the new structure core.
- [ ] Decide and create the final set of TradingView layouts instead of one overloaded chart.

## Decisions Made
- **Decision**: the best VPS replacement for broken Desktop-based Jackson is a persistent browser-backed CDP lane.  
  **Why**: Chrome on the VPS can expose real page targets and keep a logged-in TradingView profile, while the Desktop app kept returning zero targets.
- **Decision**: start indicator truth cleanup with volume profile first.  
  **Why**: it is the highest-confidence truthful upgrade and the easiest to improve without tick data.
- **Decision**: keep divergence as screening logic, not the final truth owner.  
  **Why**: even better Pine-style divergence logic still depends on swing rules and structure context.

## Files Changed / Created
| File | Platform | What Changed |
|------|----------|-------------|
| `C:\Users\becke\claudecowork\vendor_imports\tradingview-mcp-jackson\src\connection.js` | Windows local | Jackson now supports env-driven CDP host/port and better target selection |
| `C:\Users\becke\.codex\config.toml` | Windows local | Added local `tradingview-jackson` MCP server |
| `C:\Users\becke\claudecowork\trading_system\scripts\indicators\volume_profile.py` | Windows local | Rewrote profile logic to overlap-bin volume distribution and POC-centered value area expansion |
| `C:\Users\becke\claudecowork\research\platforms\2026-05-04-structure-detector-and-tradingview-reliability-audit.md` | Windows/shared | Added Windows Jackson proof and later browser-lane truth context |
| `/root/.openclaw/workspace/projects/tradingview-mcp-jackson/src/connection.js` | Live VPS | Patched env-driven CDP port/host and better target selection |
| `/root/.openclaw/workspace/projects/tradingview-mcp-jackson/scripts/run_tv_jackson_browser.sh` | Live VPS | Browser-backed Jackson wrapper |
| `/root/.openclaw/workspace/projects/tradingview-mcp-jackson/scripts/launch_tv_browser_debug_linux.sh` | Live VPS | Persistent browser CDP launcher |
| `/etc/systemd/system/tradingview-browser-cdp.service` | Live VPS | Persistent browser CDP service |
| `/root/.openclaw/openclaw.json` | Live VPS | `tradingview-jackson` now points at the browser wrapper |

## Live System State
- **Windows local**
  - TradingView Desktop is installed and running
  - `localhost:9222` has real page targets
  - local Jackson quote path worked
- **VPS browser lane**
  - service name: `tradingview-browser-cdp.service`
  - CDP port: `9333`
  - profile dir: `/root/.config/google-chrome/chimera-tv-profile`
  - current page targets: real TradingView chart pages exist
  - current saved chart title observed in list: `BTCUSDT.P ... idicators plus aavp`

## Best Source Truth Right Now
- **Bars / raw chart context**
  - Bitget candles
  - TradingView chart/browser lane
- **Best current profile math**
  - rewritten `volume_profile.py`
- **Best TradingView structure second opinion**
  - `tvremix analyze_smc_tool`
- **Best bulk tvremix tools**
  - `get_quotes_batch`
  - `get_ohlcv`
  - `analyze_swing_tool`
  - `calculate_correlation_tool`
- **Do not trust as final truth yet**
  - old FVG script
  - old order block script
  - duplicated divergence scripts as final signal owners

## Next Actions
1. **[PRIORITY]** Re-prove `tradingview-jackson` through a real MCP call against the new VPS browser lane, not just CDP target presence.
2. **[PRIORITY]** Rewrite `market_structure.py`, then rebuild FVG / order block on top of it.
3. **[PRIORITY]** Clean duplicate chart pages on VPS restart and tighten the launcher so one chart target is preferred.
4. **[MEDIUM]** Decide the final TradingView layout strategy:
   - multiple focused layouts, not one chart overloaded with everything
5. **[MEDIUM]** Build a Chimera-safe wrapper for the useful tvremix tools and block the broken/fluff ones.

## Routing Used
- **Task lane**: mixed
- **Model used**: parent review/planning on `gpt-5.5`; worker research slices on `gpt-5.4`
- **Reasoning used**: high parent, medium workers
- **Result quality**: strong on browser-lane truth and source-quality ranking; partial on final Jackson MCP re-proof

## Sync Status
- **GitHub status**: local workspace plus live VPS changes; not pushed
- **Other platforms that should pull this**: Windows Claude, future Windows Codex threads, live VPS operators
