---
name: macro-calendar
description: Read the scheduled macro event clock for Chimera. Use for FOMC, CPI, NFP, jobs, inflation, GDP, central-bank dates, and "what macro is coming up?" questions.
---

# Macro Calendar

## Current Chimera Truth

This is a `Section 6: Macro And Cross-Asset` skill.

Best current source order:

1. `reports/auto/ECONOMIC_CALENDAR.json`
2. direct macro headline helper context when needed

Do not treat this skill as the full macro regime owner.
It owns the event clock, not the whole cross-asset read.

## What This Skill Should Answer

- what macro event is next
- what is inside the next 48 hours
- how important the event is
- whether the event should change timing or conviction

## Best Current File

- live repo truth:
  - `/root/openclawtrading/reports/auto/ECONOMIC_CALENDAR.json`
- local mirror when present:
  - `C:\Users\becke\claudecowork\reports\auto\ECONOMIC_CALENDAR.json`

## What Belongs Here

- FOMC
- CPI
- PPI
- NFP
- jobless claims
- GDP
- PMIs
- central-bank speeches and rate decisions

## What Does Not Belong Here As The Main Owner

- broad cross-asset regime
- SPX / DXY / gold / oil directional state
- detailed catalyst/news interpretation
- detailed earnings interpretation

Those belong in other lanes:
- Section 6 broader macro owner
- Section 7 catalysts/news

## Practical Rule For Deezoh

Use this skill to answer:

- `is there a scheduled macro reason to delay or reduce conviction right now?`

Do not use it alone to say:

- `macro is bullish`
- `macro is bearish`
- `full risk-on`
- `full risk-off`

## Earnings Boundary

Do not treat earnings as the main content of this skill.

Broad earnings-week context can matter for `SPX / NDX` tone, but detailed earnings belong mainly in:

- `earnings-calendar`
- `Part 7: News And Catalysts`
