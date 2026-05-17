# Model Shift Guide

Reference for usage-monitor skill. Defines thresholds, shift triggers, and routing logic.

## Quota Thresholds

| Level   | Range   | Badge | Action              |
|---------|---------|-------|---------------------|
| OK      | < 60%   | `[ ]` | Use freely          |
| Caution | 60–84%  | `[!]` | Pace usage          |
| Critical| ≥ 85%   | `[!!]`| Shift or pause      |
| Maxed   | 100%    | `[X]` | Hard stop, wait     |

## Active Models in This Workspace

| Model              | Provider  | Used via                | Quota type         |
|--------------------|-----------|-------------------------|--------------------|
| kimi-for-coding    | Kimi/Moonshot | Claude Code (ANTHROPIC_BASE_URL) | Session + Weekly (claude.ai) |
| MiniMax-M*         | MiniMax   | mmx CLI / API           | Interval (4500/window) |
| speech-hd          | MiniMax   | mmx speech              | Interval + Weekly  |
| music-2.6          | MiniMax   | mmx music               | Interval + Weekly  |
| image-01           | MiniMax   | mmx image               | Interval + Weekly  |
| MiniMax-Hailuo-2.3 | MiniMax   | mmx video               | Unlimited (no cap) |

## Shift Decision Matrix

### Claude Code / Kimi session

| Session % | Weekly % | Recommendation                                              |
|-----------|----------|-------------------------------------------------------------|
| < 60%     | < 60%    | Use freely, full agentic tasks OK                           |
| 60–80%    | any      | Avoid large file reads, prefer targeted edits               |
| > 80%     | < 75%    | Wait for session reset OR batch remaining tasks efficiently  |
| > 80%     | > 75%    | Prioritize only high-value tasks, let session reset          |
| any       | > 85%    | Switch to lighter prompts; preserve Projects context        |

**To switch Claude Code model**: edit `~/.claude/settings.json` → `"model"` key.
Available on Kimi: `kimi-for-coding` (default, Kimi-k2.6, 262k context).

### MiniMax Text (MiniMax-M*)

| Text % | Resets in | Recommendation                               |
|--------|-----------|----------------------------------------------|
| < 80%  | any       | Use freely for mmx text chat tasks           |
| 80–95% | > 2h      | Finish current batch, avoid new heavy tasks  |
| > 95%  | > 1h      | Stop mmx text usage, wait for reset          |
| 100%   | any       | Hard blocked — use kimi/claude.ai instead    |

### MiniMax Speech (speech-hd)

| Weekly % | Action                                              |
|----------|-----------------------------------------------------|
| < 80%    | OK                                                  |
| 80–95%   | Reserve for priority TTS only                       |
| > 95%    | Stop speech generation; use speech-2.6 if available |
| 100%     | Interval maxed — wait for reset (check remains_time)|

### MiniMax Music / Image / Lyrics

These share 100/interval and 700/weekly quotas. They max out quickly.

- When any is at 100%: stop ALL new music/image/lyrics generation
- MiniMax video (Hailuo-2.3) is **unlimited** — route media tasks there when possible

## Model Routing by Task

| Task                     | First choice        | If quota critical     |
|--------------------------|---------------------|-----------------------|
| Coding / architecture    | kimi-for-coding     | Wait for session reset|
| Long context reading     | kimi-for-coding     | Chunk the input       |
| Text generation (long)   | kimi-for-coding     | MiniMax-M* (if ok)    |
| Quick text tasks         | MiniMax-M*          | kimi-for-coding       |
| Speech / TTS             | speech-hd           | Wait for reset        |
| Music generation         | music-2.6           | Wait (weekly resets)  |
| Image generation         | image-01            | Wait (interval resets)|
| Video generation         | MiniMax-Hailuo-2.3  | Always available      |

## Reset Schedule Reference

MiniMax intervals are typically 5-hour windows. Weekly resets on the billing cycle.
Claude.ai sessions are ~5-hour rolling windows. Weekly resets Monday 5:00 AM local.

## Efficiency Tips

1. **Batch sessions**: Start one Claude Code session for related tasks rather than many short ones — each new session uses coding-plan-vlm and coding-plan-search quota on init.
2. **Use Projects**: Claude remembers project context — avoids re-reading files and saves session tokens.
3. **Video is free**: Route any media generation to MiniMax-Hailuo-2.3 — no quota cap observed.
4. **MiniMax text resets every ~5h**: Plan heavy mmx CLI workflows around reset windows.
5. **Design quota is separate**: Claude Design (50%) has its own weekly budget — using it doesn't affect All Models %.
