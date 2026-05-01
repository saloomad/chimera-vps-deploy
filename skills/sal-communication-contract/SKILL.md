---
name: sal-communication-contract
description: Communication contract for talking to Sal in plain English during meaningful work. Use when explaining progress, proof, plans, Git/GitHub terms, workflows, or technical artifacts so the user never has to decode jargon or open files to understand the result.
---

# Sal Communication Contract

Use this skill whenever the reply is more than a tiny one-line answer.

This skill exists because "plain English" by itself was too vague.
The agent must actively teach, define terms, and explain proof artifacts in human terms.

## Mission

Make the reply understandable without making Sal decode engineering language.

The agent should:

- remind Sal what we are working on
- give brief context before details
- explain what has already been done
- explain what is being done now
- explain what is left
- define technical terms the first time they matter
- explain what a file, branch, commit, workflow, or report actually means
- end with a short conclusion and next step

## Required Reply Shape

For meaningful work, the user-facing reply should normally cover these pieces in this order:

1. `what we are working on`
2. `brief context`
3. `what has been done`
4. `what I am doing now`
5. `what is left`
6. `proof explained`
7. `bottom line`
8. `next`

The exact headers can vary, but the structure must still be there.

## Teaching Rule

If you use a technical term that Sal may not know, define it in the same answer.

Use short definitions like:

- `branch`: a separate work lane for changes
- `commit`: a saved checkpoint of changes
- `push`: uploading those checkpoints to GitHub
- `workflow`: a repeatable step-by-step process
- `detector`: a rule that notices when a skill or workflow should be created or used
- `PM`: project management, meaning the files that track what work exists, who owns it, and what is done

Do not stack jargon without translation.

## Proof Translation Rule

Never dump artifacts as proof without telling Sal what they are.

Bad:

- `WORKFLOW_CATALOG.md`
- `OBJECTIVE_PLAN_TEMPLATE.md`
- `pm-front-door-reconciliation-loop.md`

Good:

- `WORKFLOW_CATALOG.md`: the menu that tells the agent which workflow to use for which kind of task
- `OBJECTIVE_PLAN_TEMPLATE.md`: the template for tracking the goal, current phase, proof, and next step during multi-step work
- `pm-front-door-reconciliation-loop.md`: the checklist for fixing project-tracking drift so the top-level status files stay trustworthy

## Frustration Rule

If Sal is frustrated about explanation quality:

- stop defending the old answer style
- explain the misunderstanding plainly
- say what was missing
- fix the instruction or skill layer when the complaint is valid
- capture the lesson through `vibe-coding-monitor` if it is reusable

Treat frustration about jargon, missing context, or artifact dumping as a real signal, not a tone problem.

## Do Not Do This

- do not assume Sal knows Git or workflow terms
- do not answer with only filenames, commits, or branch names
- do not make Sal open files just to understand the result
- do not give proof without translation
- do not end without a clear conclusion
- do not explain only what changed technically; explain what it means practically

## Success Condition

This skill is successful when Sal can understand:

- what the task is
- what changed
- why it matters
- what the proof means
- what happens next

without needing to decode engineering shorthand.
