---
name: learning-loop
description: Run a reviewed learning loop across Codex, OpenClaw, and shared workspace surfaces. Use when capturing lessons, repeated user corrections, recurring workflow failures, or safe improvements to skills, prompts, workflows, and runbooks.
---

# Learning Loop Skill

## Purpose

Run a safe reviewed learning loop across Codex, OpenClaw, and shared workspace surfaces.

This skill exists to:

- capture raw lessons automatically
- detect user frustration and repeated correction signals
- detect cron/job-thinking failures without confusing freshness for truth
- turn signals into reviewed `candidate_lesson` and `review_decision` artifacts
- improve skills, workflows, prompts, and runbooks safely
- keep trading/execution behavior deterministic and protected from blind self-rewrites

## Core Rule

Learning must move through these states:

1. `raw_capture`
2. `review_issue`
3. `promoted_rule`

Nothing becomes policy directly from `raw_capture`.

## Primary Surfaces

- raw intake:
  - `C:\Users\becke\claudecowork\.learnings\INBOX.md`
  - `C:\Users\becke\claudecowork\.learnings\ERRORS.md`
  - `C:\Users\becke\claudecowork\.learnings\FEATURE_REQUESTS.md`

- reviewed memory:
  - `C:\Users\becke\claudecowork\.self-improving\durable-memory.md`
  - `C:\Users\becke\claudecowork\.self-improving\review-log.md`

- typed learning artifacts:
  - `C:\Users\becke\claudecowork\projects\learning-loop\templates\CANDIDATE_LESSON.template.json`
  - `C:\Users\becke\claudecowork\projects\learning-loop\templates\REVIEW_DECISION.template.json`
  - `C:\Users\becke\claudecowork\projects\learning-loop\templates\ADVISOR_REVIEW.template.json`
  - `C:\Users\becke\claudecowork\projects\learning-loop\templates\PROMOTION_LOG.template.json`
  - `C:\Users\becke\claudecowork\projects\learning-loop\templates\DECISION_JOURNAL.template.json`

- implementation utility:
  - `C:\Users\becke\claudecowork\scripts\learning_feedback_loop.py`
  - `C:\Users\becke\claudecowork\scripts\build_learning_loop_runtime_artifacts.py`

## Learning Lanes

Every signal should be classified into one of these lanes:

- `operator-friction`
  - swearing
  - repeated “again”
  - “still broken”
  - explanation quality misses
  - repeated correction loops

- `job-thinking-failure`
  - stale output treated as truth
  - cron/job false positives
  - producer/consumer mismatch
  - wrong root path accepted as healthy
  - “useful output written” mislabeled as failure or vice versa

- `decision-quality`
  - yes-manning
  - weak pushback
  - missing no-trade case
  - evidence mismatch
  - bad invalidation logic

- `capability-growth`
  - repeated reviewed lessons that justify a new skill, workflow, rubric, or test

## Session Lifecycle

### Session start

Run memory recall (Python — use `execute_code`, NOT `terminal`, on Hermes/Windows):

```python
import os, subprocess
base = r"C:\Users\becke\claudecowork"
os.makedirs(os.path.join(base, "reports", "auto", "LEARNING_LOOP"), exist_ok=True)
result = subprocess.run(
    ["python", "scripts/learning_feedback_loop.py", "recall",
     "--output", "reports/auto/LEARNING_LOOP/RECALL.md"],
    cwd=base, capture_output=True, text=True, timeout=60
)
print(result.stdout, result.stderr)
```

Then read surfaces directly via Python `os.path` + `open()` for content inspection (bash `cd` to Windows user paths fails on Hermes).

### Session end

Write session memory:

```bash
python scripts/learning_feedback_loop.py write-session \
  --summary "..." \
  --what-worked "..." \
  --what-failed "..." \
  --next-steps "..." \
  --platform-scope shared
```

### Candidate lesson creation

User frustration:

```bash
python scripts/learning_feedback_loop.py build-candidate \
  --source-kind user_message \
  --text "why the fuck does this happen again" \
  --output reports/auto/LEARNING_LOOP/candidate-user.json
```

Cron/job health:

```bash
python scripts/learning_feedback_loop.py build-candidate \
  --source-kind cron_health \
  --cron-health reports/auto/CRON_HEALTH.json \
  --output reports/auto/LEARNING_LOOP/candidate-cron.json
```

Trading decision review:

```bash
python scripts/learning_feedback_loop.py build-candidate \
  --source-kind trading_decision \
  --decision-journal reports/auto/LEARNING_LOOP/decision-journal.json \
  --output reports/auto/LEARNING_LOOP/candidate-trade.json
```

### Review decision

```bash
python scripts/learning_feedback_loop.py review-candidate \
  --candidate reports/auto/LEARNING_LOOP/candidate-trade.json \
  --decision issue \
  --reason "Needs replay and advisor review first" \
  --promotion-target playbook \
  --output reports/auto/LEARNING_LOOP/review-trade.json
```

### Advisor review for trading-impacting lessons

```bash
python scripts/learning_feedback_loop.py advisor-review \
  --candidate reports/auto/LEARNING_LOOP/candidate-trade.json \
  --verdict mixed \
  --reason "Directionally useful, but replay proof is still required." \
  --concern "Keep no-trade as a first-class winning outcome." \
  --output reports/auto/LEARNING_LOOP/advisor-trade.json
```

### Reviewed promotion log

```bash
python scripts/learning_feedback_loop.py promotion-log \
  --candidate reports/auto/LEARNING_LOOP/candidate-trade.json \
  --review reports/auto/LEARNING_LOOP/review-trade.json \
  --advisor-review reports/auto/LEARNING_LOOP/advisor-trade.json \
  --output reports/auto/LEARNING_LOOP/promotion-trade.json
```

### Runtime bridge from existing reports

```bash
python scripts/build_learning_loop_runtime_artifacts.py \
  --reports-dir reports/auto \
  --output-dir reports/auto/LEARNING_LOOP
```

Use this when the system already has:

- `DUAL_LANE_EVIDENCE_PACK.json`
- `JUDGE_DECISION.json`
- `TRADE_DECISION_SCORECARD.json`
- `LEARNING_FEEDBACK.json`
- optional `CRON_HEALTH.json`
- optional ready `HERMES_ADVISOR_REVIEW.json`

## Promotion Rules

- agents may auto-capture
- agents may not auto-promote
- trading-sensitive lessons must pass:
  - `candidate_lesson`
  - `advisor_review`
  - `review_decision`
  - `promotion_log`
- reviewed lessons may update:
  - durable memory
  - prompts
  - workflows
  - runbooks
  - draft skills
  - replay tests

- reviewed lessons may not directly update:
  - execution rules
  - live trading policy
  - order sizing
  - exchange credentials
  - direct cron mutation

## Frustration Guardrail

- treat swearing as a signal of friction, not as truth
- store the concrete blocker, not a personality judgment
- decay one-off frustration quickly unless it repeats
- do not rewrite tone policies when the real issue was proof quality or repeated misses

## Cron Guardrail

- freshness is not enough
- verify scheduler -> process -> writer -> file set -> consumer
- separate manual proof from natural cron proof
- route cron failures to reviewed issues before changing prompts or policies

## Research Pipeline Cron Integration

The chimera-research-pipeline runs 7 cron jobs. Cron health signals flow through `research_review.py` (quality score) before routing to learning-loop for reviewed lesson capture.

Cron job IDs for the research suite:
- Platform Learning Research: `9785aa88685e`
- YouTube Learning Transcripts: `5cf6f2253511`
- Knowledge Wiki Learning Analysis: `d617ea4b6d93`
- Notion Learning Sync: `72c867977033`
- Trading AI Research: `bbf61d5bc556`
- Learning Research Quality Review: `a853587f5532`
- Hourly Learning Pulse: `a296a10bed9a`

For research cron failures: run `research_review.py` first to score and diagnose, then route to learning-loop only if the issue is a repeatable pattern requiring a skill/prompt update.

## Hermes-Style Improvement

Copy from Hermes:

1. candidate lesson
2. advisor challenge
3. judge/review owner decision
4. promotion log
5. publish contract

Do not copy from Hermes:

- contract drift
- “text exists = ready”
- self-approval by the same lane that proposed the lesson

## Windows Hermes Agent — Execution Note

**CRITICAL — cron job execution context:**
This skill is invoked by Hermes Agent running as a scheduled cron job with no user present. The execution environment differs from interactive Claude Code sessions in a key way:

- Hermes Agent uses a bash (MSYS/git-bash) subprocess spawned by the Windows host
- bash `cd` commands with MSYS-style paths (`C:/Users/...`) or POSIX-style paths (`/c/Users/...`) **fail consistently** in this environment — the bash subprocess cannot resolve Windows user paths
- bash `cd` to `$HOME` also fails because `$HOME` maps to the MSYS root, not the Windows user profile
- Python `execute_code` tool (which uses a native Windows Python process) CAN use raw Windows paths (`r"C:\Users\..."`) and `os.path` APIs

**For all path operations in this skill when running under Hermes/cron:**
- Use Python `execute_code` instead of `terminal` for path existence checks, file reads, and directory listings
- Use raw Windows strings: `r"C:\Users\becke\claudecowork"` not `C:/Users/becke/claudecowork`
- Fall back to `terminal` only after confirming the target path is reachable via Python `os.path` first

**Session recall — working command (Python):**
```python
import os, subprocess
base = r"C:\Users\becke\claudecowork"
result = subprocess.run(
    ["python", "scripts/learning_feedback_loop.py", "recall",
     "--output", "reports/auto/LEARNING_LOOP/RECALL.md"],
    cwd=base, capture_output=True, text=True
)
print(result.stdout, result.stderr)
```

**File reads — working approach:**
```python
import os
base = r"C:\Users\becke\claudecowork"
inbox = os.path.join(base, ".learnings", "INBOX.md")
with open(inbox, 'r', encoding='utf-8') as f:
    content = f.read()
```

- reference: `references/hermes-windows-path-workaround.md` — Hermes/Windows bash path failure mode and the Python workaround pattern

## Cross-Platform Strategy

- Codex / Windows:
  - strongest for capture, clustering, review, drafting

- OpenClaw / VPS:
  - strongest for runtime signals, cron proof, replay proof, evidence packs

- Hermes:
  - second-opinion learning and challenge lane only

- GitHub:
  - sync truth, not execution truth

If a platform lacks the full role stack, degrade safely:

- capture raw event only
- queue review back to Codex
- do not skip the artifact contract
