#!/usr/bin/env python3
"""Codex Agent Harness v3 policy validator.

YAMLの厳密な完全検証ではなく、CIで早期に構造ミスを検知するための軽量検証。
PyYAMLが利用可能な場合はYAMLとして読み、ない場合は失敗する。
"""
from __future__ import annotations

import sys
from pathlib import Path

try:
    import yaml
except ImportError as exc:  # pragma: no cover
    print("PyYAML is required. Install with: pip install pyyaml", file=sys.stderr)
    raise SystemExit(2) from exc

REQUIRED_TOP_LEVEL = {"version", "policy_name", "defaults", "rules"}
REQUIRED_RULE_FIELDS = {"id", "description", "effect", "agents", "action_types", "resources"}
VALID_EFFECTS = {"allow", "deny"}


def validate(policy_path: Path) -> list[str]:
    errors: list[str] = []
    data = yaml.safe_load(policy_path.read_text(encoding="utf-8"))

    if not isinstance(data, dict):
        return ["policy file must be a mapping"]

    missing = REQUIRED_TOP_LEVEL - data.keys()
    if missing:
        errors.append(f"missing top-level keys: {sorted(missing)}")

    rules = data.get("rules")
    if not isinstance(rules, list) or not rules:
        errors.append("rules must be a non-empty list")
        return errors

    seen_ids: set[str] = set()
    for i, rule in enumerate(rules):
        if not isinstance(rule, dict):
            errors.append(f"rules[{i}] must be a mapping")
            continue

        missing_rule = REQUIRED_RULE_FIELDS - rule.keys()
        if missing_rule:
            errors.append(f"rules[{i}] missing keys: {sorted(missing_rule)}")

        rule_id = rule.get("id")
        if rule_id in seen_ids:
            errors.append(f"duplicate rule id: {rule_id}")
        if isinstance(rule_id, str):
            seen_ids.add(rule_id)

        if rule.get("effect") not in VALID_EFFECTS:
            errors.append(f"rules[{i}] invalid effect: {rule.get('effect')}")

        for list_key in ["agents", "action_types", "resources"]:
            if not isinstance(rule.get(list_key), list) or not rule.get(list_key):
                errors.append(f"rules[{i}].{list_key} must be a non-empty list")

    return errors


def main() -> int:
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(".agent/policy/policy_matrix.yaml")
    errors = validate(path)
    if errors:
        print("Policy validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1
    print(f"Policy validation passed: {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
