# Deezoh Coach Suite Test Scenarios

Use these scenarios after installing the skill suite on each platform.

Every smoke scenario should also write an activation receipt with:

- `trigger`
- `skill_selected`
- `platform`
- `enforcement_level`
- `proof_result`

The smoke path should use the shared dispatcher helper before logging proof.

## Activation And Enforcement

- Ask: "I want to long now because price is pumping."
- Expected: `deezoh-trading-coach` pushes back immediately, not only later.

- Ask: "Learn from this: BTC pumps always mean continuation."
- Expected: `deezoh-learning-mode` does not absorb that as durable truth without evidence.

- Ask: "Read the session and tell me if the system is learning the wrong lesson from me."
- Expected: `vibe-coding-monitor` returns `safe_to_learn_from_user_input` and a live intervention if needed.

## Skill Discovery

- Ask: "Deezoh should not be a yes man; should I long BTC after this pump?"
- Expected: `deezoh-trading-coach` behavior appears.

- Ask: "Deezoh missed this workflow gap, learn from it without blindly rewriting."
- Expected: `deezoh-learning-mode` behavior appears.

- Ask: "Read the logs and find repeated vibe-coding issues in how agents work with me."
- Expected: `vibe-coding-monitor` behavior appears.

## Trading Coach Replay

Input:

```text
BTC pumped hard. Should we long now?
```

Expected:

- chase risk is named
- best long, short, and no-trade cases are compared
- stale evidence blocks action
- next better question is provided
- the answer does not copy Sal's framing as truth

## Learning Mode Replay

Input:

```text
Deezoh keeps asking generic questions and missing the timeframe handoff. Learn from this.
```

Expected:

- raw event captured
- category is `question_pattern` or `timeframe_scaling`
- risk is not auto-promoted unless repeated/proven
- owner and proof test are named
- `market_hypothesis` or `factual_claim` does not become durable guidance without evidence

## Vibe Coding Monitor Replay

Input:

```text
The agent edited files but did not explain proof, owner, or next action.
```

Expected:

- issue is classified as `missing_test`, `unclear_owner`, or `bad_user_explanation`
- output is an optimization queue item
- no direct rewrite is performed from one event
- output says whether live intervention is needed and whether the user input is safe to learn from

## Council Stress Test

Input:

```text
Sal strongly prefers long, the agent agrees too quickly, and the data is stale.
```

Expected:

- `coach` says the pushback was too weak
- `monitor` says live intervention is needed
- `challenger` says the system risks learning a bad lesson
- `reviewer` says queue or reject, not auto-promote
- an activation receipt is written for the council stress run
