# GitHub Task Transition And Publish Loop

## Trigger

Use this workflow before a platform moves from one meaningful task to another.

## Goal

Make sure GitHub is used correctly even when the session is continuous.

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
6. Route the real files to the correct repo:
   - `chimera`
   - `chimera-vps-deploy`
   - `chimera-windows-live`
   - `chimera-linux-live`
7. Run the guard or verification script
8. Only then move to the next meaningful task

## Review Outcomes

- `complete`
  - the slice is published and no shared debt remains
- `iterate`
  - the slice moved forward but debt remains
- `blocked`
  - a real outside dependency prevents correct publish
