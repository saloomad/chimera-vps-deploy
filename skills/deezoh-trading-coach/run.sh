#!/usr/bin/env bash
set -euo pipefail

SKILL_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
INPUT="${*:-}"
MODEL="${OPENCODE_MODEL:-opencode/minimax-m2.5-free}"

if [ -z "$INPUT" ]; then
  echo "Usage: $0 \"trading question\"" >&2
  exit 2
fi

python3 - "$SKILL_DIR/prompt.md" "$INPUT" <<'PY' | opencode run -m "$MODEL"
import pathlib
import sys

prompt = pathlib.Path(sys.argv[1]).read_text(encoding="utf-8")
print(prompt.replace("{{INPUT}}", sys.argv[2]))
PY
