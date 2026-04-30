# Sub-Agent Role Map

These roles make the swarm concrete instead of hand-wavy.

## Core Roles

| Role | What it owns | Typical lane | Output |
|---|---|---|---|
| `swarm-orchestrator` | decomposition, gates, reruns, final route | strongest planning lane | `plan.md`, rerun decisions |
| `landscape-scanner` | freshness reset and broad scan | planning or medium research lane | `research/landscape_brief.md` |
| `dimension-researcher` | one bounded evidence slice | cheap worker lane first | `research/dimNN.md` |
| `cross-verifier` | confidence grading and conflict detection | stronger review lane | `research/cross_verification.md` |
| `targeted-validator` | conflict resolution or narrow rerun | stronger review lane | `research/targeted_validation.md` |
| `insight-synthesizer` | cross-dimensional pattern extraction | stronger synthesis lane | `research/insights.md` |
| `chapter-writer` | chapter draft from verified inputs | cheap or medium writing lane | `writing/chapterNN.md` |
| `assembly-editor` | final merge, structure, consistency | medium or strong review lane | `final/report.md` |
| `docx-finisher` | export formatting | cheap mechanical or medium execution lane | `final/report.docx` |

## Optional Trading-Specific Roles

Use these only when the job touches the live trading ecosystem.

| Role | What it owns |
|---|---|
| `setup-watcher` | monitor inputs and detect candidate setups |
| `context-reader` | macro, derivatives, on-chain, or narrative context feed |
| `risk-checker` | freshness, conflict, and risk validation |
| `decision-writer` | `execute`, `watch`, or `reject` closeout |
| `position-manager` | active-trade state management |
| `post-trade-reviewer` | replay, lessons, and failure analysis |

## Important Rules

- workers do not silently take over orchestration
- writers do not redo core research
- validators rerun only failed or ambiguous slices
- the orchestrator decides whether the whole job is actually a swarm or should stay a lean pipeline
