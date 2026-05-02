# Meaningful Change Lifecycle And Enforcement Loop

## Trigger

Use this workflow for any meaningful create, build, fix, refactor, workflow change, skill change, automation change, monitoring change, or behavior change.

If the work is big enough that Sal would care whether it was done safely, this workflow applies.

## Purpose

This is the default "do the whole job properly" loop.

It exists so a change does not stop at implementation only.
It forces the agent to think about:

- the workflow
- the enforcement surface
- the implementation
- what else in the system must be updated
- testing and proof
- implementation review
- documentation
- continuity and PM updates
- monitoring and follow-through

## Inputs

- ultimate objective
- current slice
- change surface
- risk level
- owner platforms
- proof requirements

## Mandatory Phases

### 1. Define the objective

- say what we are trying to change
- say which bounded slice is being worked now
- say what "done" means
- say what would make the work blocked instead of complete

### 2. Choose the workflow

- choose the main workflow from `WORKFLOW_CATALOG.md`
- if none fits cleanly, create or update the workflow first
- if the work touches multiple systems, name the workflow owner for each system

### 3. Choose the enforcement surface

Before implementation, decide how the behavior will actually be enforced.

Choose the smallest honest enforcement layer:

- startup instruction
- skill
- workflow
- detector
- hook
- slash command
- Task Flow
- Lobster
- standing order
- scheduler
- wrapper script
- monitor

Use the platform hooks matrix.

### 4. Implement the change

- make the smallest real change
- keep the write scope clear
- do not mix unrelated repairs unless they are required for the objective

### 5. Update dependent surfaces

Check what else must change because of this work:

- docs
- instructions
- shared mirrors
- workflows
- skills
- PM files
- monitoring
- reports
- scripts
- platform mirrors
- runtime bootstrap notes

If a dependent surface matters and is now stale, update it in the same pass when safe.

### 6. Test and prove

Use the strongest practical proof that fits the risk:

- file proof
- command or script proof
- local integration proof
- live runtime proof
- monitor consumer proof
- handoff proof

Do not call the change done because a file exists.

### 7. Review the implementation

Review must answer:

- did the real objective move
- did the enforcement layer actually get wired
- did all important dependent surfaces get updated
- is the proof strong enough
- should the result be `complete`, `iterate`, or `blocked`

### 8. Document and teach

If the change matters later:

- update the right workflow or skill
- update the user-facing explanation layer
- update research or wiki when the lesson is durable
- explain the result in plain English

### 9. Publish and sync

When needed:

- commit
- push
- PR
- shared mirror update
- handoff

### 10. Monitor and iterate

If the work introduced new behavior that can drift:

- choose a monitor, hook, detector, or follow-up workflow
- make sure the monitor has a consumer
- queue the next iteration if the objective is not fully complete

## Minimum Output

Every meaningful change should leave behind:

- the chosen workflow
- the chosen enforcement surface
- the implemented change
- the dependent surfaces updated
- the proof result
- the review outcome
- the documentation or continuity update
- the next step

## Review Outcomes

- `complete`
  - the full objective is done and enforced enough for the current platform reality
- `iterate`
  - one slice is done, but more work is still needed
- `blocked`
  - a real outside dependency or approval boundary prevents safe continuation
