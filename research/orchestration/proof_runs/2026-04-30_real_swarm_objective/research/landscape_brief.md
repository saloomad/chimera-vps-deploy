# Landscape Brief

Date: 2026-04-30
Objective: decide how Chimera should use deep swarm in real work, how the heartbeat and automation layer should behave, how to see the orchestration visually, and how the same logic should adapt across Codex, Claude/Cowork, OpenClaw/Kimi, and Hermes.

## Current Known Truth

- The universal base loop remains `plan -> execute -> review`.
- The deep swarm is now a separate specialized layer with explicit plan/state, role, and challenge references.
- The live trading loop should stay lean and should not turn every cycle into a large swarm.
- Cheap-worker routing is useful, but it needs a verdict schema so it returns the full contract instead of only a label.
- The best remaining proof is one real internal swarm-backed objective that starts from the plan and ends with a memo.

## Open Questions For This Proof

- Which real trading or build situations deserve the swarm instead of the lean loop?
- When should heartbeats or automations continue work, and when should they stay out of the way?
- How should the same orchestration logic be adapted for Codex, Claude/Cowork, OpenClaw/Kimi, and Hermes?
- What should a human look at to understand the orchestration without reading raw files?
