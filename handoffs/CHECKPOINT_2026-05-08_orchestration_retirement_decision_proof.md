# CHECKPOINT - 2026-05-08 Orchestration Retirement Decision Proof

## Objective

Continue the orchestration-improvement objective by tightening the stale-heartbeat protection from a documented rule into an executable decision path.

## What changed

- kept the current objective focused on the next unresolved gap after the successor-heartbeat rule:
  - the policy still had successor-related booleans, but no deterministic retirement decision helper
- updated:
  - `scripts/orchestration_policy.py`
  - `scripts/tests/orchestration_policy_matrix.py`
- added:
  - `ContinuationOwnerRequest`
  - `NextSliceCandidate`
  - `evaluate_continuation_owner()`
  - `select_next_same_objective_slice()`
  - `scripts/tests/orchestration_proof_pack.py`
  - `scripts/tests/orchestration_continuation_owner_smoke.py`
  - `scripts/tests/orchestration_continuation_action_smoke.py`
  - `scripts/tests/orchestration_replace_then_retire_receipt_smoke.py`
  - `scripts/tests/orchestration_replace_then_retire_live_contract_smoke.py`
  - `scripts/tests/orchestration_replace_then_retire_checkpoint_smoke.py`
  - `scripts/tests/fixtures/orchestration_continuation_action_cases.json`
  - `scripts/tests/fixtures/orchestration_continuation_owner_cases.json`
  - `scripts/tests/fixtures/orchestration_replace_then_retire_receipt_cases.json`
  - `scripts/tests/fixtures/orchestration_replace_then_retire_live_contract_cases.json`
  - `scripts/tests/fixtures/orchestration_replace_then_retire_checkpoint_cases.json`
  - `scripts/tests/orchestration_dynamic_slice_smoke.py`
  - `scripts/tests/fixtures/orchestration_dynamic_slice_cases.json`
  - `scripts/tests/orchestration_dynamic_carry_forward_smoke.py`
  - `scripts/tests/fixtures/orchestration_dynamic_carry_forward_cases.json`
  - `scripts/tests/orchestration_external_blocked_gap_smoke.py`
  - `scripts/tests/fixtures/orchestration_external_blocked_gap_cases.json`
  - `scripts/tests/orchestration_live_gap_narrowing_smoke.py`
  - `scripts/tests/fixtures/orchestration_live_gap_narrowing_cases.json`
  - `scripts/tests/orchestration_prompt_contract_smoke.py`
  - `scripts/tests/fixtures/orchestration_prompt_contract_cases.json`
  - `scripts/tests/orchestration_heartbeat_contract_smoke.py`
  - `scripts/tests/fixtures/orchestration_heartbeat_contract_cases.json`
  - `scripts/tests/orchestration_closeout_contract_smoke.py`
  - `scripts/tests/fixtures/orchestration_closeout_contract_cases.json`
  - `scripts/tests/orchestration_live_event_smoke.py`
  - `scripts/tests/fixtures/orchestration_live_event_cases.json`
  - `scripts/tests/orchestration_publish_visibility_smoke.py`
  - `scripts/tests/fixtures/orchestration_publish_visibility_cases.json`
  - `scripts/tests/orchestration_publish_drift_smoke.py`
  - `scripts/tests/orchestration_proof_stack_docs_smoke.py`
  - `scripts/tests/fixtures/orchestration_publish_drift_cases.json`

## New deterministic decision coverage

The policy now decides between:

- `keep_alive`
- `replace_then_retire`
- `retire`

Key tested cases:

1. stale narrower heartbeat with same-objective remaining work and no successor
   - result: `keep_alive`
2. stale narrower heartbeat with same-objective remaining work and a ready successor
   - result: `replace_then_retire`
3. same-objective remaining work relabeled as `second wave`
   - result: `keep_alive`
4. terminal objective with proof aligned and no remaining work
   - result: `retire`

## Proof

Local:

- `python scripts/tests/orchestration_proof_pack.py` -> `PASS`
- `python scripts/tests/orchestration_policy_matrix.py` -> `PASS`
- `python scripts/tests/orchestration_continuation_owner_smoke.py` -> `PASS`
- `python scripts/tests/orchestration_continuation_action_smoke.py` -> `PASS`
- `python scripts/tests/orchestration_replace_then_retire_receipt_smoke.py` -> `PASS`
- `python scripts/tests/orchestration_replace_then_retire_live_contract_smoke.py` -> `PASS`
- `python scripts/tests/orchestration_replace_then_retire_checkpoint_smoke.py` -> `PASS`
- `python scripts/tests/orchestration_dynamic_slice_smoke.py` -> `PASS`
- `python scripts/tests/orchestration_dynamic_carry_forward_smoke.py` -> `PASS`
- `python scripts/tests/orchestration_external_blocked_gap_smoke.py` -> `PASS`
- `python scripts/tests/orchestration_live_gap_narrowing_smoke.py` -> `PASS`
- `python scripts/tests/orchestration_prompt_contract_smoke.py` -> `PASS`
- `python scripts/tests/orchestration_heartbeat_contract_smoke.py` -> `PASS`
- `python scripts/tests/orchestration_closeout_contract_smoke.py` -> `PASS`
- `python scripts/tests/orchestration_live_event_smoke.py` -> `PASS`
- `python scripts/tests/orchestration_publish_visibility_smoke.py` -> `PASS`
- `python scripts/tests/orchestration_publish_drift_smoke.py` -> `PASS`
- `python scripts/tests/orchestration_proof_stack_docs_smoke.py` -> `PASS`
- `python -X utf8 C:\Users\becke\.codex\skills\.system\skill-creator\scripts\quick_validate.py C:\Users\becke\.codex\skills\objective-orchestration-loop` -> `Skill is valid!`
- one-shot proof pack step count is now `18`

VPS:

- first smoke attempt failed because the new smoke landed before `scripts/orchestration_policy.py` and `scripts/tests/orchestration_policy_matrix.py`
- a later direct recheck also caught that `scripts/tests/orchestration_proof_stack_docs_smoke.py` was still missing on `/root/openclawtrading` even though the checkpoint had already drifted ahead to a `PASS` claim
- the first rerun after mirroring that file then exposed a second real bug: the new docs smoke still used a Windows-only skill path, so it had to be patched to resolve the skill from Windows Codex, `/root/openclawtrading/skills`, or `/root/.openclaw/kimi-skills`
- after mirroring the support set:
  - `python3 /root/openclawtrading/scripts/tests/orchestration_proof_pack.py` -> `PASS`
  - `python3 /root/openclawtrading/scripts/tests/orchestration_continuation_owner_smoke.py` -> `PASS`
  - `python3 /root/openclawtrading/scripts/tests/orchestration_continuation_action_smoke.py` -> `PASS`
  - `python3 /root/openclawtrading/scripts/tests/orchestration_replace_then_retire_receipt_smoke.py` -> `PASS`
  - `python3 /root/openclawtrading/scripts/tests/orchestration_replace_then_retire_live_contract_smoke.py` -> `PASS`
  - `python3 /root/openclawtrading/scripts/tests/orchestration_replace_then_retire_checkpoint_smoke.py` -> `PASS`
  - `python3 /root/openclawtrading/scripts/tests/orchestration_dynamic_slice_smoke.py` -> `PASS`
  - `python3 /root/openclawtrading/scripts/tests/orchestration_dynamic_carry_forward_smoke.py` -> `PASS`
  - `python3 /root/openclawtrading/scripts/tests/orchestration_external_blocked_gap_smoke.py` -> `PASS`
  - `python3 /root/openclawtrading/scripts/tests/orchestration_live_gap_narrowing_smoke.py` -> `PASS`
  - `python3 /root/openclawtrading/scripts/tests/orchestration_prompt_contract_smoke.py` -> `PASS`
  - `python3 /root/openclawtrading/scripts/tests/orchestration_heartbeat_contract_smoke.py` -> `PASS`
  - `python3 /root/openclawtrading/scripts/tests/orchestration_closeout_contract_smoke.py` -> `PASS`
  - `python3 /root/openclawtrading/scripts/tests/orchestration_live_event_smoke.py` -> `PASS`
  - `python3 /root/openclawtrading/scripts/tests/orchestration_publish_visibility_smoke.py` -> `PASS`
  - `python3 /root/openclawtrading/scripts/tests/orchestration_publish_drift_smoke.py` -> `PASS`
  - `python3 /root/openclawtrading/scripts/tests/orchestration_proof_stack_docs_smoke.py` -> `PASS`
  - `python3 /root/openclawtrading/scripts/tests/orchestration_policy_matrix.py` -> `PASS`
  - one-shot proof pack step count is now `18`

The new publish-visibility honesty layer now proves one more control-path rule:

- closeout cannot frame repo-backed work as fully published when it was only pushed to a branch and is still not visible on `main`
- missing `GitHub publish decision` or `repo branch visibility` sections are treated as invalid closeout state

The new publish-drift layer now proves one more repo-backed closeout rule:

- if the work is still not visible on `main`, the closeout must also show branch-drift evidence
- a binary `not visible on main` label alone is not enough when branch-only publication debt still exists
- the full one-shot proof pack now passes on both Windows and `/root/openclawtrading` with the publish-drift layer included

The new continuation-action layer now proves one more behavior-level rule:

- same-objective remaining work cannot jump straight to `retire`
- `replace_then_retire` is only valid when the current owner is actually stale and a successor owner is ready in the same pass

The new replace-then-retire receipt layer now proves one more live-proof rule:

- when the real stale-scope replacement finally happens, the checkpoint cannot hand-wave it
- the receipt must name the stale owner, the successor owner, the broader still-open objective scope, same-pass replacement proof, and the remaining same-objective work

The new replace-then-retire live-contract layer now proves one more state-consistency rule:

- a stale-scope replacement cannot be treated as proved unless the broader heartbeat scope, iterate closeout, `replace_then_retire` decision, and replacement receipt all agree in one proof path

The new replace-then-retire checkpoint layer now proves one more documentation rule:

- if a checkpoint ever claims live stale-scope proof, it must expose the receipt block plainly instead of summarizing it away

Recommended future live-proof block:

```text
Live `replace_then_retire` proof: PASS
All four layers agree: yes
Stale owner id: <old owner id>
Successor owner id: <new owner id>
Broader objective scope: <broader still-open objective>
Same-pass replacement proof: yes
Remaining same-objective work:
- <open item 1>
- <open item 2>
```

The new dynamic-slice layer now proves one more continuation rule:

- improvement-mode objectives automatically choose the highest-value safe same-objective gap
- blocked, unsafe, or different-objective items do not steal the next slice
- fixed objectives do not auto-reselect a new slice

The new dynamic carry-forward layer now proves one more user-facing rule:

- if review outcome stays `iterate` in `dynamic_improvement` mode and work remains open, the carry-forward block must show the next highest-value remaining slice
- fixed-mode iterate replies do not need that extra next-slice line

The new external-only blocked-gap layer now proves one more stop-honesty rule:

- if the only same-objective work left is blocked on a real external event or explicit approval, and no other safe bounded same-objective improvement remains, the honest review outcome is `blocked`
- if another safe bounded same-objective improvement still exists, the correct outcome stays `iterate`

The new live-gap narrowing layer now proves one more state-honesty rule:

- once real same-objective wake evidence exists, the remaining live-proof debt must narrow to the specific missing case
- generic `future wake still needed` wording is only allowed before any real live wake evidence exists

The new proof-stack docs layer now proves one more drift-prevention rule:

- the skill, workflow, and checkpoint docs must cover every `orchestration_*` step that actually exists in the one-shot proof pack, not just a curated subset
- the documented proof stack must also keep the `quick_validate.py` step visible across those surfaces

This later real same-objective heartbeat wake also proved one live continuation behavior:

- the thread resumed from the previous unresolved gap instead of restarting
- the continuation owner stayed alive
- the next same-objective gap was reselected dynamically
- another bounded proof landed without falsely treating the objective as done

## Still open

- bounded orchestration-improvement work is now clear; the remaining stale-scope proof gap is an external live event
  - a real stale narrower heartbeat still needs to prove live `replace_then_retire` behavior, but that is now an honest external blocker rather than a reason to keep inventing synthetic iteration
- the repo is still off the user's `main`-first publication rule:
  - workspace repo: behind `10`, ahead `63` versus `origin/main`
  - `chimera-vps-deploy`: behind `4`, ahead `32` versus `origin/main`

## Next bounded step

Wait for the next real stale-scope continuation event and capture it with the receipt block as the blocked external proof, then repair the publish path back toward `main`
