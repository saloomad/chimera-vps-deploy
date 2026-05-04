---
name: automation-design-best-practices
description: Use when creating or updating Codex automations, reminders, recurring audits, heartbeats, cron jobs, or scheduled follow-up work. Helps choose heartbeat vs cron vs platform scheduler, anchor prompts to the real objective, resume from prior results, prevent drift, and keep recurring jobs from becoming dead ends. Triggers: automation, cron, heartbeat, recurring job, scheduled task, reminder, scheduler, follow-up loop.
metadata:
  short-description: Design safe, objective-anchored automations
---

# Automation Design Best Practices

Use this skill when the task is to create, update, clean up, or review a Codex automation.

## Default Choice

- Prefer a cron automation in a new chat for system work, cross-project sweeps, recurring audits, reminders, backlog review, and anything that should stand on its own.
- Prefer a thread heartbeat only when the work is tightly tied to one active conversation or needs sub-hour follow-up in the same thread.
- For system-level work, default to a new chat unless the user explicitly wants same-thread continuity.
- Do not create a system automation in the user's current chat unless the user explicitly asked for a same-thread heartbeat.

## Default Model Ceiling

- Automations should default to `gpt-5.4` with reasoning `medium`.
- Use `gpt-5.4` with reasoning `high` only for judgment-heavy recurring review or audit work.
- Prefer `gpt-5.4-mini` with reasoning `low` for cheap mechanical sweeps when that is enough.
- Do not route automations to `gpt-5.5`, `xhigh`, or open-ended expensive research loops.

## Naming Rule

The automation title must say exactly what it does.

- Good: `Codex And OpenClaw Critical Work Executor`
- Good: `Unfinished Tasks And Approval Reminder`
- Bad: `Project Helper`
- Bad: `Automation Watcher`

Use this pattern when possible:

`<scope> + <action> + <object>`

## Core Prompt Rule

Every automation prompt must make these things explicit:

1. the `ultimate objective`
2. the `current run mission`
3. what evidence to inspect first
4. how to continue from previous results
5. what it may do automatically
6. what it must not do
7. how to classify `complete`, `iterate`, or `blocked`
8. who reads or acts on the result

If there is no real receiver, redesign the automation.

## Required Prompt Shape

Use this shape for recurring prompts whenever possible:

1. `Objective`
   - name the real end state, not just the next small step
2. `Run budget`
   - say what this pass is allowed to inspect, test, or fix
3. `Evidence first`
   - list the files, reports, logs, or status surfaces that must be checked before guessing
4. `Resume rule`
   - continue from the last unresolved issue, proof gap, or blocker from the prior run before inventing new work
5. `Drift guard`
   - allow new tasks only when they clearly close a gap in the same objective
6. `Host unavailable rule`
   - missing fresh local output can mean the machine was asleep, off, or unreachable; do not convert that into a system-wide failure claim without independent proof
7. `Do not do`
   - no risky edits, no fake completion, no pretending logs are truth
8. `Output contract`
   - say what happened, what changed, what is still blocked, and who acts next

## Objective Anchor Rule

The prompt must preserve the difference between:

- `ultimate objective`
- `current slice`
- `next safe action`

If a recurring run completes one slice but the broader objective is still open:

- the outcome is `iterate`
- the prompt should explicitly move to the next objective-tied slice
- the automation must not quietly mark the overall mission complete

## Resume-From-Previous Rule

Every meaningful recurring automation should start from prior state, not from a blank slate.

Prefer this resume order:

1. the last automation output or status file
2. the active handoff or observation ledger
3. the current task or PM surface
4. fresh live or local proof

If prior state is missing:

- say that clearly
- rebuild from file-backed evidence
- do not pretend memory is enough

## Drift Guard

Recurring automations are allowed to discover the next best task only when it is still attached to the same objective.

Safe examples:

- unresolved proof gap
- repeated blocker for the same workflow
- next missing test for the same system
- stale report that blocks the same decision

Unsafe examples:

- jumping into a different subsystem because it also looks interesting
- treating a side observation as the new main mission
- widening a bounded audit into an open-ended research project

## Host Unavailable Rule

If a local Codex automation sees no new local result:

- first consider whether the PC was off, asleep, disconnected, or the automation did not get CPU time
- separate `host unavailable` from `system broken`
- use independent proof surfaces before calling the monitored system unhealthy

Examples:

- a stale local report does not prove OpenClaw failed if the local machine was off
- an SSH timeout does not prove the agent run failed if fresh artifacts landed on disk
- an absent chat reply does not prove the whole automation chain broke

## Human Output Rule

Do not expect Sal to open files just to understand what happened.

- The automation message must include the key contents in plain English first.
- Put the most important findings in the message:
  - current state
  - what changed
  - top blocker
  - what actually ran
  - what did not actually run
  - who owns the next action
- Use file links only as drill-down for detail or proof.
- If the automation writes a markdown report, the chat message should summarize its most important sections instead of saying only that the file was updated.

## Split Responsibilities

Do not overload one automation with unrelated jobs.

- Use one automation for safe execution.
- Use another automation for reminders, approvals, and blocked decisions.
- Use another automation for health or drift audits when execution would obscure the result.

## Cross-Project Rule

For work that covers both the local Codex workspace and OpenClaw:

- inspect local continuity, task, and action surfaces first
- inspect OpenClaw live state second when it matters
- use stable artifacts and named paths
- prefer evidence from files, logs, and report contracts over memory

## Safe Action Model

Executor automations may:

- continue safe, already-scoped work
- update continuity and task surfaces after real progress
- produce a brief that says what changed, why it matters, what remains blocked, and who acts next
- stop their own heartbeat when the completion contract is truly met

Executor automations must not:

- silently take risky or destructive actions
- invent approval that was never given
- claim completion without evidence
- confuse manual operator cleanup with proven self-stop behavior

Reminder automations should:

- list unfinished tasks and projects
- list pending approvals and blocked recommendations
- say why each item matters
- name the next owner and next safe action

Reminder automations should not:

- mutate risky systems
- bury approvals inside long narratives

## OpenClaw Rule

When an automation touches OpenClaw, the result should end with a real receiving path such as:

- a named agent
- a named human owner
- a task
- an inbox or pending-questions file
- a concise operator brief with a clear next reader

Avoid dead-end monitoring.

If the automation finds a structural OpenClaw problem:

- route it to a real OpenClaw owner such as `architect` when the issue is orchestration, contract, routing, or system-shape related
- route domain-specific problems to the real lane owner when that is clearer
- update project-management surfaces so the issue is not stranded in one brief

If the automation also runs from local Codex:

- ensure a local follow-through path exists too
- prefer an executor automation, tracked task, or action-log entry that will pick up safe fixes automatically

## Action Ownership Rule

Every monitoring automation must say who acts on the result.

- If the issue is safe and bounded, the automation should fix it directly.
- If the issue is not safely fixable in-cycle, the automation should route it to the correct owner with evidence.
- If the issue is recurring or structural, the automation should also update task, kanban, or continuity surfaces.
- Never leave a monitoring result as a dead-end observation with no next owner.

## Heartbeat Stop Rule

For heartbeat prompts, make the stop rule explicit:

- close the heartbeat when the objective is actually complete
- require tests or proof when needed
- stop when the work is truly blocked
- stop after `3` no-progress wakes instead of looping forever
- keep the cadence matched to the expected pass length instead of habit

## Cadence Defaults

Minute-based cadence is appropriate for active bounded work:

- urgent complex active work:
  - `3m`
- normal active multi-step work:
  - `5m`
- lighter recurring active follow-up:
  - `15m`

Hourly cadence is appropriate for:

- unfinished work sweeps
- approval reminders
- health and blocker scans
- cross-project next-action audits

Use slower cadences when the work is expensive and does not change often.

## Quick Review Checklist

Before saying an automation prompt is good enough, verify:

- the real objective is named
- the prompt resumes from prior evidence
- the prompt distinguishes `iterate` from `complete`
- the prompt has a host-unavailable rule when local execution is involved
- the output has a real owner
- the model stays at `gpt-5.4` with `medium` or `high`
