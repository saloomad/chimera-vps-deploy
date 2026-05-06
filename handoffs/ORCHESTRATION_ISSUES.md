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
