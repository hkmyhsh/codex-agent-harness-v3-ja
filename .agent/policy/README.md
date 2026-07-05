# Policy設計

このディレクトリは、Codex Agent Harness v3の権限制御ポリシーを管理する。

## RBACとABAC

- RBAC: Planner、Executor、ReviewerなどAgentの役割で制御する。
- ABAC: environment、branch、resource、action_typeなどの属性で制御する。

v3では両方を併用する。

## 重要な原則

- 未定義操作はdenyとする。
- production変更はCodex単独で行わない。
- main/masterへの直接pushは禁止する。
- Terraform apply/destroyは承認なしに実行しない。
- SecretやCredentialはCodexに直接扱わせない。

## MCP Gatewayとの関係

このポリシーは、Codexが事前に読むための設計上の制約である。
実際の強制はMCP Gateway、GitHub権限、AWS IAM、Branch Protectionで行う。
