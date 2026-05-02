# Historical Market Context Modes

## `bundle`

Best for one decision checkpoint.

Use when you want:
- what did the market look like here
- what would Deezoh have seen here
- what did the indicators say here

## `range`

Best for checkpoint sequences.

Use when you want:
- replay over a time window
- multiple decision points
- setup development across timeframes

## Optional Context Flags

### `--include-derivatives`

Adds Coinalyze history if a key is available.

Good for:
- OI up / price down
- funding context
- liquidation spikes
- long/short crowding

### `--include-news`

Adds recent historical news from GDELT.

Good for:
- event-driven setups
- catalysts
- recent macro or war headlines

Limit:
- recent rolling history only, not deep years

### `--include-economic`

Adds economic calendar context only when a truthful archived snapshot exists near the anchor time.

Good for:
- FOMC / CPI / NFP windows
- checking if a setup happened near a macro event

Limit:
- do not treat a current calendar file as deep historical truth
