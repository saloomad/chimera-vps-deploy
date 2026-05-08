# Part 7 Catalyst Context Upgrade Checkpoint

Date: 2026-05-05
Owner: Codex
Scope: turn Section 7 into a real catalyst owner with explicit source truth, persistent context, playbook memory, and live VPS proof

## What changed

- upgraded `Section 7: Catalysts, News, And Event Context` in:
  - `chimera-vps-deploy/skills/CHIMERA_RESEARCH_BUNDLE_TEMPLATE.md`
- added:
  - `source_registry`
  - persistent bundle independent-refresh tracking
  - policy-path lane coverage field
  - exact-symbol live news lane field
  - live earnings lookup field
  - richer event / playbook / asset-search fields

- upgraded the catalyst owner docs:
  - `agents/catalyst/AGENTS.md`
  - `agents/catalyst/TOOLS.md`

- upgraded the section-upgrader skill so it must now say:
  - which real sources were used
  - which are cross-check only
  - which obvious sources are not actually wired
  - whether persistent context is current and independently refreshed
  - what each cited artifact is in plain English

- fixed the catalyst loop itself:
  - `scripts/catalyst_agent/catalyst_agent.py`
    - now uses the real runtime reports path
    - now auto-refreshes `AI_CATALYST.json`
    - now auto-refreshes the persistent catalyst bundle
  - `scripts/refresh_catalyst_context_bundle.py`
    - now writes:
      - `BIAS_STATE.md`
      - `PATTERN_MEMORY.md`
    - now records persistent bundle files in `STATE.json`

- refreshed durable notes:
  - `research/platforms/2026-05-05-news-and-catalysts-source-matrix.md`
  - `research/platforms/2026-05-05-btc-part7-deezoh-example.md`

## Proof

Local Windows:
- `python scripts/catalyst_agent/catalyst_agent.py`
  - wrote fresh:
    - `CATALYST_REPORT.json`
    - `AI_CATALYST.json`
    - `agents/catalyst/SPAWN_CONTEXT.md`
    - `THOUGHTS.md`
    - `CURRENT_BRIEF.md`
    - `WATCH_ITEMS.md`
    - `PLAYBOOKS.md`
    - `BIAS_STATE.md`
    - `PATTERN_MEMORY.md`
    - `STATE.json`
- `python -m py_compile` passed for:
  - `scripts/catalyst_agent/catalyst_agent.py`
  - `scripts/refresh_catalyst_context_bundle.py`
  - `scripts/catalyst_contract_bridge.py`
- proved exact-symbol `tvremix get_news` works for:
  - `BINANCE:BTCUSDT`
  - `NASDAQ:AAPL`
  - `OANDA:XAUUSD`
  - `TVC:USOIL`
- proved live earnings lookup works through:
  - `mcp__market_data__.tradfi_news(action=earnings)`

Live VPS:
- synced:
  - catalyst agent docs
  - Section 7 template
  - catalyst loop scripts
  - refreshed source matrix
  - refreshed BTC example
- `python3 -B /root/openclawtrading/scripts/catalyst_agent.py`
  - wrote fresh:
    - `/root/openclawtrading/reports/auto/CATALYST_REPORT.json`
    - `/root/openclawtrading/reports/auto/AI_CATALYST.json`
    - `/root/.openclaw/workspace/agents/catalyst/SPAWN_CONTEXT.md`
    - `THOUGHTS.md`
    - `CURRENT_BRIEF.md`
    - `WATCH_ITEMS.md`
    - `PLAYBOOKS.md`
    - `BIAS_STATE.md`
    - `PATTERN_MEMORY.md`
    - `STATE.json`

## Current truth

- Section 7 is now owned by the `catalyst` lane, not just a news reader.
- Current primary sources are:
  - `CATALYST_REPORT.json`
  - `NEWS.json`
  - `ECONOMIC_CALENDAR.json`
  - persistent catalyst bundle files
- Current support lanes are:
  - `AI_CATALYST.json`
  - exact-symbol `tvremix get_news`
  - live earnings lookup via `mcp__market_data__.tradfi_news(action=earnings)`
  - `EARNINGS_CALENDAR.json` when healthy
- Current not-primary sources are:
  - `tvremix` as a broad catalyst owner
  - Bitget news / technical lanes
- Live VPS persistent context is now current enough for spawned children to inherit safely.

## Remaining gaps

1. Live VPS cached earnings file lane is still missing.
2. There is still no direct market-implied rate-cut-probability lane.
3. Exact-symbol search now works, but it still needs to be used automatically in the normal catalyst flow instead of only as a helper.
4. `AI_CATALYST.json` is a compatibility lane only and should not replace the canonical catalyst report.

## Next best follow-up

1. Add or prove a real earnings lane on the live VPS.
2. Add a direct policy-probability lane if we want true FedWatch-style fields instead of playbook inference.
3. Add stronger symbol-specific catalyst search for:
   - BTC / specific coins
   - gold
   - oil
   - stocks
4. Run a full Deezoh consumption test across Parts 2 through 7 together.
