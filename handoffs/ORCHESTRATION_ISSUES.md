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
