---
name: pipeline-enforcement-detector
description: Detect when a workflow needs a stronger runtime owner such as Task Flow, Lobster, commands, or review gates.
compatibility: opencode
metadata:
  platform: opencode
  workflow: enforcement
---

Use this when the question is "what should reliably own this workflow?"

For OpenCode itself, prefer:

1. agents
2. commands
3. permissions
4. project rules
5. file-backed plans

If the real owner should be OpenClaw, say so and route to Task Flow, Lobster, hooks, or standing orders instead of keeping the pipeline in chat.
