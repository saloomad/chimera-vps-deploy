# Orchestration Issues

Use this ledger for orchestration misses that should survive beyond one chat.

Each issue should capture:

- `date`
- `issue`
- `symptom`
- `root_cause`
- `missed_trigger_or_wrong_rule`
- `impact`
- `proof`
- `owner`
- `next_fix`
- `prevention_change`
- `status`

## 2026-04-30 - Continue-Until-Done Auto-Trigger Gap

- `date`: 2026-04-30
- `issue`: orchestration did not auto-trigger strongly enough from plain continue-until-done wording
- `symptom`: the system could comply manually, but the durable trigger cues were not explicit enough
- `root_cause`: the orchestration skill described the loop and cadence, but did not list enough natural-language requests that must activate it
- `missed_trigger_or_wrong_rule`: missing `continue until done` and incomplete AGENTS parity with the skill
- `impact`: continuation behavior depended too much on interpretation and could miss the heartbeat path
- `proof`: local and shared `objective-orchestration-loop` plus local and shared `AGENTS.md` now include explicit auto-trigger cues, cadence guardrails, issue routing, and proof-chain guidance
- `owner`: `architect-codex`
- `next_fix`: build a small scenario suite that checks common orchestration phrasings against expected class and heartbeat behavior
- `prevention_change`: added explicit trigger phrases, canonical issue storage, and proof-chain guidance
- `status`: fixed in instruction layer, deeper scenario testing still open

## 2026-05-01 - Meaningful-Work Starter-Stack Gap

- `date`: 2026-05-01
- `issue`: orchestration and prompt engineering were still too easy to miss on ordinary meaningful build and workflow requests
- `symptom`: the rules existed, but the normal starter path was not mirrored strongly enough across the operator skill, platform AGENTS files, and shared skills
- `root_cause`: orchestration was described mainly as a follow-through skill instead of as part of the default meaningful-work stack
- `missed_trigger_or_wrong_rule`: missing stronger "prompt -> operator -> orchestration" default stack plus weak cross-platform discoverability
- `impact`: agents could still do useful work without creating an explicit objective contract, monitoring friction, or loading the right specialist skills early enough
- `proof`: local and shared copies now include the stronger starter stack, monitoring guidance, platform instruction updates, a workflow for scenario testing, and a research note defining ideal success and current limits
- `owner`: `architect-codex`
- `next_fix`: run the new scenario loop against real future sessions and promote dedicated `test-writer`, `safe-refactor`, and `safe-migration` skills if the pattern repeats
- `prevention_change`: added starter-stack rules, monitoring scorecard guidance, platform AGENTS updates, shared skill mirrors, and a durable operator-improvement workflow
- `status`: fixed in instruction and workflow layer, real-session iteration still open

## 2026-05-02 - Mini-Goal Mistaken For Objective Completion

- `date`: 2026-05-02
- `issue`: orchestration closed a bounded implementation slice as if it were the user's true objective
- `symptom`: a heartbeat was deleted and the run was described as complete even though the broader user request still explicitly required more building, testing, and iteration
- `root_cause`: the skill described the loop and done contract, but it did not force a strong enough distinction between the user's `ultimate objective` and the current bounded slice
- `missed_trigger_or_wrong_rule`: `complete` was allowed to drift toward `slice complete` instead of staying reserved for `ultimate objective complete`
- `impact`: the system could stop early, announce completion too strongly, and force the user to reopen the larger objective manually
- `proof`: local and shared `objective-orchestration-loop` plus Windows Codex instruction layers now explicitly track `ultimate_objective` vs `current_slice`, require `iterate` when only a slice is done, and reserve heartbeat stop for the real objective
- `owner`: `architect-codex`
- `next_fix`: run future scenario tests where one strong slice lands inside a broader build-and-iterate request, and verify the system keeps the larger objective open
- `prevention_change`: added an objective hierarchy rule, updated the state contract and review semantics, and tightened heartbeat stop language around the real objective
- `status`: fixed in instruction layer, real-session validation next

## 2026-05-04 - First-Blocker Stop Instead Of Recovery Branch Orchestration

- `date`: 2026-05-04
- `issue`: orchestration stopped at the first runtime blocker instead of exhausting safe recovery branches
- `symptom`: the run surfaced `bgc missing` and stale-path failures as if they were end-state blockers instead of continuing through host checks, install, fallback, and path repair
- `root_cause`: the orchestration workflow did not force a strong enough recovery tree for dependency, import, or wrong-call-shape failures
- `missed_trigger_or_wrong_rule`: missing explicit `if dependency missing -> verify host-specificity -> check sibling runtime -> install if safe -> patch fallback -> retest` behavior
- `impact`: the user had to manually push the run to continue doing obvious repair work that should have happened automatically under orchestration
- `proof`: the same session then repaired `scripts/bitget_technical_analysis.py` with dynamic skill-path resolution and direct Bitget REST fallback, installed `bgc` on Windows, proved VPS `bgc` already existed, re-ran the script successfully on Windows and on `/root/.openclaw/workspace`, and corrected the `tvremix` structure-call misunderstanding by switching from `timeframe` to the documented `interval` parameter
- `owner`: `architect-codex`
- `next_fix`: add blocker-recovery branches to the orchestration workflow and mirror the lesson into the source-truth docs that relied on the bad stop
- `prevention_change`: orchestration now requires dependency-path-doc-check recovery passes before a run can honestly call a blocker exhausted
- `status`: fixed in workflow and truth surfaces, needs future-session regression proof

## 2026-05-04 - Heartbeat Stopped While Broader Objective Was Still Open

- `date`: 2026-05-04
- `issue`: a thread heartbeat was stopped after one strong slice landed even though the broader GitHub coordination objective still had open implementation work
- `symptom`: the run correctly finished the architecture and first proof slice, but incorrectly deleted the continuation heartbeat while Linux auto-pull and weaker-platform hardening were still open
- `root_cause`: I treated "remaining work is now a separate blocker/follow-up" as if that meant the guarded objective was resolved, instead of checking whether the user's stated broader objective had actually reached `complete` or `blocked`
- `missed_trigger_or_wrong_rule`: the real rule is "do not stop the heartbeat until the broader objective is complete or blocked," not "stop it when one phase becomes well-understood"
- `impact`: the user had to reopen the same objective manually, and it weakened trust in the orchestration guard
- `proof`: the heartbeat was recreated, the Linux GitHub auth/pull path was finished on the VPS, the Claude Code task-switch hook was hardened to deny stale transitions, the OpenCode wrapper was strengthened, and the broader coordination objective continued instead of being left in a false-done state
- `owner`: `architect-codex`
- `next_fix`: keep a stronger objective-vs-slice check in closeout review and add a durable note to the next checkpoint whenever a heartbeat is intentionally stopped while related work remains
- `prevention_change`: future closeout on this objective must explicitly state whether the remaining work is still part of the same broader objective before deleting the heartbeat
- `status`: fixed in this run, future-session regression proof still needed

## 2026-05-05 - Source Audit Stopped At Labels Instead Of Repair

- `date`: 2026-05-05
- `issue`: a source audit reported sections as `usable`, `partial`, or `not ready` before exhausting the obvious script and path repairs
- `symptom`: Part 4, Part 5, and Part 6 were described with weak labels even though live reruns, encoding fixes, path fixes, and fallback repairs could still materially improve them
- `root_cause`: the orchestration path treated evaluation as the end of the slice instead of as the start of the repair loop for broken or degraded sources
- `missed_trigger_or_wrong_rule`: missing explicit `rerun -> inspect artifact path/freshness -> patch -> rerun -> only then keep partial/blocked` behavior inside the data-source workflow
- `impact`: the user had to push the run to continue from vague grading into real fixes, and the early evaluation language understated what was still recoverable
- `proof`: the same run then repaired `scripts/bitget_unified_fetcher.py`, `scripts/market-maker/run_liquidation_scans.py`, `scripts/market-maker/run_maxpain_scan.py`, `trading_system/scripts/coinglass_maxpain_scraper.py`, `trading_system/scripts/liquidation_heatmap.py`, and `scripts/macro_bias_builder/macro_bias_builder.py`; after reruns, Bitget current derivatives fields worked, max-pain exact browser scrape worked, liquidation became screenshot-backed instead of blind proxy-only, and the macro lane read fresh news/calendar/local derivatives again
- `owner`: `architect-codex`
- `next_fix`: keep the new repair ladder in the data-source workflow and validate it on the next source-audit-heavy session
- `prevention_change`: added the explicit recovery branch to `workflows/codex/data-source-build-integration-and-mirror-loop.md`
- `status`: fixed in workflow, needs future-session regression proof

## 2026-05-05 - Strong-Lane Drift Reframed As Default Session Start

- `date`: 2026-05-05
- `issue`: Codex sessions kept behaving as if `gpt-5.5` with `high` were the normal starting lane even though the verified machine default was already `gpt-5.4` with `medium`
- `symptom`: users kept seeing fresh sessions on a stronger lane and had to ask why everything seemed to start there
- `root_cause`: the top-level Codex instruction and routing docs described planning and judgment-heavy review on `gpt-5.5` clearly, but they did not state strongly enough that those are escalation lanes rather than the default front door for new sessions
- `missed_trigger_or_wrong_rule`: missing explicit `all new Windows Codex sessions start on configured default unless user asks stronger or first pass proves escalation is needed`
- `impact`: stronger lanes looked like the platform default, which increased cost and made model-routing discipline feel fake or inconsistent
- `proof`: `C:\Users\becke\.codex\config.toml` already showed `model = "gpt-5.4"` and `model_reasoning_effort = "medium"`; this run then updated `C:\Users\becke\.codex\AGENTS.md`, `C:\Users\becke\.codex\CHIMERA_BOOTSTRAP.md`, `C:\Users\becke\.codex\skills\codex-runtime-router\SKILL.md`, `C:\Users\becke\.codex\skills\objective-orchestration-loop\references\PLATFORM_PHASE_MATRIX.md`, and `C:\Users\becke\.codex\skills\model-registry\SKILL.md` plus the mirrored shared skill copies so future sessions treat `gpt-5.4 / medium` as the startup rule and `gpt-5.5 / high` as deliberate escalation
- `owner`: `architect-codex`
- `next_fix`: validate on the next fresh Codex session that the startup header and routing explanation begin from `gpt-5.4 / medium` unless a stronger lane was explicitly chosen
- `prevention_change`: added a durable new-session-start rule to the top-level Codex instructions, bootstrap, router, platform phase matrix, and model registry
- `status`: fixed in instruction and mirror layer, needs fresh-session proof

## 2026-05-05 - Orchestration Declared Without A Live Continuation Owner

- `date`: 2026-05-05
- `issue`: orchestration was declared in the reply, but the current-thread heartbeat automation was never actually created or verified for the active multi-pass objective
- `symptom`: the reply said orchestration was needed and described the loop, but there was no live automation attached to the thread to continue until the objective was complete or blocked
- `root_cause`: the orchestration skill and Codex instructions required choosing continuation ownership, but they did not force a same-pass create-or-verify step before the run could honestly claim orchestration was active
- `missed_trigger_or_wrong_rule`: missing explicit `if multi-pass Codex thread and same-thread heartbeat chosen -> create/update/verify it now or report blocked` enforcement
- `impact`: the user saw orchestration language without real follow-through infrastructure, which made the continuation promise feel fake and forced manual escalation
- `proof`: this run created heartbeat automation `thread-objective-completion-guard-5`, patched the local and shared `objective-orchestration-loop` skills plus `C:\\Users\\becke\\.codex\\AGENTS.md`, and then mirrored the skill change across the real skill-load surfaces
- `owner`: `architect-codex`
- `next_fix`: verify in future multi-pass sessions that the heartbeat id is reported as part of the proof chain whenever orchestration chooses same-thread continuation
- `prevention_change`: orchestration now states that it is not live until the continuation owner is created, updated, or verified in the same pass
- `status`: fixed in automation and instruction layer, needs future-session regression proof

## 2026-05-05 - Browser Data Lane Reported As Failed Before Auth, Parser, And Stale-Runtime Recovery

- `date`: 2026-05-05
- `issue`: the run reported the CoinGlass exact ETH/SOL heatmap lane as failed before exhausting the obvious browser-data recovery path
- `symptom`: the user saw `ETH failed`, `SOL failed`, and `focused bundle still partial` language even though the remaining likely fixes were still available
- `root_cause`: I accepted the first failing artifact state instead of continuing through browser auth refresh, raw OCR inspection, parser repair, and stale-runtime re-execution
- `missed_trigger_or_wrong_rule`: missing explicit `browser/data-source lane -> refresh auth/session -> inspect raw artifact -> patch parser assumptions -> rerun with python -B if behavior still looks stale -> only then call blocked` recovery branch
- `impact`: the run made avoidable failure claims, hid recoverable fixes behind status language, and forced the user to push the continuation manually
- `proof`: the same pass then refreshed the CoinGlass-authenticated browser lane, fixed the 4-digit ETH axis-value rejection bug, fixed the decimal-stripping SOL parser bug, forced the exact extractor through `python -B` to avoid stale bytecode, reran `run_liquidation_scans.py`, and ended with exact `24h` heatmap extraction working for `BTC`, `ETH`, and `SOL` plus focused Deezoh bundles upgrading all three to `exact_both`
- `owner`: `architect-codex`
- `next_fix`: keep the browser-data recovery rule in the orchestration skill and add a targeted smoke for OCR axis parsing
- `prevention_change`: added the browser-data recovery branch to the orchestration skill, added `scripts/tests/coinglass_axis_value_smoke.py`, and hardened the exact runner with auth retry plus `-B`
- `status`: fixed in code, test, and instruction layer; future-session regression proof still needed

## 2026-05-05 - Scrape Workflow Framed Around Metadata Instead Of Artifact Truth

- `date`: 2026-05-05
- `issue`: scrape-based liquidation work was described as blocked because API/response metadata looked weak even when the screenshot artifact itself was already usable
- `symptom`: the run talked about `api_response` and `unauthenticated path` as if those were the owner, which hid the fact that screenshot extraction and later exact parsing could still succeed
- `root_cause`: the workflow language did not force a strong enough distinction between a scrape artifact and side metadata
- `missed_trigger_or_wrong_rule`: missing explicit `artifact first, metadata second` enforcement for scraping, screenshot, and OCR lanes
- `impact`: the user saw avoidable failure language, had to push the run past the false blocker, and lost trust that orchestration would keep looking for solutions
- `proof`: the same objective then repaired the exact CoinGlass path by treating the screenshot as primary truth, patched parser/crop/runtime issues, proved exact BTC/ETH/SOL extraction, added a spawned screenshot-review lane, and wired agent review back into the liquidation summary contract
- `owner`: `architect-codex`
- `next_fix`: keep the scrape-artifact truth rule active in future browser-data and screenshot workflows, and regression-test that a captured artifact gets analyzed before a blocker is declared
- `prevention_change`: added the scrape-artifact truth rule to `objective-orchestration-loop`, added the matching recovery branch to `openclaw-role-orchestration-loop`, and made the market-maker screenshot-review lane a real consumer instead of a side idea
- `status`: fixed in instruction, workflow, and implementation layer; future-session regression proof still needed

## 2026-05-06 - Heartbeat Was Deleted On A Completed Slice Instead Of The Broader Open Objective

- `date`: 2026-05-06
- `issue`: the thread heartbeat was deleted after the screener-packet slice landed even though the broader Chimera bundle and Deezoh-consumption objective still had open work
- `symptom`: the chat claimed the screener slice was done and stopped the continuation guard, but open work still remained on divergence routing, Deezoh proof, Part 11, and Part 12
- `root_cause`: I treated a bounded implementation slice as if it were the whole guarded objective and failed to carry forward the remaining project work into the continuation owner
- `missed_trigger_or_wrong_rule`: the real rule is `heartbeat stays alive until the broader same-project objective is complete or blocked`, not `stop when one approved sub-plan is complete`
- `impact`: the user had to reopen the broader objective manually, and orchestration looked fake because follow-through stopped while meaningful work was still open
- `proof`: this run recreated a broader heartbeat, upgraded live divergence routing, added deterministic Deezoh screener-consumption proof, and resumed the open project instead of leaving it falsely complete
- `owner`: `architect-codex`
- `next_fix`: keep the carry-forward block and checkpoint focused on the broader objective, and verify before closeout that no same-objective work remains unowned
- `prevention_change`: the next checkpoint now records the broader still-open work explicitly and the screener/Deezoh proof artifact was added as a live continuation surface instead of relying on chat memory
- `status`: fixed in this run, future-session regression proof still needed

## 2026-05-07 - "Second Wave" Relabeling Still Allowed Same-Objective Early Stop

- `date`: 2026-05-07
- `issue`: orchestration still allowed a heartbeat to be deleted by treating meaningful remaining same-objective work as `second wave improvements`
- `symptom`: the review/debug improvement objective was declared complete even though scenario packs, a real agent-run harness, and stronger eval wiring were still part of the user's stated improvement request
- `root_cause`: the stop logic distinguished `ultimate objective` from `current slice`, but it did not explicitly forbid renaming same-objective remaining work as optional follow-up when the user had asked to keep improving
- `missed_trigger_or_wrong_rule`: missing explicit `same-objective remaining work must be zero before complete` and missing explicit rejection of `second wave` relabeling for still-required work
- `impact`: continuation could stop early, the user had to reopen the same objective manually again, and trust in the orchestration guard dropped further
- `proof`: this run patched `objective-orchestration-loop`, `openclaw-role-orchestration-loop.md`, `scripts/orchestration_policy.py`, and `scripts/tests/orchestration_policy_matrix.py` so completion and heartbeat deletion now require same-objective remaining work to be clear and explicitly reject `second wave` relabeling
- `owner`: `architect-codex`
- `next_fix`: run the updated orchestration policy matrix and validate the new heartbeat/delete behavior on future real sessions
- `prevention_change`: added the same-objective remaining-work rule, heartbeat delete checklist, stricter stop rule, and deterministic policy assertions
- `status`: fixed in instruction and policy-test layer, fresh-session regression proof next

## 2026-05-08 - Stale Narrower Heartbeat Was Deleted Instead Of Retargeted

- `date`: 2026-05-08
- `issue`: a stale narrower heartbeat was deleted even though the broader same-objective improvement backlog was still open
- `symptom`: the old stop-rule heartbeat was treated as stale cleanup and removed without first retargeting or replacing it for the still-open broader orchestration-improvement objective
- `root_cause`: the rules blocked early stop in general, but they did not explicitly require a same-pass successor continuation owner when the existing heartbeat prompt had drifted narrower than the still-open parent objective
- `missed_trigger_or_wrong_rule`: missing explicit `update or replace stale sub-objective heartbeat before delete` rule
- `impact`: continuation ownership could disappear even while the same objective still had open work, which forced the user to reassert the rule manually again
- `proof`: this run patched `objective-orchestration-loop`, `openclaw-role-orchestration-loop.md`, `scripts/orchestration_policy.py`, and `scripts/tests/orchestration_policy_matrix.py` so stale narrower heartbeats now require a same-pass successor continuation owner before retirement
- `owner`: `architect-codex`
- `next_fix`: recreate a current-thread heartbeat on the broader still-open objective and verify future real sessions update or replace stale heartbeat prompts instead of deleting them
- `prevention_change`: added a stale sub-objective heartbeat rule in the skill/workflow and deterministic successor-owner assertions in the policy tests
- `status`: fixed in instruction and policy-test layer, current-thread continuation owner restoration next

## 2026-05-08 - Successor Rule Was Described But Not Executable As A Retirement Decision

- `date`: 2026-05-08
- `issue`: the orchestration policy could describe the successor-heartbeat rule without actually deciding `keep`, `replace then retire`, or `retire` in a deterministic helper
- `symptom`: the matrix only checked that successor-related booleans existed in the policy shape; it did not test the actual retirement decision for stale narrower heartbeats, same-objective remaining work, or `second wave` relabeling
- `root_cause`: the control layer encoded the stop rules as documentation and policy flags, but it still lacked an executable retirement-decision function
- `missed_trigger_or_wrong_rule`: missing deterministic `evaluate_continuation_owner` path for heartbeat retirement and replacement
- `impact`: the rules looked stronger than the actual tested decision surface, so another stale-heartbeat cleanup could still slip through without being caught by the current matrix
- `proof`: this run added `ContinuationOwnerRequest` plus `evaluate_continuation_owner()` to `scripts/orchestration_policy.py` and expanded `scripts/tests/orchestration_policy_matrix.py` to prove four cases: stale-without-successor -> keep alive, stale-with-successor -> replace then retire, `second wave` relabeling -> keep alive, and terminal-and-clear -> retire
- `owner`: `architect-codex`
- `next_fix`: mirror the updated checkpoint and verify the next real continuation wake still keeps or replaces the heartbeat instead of deleting it
- `prevention_change`: the retirement rule is now executable, not just descriptive, and the matrix checks the actual decision outcomes
- `status`: fixed in deterministic policy and tests, future live-session regression proof still needed

## 2026-05-08 - Cross-Host Continuation Smoke Initially Failed Because Support Files Were Not Mirrored Together

- `date`: 2026-05-08
- `issue`: the new continuation-owner smoke reached the VPS before its supporting policy files, which made the first live proof look broken
- `symptom`: the first VPS run failed with `ModuleNotFoundError: No module named 'orchestration_policy'`, and the VPS matrix file was also missing
- `root_cause`: the new smoke harness was mirrored alone instead of as a small verified file set with its required support files
- `missed_trigger_or_wrong_rule`: missing explicit `mirror the runnable support set, not only the new top-level smoke file`
- `impact`: a healthy rule could be mistaken for a live regression when the real problem was incomplete sync
- `proof`: this run then mirrored `scripts/orchestration_policy.py` and `scripts/tests/orchestration_policy_matrix.py` alongside the new smoke and fixture files, after which both `python3 /root/openclawtrading/scripts/tests/orchestration_continuation_owner_smoke.py` and `python3 /root/openclawtrading/scripts/tests/orchestration_policy_matrix.py` passed
- `owner`: `architect-codex`
- `next_fix`: keep mirror sets grouped by runnable dependency surface when adding new orchestration smokes
- `prevention_change`: the orchestration proof path now has a standalone smoke plus an explicit lesson that cross-host runnable sets must include support files
- `status`: fixed in this run, future sync-discipline regression proof still needed

## 2026-05-08 - Closeout Could Still Overclaim Publish Success When Work Was Not On `main`

- `date`: 2026-05-08
- `issue`: orchestration closeout could still sound more published than reality when repo-backed work was pushed to a branch but not visible on `main`
- `symptom`: the run could honestly say `committed and pushed` while still leaving the user with the false impression that the work had satisfied the `main`-first publication rule
- `root_cause`: the proof stack already covered continuation ownership, heartbeat scope, and carry-forward honesty, but it did not yet validate GitHub publish visibility as a separate closeout contract
- `missed_trigger_or_wrong_rule`: missing explicit `repo-backed closeout must say whether the result is visible on main before it can be framed as fully published`
- `impact`: a branch-only push could be mistaken for completed publication, which weakens the user's `main`-first rule and hides the real integration debt
- `proof`: this run added `scripts/tests/orchestration_publish_visibility_smoke.py` plus `scripts/tests/fixtures/orchestration_publish_visibility_cases.json`, wired the new smoke into `scripts/tests/orchestration_proof_pack.py`, and proved it locally and on `/root/openclawtrading`; the smoke rejects `committed and pushed` when the closeout still says `not visible on main`
- `owner`: `architect-codex`
- `next_fix`: keep publish-visibility honesty in future repo-backed orchestration closeouts and use the same smoke whenever the branch strategy or GitHub workflow changes
- `prevention_change`: the default orchestration proof stack now includes publish-visibility honesty, so publication claims are tested alongside continuation and closeout behavior
- `status`: fixed in proof layer and VPS mirror, future real-session regression proof still needed

## 2026-05-08 - Decision Labels Were Tested But The Actual Keep/Replace/Retire Action Was Not

- `date`: 2026-05-08
- `issue`: the proof stack could validate the policy decision label without directly validating the action the system would take on the continuation owner
- `symptom`: the suite knew whether the policy said `keep_alive`, `replace_then_retire`, or `retire`, but it did not yet fail a run that still tried to retire early or replace without stale scope
- `root_cause`: the control-layer tests were focused on decision-state honesty, not on the proposed continuation-owner action itself
- `missed_trigger_or_wrong_rule`: missing explicit `proposed continuation-owner action must match the policy decision` smoke
- `impact`: a future regression could still hide in the gap between the decision helper and the concrete owner action taken at closeout time
- `proof`: this run added `scripts/tests/orchestration_continuation_action_smoke.py` plus `scripts/tests/fixtures/orchestration_continuation_action_cases.json`, wired it into `scripts/tests/orchestration_proof_pack.py`, and proved locally that early `retire` and scope-free `replace_then_retire` are rejected
- `owner`: `architect-codex`
- `next_fix`: mirror and prove the new action-level smoke on `/root/openclawtrading`, then keep it in the default proof stack for future continuation-rule changes
- `prevention_change`: the orchestration proof stack now validates the actual continuation-owner action in addition to the policy decision label
- `status`: fixed in proof layer and VPS mirror, future real-session regression proof still needed

## 2026-05-08 - Dynamic Improvement Mode Was Documented But Next-Slice Selection Was Not Executable

- `date`: 2026-05-08
- `issue`: the orchestration rules described dynamic-improvement mode without an executable rule for how the next same-objective slice should be chosen
- `symptom`: the system could honestly say `keep improving` and `reselect the next same-objective slice`, but it still relied on ad-hoc judgment instead of a testable selector
- `root_cause`: the control layer had decision logic for stop and continuation ownership, but no deterministic helper for dynamic next-slice reselection
- `missed_trigger_or_wrong_rule`: missing explicit `choose the highest-value safe same-objective gap, and ignore blocked, unsafe, or different-objective items` policy helper
- `impact`: dynamic-improvement continuation was still weaker than the retirement and closeout paths, which made the `keep iterating` promise less durable than it should be
- `proof`: this run added `NextSliceCandidate` plus `select_next_same_objective_slice()` to `scripts/orchestration_policy.py`, added `scripts/tests/orchestration_dynamic_slice_smoke.py` with fixture coverage, wired it into `scripts/tests/orchestration_proof_pack.py`, and proved locally that dynamic mode selects the highest-value safe same-objective gap while fixed mode does not auto-reselect
- `owner`: `architect-codex`
- `next_fix`: mirror and prove the dynamic-slice smoke on `/root/openclawtrading`, then keep it in the default orchestration proof stack
- `prevention_change`: the orchestration proof stack now validates automatic next-slice reselection for dynamic-improvement objectives instead of leaving it as guidance only
- `status`: fixed in proof layer and VPS mirror, future real-session regression proof still needed

## 2026-05-08 - Dynamic Improvement Could Still Hide The Next Slice In User-Facing Closeout

- `date`: 2026-05-08
- `issue`: dynamic-improvement mode could choose the next slice internally without forcing the carry-forward block to show it to the user
- `symptom`: a reply could honestly say `iterate` and keep the same objective open, but still fail to expose the next highest-value remaining slice in the closeout
- `root_cause`: the control layer had deterministic next-slice selection but no explicit closeout-level validation for next-slice visibility
- `missed_trigger_or_wrong_rule`: missing explicit `dynamic iterate + remaining work -> carry-forward must name the next highest-value remaining slice` smoke
- `impact`: the orchestration loop could keep running while still feeling vague or finished from the user's point of view, because the next visible move was hidden
- `proof`: this run added `scripts/tests/orchestration_dynamic_carry_forward_smoke.py` plus `scripts/tests/fixtures/orchestration_dynamic_carry_forward_cases.json`, wired it into `scripts/tests/orchestration_proof_pack.py`, and proved locally that dynamic iterate replies must expose the next slice while fixed-mode replies do not
- `owner`: `architect-codex`
- `next_fix`: mirror and prove the dynamic carry-forward smoke on `/root/openclawtrading`, then keep it in the default orchestration proof stack
- `prevention_change`: the orchestration proof stack now validates that dynamic-improvement carry-forward stays visible to the user, not only to the internal selector
- `status`: fixed in proof layer and VPS mirror, future stale-scope live proof still needed

## 2026-05-08 - "Future Live Wake Proof" Was Too Broad After Real Continuation Behavior Had Already Happened

- `date`: 2026-05-08
- `issue`: the checkpoint kept saying a generic future same-objective wake was still needed even after a real later heartbeat wake had already resumed correctly and landed another bounded same-objective proof
- `symptom`: the open gap stayed broader than reality, which made the remaining live-proof debt sound vaguer than it actually was
- `root_cause`: I was carrying forward the original live-proof note without narrowing it after the later real continuation wake provided partial live evidence
- `missed_trigger_or_wrong_rule`: missing explicit `after a real same-objective wake lands another bounded slice, narrow the remaining live-proof gap to whatever still is not covered`
- `impact`: the carry-forward state could remain accurate at a high level but still undersell the actual progress already made on live continuation behavior
- `proof`: this wake resumed from the previous unresolved gap, kept the continuation owner alive, dynamically selected the carry-forward visibility gap, landed that bounded proof, and still returned `iterate`; the checkpoint now narrows the remaining live gap to real stale-scope `replace_then_retire` behavior rather than generic future-wake behavior
- `owner`: `architect-codex`
- `next_fix`: wait for a real stale-scope continuation event and use that as the live `replace_then_retire` proof instead of treating any future wake as the missing evidence
- `prevention_change`: checkpoint and carry-forward language now distinguish `live keep_alive/dynamic reselection already proved` from `live stale-scope replacement still not proved`
- `status`: fixed in checkpoint and issue ledger, future stale-scope live proof still needed

## 2026-05-08 - Live-Proof Debt Narrowing Was Not Yet Part Of The Default Proof Stack

- `date`: 2026-05-08
- `issue`: we had already learned to narrow the remaining live-proof debt after a real continuation wake, but that rule was still only captured in notes rather than enforced by the proof stack
- `symptom`: a future edit could reintroduce vague `next wake still needed` wording even after live continuation evidence existed, and the current tests would not catch it
- `root_cause`: the checkpoint and issue ledger carried the lesson, but there was no dedicated smoke for this specific wording regression
- `missed_trigger_or_wrong_rule`: missing explicit `after live same-objective wake proof exists, generic future-wake debt wording becomes invalid` smoke
- `impact`: the orchestration state could stay mechanically correct while still understating the real progress already achieved on live continuation behavior
- `proof`: this run added `scripts/tests/orchestration_live_gap_narrowing_smoke.py` plus `scripts/tests/fixtures/orchestration_live_gap_narrowing_cases.json`, wired it into `scripts/tests/orchestration_proof_pack.py`, and proved locally that generic future-wake wording is invalid once live continuation proof exists
- `owner`: `architect-codex`
- `next_fix`: mirror and prove the live-gap narrowing smoke on `/root/openclawtrading`, then keep it in the default orchestration proof stack
- `prevention_change`: the proof stack now validates that live-proof debt narrows after a real wake instead of staying vague
- `status`: fixed in proof layer and VPS mirror, future stale-scope live proof still needed

## 2026-05-08 - Branch-Only Publication Could Still Omit The Actual Drift Evidence

- `date`: 2026-05-08
- `issue`: repo-backed closeout could admit the work was not visible on `main` without also showing the branch-drift evidence that explains how far off-main it still was
- `symptom`: the closeout could say `not visible on main`, but still leave the user without the actual ahead/behind evidence needed to judge the publication debt
- `root_cause`: the publish-visibility smoke validated the yes/no visibility state, but it did not require branch-drift evidence when the work was still branch-only
- `missed_trigger_or_wrong_rule`: missing explicit `branch-only publication must include branch drift evidence` smoke
- `impact`: the repo-backed state could be honest at a high level while still hiding the scale of off-main drift that needed repair
- `proof`: this run added `scripts/tests/orchestration_publish_drift_smoke.py` plus `scripts/tests/fixtures/orchestration_publish_drift_cases.json`, wired it into `scripts/tests/orchestration_proof_pack.py`, and proved on both Windows and `/root/openclawtrading` that `not visible on main` is invalid without `Branch drift evidence: ...`; the full proof pack now also passes on both hosts with the publish-drift layer included
- `owner`: `architect-codex`
- `next_fix`: keep the publish-drift smoke in the default proof stack and apply it whenever repo-backed orchestration changes touch branch strategy or publish wording
- `prevention_change`: the orchestration proof stack now requires branch-drift evidence whenever a repo-backed closeout still sits off-main
- `status`: fixed in proof layer and VPS mirror, future real-session regression proof still needed

## 2026-05-08 - Live Stale-Scope Replacement Still Lacked A Deterministic Receipt Contract

- `date`: 2026-05-08
- `issue`: the one remaining real live gap was a stale-scope `replace_then_retire` event, but there was still no deterministic receipt contract for how that event had to be captured when it finally happened
- `symptom`: the system could eventually claim that a stale narrower heartbeat was replaced correctly, but the durable proof could still be vague about which owner was stale, which owner replaced it, and whether the replacement really happened in the same pass
- `root_cause`: the proof stack covered the decision, the action, and a synthetic live-event flow, but it did not yet validate the receipt that should document the real stale-scope replacement event itself
- `missed_trigger_or_wrong_rule`: missing explicit `real replace_then_retire proof must leave a deterministic receipt with stale owner, successor owner, same-pass proof, broader scope, and remaining work`
- `impact`: the last meaningful live-proof gap could be reached and still be captured too loosely, which would weaken the trust value of the final stale-scope proof
- `proof`: this run added `ReplaceThenRetireReceipt` plus `validate_replace_then_retire_receipt()` to `scripts/orchestration_policy.py`, added `scripts/tests/orchestration_replace_then_retire_receipt_smoke.py` plus `scripts/tests/fixtures/orchestration_replace_then_retire_receipt_cases.json`, wired the new smoke into `scripts/tests/orchestration_proof_pack.py`, and proved on both Windows and `/root/openclawtrading` that the required receipt fields are enforced; the full proof pack now also passes on both hosts with the receipt layer included
- `owner`: `architect-codex`
- `next_fix`: use that receipt contract when the real stale-scope replacement event finally happens, and keep the receipt smoke in the default proof stack for future continuation-rule changes
- `prevention_change`: the default orchestration proof stack now includes a dedicated replace-then-retire receipt layer, so the last live-proof event cannot be captured vaguely
- `status`: fixed in proof layer and VPS mirror, future stale-scope live proof still needed

## 2026-05-08 - Replace-Then-Retire Receipt Could Pass Without The Full Live Contract Agreeing

- `date`: 2026-05-08
- `issue`: the new receipt layer validated the replacement receipt by itself, but the proof stack still did not require that receipt to agree with the broader heartbeat scope, iterate closeout, and `replace_then_retire` decision in one combined proof path
- `symptom`: the system could prove a valid replacement receipt separately while a future live-event path still drifted on heartbeat scope or decision state
- `root_cause`: the proof stack had separate smokes for heartbeat, closeout, live-event decision, and receipt, but no combined contract smoke that required all four to agree for the stale-scope replacement case
- `missed_trigger_or_wrong_rule`: missing explicit `live replace_then_retire proof requires valid heartbeat scope, iterate closeout, replace_then_retire decision, and valid receipt in one contract`
- `impact`: the final synthetic proof layer for the remaining live gap was still looser than it should be, which left room for a mismatched state to look more proved than it really was
- `proof`: this run added `scripts/tests/orchestration_replace_then_retire_live_contract_smoke.py` plus `scripts/tests/fixtures/orchestration_replace_then_retire_live_contract_cases.json`, wired it into `scripts/tests/orchestration_proof_pack.py`, and proved on both Windows and `/root/openclawtrading` that the stale-scope replacement case only passes when all four layers agree together; the full proof pack now also passes on both hosts with the live-contract layer included
- `owner`: `architect-codex`
- `next_fix`: use it as the final synthetic guard before the real stale-scope event happens, and keep it in the default proof stack for future continuation-rule changes
- `prevention_change`: the default orchestration proof stack now includes a dedicated replace-then-retire live-contract layer, so the last live-proof gap has one stricter combined state check before waiting on the real event
- `status`: fixed in proof layer and VPS mirror, future stale-scope live proof still needed

## 2026-05-08 - A Future Checkpoint Could Still Claim Live Stale-Scope Proof Without Showing The Receipt Block

- `date`: 2026-05-08
- `issue`: even with the new receipt and live-contract layers, a future checkpoint could still claim live stale-scope `replace_then_retire` proof without exposing the receipt block clearly in the handoff text itself
- `symptom`: the tests could prove the event mechanically while the checkpoint only summarized the result, which would make later human review weaker than it should be
- `root_cause`: the proof stack still lacked a dedicated checkpoint-text rule for how a live stale-scope proof claim must be written once it exists
- `missed_trigger_or_wrong_rule`: missing explicit `if checkpoint claims live replace_then_retire proof, it must show the receipt block and all-four-layers line`
- `impact`: the final live proof could be real but still be captured too tersely in the handoff, which weakens auditability and future review
- `proof`: this run added `scripts/tests/orchestration_replace_then_retire_checkpoint_smoke.py` plus `scripts/tests/fixtures/orchestration_replace_then_retire_checkpoint_cases.json`, wired it into `scripts/tests/orchestration_proof_pack.py`, and proved on both Windows and `/root/openclawtrading` that a live stale-scope proof claim is invalid unless the checkpoint includes the visible receipt block; the full proof pack now also passes on both hosts with the checkpoint layer included
- `owner`: `architect-codex`
- `next_fix`: use it when the real stale-scope event finally lands, and keep the checkpoint smoke in the default proof stack for future continuation-rule changes
- `prevention_change`: the default orchestration proof stack now includes a dedicated checkpoint-text guard for future live stale-scope proof claims
- `status`: fixed in proof layer and VPS mirror, future stale-scope live proof still needed

## 2026-05-08 - Proof-Stack Docs Layer Was Claimed Live Before The New Smoke Existed On The VPS

- `date`: 2026-05-08
- `issue`: the checkpoint already claimed the new proof-stack documentation smoke was passing on `/root/openclawtrading`, but the actual smoke file was still missing from the VPS repo path
- `symptom`: a direct recheck on the live host failed with `python3: can't open file '/root/openclawtrading/scripts/tests/orchestration_proof_stack_docs_smoke.py'`
- `root_cause`: I updated the local proof stack, docs, and checkpoint faster than the live repo mirror, so the durable notes briefly outran the real live proof surface
- `missed_trigger_or_wrong_rule`: missing explicit `do not record VPS PASS for a new proof-layer file until the file itself is present on the live host and rerun there`
- `impact`: the orchestration checkpoint could look more live-proved than it really was, which weakens the trust value of the control-layer proof stack
- `proof`: this wake rechecked the claimed VPS path directly, caught the missing file, then mirrored `scripts/tests/orchestration_proof_stack_docs_smoke.py` and reran both the docs smoke and the one-shot proof pack on `/root/openclawtrading`
- `owner`: `architect-codex`
- `next_fix`: keep direct host-path existence checks and reruns in the proof flow whenever a new smoke is added to the orchestration pack
- `prevention_change`: the issue ledger and checkpoint now record that a claimed VPS PASS for a new proof layer is only valid after live-file existence plus rerun proof
- `status`: fixed after direct VPS recheck, mirror, and rerun

## 2026-05-08 - Proof-Stack Docs Smoke Was Windows-Only And Broke On The VPS

- `date`: 2026-05-08
- `issue`: the new proof-stack docs smoke used a hard-coded Windows skill path, so the live VPS run failed even after the file was mirrored
- `symptom`: `/root/openclawtrading/scripts/tests/orchestration_proof_stack_docs_smoke.py` raised `FileNotFoundError` for `C:\\Users\\becke\\.codex\\skills\\objective-orchestration-loop\\SKILL.md`
- `root_cause`: I wrote the new smoke against the Windows source-of-truth path only and did not give it a host-aware fallback to the repo or runtime skill mirrors
- `missed_trigger_or_wrong_rule`: missing explicit `new orchestration proof layers must resolve the skill path on both Windows and VPS surfaces`
- `impact`: the proof layer looked ready locally but could not provide live cross-host proof, which weakened the control-layer claim that the proof stack was already mirrored and runtime-valid
- `proof`: this wake patched `scripts/tests/orchestration_proof_stack_docs_smoke.py` to resolve the first existing skill path from Windows Codex, `/root/openclawtrading/skills`, or `/root/.openclaw/kimi-skills`, then reran the docs smoke and the one-shot proof pack on both Windows and `/root/openclawtrading`
- `owner`: `architect-codex`
- `next_fix`: keep host-aware skill-path resolution in future orchestration proof helpers instead of assuming the Windows source tree
- `prevention_change`: cross-host skill-path resolution is now part of the docs smoke itself, so the same proof layer can validate both the local source-of-truth copy and the live VPS mirrors
- `status`: fixed in proof layer and rerun proof on both Windows and VPS

## 2026-05-08 - Proof-Stack Docs Smoke Only Checked A Curated Subset Instead Of The Full Pack

- `date`: 2026-05-08
- `issue`: the proof-stack documentation smoke only checked a few named layers, so future orchestration proof steps could be added to the real pack without being required in the skill, workflow, or checkpoint docs
- `symptom`: the docs smoke could stay green even if a later proof step landed in `orchestration_proof_pack.py` but never appeared in the documented default continuation stack
- `root_cause`: the smoke used a hand-maintained shortlist of expected file names instead of deriving the expected documentation surface from the actual pack implementation
- `missed_trigger_or_wrong_rule`: missing explicit `every orchestration_* proof step in the real pack must appear in the skill, workflow, and checkpoint docs`
- `impact`: the control-layer proof stack could drift slowly again, with the docs looking complete while the real pack had already changed underneath them
- `proof`: this wake upgraded `scripts/tests/orchestration_proof_stack_docs_smoke.py` to derive every `orchestration_*` step from `scripts/tests/orchestration_proof_pack.py`, require the `quick_validate.py` mention across the documented proof stack, and reprove locally that the full 17-step pack is documented end to end
- `owner`: `architect-codex`
- `next_fix`: mirror the stronger docs smoke to `/root/openclawtrading` and keep it in the one-shot proof pack
- `prevention_change`: the docs-sync guard now validates the full documented orchestration proof stack from the implementation itself instead of relying on a curated subset
- `status`: fixed in proof layer and rerun proof on both Windows and VPS

## 2026-05-08 - The Review Layer Could Keep Iterating Forever When Only An External Live Event Was Missing

- `date`: 2026-05-08
- `issue`: the orchestration stack was strong at preventing false `complete`, but it still had no deterministic way to say `blocked` when the only remaining same-objective gap was a real external live event or explicit approval
- `symptom`: once the synthetic proof stack was green, the loop could keep waking and inventing more narrow proof work even though the last missing evidence was outside the current pass
- `root_cause`: review honesty was enforced for `complete` vs `iterate`, but not yet for `iterate` vs `blocked when only external blockers remain`
- `missed_trigger_or_wrong_rule`: missing explicit `external-only or approval-only same-objective remaining gap with no safe bounded next slice -> blocked`
- `impact`: the control layer could avoid false completion but still overstay in synthetic iteration instead of stopping honestly on the real blocker
- `proof`: this wake added `ReviewOutcomeRequest` plus `classify_review_outcome()` to `scripts/orchestration_policy.py`, added `scripts/tests/orchestration_external_blocked_gap_smoke.py` plus fixtures, wired the smoke into `scripts/tests/orchestration_proof_pack.py`, updated the source skill, workflow, and checkpoint, and proved locally that external-only and approval-only remaining gaps classify as `blocked` while mixed cases with another safe improvement stay `iterate`
- `owner`: `architect-codex`
- `next_fix`: mirror the new blocked-gap rule and smoke to `/root/openclawtrading`, rerun the full proof pack there, and then use this rule when the orchestration backlog is reduced to a real live-event blocker
- `prevention_change`: the review layer now has an explicit blocked-on-external-gap rule, so the loop is less likely to spin forever once only real-world evidence is missing
- `status`: fixed in proof layer and rerun proof on both Windows and VPS

## 2026-05-06 - Proxy Fallback Clobbered Higher-Truth Liquidation Output

- `date`: 2026-05-06
- `issue`: a later fallback step overwrote the higher-truth exact-plus-agent liquidation summary with a lower-truth proxy summary
- `symptom`: Part 5 looked correct immediately after the native VPS Kimi review run, then `LIQUIDATION_SUMMARY.json` later showed `fresh_proxy_current_exact_heatmap_stale_reference` and dropped the exact/agent framing
- `root_cause`: `build_liquidation_summary_fallback.py` always wrote a new fallback file without first checking whether the current summary already contained fresher exact extraction or native agent review
- `missed_trigger_or_wrong_rule`: missing explicit `do not let a lower-truth fallback overwrite a higher-truth artifact in the same surface` guard
- `impact`: live proof could appear to regress after success, and the user would see a downgraded report that hid the working VPS-native review lane
- `proof`: the live writer was traced to `run_research_bundle_refresh.sh -> build_liquidation_summary_fallback.py`; this run then patched the fallback builder to preserve existing summaries that already contain exact heatmap extraction or native `vps_kimi_chart_agent_review`, reran the VPS-native review path, and proved the fallback no longer clobbers the upgraded summary
- `owner`: `architect-codex`
- `next_fix`: keep the higher-truth-preservation guard for other fallback writers that share report surfaces
- `prevention_change`: added a higher-truth-preservation check to the fallback builder and kept the native review output in the same canonical report surface instead of a side file only
- `status`: fixed in code and live VPS proof, future-session regression proof still needed
