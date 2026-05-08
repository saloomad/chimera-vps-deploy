---
name: sal-communication-contract
description: Communication contract for talking to Sal in plain English during meaningful work. Use when explaining progress, proof, plans, Git/GitHub terms, workflows, or technical artifacts so the user never has to decode jargon or open files to understand the result.
---

# Sal Communication Contract

Use this skill on every meaningful user-facing reply.

Only skip it for a tiny one-line mechanical answer where no explanation is needed.

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
- assume Sal may not remember prior tracker codes, file names, or project shorthand unless the current answer reintroduces them in plain English
- define technical terms the first time they matter
- explain what a file, branch, commit, workflow, or report actually means
- end with a short conclusion and next step

## Teaching Style Rule

When Sal asks for an explanation, especially after saying the answer felt confusing, disconnected, or too report-like, default to a teacher or professor style.

That means:

- explain from one idea to the next, not as disconnected status bullets
- show cause and effect
- say what problem existed, what changed, why that change matters, and what remains
- use headers that make the answer easy to scan
- make the reader feel guided through the logic, not handed fragments

The goal is not to sound academic.
The goal is to make the explanation build naturally.

## Preferred Explanation Shape

When the answer is explanatory rather than just status, prefer this order:

1. `What This Is About`
2. `What Was Wrong Before`
3. `What I Changed`
4. `Why That Fix Matters`
5. `What We Gained`
6. `What Is Still Left`
7. `Bottom Line`

Use short paragraphs under each header.
Bullets are allowed inside a section when listing examples or concrete items, but the answer should not collapse into bullet-only reporting if Sal asked for understanding.

## Navigation Rule

Make meaningful explanations easy to navigate.

Prefer:

- short headers
- one idea per paragraph
- transitions like `before this`, `because of that`, `so the fix was`, `what this means now`

Avoid:

- long walls of text with no sectioning
- one-line bullet dumps with no connective explanation
- jumping straight from file names to conclusions without teaching the middle

## Recommended Teaching Template

When Sal wants a full explanation, this is the default answer skeleton:

```md
## What This Is About

One short paragraph that names the real topic in plain English.

## What Was Wrong Before

Explain the old problem or confusion in 1 to 3 short paragraphs.

## What I Changed

Explain the fix in the order it happened.
Use bullets only if several concrete changes need listing.

## Why That Matters

Connect the fix back to the real user concern.

## What We Gained

Explain the new capability, protection, or clarity that now exists.

## What Is Still Left

Explain the honest remaining gap or next dependency.

## Bottom Line

End with the simplest practical takeaway.
```

This is not meant to make every answer longer.
It is meant to make explanatory answers easier to follow from top to bottom.

## Default Rule

Treat this skill as mandatory by default, not optional.

If the reply involves progress, proof, GitHub, workflow, planning, debugging, tradeoffs, or next steps, this skill should already be active.

If Sal recently complained that the explanation was confusing, do not fall back to shorthand later in the same objective.

If Sal complained that tracker IDs, file dumps, or shorthand were confusing:

- do not lead with task IDs, project IDs, branch names, or filenames
- restate the human meaning first
- only mention the code or file name after the plain-English explanation, and only if it still helps

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

If Sal explicitly asks for the explanation to be easier to follow, use visible markdown headers instead of relying on implied structure.

Do not assume Sal remembers the last reply.
Reintroduce the human meaning of the current work before relying on earlier labels.

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

Also treat internal tracker shorthand as jargon.

This includes:

- task IDs like `T-238`
- project IDs like `P-006`
- GitHub labels like `PR #2`
- internal names like `GL-002`

If one of these appears, immediately translate it into plain English.

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

If you mention a file that was edited, also say:

- what kind of file it is
- why that file matters
- what changed inside it

## Frustration Rule

If Sal is frustrated about explanation quality:

- stop defending the old answer style
- explain the misunderstanding plainly
- say what was missing
- fix the instruction or skill layer when the complaint is valid
- capture the lesson through `vibe-coding-monitor` if it is reusable

Treat frustration about jargon, missing context, or artifact dumping as a real signal, not a tone problem.

If Sal has already complained about shorthand in the current objective:

- slow down
- assume Sal may have forgotten the earlier context
- restate the plain-English meaning instead of saying only the tracker code or filename

## Do Not Do This

- do not assume Sal knows Git or workflow terms
- do not assume Sal remembers task numbers, project numbers, or file names from earlier turns
- do not answer with only filenames, commits, or branch names
- do not answer with only task IDs, project IDs, pull request numbers, or internal labels
- do not make Sal open files just to understand the result
- do not give proof without translation
- do not end without a clear conclusion
- do not explain only what changed technically; explain what it means practically
- do not dump a list of edited files without saying what each one is and why it changed

## Success Condition

This skill is successful when Sal can understand:

- what the task is
- what changed
- why it matters
- what the proof means
- what happens next

without needing to decode engineering shorthand.
