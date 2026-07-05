#!/usr/bin/env python3
"""Append one audit log entry for Codex Agent Harness v3."""
from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--task-id", required=True)
    parser.add_argument("--agent", required=True)
    parser.add_argument("--action", required=True)
    parser.add_argument("--target", required=True)
    parser.add_argument("--decision", required=True, choices=["allow", "deny", "require_approval", "record_only"])
    parser.add_argument("--reason", required=True)
    parser.add_argument("--policy-result", default="not_checked")
    parser.add_argument("--approval-required", action="store_true")
    parser.add_argument("--tool-name")
    parser.add_argument("--risk-level", default="low", choices=["low", "medium", "high", "critical"])
    parser.add_argument("--log-path", default=".agent/audit/audit_log.jsonl")
    args = parser.parse_args()

    entry = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "task_id": args.task_id,
        "agent": args.agent,
        "action": args.action,
        "target": args.target,
        "decision": args.decision,
        "reason": args.reason,
        "policy_result": args.policy_result,
        "approval_required": args.approval_required,
        "tool_name": args.tool_name,
        "risk_level": args.risk_level,
    }

    log_path = Path(args.log_path)
    log_path.parent.mkdir(parents=True, exist_ok=True)
    with log_path.open("a", encoding="utf-8") as f:
        f.write(json.dumps(entry, ensure_ascii=False) + "\n")

    print(f"audit log appended: {log_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
