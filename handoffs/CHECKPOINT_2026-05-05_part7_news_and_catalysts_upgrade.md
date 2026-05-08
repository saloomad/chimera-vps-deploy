# Part 7 News And Catalysts Upgrade Checkpoint

Date: 2026-05-05
Owner: Codex
Scope: Section 7 contract upgrade, news source proof, news owner tuning, live runtime sync

## What changed

- upgraded `Section 7: News And Catalysts` in:
  - `chimera-vps-deploy/skills/CHIMERA_RESEARCH_BUNDLE_TEMPLATE.md`
- added:
  - explicit objective
  - Deezoh question set
  - relevance-filter contract
  - noise-vs-relevant headline separation
  - catalyst tradeability state
  - catalyst resolution state
  - missing news lanes fields
  - improve / break conditions

- replaced the stub `news-monitor` owner docs:
  - `agents/news-monitor/AGENTS.md`
  - `agents/news-monitor/TOOLS.md`

- added durable notes:
  - `research/platforms/2026-05-05-news-and-catalysts-source-matrix.md`
  - `research/platforms/2026-05-05-btc-part7-deezoh-example.md`

- fixed the shared news bridge:
  - `scripts/skill_bridges/market_mcp_utils.py`
    - Windows local `mcporter` detection
    - Linux live `npx mcporter` fallback
    - UTF-8-safe subprocess decoding
  - `scripts/skill_bridges/build_news_json.py`
    - null-safe title / summary handling

## Proof

Local Windows:
- proved direct `mcporter` news feed calls work
- re-ran:
  - `python scripts/skill_bridges/build_news_json.py`
- fresh local `NEWS.json` now shows:
  - skill-first generation
  - no `_meta.errors`
  - `article_count = 98`
  - `breaking_count = 17`

Live VPS:
- synced:
  - `CHIMERA_RESEARCH_BUNDLE_TEMPLATE.md`
  - `agents/news-monitor/AGENTS.md`
  - `agents/news-monitor/TOOLS.md`
  - `scripts/skill_bridges/market_mcp_utils.py`
  - `scripts/skill_bridges/build_news_json.py`
  - both new research notes
- cleared stale `__pycache__`
- re-proved live feed calls
- re-ran the live builder through module execution and refreshed:
  - `/root/openclawtrading/reports/auto/NEWS.json`
- fresh live `NEWS.json` now shows:
  - no `_meta.errors`
  - `article_count = 98`
  - `breaking_count = 18`

## Current truth

- `NEWS.json` is now the strongest current Section 7 owner
- the lane is fresh both locally and on the live VPS
- the current headline tape is useful, but still needs symbol-level relevance filtering
- `AI_CATALYST.json` was not present in the local Windows workspace during this pass, so the catalyst-gate lane remains missing there

## Remaining gaps

- the current skill-first lane still groups a lot of non-crypto narrative into a broad bucket
- theme clustering is helper-grade and can over-match broad keywords
- Section 7 still lacks a stronger file-backed scheduled catalyst lane for:
  - symbol-specific regulatory events
  - exchange/listing events
  - unlocks / governance events
  - stock earnings when the asset is equity-like

## Next best follow-up

1. Add a dedicated scheduled-catalyst lane by asset type.
2. Add a stronger symbol-relevance scorer so Deezoh gets fewer noisy headlines.
3. Run a full bundle example where Deezoh consumes:
   - Part 2
   - Part 3
   - Part 4
   - Part 5
   - Part 6
   - Part 7
   together.
