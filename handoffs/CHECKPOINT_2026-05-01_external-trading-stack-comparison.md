# Agent Session Handoff - Chimera Ecosystem

## Session Info
- **Ended by**: Windows Codex
- **Ended at**: 2026-05-01T20:55:00+03:00
- **Platform**: Windows Codex
- **Session focus**: compare external trading-agent and chart repos against Chimera, choose the right borrow-vs-reference strategy, and implement the first reusable stock-plus-crypto research spine locally

## Original Goal
Deeply analyze `Vibe-Trading`, both TradingView MCP repos, `claude-trading-skills`, `EVClaw`, and `claude-code-trading-terminal`, decide how they should affect Chimera, capture the result durably, and execute a real first implementation slice instead of stopping at a memo.

## Completed Work
- [x] Compared all six repos locally and with a council of subagents
- [x] Determined the best ideal target is a Chimera hybrid desk: Chimera keeps live truth and execution boundaries, while a cleaner stock-plus-crypto research layer feeds typed decisions into it
- [x] Wrote a durable comparison note at `C:\Users\becke\claudecowork\research\platforms\2026-05-01-external-trading-stack-comparison.md`
- [x] Indexed the note in `C:\Users\becke\claudecowork\research\INDEX.md`
- [x] Added a reusable instrument registry at `C:\Users\becke\claudecowork\linuxopenclawtrading\trading_system\scripts\instrument_registry.py`
- [x] Added an append-only decision journal at `C:\Users\becke\claudecowork\linuxopenclawtrading\trading_system\scripts\decision_journal.py`
- [x] Added a one-shot research graph runner at `C:\Users\becke\claudecowork\linuxopenclawtrading\trading_system\scripts\chimera_research_graph.py`
- [x] Updated `research_decision_engine.py` to use the shared instrument registry
- [x] Updated `chimera_entry_exit_sim.py` so the local overlay now consumes the shared research graph path and carries instrument-profile metadata
- [x] Added unit tests for registry and research-graph behavior
- [x] Captured the work into the Chimera knowledge wiki source surfaces
- [x] Extended the research graph from bundle-only input into a simple live-lite fetch path that produced real local outputs for `BTCUSDT` and `AAPL`
- [x] Added richer live-lite stock context and journal-aware replay output so the comparison layer can see recent research memory for the symbol under test

## Partially Done
- [~] The new research graph is real and locally proven and now supports richer live-lite context, but it still lacks deeper stock and crypto context such as dedicated earnings/news pipelines, fuller fundamentals coverage, and broader derivatives history
- [~] The local mirror still has old path assumptions in `runtime_paths.py` and other surfaces, so this slice stayed path-safe and local instead of pretending the whole mirror is already migration-clean

## Not Done
- [ ] Broaden the new research graph from live-lite price-plus-indicator fetches into fuller stock-plus-crypto context
- [ ] Feed the decision journal into broader replay/backtest evaluation
- [ ] Rebuild the chart lane from the original `tradingview-mcp` base if that becomes the next priority
- [ ] Promote any of this into the live paper desk path on the VPS before broader proof exists

## Decisions Made
- **Decision**: do not transplant external repos into Chimera | **Why**: each repo is strongest in a different layer, and Chimera already owns the live desk, watchdog, and operator truth layers
- **Decision**: implement instrument routing plus research graph plus decision journal first | **Why**: every useful path from the council depended on a reusable stock-plus-crypto spine before more agents or more prompts would matter
- **Decision**: keep the new slice local and proof-first | **Why**: bundle-driven research output is useful now, but it is not ready for live desk promotion

## Files Changed / Created
| File | Platform | What Changed |
|------|----------|-------------|
| C:\Users\becke\claudecowork\linuxopenclawtrading\trading_system\scripts\instrument_registry.py | Windows local mirror | New stock-plus-crypto instrument profile and loader routing layer |
| C:\Users\becke\claudecowork\linuxopenclawtrading\trading_system\scripts\decision_journal.py | Windows local mirror | New append-only decision journal helper |
| C:\Users\becke\claudecowork\linuxopenclawtrading\trading_system\scripts\chimera_research_graph.py | Windows local mirror | New bundle-driven typed research graph entrypoint |
| C:\Users\becke\claudecowork\linuxopenclawtrading\trading_system\scripts\research_decision_engine.py | Windows local mirror | Switched asset-class inference to the shared instrument registry |
| C:\Users\becke\claudecowork\linuxopenclawtrading\trading_system\scripts\chimera_entry_exit_sim.py | Windows local mirror | Local overlay now uses the shared research graph path and preserves instrument-profile metadata |
| C:\Users\becke\claudecowork\linuxopenclawtrading\trading_system\scripts\test_instrument_registry.py | Windows local mirror | New unit tests for symbol routing |
| C:\Users\becke\claudecowork\linuxopenclawtrading\trading_system\scripts\test_chimera_research_graph.py | Windows local mirror | New unit tests for bundle analysis and journal writes |
| C:\Users\becke\claudecowork\research\platforms\2026-05-01-external-trading-stack-comparison.md | Windows workspace | New durable comparison and implementation note |
| C:\Users\becke\claudecowork\research\INDEX.md | Windows workspace | Indexed the new note |
| C:\Users\becke\claudecowork\research\chimera-knowledge-wiki\raw\build_and_skills\2026-05-01-external-trading-stack-comparison.md | Windows workspace | Raw wiki capture for the comparison and implementation slice |
| C:\Users\becke\claudecowork\research\chimera-knowledge-wiki\wiki\sources\external-trading-stack-comparison-2026-05-01.md | Windows workspace | New wiki source page |
| C:\Users\becke\claudecowork\research\chimera-knowledge-wiki\wiki\index.md | Windows workspace | Added the new source to the source index |
| C:\Users\becke\claudecowork\research\chimera-knowledge-wiki\wiki\log.md | Windows workspace | Logged the new ingest |

## Skills Created / Updated
- [ ] none in this slice

## Other Durable Outputs Created
- [x] `C:\Users\becke\claudecowork\linuxopenclawtrading\reports\research_lab\research_graph_BTCUSDT.json`
- [x] `C:\Users\becke\claudecowork\linuxopenclawtrading\reports\research_lab\decision_journal.jsonl`
- [x] `C:\Users\becke\claudecowork\linuxopenclawtrading\reports\research_lab\research_graph_BTCUSDT_live.json`
- [x] `C:\Users\becke\claudecowork\linuxopenclawtrading\reports\research_lab\research_graph_AAPL_live.json`

## Sync Status
- **GitHub status**: local only
- **Other platforms that should pull this**: Windows Claude and Kimi VPS if this architecture note or research spine should become shared truth
- **What still needs sync**: decide whether to move the new research graph and journal pattern into the VPS repo and whether to mirror the wiki updates there

## Routing Used
- **Task lane**: mixed
- **Model used**: gpt-5.5
- **Reasoning used**: high
- **Result quality**: strong
- **Rerun needed**: yes
- **Better route next time**: same route, but next pass should split into research-fetch expansion versus live-path integration

## Next Actions (for next agent)
1. **[PRIORITY]** Expand `chimera_research_graph.py` from the current live-lite context into fuller dedicated stock and crypto context with better news, earnings, and derivatives coverage
2. **[MEDIUM]** Push the journal-aware replay path further into thesis-memory and broader evaluation summaries
3. **[MEDIUM]** Clean the old path layer, starting with `runtime_paths.py`, before any VPS-side promotion
4. **[LOW]** Rebuild the chart lane from the original `tradingview-mcp` base if chart modernization becomes the active objective

## Skills to Read Before Starting
- [x] objective-orchestration-loop
- [x] vibe-coding-operator
- [ ] chimera-knowledge-wiki
- [ ] pipeline-simulation-lab

## Live System State (if applicable)
- **OpenClaw Gateway**: not checked in this slice
- **TradingView Desktop**: not checked in this slice
- **Discord Bot**: not checked in this slice
- **Last data update**: not checked in this slice

## Reading List for Next Agent
- `C:\Users\becke\claudecowork\research\platforms\2026-05-01-external-trading-stack-comparison.md`
- `C:\Users\becke\claudecowork\linuxopenclawtrading\trading_system\scripts\instrument_registry.py`
- `C:\Users\becke\claudecowork\linuxopenclawtrading\trading_system\scripts\chimera_research_graph.py`
- `C:\Users\becke\claudecowork\linuxopenclawtrading\reports\research_lab\research_graph_BTCUSDT.json`
- `C:\Users\becke\claudecowork\linuxopenclawtrading\reports\research_lab\decision_journal.jsonl`
- `C:\Users\becke\claudecowork\linuxopenclawtrading\reports\research_lab\research_graph_BTCUSDT_live.json`
- `C:\Users\becke\claudecowork\linuxopenclawtrading\reports\research_lab\research_graph_AAPL_live.json`
