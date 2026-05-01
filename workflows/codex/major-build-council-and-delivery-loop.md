# Major Build Council And Delivery Loop

## Trigger

Use this workflow for:

- big builds
- project-wide or architecture changes
- routing, orchestration, monitoring, or operating-model changes
- key decisions where one fast opinion is not enough

## Inputs

- objective
- affected systems
- approval boundary
- current constraints
- strongest obvious alternatives

## Council Phase

Before implementation, run a real council with at least these perspectives:

1. builder / proposer
2. skeptic / critic
3. operator / maintainer
4. tester / integrator
5. final judge

The council must compare:

- most ambitious path
- smallest viable phased path
- do nothing / defer for now

If the topic is a trade or strategy decision, map that to:

- best long
- best short
- best no-trade

## Required Decision Output

The chosen path must name:

1. what problem is being solved
2. what alternatives were considered
3. why the chosen path won
4. what was intentionally deferred
5. what would invalidate the plan later
6. what the first safe slice is
7. what proof shape delivery must satisfy

Write that decision into the active `plan.md` when the work is multi-pass.

If a real council did not happen, say that clearly.

## Ownership Split

- council writes `chosen_path`
- orchestration owns execution
- reviewer owns `complete | iterate | blocked`

Council agreement is not the completion bar by itself.

## Delivery Loop

After the decision:

1. define the smallest safe phase
   - write it into `plan.md`
2. define tests before implementation:
   - local checks
   - integration checks
   - bounded live proof if reachable
   - monitoring need
3. define backup and rollback if the change is critical
4. implement the smallest real slice
5. verify producer and consumer integration
6. update guide docs for future humans and agents
7. update tasks, action log, continuity, and lessons
8. repeat the loop until:
   - done criteria are satisfied
   - a real blocker exists
   - or a new approval boundary is reached

## Session Hygiene

If the build introduces a different objective from the current thread:

1. recommend a session split
2. suggest a session name
3. say what belongs in the current thread vs the new one

Be honest if the platform does not expose native thread creation or renaming tools.

## Expected Outputs

- explicit council result
- phased build plan
- real tests and integration proof shape
- durable guide or updated guide
- orchestration loop until done or honestly blocked
