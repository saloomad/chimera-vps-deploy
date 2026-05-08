# Agent Session Handoff - Chimera Ecosystem

## Session Info
- **Ended by**: Windows Codex
- **Ended at**: 2026-05-02T04:00:00+03:00
- **Platform**: Windows Codex
- **Session focus**: audit Chimera trading scripts against available skills, document the real decision/data architecture, and do the first safe cleanup pass

## Original Goal
Figure out which trading scripts are still needed, which can be replaced by skills or agent reasoning, what data Deezoh is actually using, and what should be cleaned up first without drifting into useless work.

## Completed Work
- [x] Replaced the stale script README with a clearer current pointer doc
- [x] Wrote `ARCHITECTURE_GUIDE.md` with current data flow, data sources, keep-vs-replace logic, and diagrams
- [x] Wrote `SKILL_REPLACEMENT_AUDIT.md` with a practical keep / replace / retire map
- [x] Wrote a durable research note in `research/operations/2026-05-02-chimera-script-skill-rationalization.md`
- [x] Archived the safest clutter out of the main scripts lane:
  - `chimera_entry_exit_sim.py.bak_`
  - `execution_agent.py.bak_20260420_1627`
  - `phase2_demo.py`
  - `phase2_enhanced_demo.py`
  - `phase2_simple_demo.py`
  - `news_scraper.py`
  - `economic_calendar_scraper.py`
  - `macro_calendar_checker.py`
  - `paper_trading_bitget.py`
  - `heartbeat_fixed.py`
  - `heartbeat_orchestrator.py`
  - `heartbeat_cli.py`
  - `heartbeat_direct.py`
  - `tradingview_heartbeat.py`
- [x] Removed generated Python cache clutter from the local scripts tree (`__pycache__/` and `.pyc`)
- [x] Checked the live VPS crontab and repo consumers before archiving the old scraper and heartbeat variants locally

## Partially Done
- [~] The script-vs-skill map is now clear enough to act on
- [~] The main remaining unknown is `price_monitor.py` and a few older wrapper paths, not the archived scraper or heartbeat variants

## Not Done
- [ ] Move root-level test files into a clearer tests folder
- [ ] Thin or retire older scanner and decision wrappers after consumer checks
- [ ] Build or install a stronger stock-analysis skill lane beyond earnings-risk context

## Decisions Made
- **Decision**: do not try to replace every collector with a skill | **Why**: skills are strong reasoning layers, but weak as headless deterministic collectors unless ported into a callable runtime surface
- **Decision**: preserve the newer typed research overlay as the simplification direction | **Why**: it is already the cleanest stock-plus-crypto decision spine in the repo
- **Decision**: archive the old scraper and heartbeat variants locally after a live VPS consumer check | **Why**: live crontab and repo grep showed active fetchers, not those older variants

## Files Changed / Created
| File | Platform | What Changed |
|------|----------|-------------|
| C:\Users\becke\claudecowork\linuxopenclawtrading\trading_system\scripts\README.md | Windows local mirror | Replaced stale inventory with current pointer doc |
| C:\Users\becke\claudecowork\linuxopenclawtrading\trading_system\scripts\ARCHITECTURE_GUIDE.md | Windows local mirror | New architecture/data-flow guide |
| C:\Users\becke\claudecowork\linuxopenclawtrading\trading_system\scripts\SKILL_REPLACEMENT_AUDIT.md | Windows local mirror | New keep/replace/remove audit |
| C:\Users\becke\claudecowork\linuxopenclawtrading\trading_system\scripts\_archive_candidates\README.md | Windows local mirror | Explains the first archive pass |
| C:\Users\becke\claudecowork\research\operations\2026-05-02-chimera-script-skill-rationalization.md | Windows workspace | Durable research note |
| C:\Users\becke\claudecowork\research\INDEX.md | Windows workspace | Indexed the new note |

## Other Durable Outputs Created
- [x] `trading_system/scripts/_archive_candidates/chimera_entry_exit_sim.py.bak_`
- [x] `trading_system/scripts/_archive_candidates/execution_agent.py.bak_20260420_1627`
- [x] `trading_system/scripts/_archive_candidates/phase2_demo.py`
- [x] `trading_system/scripts/_archive_candidates/phase2_enhanced_demo.py`
- [x] `trading_system/scripts/_archive_candidates/phase2_simple_demo.py`
- [x] `trading_system/scripts/_archive_candidates/news_scraper.py`
- [x] `trading_system/scripts/_archive_candidates/economic_calendar_scraper.py`
- [x] `trading_system/scripts/_archive_candidates/macro_calendar_checker.py`
- [x] `trading_system/scripts/_archive_candidates/paper_trading_bitget.py`
- [x] `trading_system/scripts/_archive_candidates/heartbeat_fixed.py`
- [x] `trading_system/scripts/_archive_candidates/heartbeat_orchestrator.py`
- [x] `trading_system/scripts/_archive_candidates/heartbeat_cli.py`
- [x] `trading_system/scripts/_archive_candidates/heartbeat_direct.py`
- [x] `trading_system/scripts/_archive_candidates/tradingview_heartbeat.py`

## Sync Status
- **GitHub status**: local only
- **What still needs sync**: the next useful sync point is after `price_monitor.py` and the root-level test-file reorg are resolved too

## Routing Used
- **Task lane**: mixed
- **Model used**: gpt-5.5
- **Reasoning used**: high
- **Result quality**: strong
- **Rerun needed**: yes
- **Better route next time**: same route, but with a VPS-first consumer check for old scrapers and heartbeat variants

## Next Actions (for next agent)
1. **[PRIORITY]** Check `price_monitor.py` and related shadow monitor consumers more directly before archiving it
2. **[MEDIUM]** Move root-level test files into a clearer tests folder
3. **[MEDIUM]** Thin or retire older wrapper scripts in favor of collectors + research overlay + execution engine
4. **[LOW]** Strengthen the stock-analysis skill lane so more old stock logic can be retired cleanly
