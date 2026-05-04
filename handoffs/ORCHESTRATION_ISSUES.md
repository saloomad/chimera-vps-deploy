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
