#!/usr/bin/env bash
set -e
TASK="${1:?Usage: $0 <task> [workdir] [max_turns]}"
WORKDIR="${2:-/home/open-claw/openclawtrading}"
MAX_TURNS="${3:-15}"
cd "$WORKDIR"
claude -p "$TASK" --allowedTools Read,Edit,Bash,Write,Notebook --max-turns "$MAX_TURNS" --model MiniMax-M2.7-highspeed 2>&1
