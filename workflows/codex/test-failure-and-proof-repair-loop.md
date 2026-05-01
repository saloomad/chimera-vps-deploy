# Test Failure And Proof Repair Loop

## Trigger

Use this workflow when:

- tests fail
- tests are missing
- proof is weaker than the claim
- verification only partially covered the behavior

## Inputs

- failing or missing proof surface
- changed files
- expected behavior
- current blocker

## Steps

1. State the proof gap plainly.
2. Decide whether the issue is:
   - missing test
   - failing test
   - missing integration proof
   - false completion claim
3. Repair the smallest proof gap first.
4. Re-run the proof.
5. If the proof still fails, loop again or downgrade the claim honestly.
6. Only allow `complete` when proof matches the claim.

## Expected Outputs

- repaired proof
- downgraded or corrected claim when proof is still insufficient
- next step if more repair is needed
