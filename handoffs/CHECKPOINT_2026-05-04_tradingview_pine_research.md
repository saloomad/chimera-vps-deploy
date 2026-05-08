# Agent Session Handoff - TradingView Pine Research

## Session Info
- **Ended by**: Windows Codex
- **Ended at**: 2026-05-04T23:59:00+03:00
- **Platform**: Windows Codex
- **Session focus**: compare public TradingView/Pine and GitHub indicator patterns against the local Chimera divergence, FVG, order block, market structure, and volume profile scripts

## Original Goal
Produce a concise, source-backed recommendation for which public Pine patterns are worth borrowing or rewriting locally, with exact guidance on what to copy, what to avoid, and which local scripts are truthful enough to keep.

## Completed Work
- [x] Re-read bootstrap, runtime-router, latest handoff, and relevant memory before research.
- [x] Audited the current local indicator scripts in `trading_system/scripts/indicators/`.
- [x] Reviewed public TradingView / GitHub Pine sources for divergence, FVG, market structure, order blocks, and volume profile.
- [x] Updated the existing local structure audit with an explicit copy / avoid / target map.

## Partially Done
- [~] No code rewrite was started. This pass stopped at research and durable capture so implementation can be sequenced cleanly.

## Not Done
- [ ] Rewrite `volume_profile.py` around overlapping-bin distribution and POC-centered value-area expansion.
- [ ] Build a standalone local market-structure core for pivots, BOS, and CHoCH.
- [ ] Rewrite `fvg_detector.py` and `order_block_detector.py` on top of that structure core.

## Decisions Made
- **Decision**: treat VPVR-style volume profile logic as the best first rewrite target | **Why**: it is the clearest accuracy upgrade over the current local approximation.
- **Decision**: treat divergence as helper-only even after improvement | **Why**: public Pine examples are still mostly heuristic and not strong enough for authoritative truth.
- **Decision**: avoid direct monolithic Pine ports | **Why**: they mix rendering, alerts, state, and entries in ways that do not map cleanly to the local Python stack.

## Files Changed / Created
| File | Platform | What Changed |
|------|----------|-------------|
| `research/platforms/2026-05-04-structure-detector-and-tradingview-reliability-audit.md` | Windows | Added public-source comparison and exact copy / avoid / target guidance. |
| `research/chimera-knowledge-wiki/wiki/sources/structure-detector-and-tradingview-reliability-audit-2026-05-04.md` | Windows | Tightened the summary with the new rewrite direction. |
| `chimera-vps-deploy/handoffs/CHECKPOINT_2026-05-04_tradingview_pine_research.md` | Windows | Added this handoff. |

## Skills Created / Updated
- [ ] none

## Other Durable Outputs Created
- [x] updated research audit and wiki source note - local only

## Sync Status
- **GitHub status**: local only
- **Other platforms that should pull this**: Windows Claude, Kimi VPS if rewrite work starts later
- **What still needs sync**: push the updated research note and handoff if Sal wants this preserved cross-platform

## Routing Used
- **Task lane**: research
- **Model used**: gpt-5.4
- **Reasoning used**: medium
- **Result quality**: strong
- **Rerun needed**: no
- **Better route next time**: same

## Next Actions (for next agent)
1. **[HIGH]** Rewrite `trading_system/scripts/indicators/volume_profile.py` first using overlapping-bin allocation and outward VA expansion from POC.
2. **[MEDIUM]** Add a local `market_structure.py` core using confirmed pivots and explicit BOS / CHoCH state.
3. **[MEDIUM]** Rebuild FVG and order block detectors on top of that structure core instead of patching the current heuristics.

## Skills to Read Before Starting
- [x] codex-runtime-router - for routing and header discipline
- [x] agent-session-resume - if continuing this handoff
- [ ] technical-analysis - only if Bitget-backed indicator comparison is needed again

## Live System State (if applicable)
- **OpenClaw Gateway**: not checked in this pass
- **TradingView Desktop**: not checked in this pass
- **Discord Bot**: not checked in this pass
- **Last data update**: not applicable

## Reading List for Next Agent
- `research/platforms/2026-05-04-structure-detector-and-tradingview-reliability-audit.md`
- `research/chimera-knowledge-wiki/wiki/sources/structure-detector-and-tradingview-reliability-audit-2026-05-04.md`
