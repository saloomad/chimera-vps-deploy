---
name: chimera-bundle-section-proof-and-hardening
description: Build or repair a Chimera research-bundle section with explicit ownership, live source proof, transparency, replay/backtest proof, and Deezoh-usefulness checks.
triggers:
  - bundle section proof
  - harden this bundle section
  - make this section real
  - prove this section
  - make Deezoh use this section
---

# Chimera Bundle Section Proof And Hardening

Use this skill when a Chimera bundle section needs to become real, tested, and useful instead of staying a template or a chat-only design.

## Read First

1. `C:/Users/becke/claudecowork/workflows/codex/chimera-bundle-section-proof-and-hardening-loop.md`
2. `C:/Users/becke/claudecowork/chimera-vps-deploy/skills/CHIMERA_RESEARCH_BUNDLE_TEMPLATE.md`
3. the current section owner agent instructions
4. the latest proof note and checkpoint for the section

## What This Skill Enforces

- one clear section objective
- one clear owner
- field-by-field source ownership
- live/local proof before confidence claims
- freshness and provenance fields
- replay/backtest proof where relevant
- Deezoh question coverage
- council review before freeze

## Required Outputs

For the current section, produce:

1. a source matrix
2. a filled section artifact
3. a readable markdown artifact
4. a replay/backtest result if relevant
5. updated owner instructions
6. a durable proof note
7. a checkpoint/handoff

## Direct Versus Derived Rule

Every field must be marked as either:

- `direct`
- `derived_from_direct_artifacts`
- `inferred`
- `missing`

Do not flatten those into one fake-confidence surface.

## Agent Role Split

| Role | Responsibility |
|---|---|
| section owner | fills the section fields |
| proof owner | proves sources and runtime behavior |
| replay owner | historical section replay / backtest |
| Deezoh reviewer | asks the downstream questions |
| council reviewers | find missing logic and weak assumptions |

## Failure Recovery Rule

If a source or script fails:

1. repair it if safe
2. rerun it
3. if still blocked, route to the approved fallback
4. record the limitation

Do not stop at the first failure if a safe fallback or repair exists.

## Replay Gate Rule

If the section has scoring, ranking, or classification logic:

1. run the section replay or historical proof harness
2. record:
   - the source stack replayed
   - the numeric regression budget
   - what passed
   - what failed
   - changed or losing historical windows
3. mark the replay verdict as:
   - `pass`
   - `iterate`
   - `blocked`

If the new logic falls outside the allowed replay budget, the correct result is `iterate`, not `complete`.

## Closeout Standard

The section is only ready when:

- the owner knows which source to use
- the artifact is transparent
- Deezoh can use it
- replay/backtest evidence exists when relevant
- replay verdict is explicit when scoring logic changed
- council found no more important improvements in the current slice
