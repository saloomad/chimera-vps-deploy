#!/usr/bin/env bash
# Usage: spawn-claude.sh "task" [model] [workdir] [max_turns]
# Models: k2.6 (Kimi default), MiniMax-M2.7-highspeed (MiniMax)

set -e
TASK="${1:?Usage: $0 <task> [model] [workdir] [max_turns]}"
MODEL="${2:-k2.6}"
WORKDIR="${3:-/home/open-claw/openclawtrading}"
MAX_TURNS="${4:-15}"
CONFIG="/home/open-claw/.hermes/config.yaml"

KEY=$(python3 -c "import yaml;d=yaml.safe_load(open('$CONFIG'));print(d.get('model',{}).get('api_key',''))")

cd "$WORKDIR"
export ANTHROPIC_API_KEY="$KEY"
export ANTHROPIC_BASE_URL="https://api.minimax.chat/v1"

claude -p "$TASK" --model "$MODEL" --allowedTools Read,Edit,Bash,Write,Notebook --max-turns "$MAX_TURNS" 2>&1
