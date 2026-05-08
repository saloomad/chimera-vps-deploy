---
name: response-structure-enforcer
description: Compatibility wrapper for older references. The communication and reply-structure rules now live in `sal-communication-contract`, which should be treated as the single source of truth.
metadata:
  short-description: Redirect to sal-communication-contract
---

# Response Structure Enforcer

This skill has been merged into `sal-communication-contract`.

Do not maintain a separate communication policy here.
Do not let the two skills drift.

If this skill is triggered by an older workflow, instruction file, or habit:

1. immediately use `sal-communication-contract`
2. apply its direct-answer, teaching-style, transparency, proof-translation, and formatting rules
3. treat `sal-communication-contract` as the source of truth for reply quality

## Why This Wrapper Still Exists

Older workflows and notes may still mention `response-structure-enforcer`.

This wrapper remains only so those references do not silently break while the system is being cleaned up.

## Migration Rule

When you edit instruction files, workflows, or platform guidance, prefer pointing them directly to `sal-communication-contract`.

Do not add new independent rules here unless they are also added to `sal-communication-contract`.
