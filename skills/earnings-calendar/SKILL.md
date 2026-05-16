---
name: earnings-calendar
description: Check direct earnings dates and earnings-sensitive event risk for Chimera. Use when earnings matter to the current setup or when broad tech earnings can affect SPX, NDX, or crypto risk sentiment.
---

# Earnings Calendar

## Current Chimera Truth

This is mainly a `Section 7: News And Catalysts` skill.

It can also provide helper context to `Section 6` when a broad earnings week is materially affecting:

- `SPX`
- `NDX`
- tech-risk sentiment
- crypto setups that are behaving like risk assets

## Best Current Source Order

1. direct earnings lookup:
   - `mcp__market_data__.tradfi_news` with `action=earnings`
2. fresh `EARNINGS_CALENDAR.json` only when it actually exists and is current

Do not default to stale local earnings files.

## What This Skill Should Answer

- when the next relevant earnings event is
- whether that earnings event matters to the setup
- whether it is symbol-specific or broad market context

## Main Boundary

### Keep mainly in Section 7

- detailed earnings-event interpretation
- earnings as active catalyst flow
- stock or proxy-name event risk

### Use only as helper context in Section 6

- broad earnings-week pressure on `SPX / NDX`
- big-tech earnings when they materially affect crypto risk sentiment

## Practical Rule For Deezoh

For crypto:
- earnings are usually helper context, not the main macro owner

For stocks or index-sensitive setups:
- earnings can be a real catalyst lane
