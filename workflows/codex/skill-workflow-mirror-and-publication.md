# Skill Workflow Mirror And Publication

## Trigger

Use this workflow when:

- a local skill changed
- a local workflow changed
- a useful local-only workflow should become shared

## Inputs

- changed local skill or workflow
- shared mirror target
- cross-platform relevance

## Steps

1. Decide whether the artifact should stay local or become shared.
2. If shared, mirror it into `chimera-vps-deploy`.
3. Update any AGENTS or bootstrap surface that should mention it.
4. Record sync status in the current handoff.
5. Commit and push when appropriate.

## Expected Outputs

- mirrored shared artifact or explicit local-only decision
- updated discoverability surface
- handoff note with sync status
