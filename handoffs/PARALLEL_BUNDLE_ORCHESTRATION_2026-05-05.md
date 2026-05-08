# Parallel Bundle Orchestration Tracker

Date: 2026-05-05
Scope: parallel section-fork orchestration for the Chimera research bundle after `Part 3`
Coordinator: main Codex thread
Purpose: make the parallel work legible, recoverable, and merge-ready instead of looking like unrelated subagent noise

## What Happened

The bundle review split into parallel section forks.

That choice was valid.

The orchestration shape was weak.

The miss:

- forks were launched before a visible orchestration tracker existed
- the user saw subagent completions but not the manager state
- remaining sections were not queued visibly after the agent-thread cap hit
- the merge path was implied, not recorded

## Correct Orchestration Shape

For this kind of work, the main thread must act as:

- orchestrator
- status board
- merge gate
- failure-recovery owner

Each subagent thread should be treated as:

- one section owner
- one isolated output file
- one bounded proof artifact

## Current Parallel Fork Registry

| Part | Thread Name | Agent ID | Output File | Status | Notes |
|---|---|---|---|---|---|
| 4 | `Part 4 - Derivatives And Positioning` | `019df544-7232-7081-98ea-0f46040ea9b4` | `parallel_part4_derivatives_and_positioning.md` | complete | standalone proposal written |
| 5 | `Part 5 - Liquidation Heat Map` | `019df544-bc0f-7913-9391-5dc6d04b5989` | `parallel_part5_liquidation_heat_map.md` | complete | standalone proposal written |
| 6 | `Part 6 - Macro And Cross-Asset` | `019df545-07c6-7ac2-88ea-7d424daab2c0` | `parallel_part6_macro_and_cross_asset.md` | complete | standalone proposal written |
| 7 | `Part 7 - News And Catalysts` | `019df545-66c6-7313-a7eb-de5b4f8d0052` | `parallel_part7_news_and_catalysts.md` | complete | standalone proposal written |
| 8 | `Part 8 - Structural / Market Intel` | `019df545-a55c-7d51-9200-a1fa41d88cb7` | `parallel_part8_structural_market_intel.md` | complete | standalone proposal written |
| 9 | `Part 9 - Risk And Invalidation` | `019df545-dc63-7b82-bb92-825fffd9181c` | `parallel_part9_risk_and_invalidation.md` | complete | standalone proposal written |
| 10 | `Part 10 - Setup Candidates` | not spawned yet | pending | queued | blocked only by agent-thread cap |
| 11 | `Part 11 - Position Management And Risk` | not spawned yet | pending | queued | blocked only by agent-thread cap |
| 12 | `Part 12 - Final Decision` | not spawned yet | pending | queued | blocked only by agent-thread cap |

## Merge Rules

Do not merge a fork into the shared template until all of these are true:

- the fork contains:
  - objective
  - section owner
  - what belongs here
  - what does not belong here
  - exact fields
  - definitions
  - Deezoh completion rule
  - source order
  - proof/capability notes
  - one ideal example
- terminology does not conflict with locked earlier parts
- ownership is concrete, not vague
- source truth is honest
- no section silently steals another section's responsibility

## Failure Branches For This Parallel Pattern

1. if agent-thread cap is hit
   - record which parts were queued but not spawned
   - wait for the first completed fork
   - close finished agents
   - spawn the next queued parts

2. if two forks define overlapping ownership
   - do not merge either one blindly
   - compare responsibilities in the main thread
   - tighten the boundary before merge

3. if a fork uses invented source capability
   - require proof note or downgrade the source claim
   - do not promote it into the shared template until corrected

4. if the user wants to review sections separately
   - keep each section in its own fork file
   - only merge the approved ones

## Next Actions

1. close the six completed fork agents after harvesting their files
2. spawn `Part 10`, `Part 11`, and `Part 12`
3. review each fork in the main thread
4. merge only the approved sections into the shared template

## Durable Learning

For parallel document work, orchestration is not just "spawn several agents."

It must include:

- visible registry
- queue state
- merge gate
- failure branches
- explicit ownership of the integration thread
