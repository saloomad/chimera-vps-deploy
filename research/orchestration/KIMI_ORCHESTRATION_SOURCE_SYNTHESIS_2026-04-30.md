# Kimi Orchestration Source Synthesis

Updated: 2026-04-30

## Purpose

This note captures what was actually useful from the Kimi orchestration research pack, what was outdated, and what should be preserved as reusable design input for the Chimera cross-platform orchestration stack.

## Sources Reviewed

- `C:\Users\becke\Downloads\orchestration_playbook.md`
- `C:\Users\becke\Downloads\deep-research-swarm-skill.md`
- `C:\Users\becke\Downloads\iterative_swarm_architecture.md`
- `C:\Users\becke\Downloads\universal_orchestration_playbook (1).md`
- Notion page `orchestration kimmi`
- Notion page `kimi agent swarm examples`
- `C:\Users\becke\Downloads\Kimi_Agent_Bitcoin TA_ Entry & Stick\plan.md`
- `C:\Users\becke\Downloads\Kimi_Agent_Bitcoin TA_ Entry & Stick\bitcoin_crypto_analysis.docx`

## What The Research Got Right

### 1. File-Based State First

The strongest transferable idea is that parallel workers do not share memory.
Durable files should carry the workflow state:

- `plan.md`
- research dimension files
- cross-verification
- insights
- writing outputs
- final report

This fits Chimera well because it also makes restarts, proofs, and human inspection easier.

### 2. Research And Writing Should Be Separate

The Kimi flow correctly keeps evidence gathering separate from writing.
That is worth preserving.

### 3. Contradictions Are Signal

The research emphasized that disagreement should be surfaced, not flattened away.
That is useful for:

- theses
- postmortems
- event reviews
- risk-heavy trade analysis

### 4. Narrow Reruns Beat Whole-Restart Loops

The best part of the seven-phase model is not "many agents."
It is the idea that weak slices should be rerun narrowly instead of restarting the whole job.

### 5. Trading Needs A Different Shape

The iterative architecture correctly distinguished:

- one-shot research/report swarms
- continuous trading pipelines

That split is now part of the Chimera standard.

## What Was Outdated Or Overclaimed

### Platform Claims

Some model, product, and platform claims in the source pack were dated.
Examples:

- older OpenAI model names and prices
- older Claude Code and Codex limitations
- generic Codex task-queue descriptions not proven in this runtime

For current model facts, use:

- `skills/model-registry/SKILL.md`
- `skills/codex-runtime-router/references/MODEL_ROUTING_SPEC.md`

### OpenClaw Details

Some OpenClaw details in the source pack were design inferences rather than verified live mechanics.
Those are still useful as patterns, but they should not be treated as live-proof documentation unless verified against the real VPS.

## What We Preserved In Chimera

- universal base loop stays `plan -> execute -> review`
- deep swarm is a separate specialized layer
- file-based state and handoffs
- explicit sub-agent roles
- cross-verification and targeted validation
- lean live trading loop stays separate from research swarm
- cheap workers first, stronger reruns only when needed

## What We Intentionally Did Not Copy Blindly

- forcing every task into a seven-phase swarm
- pretending all platforms have the same native orchestration primitives
- requiring a giant agent count for smaller useful research jobs
- treating inferred OpenClaw YAML or hook patterns as proven runtime truth without a live check

## Main Lesson

The Kimi pack was most valuable as a design pattern library, not as a literal current-product specification.
The right Chimera move was:

1. keep the file-first and contradiction-first ideas
2. separate deep research from the universal base loop
3. route by task type so live trading stays lean
