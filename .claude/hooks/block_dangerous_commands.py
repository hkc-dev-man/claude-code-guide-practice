#!/usr/bin/env python3
import json
import re
import sys

_RM = (
    r"rm\s+-[^\s]*r[^\s]*\s+-[^\s]*f[^\s]*"
    r"|rm\s+-[^\s]*f[^\s]*\s+-[^\s]*r[^\s]*"
    r"|rm\s+-rf|rm\s+-fr"
)
_GIT_FORCE = (
    r"git\s+push\s+(--force|-f)\b"
    r"|git\s+push\s+[^\s]+\s+(--force|-f)\b"
)

DANGEROUS_PATTERNS = [
    (_RM, "rm -rf"),
    (r"drop\s+table", "DROP TABLE"),
    (_GIT_FORCE, "git push --force"),
]

data = json.load(sys.stdin)
command = data.get("tool_input", {}).get("command", "")

for pattern, label in DANGEROUS_PATTERNS:
    if re.search(pattern, command, re.IGNORECASE):
        reason = f"Blocked dangerous command: '{label}' detected in: {command!r}"
        print(json.dumps({
            "hookSpecificOutput": {
                "hookEventName": "PreToolUse",
                "permissionDecision": "deny",
                "permissionDecisionReason": reason,
            }
        }))
        sys.exit(0)
