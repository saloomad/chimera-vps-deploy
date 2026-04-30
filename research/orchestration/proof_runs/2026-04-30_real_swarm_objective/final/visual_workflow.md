# Visual Workflow

## Control Room Checklist

- Objective
- Orchestration class
- Current phase
- Current gate
- Active workers
- Conflict status
- Rerun status
- Stop condition
- Final output path

## Mermaid Flow

```mermaid
flowchart LR
    A["Objective"] --> B["Plan.md"]
    B --> C["Landscape Brief"]
    C --> D["Dimension Decomposition"]
    D --> E1["Dim 01 Use-Case Routing"]
    D --> E2["Dim 02 Platform Routing"]
    D --> E3["Dim 03 Heartbeat Policy"]
    D --> E4["Dim 04 Visual Observability"]
    E1 --> F["Cross Verification"]
    E2 --> F
    E3 --> F
    E4 --> F
    F --> G["Targeted Validation"]
    G --> H["Insights"]
    H --> I["Writing Outline"]
    I --> J["Deployment Memo"]
    I --> K["Visual Workflow"]
```

## Human View Recommendation

### Top Summary

- show class, phase, freshness, and gate in one line

### Worker Matrix

| Dimension | Owner | Verdict | Confidence | Rerun Needed |
|---|---|---|---|---|
| use-case-routing | worker | aligned | high | no |
| platform-routing | worker | aligned with caveats | medium | no |
| heartbeat-policy | worker | aligned | high | no |
| visual-observability | worker | aligned | high | no |

### Conflict View

- no hard recommendation conflict
- medium-confidence gap around live platform proof expectations
- no targeted content rerun needed

## What To Avoid

- raw activity-only dashboards
- hiding unresolved issues in final conclusions
- treating heartbeat ticks as orchestration progress
