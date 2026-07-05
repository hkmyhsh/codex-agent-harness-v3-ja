# MCP Gateway Policy

## 役割

MCP Gatewayは、Codex Agentと外部Toolの間に置く実行境界である。

Codexに自然言語で禁止事項を書くだけでは、誤実行・迂回・過剰権限のリスクが残る。
そのため、MCP Gateway側でもTool単位・操作単位・対象リソース単位で実行可否を判定する。

## 基本方針

- Codexに与えるToolは最小権限にする。
- Agentごとに利用可能Toolを分離する。
- production変更はHuman Approvalを必須にする。
- Secret値はCodexに返さない。
- 書き込み操作はすべて監査ログに記録する。
- denyされた操作も監査ログに記録する。

## 判定に使う属性

- agent
- environment
- repository
- branch
- action_type
- resource
- approval_status
- risk_level

## 判定例

### 許可

```yaml
agent: Executor
environment: dev
branch: feature/runner-wait-monitor
action_type: run_test
resource: repository
```

### 承認必須

```yaml
agent: Executor
environment: staging
branch: develop
action_type: git_push
resource: repository
```

### 拒否

```yaml
agent: Executor
environment: production
action_type: terraform_apply
resource: terraform
```

## Codexへの期待

CodexはMCP Gatewayで拒否される操作を試行してはならない。
実行前に `.agent/policy/policy_matrix.yaml` を確認し、拒否または承認必須の操作は停止すること。
