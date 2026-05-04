# GitHub Task Transition And Publish Loop

## Trigger

Use this workflow before a platform moves from one meaningful task to another.

## Goal

Make sure GitHub is used correctly even when the session is continuous.

Testing and integration are part of the workflow, not optional cleanup.

## Steps

1. Read the shared coordination truth:
   - newest handoff
   - `session-states/`
   - `publish-queue/`
2. Review the current slice:
   - done enough to publish
   - still in progress
   - blocked
3. Choose the publish state:
   - `published-ready`
   - `in-progress-not-ready`
   - `blocked-needs-follow-up`
4. Update `session-states/<platform>.yaml`
5. Update `publish-queue/<platform>.yaml` when the code is not publish-ready
6. Run `task-change-readiness-gate` and do not proceed unless the current task is honestly ready to leave
7. Route the real files to the correct repo:
   - `chimera`
   - `chimera-vps-deploy`
   - `chimera-windows-live`
   - `chimera-linux-live`
8. Integrate the right files into the right shared surface:
   - shared state and handoffs in `chimera-vps-deploy`
   - Windows live files in `chimera-windows-live`
   - Linux or OpenClaw live files in `chimera-linux-live`
   - project code in `chimera`
9. If the pass created or changed durable coordination artifacts, update:
   - `docs/GITHUB_COORDINATION_FILE_USAGE_REGISTRY_2026-05-04.md`
   - the relevant guide or architecture file
   - the verifier if proof rules changed
10. Run proof:
   - `github_coordination_guard.py validate-platform`
   - `github_coordination_guard.py startup-summary`
   - `verify_github_coordination_system.py` after coordination changes
11. If the platform has a native runtime gate, smoke-test that gate with:
   - one allowed task transition
   - one blocked task transition
12. Only then move to the next meaningful task

## Review Outcomes

- `complete`
  - the slice is published and no shared debt remains
- `iterate`
  - the slice moved forward but debt remains
- `blocked`
  - a real outside dependency prevents correct publish

## Minimum Done Contract

The workflow is only done when all of these are true:

1. the shared state is current
2. repo ownership is clear
3. the correct shared repo was updated
4. the verification step passed
5. the platform can explain what is still open without guessing
