# CHECKPOINT_2026-05-07 Part 6 Runtime Bridge And Bundle Proof

## Objective

Finish the remaining live Part 6 repair work after the autonomous Fed policy-path owner landed:

- make the real scheduler-owned macro builder path use the improved Part 6 producer
- stop the live report from regressing back to the old 27-key schema
- fix the `action_recommendation` mismatch so macro is not always flattened to `WAIT`
- prove the repaired Part 6 fields actually reach the live research bundle and Deezoh-facing outputs

## Completed Work

- created the real scheduler entrypoint at:
  - `scripts/macro_bias_builder.py`
- made that entrypoint delegate to the improved nested producer:
  - `scripts/macro_bias_builder/macro_bias_builder.py`
- synced both files to the live VPS runtime surfaces:
  - `/root/openclawtrading/scripts/macro_bias_builder.py`
  - `/root/openclawtrading/scripts/macro_bias_builder/macro_bias_builder.py`
  - `/root/.openclaw/workspace/scripts/macro_bias_builder.py`
  - `/root/.openclaw/workspace/scripts/macro_bias_builder/macro_bias_builder.py`
- fixed the macro action bridge inside the nested producer:
  - `STAY OUT` / `NO DATA` -> `WAIT`
  - directional macro edge with passing checks -> `LONG` or `SHORT`
  - mixed or non-promotable context -> `WATCH`
- proved the live cron-owned runtime path now writes the enriched report instead of the old 27-key payload
- patched the Part 6 bundle bridge in:
  - `scripts/build_research_bundle.py`
- added the new Part 6 fields to `macro_core`:
  - `macro_tradeability_state`
  - `macro_recommendation_state`
  - `how_deezoh_should_use_macro_now`
  - `recommendation_weight`
  - `macro_recommendation_explanation`
  - `deezoh_context_now`
  - `fed_policy_context`
  - `market_implied_policy_path`
  - `explanation_support_used`
- replaced the old Part 6 `deezoh_read` wording:
  - from `veto or permission layer`
  - to recommendation/conviction-weighting wording
- rebuilt the live research bundle and re-proved the bundle contract
- refreshed the workspace registry after creating the new scheduler entrypoint

## Live Proof

### Scheduler-owned macro report

Exact live path tested:

- `cd /root/openclawtrading/scripts && python3 macro_bias_builder.py`

Current live output under:

- `/root/openclawtrading/reports/auto/MACRO_BIAS.json`

Proof:

- key count: `70`
- `action_recommendation: WATCH`
- `macro_tradeability_state: WATCH`
- `macro_recommendation_state: btc_quality_context`
- `how_deezoh_should_use_macro_now: prefer_btc_over_broad_alts`
- `recommendation_weight: medium`
- `market_implied_policy_path` present
- `fed_policy_context` present

### Bundle bridge proof

Exact live path tested:

- `cd /root/openclawtrading && python3 scripts/build_research_bundle.py`

Current live output under:

- `/root/openclawtrading/reports/auto/RESEARCH_BUNDLE_latest.json`
- `/root/openclawtrading/reports/auto/RESEARCH_BUNDLE_latest.md`

Part 6 now carries the richer macro fields in the bundle itself.

Current live Part 6 proof:

- `deezoh_read` now uses recommendation/conviction-weighting wording
- `section_summary` now says how Deezoh should use the macro layer now
- `macro_core` includes the enriched Part 6 fields instead of only the old short subset

### Contract and consumer proof

Live contract smoke:

- `python3 scripts/tests/research_bundle_contract_smoke.py`
- result: `ok = true`

Live tail-consumption proof:

- `python3 scripts/simulate_deezoh_bundle_tail_consumption.py`
- result:
  - `status = OK`
  - `selected_workflow = range_rotation`
  - `final_decision.final_posture = no_trade`

### Follow-up cross-asset lane upgrade

After the runtime bridge was fixed, Part 6 still underused the live `CROSS_ASSET.json` feed.

That follow-up landed too:

- `scripts/cross_asset_fetcher.py`
  - now populates China proxies:
    - `FXI`
    - `MCHI`
    - `KWEB`
- `scripts/macro_bias_builder/macro_bias_builder.py`
  - now maps the already-fetched outside lanes into usable Part 6 fields:
    - `ndx_lane`
    - `vix_lane`
    - `gold_lane`
    - `oil_lane`
    - `china_lane`
  - upgraded `dxy_lane` and `yields_lane` from weak placeholder wording to usable current-direction helpers
  - changed `event_timing` from fake-missing to exact when the live calendar file is present
  - changed the macro explanation so it names the actual outside-lane tape instead of still saying those lanes are missing

Current live lane proof after the follow-up:

- `spx_lane.coverage = partial`
- `ndx_lane.coverage = partial`
- `vix_lane.coverage = exact`
- `dxy_lane.coverage = exact`
- `yields_lane.coverage = exact`
- `gold_lane.coverage = exact`
- `oil_lane.coverage = exact`
- `china_lane.coverage = partial`
- `lane_coverage.event_timing = exact`

Current live explanation shape after the follow-up:

- Part 6 now names the actual outside tape in plain English, for example:
  - SPX proxy down
  - Nasdaq proxy down
  - VIX up
  - DXY up
  - US10Y up
  - gold up
  - oil up

That makes the macro section much more decision-useful for Deezoh than the old “outside lanes still missing” wording.

## Files Changed

- `scripts/macro_bias_builder.py`
- `scripts/macro_bias_builder/macro_bias_builder.py`
- `scripts/cross_asset_fetcher.py`
- `scripts/build_research_bundle.py`
- `chimera-vps-deploy/handoffs/CHECKPOINT_2026-05-07_part6_runtime_bridge_and_bundle_proof.md`

## Remaining Honest Gap

- Part 6 now has much better outside-lane coverage, but `SPX`, `NDX`, and `China` are still proxy-based rather than first-class chart-board owners
- the broader bundle objective can still be improved further outside this Part 6 slice, but the live lifecycle and bundle contract smokes are now passing again on the VPS

## Follow-up Proof After Publish And Regression Recheck

- explicit GitHub publish proof for the bounded main-repo slice:
  - local branch commit: `822b5cd`
  - successful branch-targeted push: `git push origin HEAD:add-remaining-files`
- live VPS regression recheck after the follow-up:
  - `python3 scripts/tests/current_focus_full_lifecycle_smoke.py`
    - result: `ok = true`
  - `python3 scripts/build_research_bundle.py`
    - result: `quality = strong`
  - `python3 scripts/tests/research_bundle_contract_smoke.py`
    - result: `ok = true`
