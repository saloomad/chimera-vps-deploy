# CHECKPOINT - Deezoh structured heatmap contract fix

Date: 2026-05-05
Operator: Codex

## Objective

Resume the Deezoh/Hermes improvement loop from the narrowed liquidity owner and prove whether the remaining `proxy_liquidity` style downgrade was still a real upstream absence or a stale Deezoh evidence-contract mismatch.

## What changed

Updated:

- `scripts/deezoh_question_engine.py`
- `scripts/tests/deezoh_derivatives_context_smoke.py`
- `scripts/tests/deezoh_provenance_contract_smoke.py`
- `chimera-vps-deploy/research/operations/DEEZOH_HERMES_AGENT_IMPROVEMENT_OBSERVATIONS.md`

Mirrored to VPS:

- `/root/openclawtrading/scripts/deezoh_question_engine.py`
- `/root/.openclaw/workspace/scripts/deezoh_question_engine.py`
- `/root/openclawtrading/scripts/tests/deezoh_derivatives_context_smoke.py`
- `/root/.openclaw/workspace/scripts/tests/deezoh_derivatives_context_smoke.py`
- `/root/openclawtrading/scripts/tests/deezoh_provenance_contract_smoke.py`
- `/root/.openclaw/workspace/scripts/tests/deezoh_provenance_contract_smoke.py`

## What the fix did

- Deezoh now distinguishes `exact_structured_heatmap_plus_maxpain` from the older `exact_maxpain_only` / `proxy-only` story.
- Structured exact cluster fields such as `liquidation_clusters`, `strongest_cluster`, `nearest_above_cluster`, and `nearest_below_cluster` now count as partial exact liquidity proof even when CoinGlass API metadata is empty.
- The remaining owner is now explicit: directional liquidation typing and long/short skew, not a generic missing-heatmap claim.

## Proof

Local:

- `python scripts/tests/deezoh_derivatives_context_smoke.py`
- `python scripts/tests/deezoh_provenance_contract_smoke.py`
- `python -m py_compile scripts/deezoh_question_engine.py`

Live:

- `python3 -m py_compile scripts/deezoh_question_engine.py scripts/tests/deezoh_derivatives_context_smoke.py scripts/tests/deezoh_provenance_contract_smoke.py`
- `python3 scripts/tests/deezoh_derivatives_context_smoke.py`
- `python3 scripts/tests/deezoh_provenance_contract_smoke.py`
- `/root/openclawtrading/.venv-coinglass/bin/python -B /root/openclawtrading/trading_system/scripts/coinglass_heatmap_exact.py --coin BTC --timeframes 24h --reuse-existing-screenshot`
- `python3 scripts/build_deezoh_thoughts.py`

Fresh live result:

- `/root/openclawtrading/reports/auto/DEEZOH_THOUGHTS.json`
  - `status = partial_exact_liquidity`
  - `precision_state = exact_structured_heatmap_plus_maxpain`
  - `missing_exact_fields = [liquidation_directional_bias, long_short_skew]`
  - `has_exact_cluster_levels = true`
  - `has_exact_liquidation = false`

## Still open

- Hermes recurrence is still an approval-owned scheduler question; no live scheduler mutation was made.
- BTC 24h exact heatmap extraction still does not emit directional cluster typing or usable nearest-above/below sweep cues.
- The live BTC derivatives bundle still lacks `long_short_skew`.

## Next owner

- `liquidation/vision lane owner`: classify exact clusters into directional liquidation cues and emit `vulnerable_side` / `sweep_bias`
- `derivatives lane owner`: restore `long_short_skew`
- `architect-codex + Sal`: Hermes recurrence approval/owner decision
