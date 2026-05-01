---
name: deezoh-learning-mode
description: "Safe Deezoh learning mode. Use when Sal corrects Deezoh, asks why it missed something, suggests workflow/data/agent improvements, or wants learning without blind rewrites. Triggers: Deezoh learn this, why did Deezoh miss, improve Deezoh, workflow gap, learn from Sal."
---

# Deezoh Learning Mode

> **READ THIS FIRST** when Sal teaches, corrects, challenges, or improves Deezoh.
> **Safety rule**: raw learning is evidence, not durable truth.

## Mission

Turn Sal's questions, corrections, and observations into safer system improvements.

This skill records what happened, classifies the lesson, proposes the smallest useful improvement, and routes coding or workflow changes to the right owner.

## Safe Learning Loop

Use this order every time:

1. Capture the raw moment.
2. Classify the issue.
3. Check whether it is repeated or one-off.
4. Identify affected timeframe, workflow, data source, agent, or skill.
5. Propose the smallest improvement.
6. Assign an owner.
7. Mark the risk level.
8. Define a proof test.
9. Promote only after review.

Do not let Deezoh rewrite core files from raw capture alone.

## Source Credibility Gate

Do not learn equally from every statement.

For each learning moment, classify the source content:

- `preference_signal`: how Sal wants help, tone, pacing, or workflow support
- `experience_signal`: repeated friction or confusion Sal is honestly reporting
- `market_hypothesis`: Sal's read on price, setup, direction, or timing
- `factual_claim`: something presented as true about runtime, data, logs, or results

Rules:

- `preference_signal` can be adopted quickly if low-risk.
- `experience_signal` can drive interaction and workflow improvements.
- `market_hypothesis` must not become durable trading truth without evidence.
- `factual_claim` must be checked against logs, files, or runtime before it changes instructions.

This is how the system avoids copying the wrong lesson from Sal's understandable inexperience.

## What To Record

Every record should include:

```json
{
  "captured_at": "UTC ISO timestamp",
  "source": "Sal | Deezoh | Codex | Claude Code | OpenCowork | OpenClaw | OpenCode",
  "raw_event": "What was said or observed",
  "what_happened": "Plain-English summary",
  "why_it_matters": "Impact on trading, coding, workflow, or trust",
  "pattern_status": "one_off | repeated | unknown",
  "source_reliability": "trusted_preference | useful_but_unverified | contradicted | verified",
  "evidence_status": "not_checked | supported | mixed | contradicted",
  "category": "question_pattern | workflow_gap | data_source_gap | agent_behavior_gap | timeframe_scaling | coding_gap | project_management_gap",
  "affected_surface": "file, agent, workflow, report, timeframe, or source",
  "proposed_fix": "Smallest useful improvement",
  "owner": "Deezoh | Orchestrator | Architect | Codex | Claude Code | OpenCowork | OpenClaw | OpenCode",
  "risk": "safe_now | needs_review | needs_sal_approval",
  "approval_needed": true,
  "proof_test": "How we prove the improvement worked",
  "status": "captured | queued | approved | implemented | verified | rejected"
}
```

## Improvement Buckets

Use exactly one primary bucket:

- `safe_now`: low-risk wording, question-template, or queue capture change
- `needs_review`: workflow, skill, data-source, routing, or monitoring change
- `needs_sal_approval`: trading execution behavior, risk policy, destructive cleanup, credential changes, or broad rewrites

## Promotion Rules

- Raw capture goes to `.learnings/` or Deezoh's learning log.
- Reviewed durable lessons go to `.self-improving/`, Deezoh workflow files, or a relevant skill.
- Architect/Codex is the default promotion owner unless Sal names another owner.
- A lesson is not "learned" until a reviewed durable surface changes or the queue marks it intentionally rejected.

## Owner Routing

- Deezoh: trading-question pattern, timeframe coaching, desk behavior proposal
- Orchestrator: routing gaps, stuck loops, missing owner, stale consumer path
- Architect: operating-model and durable workflow promotion
- Codex: local code, tests, skill files, validation
- Claude Code: planning-heavy redesign, review, cross-platform synthesis
- OpenCowork/OpenClaw: live runtime behavior under `/root/openclawtrading`
- OpenCode: manual prompt-template or wrapper execution

## Blind-Rebuild Guard

Before any durable change, ask:

- Is this a repeated pattern or only one frustrating moment?
- Could the fix make another workflow worse?
- Is there proof that the current workflow actually failed?
- Who consumes the new output?
- How will we know the change worked?

If those answers are missing, queue the improvement instead of editing.

## Contradiction Rule

If Sal's suggested lesson conflicts with runtime truth, logs, or repeated evidence:

- do not absorb it as durable guidance
- explain the contradiction plainly
- capture the interaction as a coaching or explanation issue if needed
- ask `vibe-coding-monitor` to review whether the real problem was agent explanation, missing proof, or workflow confusion

Learning mode should protect Sal from bad system learning, not obey every teaching moment literally.

---
*deezoh-learning-mode v1.0 | 2026-05-01 | Shared Chimera skill*
