# GitHub Publish And Shared Sync

## Trigger

Use this workflow when:

- a change should be committed
- a branch, push, PR, or pull is needed
- shared skills or workflows should be mirrored into `chimera-vps-deploy`

## Inputs

- changed files
- target repo
- branch intent
- approval boundary

## Steps

1. Check repo status and identify unrelated dirty work.
2. Isolate the intended files.
3. Verify the change before committing.
4. Create or switch to the right branch if needed.
5. Commit with a clear message.
6. Push when ready.
7. Open a PR when review or merge is wanted.
8. If the change is a shared skill or workflow, verify the mirrored copy also exists in `chimera-vps-deploy`.
9. Update the handoff with sync status.

## Expected Outputs

- isolated commit or honest blocked state
- push/PR status
- mirrored shared-skill status when relevant
