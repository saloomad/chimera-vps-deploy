# CHECKPOINT — 2026-05-05 — data-source router, workflow, and OpenClaw TradingView docs

## What landed

- Proved the live VPS TradingView Jackson lane works on the browser-backed persistent profile.
- Added the first deterministic local indicator foundation:
  - market structure
  - anchored VWAP
  - anchored volume profile
  - Monday/day/week ranges
  - explicit-anchor Fibonacci
- Upgraded the first local FVG and order-block detectors in the main workspace.
- Added a reusable loop-until-done workflow for source build/integration work.
- Added a shared `chimera-data-source-router` skill and mirrored it to the real active skill-load paths.
- Added durable data-source documentation and copied the key docs to the live VPS repo.

## Live proof

### VPS TradingView / Jackson

Host:
- `root@100.67.172.114`

Working lane:
- browser-backed CDP on `127.0.0.1:9333`
- persistent profile at `/root/.config/google-chrome/chimera-tv-profile`
- service: `tradingview-browser-cdp.service`

Verified in this pass:
- Jackson `quote` worked
- Jackson `ohlcv --summary` worked
- Jackson `values` worked
- Jackson `data lines` worked

### OpenClaw skill proof

Verified:
- `openclaw skills list` shows `chimera-data-source-router` as `ready`
- skill copied to:
  - `/root/openclawtrading/skills/chimera-data-source-router`
  - `/root/.openclaw/kimi-skills/chimera-data-source-router`

### Live VPS docs copied

Verified in `/root/openclawtrading/docs/`:
- `CHIMERA_DATA_SOURCE_BUILD_AND_INTEGRATION_LOOP_2026-05-05.md`
- `CHIMERA_DATA_SOURCE_CATALOG_2026-05-05.md`
- `CHIMERA_TRADINGVIEW_OWNER_MAP_2026-05-05.md`
- `CHIMERA_DATA_SOURCE_KEEP_DEMOTE_AVOID_2026-05-05.md`

## Main files touched

### Indicator foundation

- `trading_system/scripts/indicators/market_structure.py`
- `trading_system/scripts/indicators/anchored_vwap.py`
- `trading_system/scripts/indicators/anchored_volume_profile.py`
- `trading_system/scripts/indicators/create_anchored_volume_profile.py`
- `trading_system/scripts/indicators/range_levels.py`
- `trading_system/scripts/indicators/fibonacci_calculator.py`
- `trading_system/scripts/indicators/fvg_detector.py`
- `trading_system/scripts/indicators/order_block_detector.py`

### Workflow and docs

- `workflows/codex/data-source-build-integration-and-mirror-loop.md`
- `workflows/codex/WORKFLOW_CATALOG.md`
- `research/platforms/2026-05-05-chimera-data-source-catalog.md`
- `research/platforms/2026-05-05-data-source-keep-demote-avoid-decisions.md`
- `research/platforms/2026-05-05-tradingview-jackson-and-deterministic-indicator-owner-map.md`
- `research/chimera-knowledge-wiki/wiki/sources/chimera-data-source-catalog-2026-05-05.md`
- `research/chimera-knowledge-wiki/wiki/sources/data-source-keep-demote-avoid-decisions-2026-05-05.md`
- `research/chimera-knowledge-wiki/wiki/sources/tradingview-jackson-and-deterministic-indicator-owner-map-2026-05-05.md`
- `chimera-vps-deploy/docs/CHIMERA_DATA_SOURCE_BUILD_AND_INTEGRATION_LOOP_2026-05-05.md`

### Shared skill

- `chimera-vps-deploy/skills/chimera-data-source-router/SKILL.md`
- `chimera-vps-deploy/skills/chimera-data-source-router/references/current-source-map.md`

### Shared continuity

- `shared_ai_context/CURRENT_STATE.md`
- `shared_ai_context/NEXT_ACTIONS.md`
- `shared_ai_context/TASKS_LEFT.md`
- `shared_ai_context/SKILLS_AVAILABLE.md`

## Current owner split

- deterministic local scripts = truth owner for repeatable level math
- deterministic local scripts now also own the first real market-structure layer
- Coinalyze = main direct derivatives source
- Bitget skill pack = crypto analyst-layer context
- TradingView Jackson on VPS browser lane = live chart-state reader
- tvremix = limited-budget second-opinion lane

## Source-pruning decisions that landed

### Keep as first-class

- deterministic local indicator scripts
- Coinalyze and `derivatives`
- Bitget skill pack
- TradingView Jackson browser-backed lane
- tvremix
- `macro-calendar`
- `historical-market-context`
- `coinglass_daily_scout.py`
- `news_fetcher.py`
- `market_context_fetcher.py`
- `economic_calendar_fetcher.py`
- `earnings_calendar_fetcher.py`

### Demote

- `tradingview-screener`
- `news-reader`
- `altfins`
- `chimera-bitget-derivatives-data`
- `coinglass_maxpain_scraper.py`
- `liquidation_heatmap.py`
- `trading_system/scripts/data/ccxt_fetcher.py`
- `trading_system/scripts/data/tradingview_api.py`

### Avoid as current owners

- `earnings-calendar` as a separate source lane
- `coingecko_narratives_fetcher.py`
- `trading_system/scripts/data/coinglass_scraper.py`
- `trading_system/scripts/data/liquidation_fetcher.py`
- `trading_system/scripts/data/tradingview_explorer.py`
- `trading_system/scripts/data/tv_simple_test.py`
- `trading_system/scripts/data/test_scraper.py`

These decisions were written into:

- the shared platform catalog
- the new keep/demote/avoid research note
- the wiki
- the shared `chimera-data-source-router`
- the live VPS OpenClaw runtime copies

## Still open

- collapse duplicated divergence paths into one secondary detector
- add stronger regression tests around structure, FVG, and order blocks
- wire the new structure owners into higher-level consumers
- keep expanding the router skill and source catalog as new source families are added
- turn the new demote and avoid decisions into deeper cleanup so legacy lanes stop competing with the first-class owners
