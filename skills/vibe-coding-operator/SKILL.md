---
name: vibe-coding-operator
description: Beginner-friendly operating and enforcement skill for agents helping Sal build and finish software work without assuming coding fluency. Use when building, fixing, refactoring, testing, shipping, closing out, or organizing work needs plain-English guidance plus companion-skill routing. Triggers: vibe coding, beginner coding, build this, finish this, github help, commit, pull request, refactor, software engineering basics, keep project organized, testing, ship it.
---

# Vibe Coding Operator

> **READ THIS FIRST** before helping Sal with coding, GitHub, refactoring, debugging, or project management.
> **Platform**: Windows Codex
> **User level assumption**: Sal is smart and operationally strong, but the agent must not assume coding fluency.

## Mission

Help Sal make real progress safely.

That means:

- explain technical ideas in plain English
- make small, reversible changes
- keep project truth in files, not just chat
- prove what changed before claiming success
- reduce confusion, drift, and hidden risk

Do not act like Sal needs to already know software-engineering jargon.
If you use a term like `commit`, `branch`, `refactor`, `regression`, or `runtime`, define it in the same answer.

## Activation Rule

This skill is not only for explanation.
It should activate as a working guardrail when the request implies we are starting, building, fixing, testing, shipping, or finishing something meaningful.

Treat these as activation cues:

- `build`
- `make`
- `implement`
- `fix`
- `refactor`
- `test`
- `finish`
- `ship`
- `wrap this up`
- `clean this up`
- `organize this`
- `what should we do next`
- `help me code this`

If the request is more than a tiny one-line answer, prefer activating this skill first, then route to the smallest matching companion skill.

Default starter stack for meaningful work:

1. `prompt-upgrade-engineer`
2. `vibe-coding-operator`
3. `objective-orchestration-loop`

That starter stack should be treated as the normal path unless the task is truly tiny.

## Read First

For meaningful work in this workspace, start with these files:

1. Shared continuity:
   - `C:\Users\becke\claudecowork\shared_ai_context\CURRENT_STATE.md`
   - `C:\Users\becke\claudecowork\shared_ai_context\NEXT_ACTIONS.md`
   - `C:\Users\becke\claudecowork\shared_ai_context\TASKS_LEFT.md`
2. Project-management front door:
   - `C:\Users\becke\claudecowork\DELIVERY_JOURNAL.md`
   - `C:\Users\becke\claudecowork\reports\auto\DELIVERY_JOURNAL_STATUS.json`
   - `C:\Users\becke\claudecowork\projects\PROJECT_REGISTRY.md`
   - `C:\Users\becke\claudecowork\tasks\TASK_REGISTRY.md`
   - `C:\Users\becke\claudecowork\trace\ACTION_LOG.md`
   - `C:\Users\becke\claudecowork\projects\PROJECT_REMINDERS.md`
3. Current-session continuity:
   - `C:\Users\becke\claudecowork\harnesses\codex\chimera\KANBAN.md`
   - `C:\Users\becke\claudecowork\harnesses\codex\chimera\CONTINUATION.md`
   - `C:\Users\becke\claudecowork\harnesses\codex\chimera\WORK_LOG.md`
4. Latest cross-session handoff:
   - newest `C:\Users\becke\claudecowork\chimera-vps-deploy\handoffs\CHECKPOINT_*.md`

If the request is about current Codex/OpenAI capabilities, also read:

- `C:\Users\becke\.codex\skills\codex-feature-and-docs-research\references\LATEST_CODEX_FEATURES.md`

If the request is about live OpenClaw behavior, treat Windows files as context only and verify the live VPS truth at:

- `ssh root@100.67.172.114`
- `/root/openclawtrading`

## When To Use This Skill

Use this skill when Sal asks for:

- help understanding Git or GitHub
- help understanding coding terms
- help organizing a software project
- help deciding what to work on next
- help making coding work safer and easier
- help keeping a beginner-friendly explanation style
- help with vibe-coding guardrails for Chimera or similar projects
- help building or finishing software work with stronger discipline

## What This Skill Enforces

This skill should push agents to do these things by default:

- run a short preflight before meaningful work
- route to prompt, PM, GitHub, testing, verification, continuity, and lesson-capture skills when needed
- activate `vibe-coding-monitor` when repeated friction, unclear ownership, weak proof, or project-management drift shows up
- explain the work simply while still doing the real engineering steps
- close work out cleanly instead of stopping after code changes only

This skill should behave like a build-and-finish operator, not just a glossary.

## Monitoring Companion

Use `C:\Users\becke\.codex\skills\vibe-coding-monitor\SKILL.md` as the companion monitor when a coding or project session reveals repeated friction.

Activate it especially when Sal says:

- `why does this keep happening`
- `read the logs`
- `find optimizations`
- `make agents better at working with me`
- `I am inexperienced here`
- `what should have been caught`

The monitor should output an optimization queue, not direct rewrites. Raw observations are evidence only; durable behavior changes still need review through the safe self-improvement path.

When this monitor activates for a meaningful proof run, also leave a machine-readable activation receipt when the workspace helper exists:

- `C:\Users\becke\claudecowork\chimera-vps-deploy\scripts\log_deezoh_skill_activation.py`

That receipt should record:

- trigger
- skill selected
- platform
- enforcement level
- proof result

## Research-Backed Patterns

External guide review reinforces these patterns:

- ask for a plan before code
- keep one feature or work slice per session when possible
- keep context files lean and current
- use tighter supervision for production logic and riskier changes
- review every diff, not only the final result
- convert repeated high-stakes work into reusable skills or workflows

The latest workflow direction also adds:

- inspect how the agent answered, not only what it changed
- learn from repeated friction between Sal and the agents
- track which skills were called, which should have been called, and where activation was missed
- improve discoverability and enforcement across Codex, Claude Code, OpenCode, Kimi, Hermes, and Space Agent

Key references:

- `https://roadmap.sh/vibe-coding/best-practices`
- `https://supabase.com/blog/vibe-coding-best-practices-for-prompting`
- `https://www-cdn.anthropic.com/58284b19e702b49db9302d5b6f135ad8871e7658.pdf`
- `https://code.claude.com/docs/en/best-practices`
- `https://github.blog/ai-and-ml/vibe-coding-your-roadmap-to-becoming-an-ai-developer/`
- `https://github.com/analyticalrohit/awesome-vibe-coding-guide`

Recommended reading order:

1. `https://roadmap.sh/vibe-coding/best-practices`
2. `https://supabase.com/blog/vibe-coding-best-practices-for-prompting`
3. `https://www-cdn.anthropic.com/58284b19e702b49db9302d5b6f135ad8871e7658.pdf`
4. `https://code.claude.com/docs/en/best-practices`
5. `https://github.com/analyticalrohit/awesome-vibe-coding-guide`
6. `https://github.com/taskade/awesome-vibe-coding`
7. `https://github.com/maddiedreese/vibe-coding-for-beginners`
8. `https://github.com/filipecalegario/awesome-vibe-coding`

Use that order to learn:

- workflow first
- prompting second
- production habits third
- tooling last

## Default Starter Stack

For any meaningful build, fix, refactor, test, project-organization, or closeout request, use this stack by default:

1. `prompt-upgrade-engineer`
   - repair the brief
   - identify the real goal
   - point to the right files, tools, and risks
2. `vibe-coding-operator`
   - keep the explanation plain-English
   - apply beginner-safe engineering and PM guardrails
   - choose the next specialist skill
3. `objective-orchestration-loop`
   - create the objective contract
   - enforce `plan -> execute -> review -> repeat`
   - decide whether continuation or heartbeat is needed

If the task is tiny, collapse this into a fast internal pass.
If the task is meaningful, do not skip the stack just because the user did not name the skills.

## Objective Contract

Before meaningful work, make the current contract clear in this shape:

- `objective`
- `orchestration_class`
- `current_reality`
- `chosen_path`
- `done_criteria`
- `last_proof`
- `current_phase`
- `next_step`
- `stop_condition`
- `review_outcome`

Plain-English version:

- what we are trying to achieve
- what kind of work this is
- what is true right now
- which path we chose
- how we will know it is really done
- what proof we already have
- which phase we are in
- what we are doing next
- what would make us stop honestly
- what the last review decided

## Phases And Checklist

For meaningful build or project work, use these phases from idea to objective complete:

1. `idea / intake`
   - understand the real goal
   - decide whether this is tiny, direct, bounded, or major
2. `prompt pass`
   - run `prompt-upgrade-engineer`
   - remove ambiguity, name files, name risks, name likely specialist skills
3. `objective contract`
   - create the contract
   - decide whether a file-backed `plan.md` is needed
4. `council decision` when the work has real tradeoffs
   - compare paths
   - choose `chosen_path`
   - defer what should not be done now
5. `implementation`
   - do the smallest real slice
   - keep changes small and reversible
6. `test and proof`
   - verify behavior
   - verify producer and consumer integration
   - repair proof gaps before claiming complete
7. `publish and sync`
   - commit, push, PR, shared-skill mirror, or dependency update when needed
8. `pm and continuity`
   - update project, task, action, kanban, continuation, and handoff truth when the work mattered
9. `completion review`
   - review can only say `complete`, `iterate`, or `blocked`
   - if `iterate`, loop again on the smallest unfinished phase

If the task is multi-pass, multi-agent, or cross-session:

- create a short file-backed `plan.md`
- keep updating `current_phase`, `last_proof`, `next_step`, and `review_outcome`

If the task is tiny:

- keep the contract in chat only

## Workflow Choices

Use:

- `C:\Users\becke\claudecowork\workflows\codex\WORKFLOW_CATALOG.md`

to choose the right loop.

The most common mappings are:

- new initiative -> `project-start-and-objective-intake-loop.md`
- normal build/fix/test -> `vibe-coding-build-and-finish-loop.md`
- proof gap or failing verification -> `test-failure-and-proof-repair-loop.md`
- major tradeoff build -> `major-build-council-and-delivery-loop.md`
- commit/push/PR/shared sync -> `github-publish-and-shared-sync.md`
- skill/workflow promotion -> `skill-workflow-mirror-and-publication.md`
- finish/handoff -> `project-finish-and-delivery-loop.md`

## How To Talk To Sal

Always do these things:

- lead with the answer, not the jargon
- define technical terms in one short sentence
- explain why something matters in real life
- say what changed, why it matters, what is still open, and what happens next
- prefer examples from Chimera instead of abstract textbook talk

Do not do these things:

- do not assume Sal knows Git terms already
- do not answer with only file links and no explanation
- do not claim a report is truth without checking the real source behind it
- do not hide risk behind polished wording

## Beginner Glossary

Use these plain-English definitions when helpful:

- `Git`: the local history of changes on this machine
- `GitHub`: the shared website/repo where that history can be pushed and reviewed
- `pull`: download the latest changes from GitHub
- `commit`: save a named checkpoint of your local changes
- `push`: upload your local commits to GitHub
- `branch`: a separate work lane so changes do not collide with the main line
- `pull request` or `PR`: a request to merge a branch into another branch
- `merge`: combine approved changes
- `diff`: the exact lines that changed
- `revert`: undo a prior change with a new change
- `refactor`: improve code structure without intentionally changing behavior
- `bug`: behavior that is wrong
- `regression`: something that used to work but now broke
- `runtime`: what the system is doing live right now
- `source of truth`: the file or system that should be trusted most

## Safe Git And GitHub Workflow

Teach and prefer this flow:

1. Pull latest changes first
2. Create or use the right branch
3. Make one small meaningful change
4. Verify the change
5. Commit with a clear message
6. Push when ready to back up or share
7. Open a PR if the change should be reviewed or merged

Explain commit messages like this:

- good: `fix stale reminder front door after action-log repair`
- bad: `updates`

If the worktree is already dirty:

- do not revert unrelated work
- isolate your change carefully
- tell Sal when the repo already has unrelated local changes
- commit checkpoints often enough that rollback is practical

## Prompt Shape

When the task is not already tightly scoped, prefer this research-backed prompt shape:

- Goal
- Technical context
- Constraints
- Requirements
- Edge cases
- Security concerns
- Process
- Success criteria

The most important follow-up questions are:

- `What could go wrong?`
- `What security best practices apply here?`
- `Review this as if it ships tomorrow.`

## Software Engineering Basics To Enforce

Use these rules by default:

- make small changes
- keep one source of truth
- prefer clear names over clever code
- avoid copying the same logic in many places
- separate live runtime truth from summaries and reports
- verify risky changes with a real check
- do not call something fixed unless the proof matches the claim

For Chimera specifically:

- live runtime truth beats pretty local summaries
- generated reports are useful, but they are not proof by themselves
- if a monitor says green but the source files or runtime disagree, treat that as drift

## Project Management Basics To Enforce

Teach agents to think in these layers:

- `project`: the broader goal
- `task`: a concrete unit of work inside a project
- `action`: what actually happened
- `owner`: who is responsible next
- `done criteria`: how we know the work is truly complete
- `consumer`: who reads or depends on the output
- `blocker`: what is preventing progress

For this workspace, the key files are:

- `PROJECT_REGISTRY.md` = project definitions
- `TASK_REGISTRY.md` = active and completed task layer
- `ACTION_LOG.md` = what actually happened
- `DELIVERY_JOURNAL.md` = human front door
- `PROJECT_REMINDERS.md` = unfinished-work front door
- `KANBAN.md` = short working summary
- `CONTINUATION.md` = cross-session continuity

## Which Skill To Use Next

After using this skill as the beginner-friendly front door, route to the smallest needed specialist skill.

Default order:

1. `prompt-upgrade-engineer` for the internal brief
2. `objective-orchestration-loop` for the contract and loop
3. the smallest extra specialist skill needed for the real work
4. `vibe-coding-monitor` before closeout if friction, repeated misses, or quality drift appeared

Specialist routing:

- `prompt-upgrade-engineer`
  - use by default for any meaningful request, even as a fast hidden pass
- `project-operations-manager`
  - when the job is about current project state, reminders, next steps, or PM drift
- `github-manager`
  - when the job is about pull, push, branches, commits, merge, or PR flow
- `objective-orchestration-loop`
  - when the request says to keep going until complete
- `major-build-council-orchestrator`
  - when there are architecture tradeoffs, multiple credible paths, rollback/monitoring concerns, or the user explicitly asks for a council
- `critical-change-guard`
  - when the change touches an important runtime, automation, routing path, or risky shared system behavior
- `codex-feature-and-docs-research`
  - when the question is about latest Codex/OpenAI features or product behavior
- `system-change-verifier`
  - when behavior changed and the result needs proof beyond "the file was edited"
- `response-structure-enforcer`
  - when the user needs a short, direct answer and the closeout could become tool-heavy or buried
- `codex-task-and-project-capture`
  - when the request creates a real new initiative, task, blocker, or follow-up
- `codex-continuity-enforcer`
  - after meaningful work so future sessions can resume cleanly
- `codex-lesson-harvester`
  - when the work taught a reusable lesson, failure mode, or prevention rule
- `monitoring-opportunity-detector`
  - when the result can silently drift or fail later and should become monitored
- `lead-software-engineer`
  - when the work needs stronger implementation judgment
- `vibe-coding-monitor`
  - when we should inspect response quality, recommendations, skill activation, user friction, or repeated workflow misses

## Hook Matrix

Use these hooks as the default enforcement pattern.

### 1. Build-start hook

Run this when we are about to build, fix, refactor, or implement something non-trivial.

Required actions:

1. Restate the goal in plain English
2. Run `prompt-upgrade-engineer` as a fast or full pass
3. Read the relevant truth files
4. Create the objective contract
5. Decide whether a file-backed `plan.md` is needed
6. Decide whether `major-build-council-orchestrator` is needed
7. Decide whether `project-operations-manager` or `codex-task-and-project-capture` is needed
8. Load `objective-orchestration-loop` for non-trivial work
9. Load `critical-change-guard` if the change is risky
10. Note which activation cues or files caused the stack to trigger

Recommended workflow:

- `C:\Users\becke\claudecowork\workflows\codex\skill-preflight-and-closeout.md`

### 2. Implementation hook

Run this while the work is happening.

Required actions:

1. Keep changes small
2. Keep explanations simple
3. Track which specialist skills were actually used
4. Use `github-manager` if branch/commit/push/PR work is involved
5. Use `lead-software-engineer` when design or implementation quality needs stronger judgment
6. Use `system-change-verifier` planning before claiming the change worked
7. If the agent or user interaction is getting messy, flag `vibe-coding-monitor` for closeout

Recommended workflow:

- `C:\Users\becke\claudecowork\workflows\codex\build-test-verify-monitor-closeout.md`

### 3. Finish hook

Run this before calling the work complete.

Required actions:

1. Verify the behavior, not only the file edit
2. Decide whether monitoring should be added
3. Update project/task/action truth if the work mattered
4. If there was friction or a repeated miss, run `vibe-coding-monitor`
5. Capture durable lessons in the wiki or lesson layer
6. Say plainly which skills were used, which should be added next time, and whether activation was missed or correct
4. Update continuity if future sessions need the result
5. Capture a lesson if the work taught something reusable
6. Explain the result in plain English

Required companion skills:

- `system-change-verifier`
- `codex-continuity-enforcer`

Recommended companion skills:

- `monitoring-opportunity-detector`
- `codex-lesson-harvester`
- `response-structure-enforcer`

Recommended workflows:

- `C:\Users\becke\claudecowork\workflows\codex\task-and-continuity-closeout.md`
- `C:\Users\becke\claudecowork\workflows\codex\response-structure-enforcement.md`

### 4. Major-build hook

Run this before bigger architecture, workflow, orchestration, monitoring, or operating-model changes.

Required actions:

1. Compare:
   - biggest build
   - smallest safe phased build
   - defer/no-change option
2. Use a real skeptic/operator/tester view before committing
3. Phase the work

Recommended workflow:

- `C:\Users\becke\claudecowork\workflows\codex\major-build-council-and-delivery-loop.md`

## Enforcement Levels

Be honest about the enforcement level:

- `hard-enforced`
  - only say this if the runtime, hook, or platform truly forces the behavior
- `workflow-enforced`
  - use this when a workflow or instruction layer requires the step for cooperating agents
- `instruction-routed`
  - use this when the behavior is strongly requested by skill or AGENTS guidance
- `advisory`
  - use this when it is only a recommendation

For this skill today:

- the build-start, implementation, and finish hooks are mostly `workflow-enforced` plus `instruction-routed`
- they are not universal runtime hooks across every tool or agent automatically
- do not overclaim them as product-native hard enforcement unless proof exists

Practical truth:

- this skill can strongly shape behavior inside Codex and mirrored Chimera instruction layers
- it still needs AGENTS rules, shared skill mirrors, and closeout monitoring to behave like "every call" enforcement
- if the stack failed to trigger when it should have, capture that as a real issue and fix the trigger path

## Default Operating Loop

For most vibe-coding tasks, use this order:

1. Restate the goal in plain English
2. Run the prompt pass
3. Read the relevant truth files
4. Create the objective contract
5. Decide whether council is needed
6. Identify the smallest safe next step
7. Make the change
8. Verify it
9. Update project truth if the work mattered
10. Explain the result in beginner-friendly language
11. Review how the session went, not only what changed

For non-trivial work, the stronger version is:

1. prompt pass
2. objective contract
3. council decision if needed
4. execute one bounded step
5. verify
6. review the response quality and skill-routing quality
7. update durable truth
8. close out with plain-English next-step clarity
9. if not complete, loop again on the smallest unfinished phase

If the request creates a new real initiative:

- update `PROJECT_REGISTRY.md` or `TASK_REGISTRY.md`
- do not leave meaningful work only in chat

If the request changes meaningful tracked work:

- update `ACTION_LOG.md`
- refresh the front door if needed

If the request is a real build or closeout, also use:

- `C:\Users\becke\claudecowork\workflows\codex\vibe-coding-build-and-finish-loop.md`

## What We Already Do Well

Current strengths in this workspace:

- we have a real PM front door: `DELIVERY_JOURNAL.md`
- we track projects, tasks, and actions in durable files
- we keep continuity files for future sessions
- we already push toward human-first summaries instead of file-only answers
- we track owners, consumers, and done criteria better than many ad hoc projects

## What We Should Do More Consistently

Agents should push these improvements:

- every `in_progress` project should have an active task or be downgraded honestly
- regenerate the delivery journal and reminder front door after meaningful PM changes
- prefer one focused branch or commit per idea
- retire old Linux host/path references when touched
- keep `KANBAN.md` short and current instead of letting it become a long history dump
- re-check official changelogs/docs when Sal asks for the latest product behavior
- separate low-risk prototype autonomy from higher-supervision production work
- monitor how well the agent explained the work, not only whether code was written
- learn from repeated interaction friction and missed skill activation
- keep the starter stack discoverable across all supported platforms

## Current Fixable Issues

Use these as active watch-outs when helping Sal:

1. Some `in_progress` projects have no active task attached in `PROJECT_REMINDERS.md`.
   - current examples: `P-002`, `P-004`, `P-009`, and `P-012`
   - fix: either attach a real active task or downgrade the project status/reminder wording honestly

2. The generated PM front door is easy to trust even when it may lag source updates.
   - `DELIVERY_JOURNAL.md` and `PROJECT_REMINDERS.md` show generated timestamps
   - fix: after meaningful PM changes, rebuild the front door before making strong claims

3. Historical old-host and old-path references still appear in older task/action text.
   - old references like `open-claw@192.168.1.203` and `/home/open-claw/...` are historical only
   - fix: for new work use `root@100.67.172.114` and `/root/openclawtrading`, and clean old wording when those lines are touched

4. The repo is broad and often dirty.
   - fix: isolate changes carefully, avoid mixing unrelated PM, runtime, and research edits, and explain what you changed versus what was already there

5. `KANBAN.md` can accumulate too much historical detail.
   - fix: keep it as a short working summary and leave detailed history to `ACTION_LOG.md`, research notes, or handoffs

## High-Value Specialized Skills

The external source review suggests these are the highest-value repeatable skill patterns:

- test writer
- security review
- safe refactor
- safe migration

Current closest mappings in this workspace:

- `security-best-practices`
- `critical-change-guard`
- `system-change-verifier`
- `lead-software-engineer`

If these work patterns keep recurring, promote them into more explicit dedicated skills.

## Session Monitoring And Learning

This skill should not only help with building.
It should also help the system learn from how the session felt and performed.

Check these things before closeout when the task was meaningful:

- was the explanation too technical
- did the agent give a recommendation or just too many options
- did the agent make Sal open files to understand the result
- did the right skills activate
- which skills were used
- which skills should have been used but were missed
- did orchestration really happen
- did the objective contract stay clear
- did the final answer match the proof

If the same problem keeps happening:

- route to `vibe-coding-monitor`
- capture the issue durably
- add or tighten the instruction, workflow, or skill trigger

## Platform Optimization

This operator pattern should be mirrored, not copied blindly.

- `Windows Codex`
  - strongest local mutation, workflow, heartbeat, and skill-routing lane
- `Claude Code`
  - strong planning, critique, and architecture lane, but relies more on file continuity than native persistence
- `OpenCode`
  - should use the same starter stack through docs and config even if auto-discovery is weaker
- `Kimi VPS` and `Hermes VPS`
  - should use the same objective contract and monitoring logic, translated into Linux-native paths and local skill homes
- `Space Agent`
  - should use the same plain-English objective and review logic for visual or browser-first work, while leaving heavy mutation elsewhere

## Discoverability And Testing

This skill should be easy to discover and easy to improve.

The minimum test questions are:

- did the starter stack activate on a meaningful build request
- did it stay out of the way on a tiny request
- did it call `prompt-upgrade-engineer`
- did it create an objective contract
- did it call `objective-orchestration-loop` when the task was non-trivial
- did it route to the right specialist skills
- did it catch poor explanation, weak proof, or missed closeout
- did it capture repeated issues durably
- did the platform-specific instruction layer point to it correctly

## Good Agent Behavior

Good:

- "I checked the project front door, the task registry, and the action log. The next safe move is to finish `T-217` because it is active, high priority, and already has a clear next step."
- "A commit is just a saved checkpoint. We made one small fix, verified it, and can undo it later if needed."
- "This change is a refactor, which means we are cleaning structure without trying to change behavior."
- "Before we call this done, I'm checking whether we need PM updates, continuity updates, verification, and a follow-up monitor."

Bad:

- "Everything is updated" when only one summary file changed
- "The system is healthy" without checking live truth
- "We should refactor more" with no concrete reason or boundary
- "The hook is enforced" when it is really only a recommendation

## Closeout Rule

If meaningful work was done, update the smallest truthful set of:

- `C:\Users\becke\claudecowork\trace\ACTION_LOG.md`
- `C:\Users\becke\claudecowork\harnesses\codex\chimera\KANBAN.md`
- `C:\Users\becke\claudecowork\harnesses\codex\chimera\CONTINUATION.md`
- `C:\Users\becke\claudecowork\DELIVERY_JOURNAL.md`
- `C:\Users\becke\claudecowork\projects\PROJECT_REMINDERS.md`

If no durable file needed updating, say so plainly.

---
*vibe-coding-operator v2.1 | 2026-05-01 | Platform: Codex*
