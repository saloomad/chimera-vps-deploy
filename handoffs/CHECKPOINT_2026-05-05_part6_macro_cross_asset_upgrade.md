# Part 6 Macro And Cross-Asset Upgrade Checkpoint

Date: 2026-05-05
Owner: Codex
Scope: Section 6 contract upgrade, source proof, macro agent tuning, live runtime sync

## What changed

- upgraded `Part 6: Macro And Cross-Asset` in:
  - `chimera-vps-deploy/skills/CHIMERA_RESEARCH_BUNDLE_TEMPLATE.md`
- redesigned the section around recommendation-based analysis instead of lock or veto language
- made the section explicitly answer:
  - what `SPX` is saying
  - what `DXY` and yields are saying
  - what `gold` and `oil` are saying
  - what `BTC.D`, `USDT.D`, and `TOTAL3 ex BTC/ETH` are saying
  - how much macro weight Deezoh should give the setup right now
  - what macro confirms now versus what it still does not confirm
- replaced old permission-style fields with:
  - `macro_recommendation_state`
  - `how_deezoh_should_use_macro_now`
  - `recommendation_weight`
  - `when_partial_macro_is_still_usable`
  - `what_macro_confirms_now`
  - `what_macro_does_not_confirm_yet`
  - `what_macro_should_make_deezoh_do`
  - `what_macro_should_not_be_used_for`
- replaced generic lane coverage with explicit lanes for:
  - `spx`
  - `dxy`
  - `yields`
  - `gold`
  - `oil`
  - `btc_d`
  - `usdt_d`
  - `total3_ex_btc_eth`
- clarified placement:
  - economic calendar belongs in `Part 6`
  - company earnings normally belong in `Part 7: News And Catalysts`
  - broad earnings-season tone can be helper-only context for index-sensitive setups

- upgraded macro owner instructions:
  - `agents/macro-bias/AGENTS.md`
  - `agents/macro-bias/TOOLS.md`

- upgraded durable notes:
  - `research/platforms/2026-05-05-macro-and-cross-asset-source-matrix.md`
  - `research/platforms/2026-05-05-btc-part6-deezoh-example.md`
  - `research/platforms/2026-05-05-part6-macro-deezoh-simulation-and-improvement.md`

- earlier builder fixes remain part of the same section hardening:
  - `scripts/macro_bias_builder/macro_bias_builder.py`
  - corrected event-name extraction so `title` is used when `name` is absent
  - corrected gate-check wording so event presence is not mislabeled as `Clear`
  - corrected event filtering so only truly relevant high-impact next-48h events can force a stand-down style warning
  - hardened importance parsing so VPS-side labels like `CRITICAL` no longer crash the builder

## Proof

Local:
- inspected fresh outputs:
  - `reports/auto/ECONOMIC_CALENDAR.json`
  - `reports/auto/MACRO_BIAS.json`
  - `reports/auto/MARKET_CONTEXT.json`
  - `reports/auto/CROSS_ASSET.json`
  - `reports/auto/EARNINGS_CALENDAR.json`
- verified the updated section, owner files, and research notes locally
- verified that the new recommendation language and explicit lane coverage are present

Live VPS:
- synced and verified:
  - `CHIMERA_RESEARCH_BUNDLE_TEMPLATE.md`
  - `agents/macro-bias/AGENTS.md`
  - `agents/macro-bias/TOOLS.md`
  - `research/platforms/2026-05-05-macro-and-cross-asset-source-matrix.md`
  - `research/platforms/2026-05-05-btc-part6-deezoh-example.md`
  - `research/platforms/2026-05-05-part6-macro-deezoh-simulation-and-improvement.md`

## Current truth

- `Part 6` is now recommendation-based, not permission-based
- strongest current sources for this section are:
  - `ECONOMIC_CALENDAR.json` for event timing
  - `MACRO_BIAS.json` for macro backdrop wording
  - `MARKET_CONTEXT.json` for `BTC.D`, `USDT.D`, and `TOTAL3 ex BTC/ETH`
- helper-only or partial sources today are:
  - `CROSS_ASSET.json`
  - yields snapshots
- there is still no strong current direct file-backed owner for:
  - `SPX`
  - `DXY`
  - `gold`
  - `oil`

- Deezoh can now use Part 6 honestly as:
  - a recommendation layer
  - a caution or confirmation overlay
  - a way to understand when crypto-internal context is strong even if full macro coverage is not

## Remaining gaps

- `Part 6` still needs a stronger direct current-state lane for:
  - `SPX`
  - `DXY`
  - `gold`
  - `oil`
- `CROSS_ASSET.json` is still helper-grade, not a full current-state owner
- yields are still only partial, not a full macro rates surface
- `EARNINGS_CALENDAR.json` exists but is stale, so it should not be treated as live Part 6 truth

## Next best follow-up

1. Add a durable direct market snapshot lane for:
   - `SPX`
   - `DXY`
   - `gold`
   - `oil`
2. Strengthen the yields lane from partial context to a fuller regime read
3. Keep Part 6 focused on recommendation weight and context, not on trade permission wording
