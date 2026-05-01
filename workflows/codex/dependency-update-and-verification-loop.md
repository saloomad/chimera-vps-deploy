# Dependency Update And Verification Loop

## Trigger

Use this workflow when:

- package, library, model, or tool dependencies are added or updated
- the user asks to update dependencies

## Inputs

- current dependency state
- target package or tool
- compatibility risk
- verification commands

## Steps

1. Define why the dependency is changing.
2. Check whether the change is approved and necessary.
3. Update the dependency in the smallest safe way.
4. Run typecheck, tests, or smoke proof that matches the change.
5. Name any migration or rollback concern.
6. Update docs or workflow notes if the change affects future sessions.

## Expected Outputs

- updated dependency or honest blocker
- proof that the environment still works
- explicit rollback or compatibility note when needed
