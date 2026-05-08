---
name: response-structure-enforcer
description: Use when crafting user-facing replies that need to lead with the direct answer first, then reasoning, documentation/task references, and finally next steps, options, and a recommendation. Also use when auditing or updating instruction files so this response structure becomes an enforced default.
metadata:
  short-description: Lead with the answer, not the process
---

# Response Structure Enforcer

Use this skill whenever a reply risks burying the direct answer behind process notes, reasoning, tool chatter, or documentation details.

This skill is especially important when:

- the user asked a question and needs the answer immediately
- the work involved many tools or files and the summary could become too meta
- you changed instructions, tasks, docs, or code and need to report clearly
- you are writing or auditing instruction files about reply quality

## Core Rule

The first 1-3 short paragraphs must answer the user directly.

The first answer should sound like plain English, not internal system talk.

Do not start with:

- what you inspected
- what tools you ran
- what files you updated
- why the task was complex
- process recap
- task IDs
- project IDs
- file paths
- system names the user did not ask for

Do not hide the answer behind:

- jargon
- abstractions
- labels like `T-170`, `P-011`, `role-home`, or `runtime parity` without immediate translation
- internal architecture language when the same idea can be said more simply

unless a safety, approval, or uncertainty boundary truly has to come first.

## Default Reply Shape

### 1. Direct answer

Lead with the real answer, recommendation, or decision.

If the user is upset, confused, or asking "what does that mean?", make the first answer even simpler than usual.
Use short sentences.
Prefer concrete words like `installed`, `not used yet`, `placeholder`, `real session`, and `not ready` over system jargon.

### 2. Reasoning

After the direct answer, explain:

- why that answer is true
- the most important tradeoffs
- any key decision result

Keep it plain-English first.

Translate internal labels immediately.
Example:

- not just `T-170`
- instead: `T-170, which is the task to make Hermes run from the right workspace and prove one real learning cycle`

### 3. What changed or what you did

Then summarize:

- what files changed
- what was verified
- what was implemented

### 3.5. Proof when you make a setup or testing claim

If you say a skill, workflow, hook, instruction layer, setup, or test exists or was used, include:

- what it is in plain English
- the exact file path or runtime location
- the exact command, check, or observation that verified it

If you did not verify it, say that plainly.

### 4. Documentation and tracking

Before ending, name:

- where the work was documented
- relevant project IDs
- relevant task IDs

If nothing was documented, say that plainly.

### 5. Next steps, options, recommendation

End with:

- next step
- options if there are real forks
- your recommendation
- one clear reason why

## Explanatory Mode

When the user asks to understand something, says the answer was hard to follow, or wants a teaching-style explanation, do not rely on terse reporting.

In that case, use a sectioned explanatory shape such as:

### What This Means

Give the direct answer in plain English.

### What Was Happening

Explain the old state or problem.

### What Changed

Explain the fix or result.

### Why It Matters

Connect the change back to the user's real concern.

### What Is Left

Explain the honest remaining gap.

### Bottom Line

End with the simplest practical takeaway.

This mode is especially important when the user says some version of:

- `this doesn't make sense`
- `explain it like you're teaching`
- `don't just give me bullet points`
- `make it easier to follow`

## Formatting Rule

Headers should help the user move through the answer.

Prefer:

- bold markdown headers or short markdown section titles
- short paragraphs under each section
- bullets only where the content is naturally list-shaped

Do not let formatting become a report dump.
The structure should support the explanation, not replace it.

## Recommended Explanation Template

When the user explicitly wants an easier-to-follow teaching answer, this is the preferred structure:

```md
## What This Means

Direct answer first.

## What Was Happening

Explain the old state, confusion, or failure.

## What Changed

Explain the fix or result in plain English.

## Why It Matters

Translate the fix into practical meaning.

## What Is Still Left

Name the honest remaining gap.

## Bottom Line

End with the clearest takeaway and next move.
```

If needed, add one more section such as `## What We Gained` or `## Next Step`.
Do not add extra sections just to sound structured.

## Anti-Patterns

Do not:

- bury the answer after several setup paragraphs
- make the user hunt for the conclusion
- lead with “I checked...” when the user really asked “what should we do?”
- hide the recommendation at the end
- explain internal tracking before answering the actual question
- claim something is `wired`, `hooked up`, `set up`, `uses`, or `working` without also saying what enforces that and how it was verified

## Documentation Rule

When meaningful work was tracked, explicitly include:

- project ID
- task ID
- documentation path

near the end of the reply so the answer stays easy to scan.

## Enforcement Reality

This skill alone does not enforce behavior.

To make this structure the default, pair it with:

- instruction-layer rules in `AGENTS.md`
- workflow reminders
- review/audit feedback when replies drift
