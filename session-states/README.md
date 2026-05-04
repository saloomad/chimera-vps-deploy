# Session States

This directory is the shared cross-platform front door for "what each platform is doing now."

Do not wait for session end.
Update the platform state whenever a meaningful task or bounded slice changes.

## Required Rule

Before a platform starts a new meaningful task, it must:

1. `git fetch` the coordination repo
2. read the newest handoff in `handoffs/`
3. read every file in `session-states/`
4. read every file in `publish-queue/`
5. update its own platform file before leaving the current task behind

## File Ownership

Each platform owns only its own file:

- `windows-codex.yaml`
- `windows-claude.yaml`
- `opencowork-local.yaml`
- `kimi-vps.yaml`
- `opencode.yaml`

Other platforms may read them all, but should not overwrite another platform's file casually.

## Minimum Fields

```yaml
platform: windows-codex
project: chimera
status: active
current_task: github-coordination-enforcement
review_outcome: iterate
shared_publish_status: in-progress-not-ready
last_updated: 2026-05-04T12:00:00Z
proof: Added shared publish guard docs and hook enforcement; live code push still pending.
next_action: Run guard script self-test and update platform mirrors.
```

## Status Values

- `active`
- `blocked`
- `idle`
- `complete`

## Shared Publish Status Values

- `published-ready`
- `in-progress-not-ready`
- `blocked-needs-follow-up`
- `idle`

## Rule Of Thumb

If another platform needs to understand what you were doing without reading chat, this file was supposed to be updated already.
