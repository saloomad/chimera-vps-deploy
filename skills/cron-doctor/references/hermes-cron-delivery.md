# Hermes Agent Cron Delivery — Critical Pattern

**Symptom:** Cron fires, job completes `ok`, but user never sees results anywhere.

**Root cause:** Default `deliver: "local"` only saves to Hermes session storage. User is never notified.

## The Fix

When creating or updating ANY cron that should reach the user, ALWAYS set:

```json
"deliver": "origin,discord:GUILD_ID:CHANNEL_ID"
```

To find your Discord IDs:
1. Open `C:\Users\becke\.openclaw\openclaw.json`
2. Look at `channels.discord.guilds` — key is GUILD_ID, nested `channels` key is CHANNEL_ID

Current working config:
- GUILD: `1473437666262646836`
- CHANNEL: `1473437667197845588`

## Delivery Options

| Value | What it does |
|-------|-------------|
| `local` | Only Hermes session storage (default) — user sees nothing |
| `origin` | Reply back to the originating channel (Telegram/Slack/etc that triggered it) |
| `discord:GUILD:CHANNEL` | Push result to specific Discord channel |
| `origin,discord:...` | Both — recommended for all user-facing jobs |

## Discord Must Be Enabled

Check `C:\Users\becke\.openclaw\openclaw.json`:
```json
"channels": {
  "discord": {
    "enabled": true,   // must be true
    "token": "...",
    ...
  }
}
```

If `enabled: false`, set it to `true` and restart Hermes/OpenClaw.

## Anti-Pattern (what we had)

```json
"deliver": "local"  // WRONG — results vanish into storage
```

Always verify `last_delivery_error: null` after a cron run. A non-null value means delivery failed even if the job itself succeeded.
