# Deezoh Coach Suite Runtime And Enforcement

Use this file to explain how the three-skill suite should behave together in live work.

## Why The Skills Stay Separate

They are separate because they do different jobs:

- `deezoh-trading-coach`
  - live answer quality
  - real-time pushback
  - trading education
- `deezoh-learning-mode`
  - safe capture and promotion control
  - protects the system from learning the wrong lesson
- `vibe-coding-monitor`
  - interaction audit
  - log review
  - activation, enforcement, and discoverability checks

They should not behave as isolated silos.
They should operate as a handshake.

## Handshake

1. Coach answers and pushes back in the moment.
2. Learning mode decides whether the moment is safe to capture.
3. Monitor checks whether the interaction itself failed, whether a skill should have activated, and whether the user input was safe to learn from.
4. Reviewer decides whether the lesson becomes durable guidance.

## Activation Rules

Activate `deezoh-trading-coach` when:

- Sal asks for a trade decision
- Sal frames a move as obvious
- Sal asks whether to enter now
- Sal asks how to think better as a trader

Activate `deezoh-learning-mode` when:

- Sal says Deezoh missed something
- Sal suggests a new workflow or question style
- Sal teaches a better way to think
- a repeated trading mistake or system gap appears

Activate `vibe-coding-monitor` when:

- Sal asks why this keeps happening
- logs or session traces should be inspected
- an answer felt technically correct but operationally weak
- a skill should have activated and did not
- the system may be learning from the wrong user input

## Enforcement Hooks

Minimum enforcement surfaces:

- Deezoh `AGENTS.md`
- Codex `vibe-coding-operator`
- shared platform skill index
- replay scenario suite
- live OpenClaw skill availability
- OpenCode wrapper tests
- activation receipt logger
- stale-runtime lint
- pre-response dispatcher helper

Preferred future enforcement:

- OpenClaw hook or bootstrap line that reminds Deezoh to run the coach/learning/monitor handshake
- periodic monitor run over recent handoffs and action logs
- explicit taskflow or lobster stage that captures accepted improvements

## Log Review Loop

Use this order:

1. current chat
2. current continuation files
3. `trace/ACTION_LOG.md`
4. newest checkpoint
5. task/project front door
6. live OpenClaw logs

Questions the monitor should answer:

- what repeated friction happened
- did the right skill activate
- did the agent push back when it should have
- did the system nearly learn from a bad claim
- what small improvement has the highest payoff
- who owns the fix
- how will we verify it

## Council Test Shape

Use this council whenever the suite itself is being improved:

- `coach`
  - grades live pushback quality
- `monitor`
  - grades activation and interaction diagnosis
- `challenger`
  - finds the bad lesson the system might wrongly absorb
- `reviewer`
  - decides `promote`, `queue`, or `reject`

## Proof Standard

Do not claim the suite works because files exist.

Require:

- skill validation
- runtime availability
- one live replay per skill
- one contradiction test where the user input should not be learned literally
- one council stress test
- one activation receipt per smoke scenario
- one stale-runtime lint pass before claiming live-truth enforcement

## Implemented Proof Helpers

- `chimera-vps-deploy/scripts/log_deezoh_skill_activation.py`
  - appends machine-readable activation receipts
- `chimera-vps-deploy/scripts/lint_deezoh_runtime_paths.py`
  - fails on old host or path references
- `chimera-vps-deploy/scripts/run_deezoh_coach_suite_smoke.py`
  - writes smoke receipts for the main scenarios
- `chimera-vps-deploy/scripts/select_deezoh_coach_skill.py`
  - chooses the coach / learning / monitor stack before response
