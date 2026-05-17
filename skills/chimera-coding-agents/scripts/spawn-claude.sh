#!/usr/bin/env bash
# Spawn Claude Code for a Chimera task
# Usage: ./spawn-claude.sh "task description" [workdir] [max_turns]

set -e

TASK="${1:?Usage: $0 <task> [workdir] [max_turns]}"
WORKDIR="${2:-/home/open-claw/openclawtrading}"
MAX_TURNS="${3:-15}"

cd "$WORKDIR"
echo "[$(date)] Starting Claude Code: $TASK"
claude -p "$TASK" \
    --allowedTools Read,Edit,Bash,Write,Notebook \
    --max-turns "$MAX_TURNS" \
    --model sonnet \
    2>&1
echo "[$(date)] Claude Code done"
