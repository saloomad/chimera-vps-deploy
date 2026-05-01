---
name: vibe-coding-monitor
description: "Monitoring companion for vibe-coding-operator. Use when coding sessions, handoffs, or agent interactions need review for repeated friction, weak proof, unclear owners, or PM gaps. Triggers: vibe coding monitor, monitor my sessions, coding friction, repeated issue, log mining."
---

# Vibe Coding Monitor

> **READ THIS FIRST** after or during normal coding/project sessions when the goal is to learn from friction.
> **Companion skill**: `vibe-coding-operator`.

## Mission

Find repeated issues in how agents work with Sal and turn them into practical improvements.

This is not a blame tool. It is a monitor for patterns that make work harder than it needs to be.

It should inspect both sides of the collaboration:

- how the agent responded, routed, and proved things
- how Sal's request could be made easier for future agents to execute well

It is not only a postmortem tool.
It may intervene during a live session when the interaction itself is drifting toward confusion, weak proof, or learning from bad input.

## What To Watch

Look for:

- unclear next action
- no owner named
- no done criteria
- missing test or weak proof
- stale source-of-truth
- agent made Sal open files to understand the result
- too much jargon
- jargon used without definition
- commit, branch, workflow, detector, or PM terms used without translation
- proof dumped as filenames or commit ids without explanation
- no brief context at the start of the answer
- no end summary or next step
- too many options when a recommendation was needed
- hidden assumptions
- repeated handoff drift
- duplicate task capture
- scope creep without a split recommendation
- implementation without closeout
- reports with no consumer
- risky changes without review
- weak prompt upgrade
- missed orchestration trigger
- missing objective contract
- wrong skill activated
- important skill not activated
- poor recommendation quality
- no interaction learning captured
- user claim repeated as truth without verification
- agent learned from a bad market read or stale claim
- pushback that should have happened but did not
- no-trade case collapsed too early

## Log Sources

Use available sources, starting with the cheapest reliable ones:

- current conversation summary
- `harnesses/codex/chimera/WORK_LOG.md`
- `harnesses/codex/chimera/CONTINUATION.md`
- `harnesses/codex/chimera/KANBAN.md`
- `trace/ACTION_LOG.md`
- `projects/PROJECT_REMINDERS.md`
- `tasks/TASK_REGISTRY.md`
- newest `chimera-vps-deploy/handoffs/CHECKPOINT_*.md`
- relevant paper-watch, agent, test, and failure reports
- live `/root/openclawtrading` logs only after VPS truth is verified

Use this on both surfaces when relevant:

- Codex and workspace interactions on Windows
- Deezoh and operator interactions on the VPS after live truth is verified

Prefer this audit order:

1. current conversation and immediate closeout
2. current harness continuity files
3. `trace/ACTION_LOG.md`
4. newest handoff
5. task/project front door
6. live OpenClaw logs and reports when the issue depends on runtime truth

## Classification

Every optimization item should use one primary type:

- `prompt_issue`
- `workflow_issue`
- `data_freshness_issue`
- `missing_test`
- `unclear_owner`
- `bad_user_explanation`
- `stale_source_of_truth`
- `project_management_gap`
- `handoff_gap`
- `monitor_without_consumer`
- `scope_split_needed`
- `skill_activation_gap`
- `orchestration_gap`
- `recommendation_quality_issue`
- `interaction_learning_gap`

## Output Contract

Produce an optimization queue, not direct rewrites:

```json
{
  "captured_at": "UTC ISO timestamp",
  "source_files": ["paths or reports checked"],
  "issue": "Plain-English issue",
  "type": "workflow_issue",
  "recurrence": "one_off | repeated | unknown",
  "impact": "Why this hurts Sal or the project",
  "recommended_change": "Smallest useful improvement",
  "owner": "Codex | Claude Code | OpenCowork | OpenClaw | OpenCode | Architect | Sal",
  "risk": "safe_now | needs_review | needs_sal_approval",
  "proof_test": "How to know the fix worked",
  "status": "queued"
}
```

If a live interaction is drifting right now, also produce:

- `live_intervention_needed`: `yes | no`
- `pushback_now`: one plain-English sentence the agent should say immediately
- `safe_to_learn_from_user_input`: `yes | no | only_preference_layer`

Also produce a short session scorecard when the session was meaningful:

- `activation_quality`: `strong | partial | weak`
- `orchestration_quality`: `strong | partial | weak`
- `explanation_quality`: `strong | partial | weak`
- `proof_quality`: `strong | partial | weak`
- `recommendation_quality`: `strong | partial | weak`
- `learning_capture_quality`: `strong | partial | weak`
- `skills_used`
- `skills_missing`
- `should_update_instruction_layer`: `yes | no`

## Routing Rules

- Codex owns local code, tests, skill edits, validation, and concise closeout.
- Claude Code owns planning-heavy review, architecture synthesis, and project-shape critique.
- OpenCowork/OpenClaw owns live runtime checks and fixes under `/root/openclawtrading`.
- OpenCode owns manual prompt-wrapper runs; it has no native auto-discovery.
- Sal owns business/trading risk approvals and broad behavior-policy decisions.

## Live Intervention Rule

If the monitor sees that Sal is about to be taught the wrong thing, or the system is about to learn from the wrong thing, it should not wait for a later report.

Intervene now when:

- the agent is agreeing too quickly
- the no-trade case disappeared without evidence
- a stale claim is being reused as truth
- a repeated user frustration is being explained away instead of fixed
- a skill that should have activated clearly did not
- the answer is technically correct but not understandable without opening files

The intervention should be short and actionable:

- what is going wrong
- what to correct now
- what to capture for later improvement

## Attachment To Vibe Coding Operator

When `vibe-coding-operator` is active and a session reveals repeated friction, activate this monitor before closeout.

Use it especially when Sal says:

- "why does this keep happening"
- "make agents better at working with me"
- "I am inexperienced here"
- "what should have been caught"
- "improve the workflow"
- "read the logs and find optimizations"

Use it by default on:

- repeated workflow complaints
- missed orchestration or missed prompt engineering
- sessions where the answer felt technically correct but operationally unsatisfying
- cross-platform behavior drift
- discoverability testing for a skill or workflow

## Interaction Improvement Questions

Ask these before closeout when the session was meaningful:

- did the agent understand Sal's real goal
- did the answer stay plain-English enough
- did the agent recommend a best move instead of dumping choices
- did the right skills activate
- which skills were used
- which skills should have activated but did not
- did the orchestration loop actually happen
- was the objective contract clear
- what should Sal say next time to get a better result faster
- what should the agent or skill layer change so Sal does not need to say it next time

Also ask:

- did the reply remind Sal what we were working on
- were proof artifacts explained in plain English
- was every important term translated instead of assumed
- could Sal understand the result without opening files

## Discoverability And Iteration

Use this monitor to improve discoverability too.

Check:

- could a future agent tell when to activate the skill
- did AGENTS or platform bootstrap point clearly enough to it
- is the trigger language too narrow
- does a small scenario suite exist for the main use cases
- did a platform-specific mirror drift from the shared rule

## Frustration Learning Rule

When Sal is frustrated about explanation quality, treat that as a candidate durable lesson.

If the complaint is valid and reusable:

- capture it as `interaction_learning_gap`
- say what the agent did wrong in plain English
- propose the smallest instruction or skill change that would prevent it
- prefer updating `sal-communication-contract`, `vibe-coding-operator`, or platform `AGENTS.md` over writing a dead-end report

## Council Review Mode

Use a lightweight council when improving the suite itself:

- `coach`: did the live answer push back enough
- `monitor`: did the monitor catch the interaction failure
- `challenger`: what bad lesson could the system wrongly learn here
- `reviewer`: should this become durable guidance, stay queued, or be rejected

Do not promote a controversial lesson without this review shape.

## Guardrails

- Do not shame Sal for inexperience.
- Do not turn one awkward session into a universal rule.
- Do not write durable behavior changes without review.
- Do not create reports nobody reads.
- Prefer one concrete improvement with proof over ten vague recommendations.
- Do not confuse "the skill exists" with "the skill was actually activated and followed."

---
*vibe-coding-monitor v1.1 | 2026-05-01 | Shared Chimera skill*
