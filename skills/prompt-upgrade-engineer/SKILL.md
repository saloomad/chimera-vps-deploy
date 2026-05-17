---
name: prompt-upgrade-engineer
description: Default first-pass skill for every Sal instruction. Transform rough non-technical ideas into stronger execution briefs that help the next agent reason, inspect the right context, and answer with better structure.
triggers:
  - rewrite my prompt
  - improve my prompt
  - clarify what i mean
  - make this instruction better
  - turn this into a better brief
  - i am not experienced
  - ask clarifying questions
  - fill in the gaps
  - what i probably mean
  - turn this into professional terms
---

## Redirection Pattern — RECOGNIZE AND HONOR IMMEDIATELY

Sal will sometimes cut off a deep analysis with a redirect like:
- "forget lobster / vps / architecture — what can Hermes do RIGHT NOW"
- "doesnt have to be X, just look at Y"
- "forget the details, just tell me what works"

This is a FIRST-CLASS signal, not a vague prompt. When you see it:
1. STOP the current analysis track
2. Pivot directly to actionable implementation
3. Give the practical answer in 2-3 paragraphs max
4. Do NOT re-explain why you were going down that path
5. Do NOT offer multiple options if Sal clearly wants one path

Implementation is the default mode. Architecture is only for when Sal explicitly asks for it.

## Use This Skill As Default First Pass

Use this skill as the default first pass on every Sal instruction.

The point is not cosmetic rewriting.
The point is to translate Sal's real intent into a stronger internal execution brief so the next agent:
- understands the real objective
- checks the right files, tools, skills, and workflow rules
- avoids drifting on non-technical wording
- asks fewer but better clarifying questions

## What This Skill Is For

Sal often knows the outcome he wants, but not always:
- the best technical wording
- the clean priority order
- the exact file/report/tool checks needed first
- which parts should be done now versus tracked later

This skill should repair that gap without turning every request into slow bureaucracy.

## Design Goal

Think like a professional technical translator, not a copy editor.

The skill should:
- preserve Sal's real goal
- add missing execution structure
- surface the few real forks that matter
- point the next agent to the right proof path
- make prompt enhancement visible when it materially changed the working brief
- prepare the reply so Sal gets context, explanation, and a short conclusion instead of artifact dumps

The skill should not:
- hide uncertainty with polished wording
- dump chain-of-thought
- ask busywork questions
- pretend the rewrite itself completed the job

## Modes

### 1. Fast pass

Use for tiny direct asks.

Goal:
- confirm the real objective quickly
- avoid over-processing
- keep the pass mostly invisible

### 2. Full pass

Use when the request is:
- long
- vague
- cross-system
- emotionally frustrated
- mixing several goals
- likely to fail if taken literally
- likely to need files, tools, skills, reports, or tracked context

## Read First

Read the smallest useful set of:
- `AGENTS.md`
- `tasks/TASK_REGISTRY.md`
- `projects/PROJECT_REGISTRY.md`
- `trace/ACTION_LOG.md`
- `harnesses/codex/chimera/CONTINUATION.md` when Chimera continuity matters
- relevant agent files, workflow files, reports, or docs tied to the request

If the request is about OpenClaw prompt quality or routing, also inspect:
- `/root/openclawtrading/skills/prompt-upgrade-engineer/SKILL.md` when Linux is reachable
- `/root/openclawtrading/agents/prompt-engineer/AGENTS.md`
- `/root/openclawtrading/agents/prompt-engineer/WORKFLOW.md`

## What This Skill Must Do

1. Infer the real objective
2. Translate non-technical wording into professional internal terms
3. Separate desired outcome from the user's guessed implementation
4. Identify hidden constraints, approval boundaries, and likely follow-ups
5. Decide what must be done now versus tracked later
6. Point the next agent to the most likely relevant files, tools, skills, and workflow rules
7. Ask clarifying questions only if a real fork still remains
8. Reference relevant prior tracked work when it materially reduces ambiguity
9. Produce a stronger internal execution brief

## What The Skill Adds

For large or messy requests, this skill should usually add:
- a clearer objective
- a priority order
- a "do now" vs "track later" split
- the most relevant files and reports to inspect first
- likely skills and tools to check
- a verification shape
- a named consumer or owner so the output does not die in chat
- whether a build council is likely needed before implementation

If the prompt is already strong, say that plainly and keep the pass minimal.

## Clarifying Question Rule

Ask a clarifying question only if:
- two or more choices have materially different consequences
- the repo, logs, or live files cannot answer it
- the wrong assumption would waste real time or create real damage

If a safe assumption is possible:
- make it
- say it plainly
- keep moving

## Proof / Demo Rule

If Sal explicitly asks to see the transformation:
- show the raw request
- show the transformed brief
- show `what it added`
- stop there unless the user also explicitly asked for the next execution phase in the same turn

Do not end with a vague permission-loop close like:
- "ready to proceed?"
- "I can do that next if you want"

unless a real new approval boundary still remains.

If the instruction explicitly says:
- `stop after the proof`
- `proof only`
- `show the transformation only`

then do not:
- propose next steps
- auto-spawn council
- auto-broaden into implementation planning

## Important Boundary

This skill should **name** the likely relevant files, tools, skills, and checks.
It should **not replace** the next agent's actual enforcement layer.

So:
- prompt-engineer can say: "check these skills/tools/files first"
- the next agent still has to actually do its preflight
- prompt-engineer can say: "a build council is likely needed"
- the orchestration and operator layers still decide whether to spawn that council

## Rewrite Format

When this skill is used, produce an internal brief with:

1. `raw_user_intent`
2. `probable_real_goal`
3. `user_experience_translation`
4. `task_class`
5. `priority_order`
6. `must_do_now`
7. `follow_up_later`
8. `assumptions`
9. `conversation_anchors`
10. `context_to_read_first`
11. `skills_to_consider`
12. `tools_to_check`
13. `workspace_rules_to_check`
14. `freshness_requirements`
15. `done_criteria`
16. `verification_shape`
17. `monitoring_need`
18. `consumer_or_owner`
19. `likely_risks`
20. `best_execution_shape`
21. `minimal_clarifying_questions`
22. `transformation_delta`
23. `user_visible_marker`
24. `user_visible_summary`
25. `rewritten_instruction_for_agent`
26. `reply_shape_for_sal`

For tiny direct asks, this can collapse into a short internal brief as long as the pass still happened.

`conversation_anchors` means:
- the tracked task, report, decision, or earlier file-backed work this request clearly relates to

`transformation_delta` means:
- what the skill added that the raw prompt did not say clearly enough
- why that addition helps execution

`user_visible_marker` means:
- a short visible status line for the final user-facing reply
- use:
  - `Prompt enhanced: full`
  - `Prompt enhanced: fast`
  - `Prompt enhanced: minimal`

`user_visible_summary` means:
- one short line saying what the enhancement materially added
- example:
  - `Added: objective, done criteria, proof path`

`reply_shape_for_sal` means:
- the brief reminder the next agent should give Sal at the start
- what terms probably need definition
- what proof artifacts need translation into plain English
- what short conclusion should exist at the end

## Best Execution Shape

Choose one:
- `direct`
- `direct + verify`
- `direct + verify + monitor`
- `lead does fast prompt pass then execute`
- `spawned prompt-engineer pre-pass then lead executes`
- `orchestrated`
- `orchestrated with reviewer/tester`

Say why.

## Prior-Work Referencing Rule

If the current request clearly relates to prior tracked work:
- name the relevant task/project/report files
- use them to tighten the brief
- do not pretend old chat memory is available if it is not in files

## Hidden Reasoning Rule

Use internal reasoning to improve the brief.
Do **not** dump hidden chain-of-thought.

The user-facing result should be:
- clearer
- more structured
- more actionable

Not more verbose for its own sake.

## Example

Rough request:
- "fix the system it keeps messing up and make the agents smarter"

Better internal brief:
- `probable_real_goal`: identify the current concrete failure mode instead of doing generic cleanup
- `user_experience_translation`: Sal is asking for fewer repeated mistakes, not a theoretical redesign
- `task_class`: `COMPLEX`
- `context_to_read_first`: task registry, latest incident report, affected agent instructions, runtime logs
- `skills_to_consider`: prompt-upgrade-engineer, system-change-verifier, codex-task-and-project-capture, monitoring-opportunity-detector
- `tools_to_check`: live logs, current config, relevant scripts, Linux runtime access
- `done_criteria`: root cause identified, fix implemented or blocker captured, proof recorded, consumer named
- `rewritten_instruction_for_agent`: "Inspect the live runtime and the affected agents, identify the concrete failure mode causing the visible bad behavior, implement the smallest real fix, verify it, and record the result plus named follow-up path."

## What Not To Do

- do not just paraphrase the user with nicer wording
- do not make the prompt longer without making it clearer
- do not ask obvious questions the repo can answer
- do not turn every request into a permission loop
- do not pretend the rewrite itself solved the task
- do not confuse "which checks should happen" with "those checks already happened"

## Success Condition

This skill is successful when:
- the next action becomes clearer
- Sal's real intent is represented better than the raw wording
- missing technical structure is filled in
- the next agent knows what to inspect first
- unnecessary confusion and drift are reduced before execution starts
- the transformation can be explained afterward in plain English if Sal asks what changed
- when the pass materially helped, the user can also see that it happened through a short visible marker instead of having to trust hidden internal behavior
- the next reply is easier for Sal to follow without opening files or decoding jargon
