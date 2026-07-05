#!/usr/bin/env python3
"""Validate .agent/state.json for Codex Agent Harness v3."""
from __future__ import annotations

import json
import sys
from pathlib import Path

try:
    from jsonschema import Draft202012Validator
except ImportError as exc:  # pragma: no cover
    print("jsonschema is required. Install with: pip install jsonschema", file=sys.stderr)
    raise SystemExit(2) from exc


def main() -> int:
    state_path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(".agent/state.json")
    schema_path = Path(sys.argv[2]) if len(sys.argv) > 2 else Path(".agent/state.schema.json")

    state = json.loads(state_path.read_text(encoding="utf-8"))
    schema = json.loads(schema_path.read_text(encoding="utf-8"))

    validator = Draft202012Validator(schema)
    errors = sorted(validator.iter_errors(state), key=lambda e: e.path)
    if errors:
        print("state.json validation failed:", file=sys.stderr)
        for error in errors:
            location = ".".join(str(p) for p in error.path) or "<root>"
            print(f"- {location}: {error.message}", file=sys.stderr)
        return 1

    if state["retry_count"] > state["max_retry"]:
        print("retry_count exceeds max_retry", file=sys.stderr)
        return 1

    print(f"state.json validation passed: {state_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
