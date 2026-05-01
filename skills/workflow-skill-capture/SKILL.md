---
name: workflow-skill-capture
description: Turn repeated pain, repeated tasks, or repeated decisions into reusable workflows and skills. Use when the same issue appears more than once, when a project needs a repeatable process, or when important project knowledge should be captured instead of relearned.
triggers:
  - create a workflow
  - create a skill
  - this keeps happening
  - capture this pattern
  - make this reusable
  - document this process
  - auto create skills
  - recurring problem
---

# Workflow Skill Capture

Use this skill to convert repeated project pain into reusable system assets.

## When To Trigger Automatically

Create or update a workflow/skill when you see one of these:

1. The same failure happens twice
2. The same manual task happens three times
3. A high-risk procedure has more than five steps
4. The team asks for the same explanation repeatedly
5. A project-specific rule is important enough that forgetting it would be costly
6. A workflow clearly needs to loop until `complete`, `iterate`, or `blocked`
7. A pattern now matters across more than one platform

## Decision Rule

Choose:
- `docs/` when the team mainly needs explanation
- `workflow` when the team needs a repeatable sequence
- `skill` when the agent needs reusable behavior
- all three when the pattern is both human and agent critical

Promotion rule:

- `note -> workflow` when order matters
- `workflow -> skill` when agent behavior must become reusable
- `skill -> shared mirror + AGENTS mention` when the pattern matters across platforms

## Capture Workflow

1. Name the repeated pattern
2. Describe the trigger
3. Describe the input
4. Describe the desired output
5. Write the shortest useful repeatable workflow
6. Create or update the skill if the agent should apply it directly
7. Link the related documentation
8. Mention the new artifact in the relevant instructions if it is important
9. Decide whether the workflow is:
   - one-pass
   - loop-until-done
10. If looped, define:
   - objective contract
   - review outcomes
   - stop condition
11. Score the promotion need using:
   - importance
   - dependencies
   - recurrence
   - cross-platform relevance

## Minimum Deliverable

For each captured pattern, leave:
- one named artifact
- one clear trigger
- one clear expected output
- one place where teammates can find it again
- one clear statement of whether the workflow should loop until done

## Related References

- [Workflow And Skill Capture Policy](../../docs/WORKFLOW_AND_SKILL_CAPTURE_POLICY.md)
