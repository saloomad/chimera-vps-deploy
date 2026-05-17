# External Patterns

Use these as pattern sources, not as blind replacements.

## OpenAI Agent Evals / Trace Grading / Graders

Best for:

- dataset-backed regression checks
- workflow trace scoring
- reusable judge criteria

Borrow:

- trace-first grading
- versioned evaluation datasets
- scorer reuse

Do not copy blindly:

- generic graders should not replace domain-specific decision logic

## LangSmith

Best for:

- evaluator reuse
- experiment comparison
- pairwise A/B judging

Borrow:

- same evaluator across many runs
- baseline vs candidate compare

Do not copy blindly:

- hosted traces are not a replacement for local runtime truth

## Promptfoo

Best for:

- adversarial matrices
- prompt and workflow red-team cases
- CI-style regression gates

Borrow:

- scenario packs
- declarative failure cases

Do not copy blindly:

- safety red-team scores are not the same as workflow usefulness or strategy quality

## Braintrust

Best for:

- experiment tracking
- offline vs online evaluation split
- scorer discipline

Borrow:

- systematic comparison mindset
- experiment history

Do not copy blindly:

- generic AI-app scoring should not collapse domain-specific failure classes
