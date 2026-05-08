# CHECKPOINT - 2026-05-07 Hybrid Proof-Order And Review-Freshness Hardening

## What Landed

- fixed outcome-matrix workspace collisions
- fixed nested lifecycle-matrix seeding from mutated synthetic state
- fixed isolated Part 12 degradation by rebuilding strategy-reasoning artifacts in the synthetic run
- hardened hybrid proof so an old agent-review artifact no longer counts as current hybrid proof
- added the explicit stale-helper wrong-side temptation scenario to the hybrid matrix
- fixed scenario focus selection so Deezoh can keep a cleaner active symbol over a higher raw screener score
- added the explicit `cleaner second-choice symbol wins` scenario and symbol-choice assertions
- added the inverse `favorite symbol correctly beats tempting second choice` scenario and assertions
- added a synthetic-vs-natural comparison lane so the system can classify whether a real closeout or live symbol-choice analogue exists yet
- added real-outcome judgment fields so the comparison lane can score a future natural outcome as `right`, `early`, `late`, `wrong`, or `pending`
- added an unresolved-case watchdog so live symbol-choice analogues are classified as `fresh_watch`, `aging_watch`, or `stale_watch`

## Files Changed

- `scripts/tests/current_focus_lifecycle_outcome_matrix.py`
- `scripts/tests/current_focus_full_lifecycle_smoke.py`
- `scripts/deezoh_question_engine.py`
- `scripts/run_hybrid_market_condition_scenario_matrix.py`
- `scripts/build_synthetic_natural_comparison_review.py`
- `scripts/tests/synthetic_natural_comparison_review_smoke.py`
- `C:\Users\becke\.codex\skills\chimera-hybrid-scenario-lab\SKILL.md`
- `reports/auto/HYBRID_SCENARIO_AGENT_REVIEW.json`

## Live Proof

VPS:
- `root@100.67.172.114`

Current live results:
- `CURRENT_FOCUS_FULL_LIFECYCLE_SMOKE.json`: `ok=true`
- `CURRENT_FOCUS_LIFECYCLE_OUTCOME_MATRIX.json`: `PASS`, `4/4`
- `HYBRID_SCENARIO_MATRIX_REPORT.json`: `PASS`, `13/13`
- hard gate failures: `0`
- fresh agent review enforced: `yes`
- `cleaner_second_choice_symbol_wins`: `PASS`
- selected focus stayed on `SOLUSDT` while the top raw screener rank was `BTC`
- `favorite_symbol_correctly_beats_tempting_second_choice`: `PASS`
- selected focus correctly stayed on `BTCUSDT` over tempting `SOLUSDT`
- `SYNTHETIC_NATURAL_COMPARISON_REVIEW.json`: `live_symbol_choice_case_waiting_for_outcome`
- live analogue exists now:
  - focus `SOLUSDT`
  - screener best short `ASTERUSDT`
  - selection mode `existing_focus_overrides_screener_top_pick`
  - still unresolved because final posture is `no_trade` and no natural closeout exists yet
- real outcome comparison fields now exist:
  - verdict: `pending`
  - expected synthetic symbol: `SOLUSDT`
  - natural symbol so far: `SOLUSDT`
  - reason: no real closeout exists yet
- unresolved-case watchdog fields now exist:
  - state: `active`
  - age bucket: `fresh_watch`
  - first seen / last seen timestamps are recorded for the live analogue fingerprint

## Real Remaining Work

- compare synthetic symbol-choice and closeout lessons with a natural paper-trade closeout when one exists
- keep the fresh-review gate active so hybrid proof never falls back to stale human review
- add longer-horizon follow-through checks so symbol-choice outcomes can later be judged right, early, late, or wrong

## Review Outcome

- `iterate`
