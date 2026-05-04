# Publish Queue

This directory is where platforms publish debt when code is not ready yet.

The queue exists so other platforms can see:

- what changed locally
- what is still incomplete or untested
- what should happen next
- which repo owns the eventual real code publish

## Required Rule

If a platform moves to another meaningful task and the current slice is not ready to push as code, it must update its `publish-queue/<platform>.yaml` file first.

That rule is not optional just because the session is still open.

## Minimum Fields

```yaml
platform: windows-codex
project: chimera
publish_required: true
current_task: github-coordination-enforcement
reason_not_published: Hook and workflow edits are still being tested.
local_only_changes:
  - workflows/codex/github-publish-and-shared-sync.md
  - chimera-vps-deploy/platforms/windows-codex/AGENTS.md
target_repo: saloomad/chimera
next_action: Run self-test and platform mirror validation, then publish ready artifacts.
```

## publish_required

- `true` means another platform must treat this as open debt
- `false` means no unfinished publish debt remains for that platform

## Ownership

Each platform owns only its own queue file.
Other platforms read it to decide what to continue or avoid duplicating.
