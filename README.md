# Codex Agent Harness v3 日本語テンプレート

このテンプレートは、Codexを利用してAI Agentを案件内で安全に自律実行させるためのHarness雛形です。

v3では、v2の6 Agent構成とMemory Storeに加えて、以下を追加しています。

- Agent別RBAC
- 環境・リポジトリ・ブランチ・操作種別に基づくABAC
- Human Approval Gate
- MCP Gateway前提のTool Policy
- 監査ログスキーマ
- GitHub ActionsによるHarness品質ゲート
- Policy検証スクリプト
- MemoryとAudit Logの分離

## 使い方

対象リポジトリのルートに、このテンプレートのファイル群を配置します。

その後、Codexに次のように依頼します。

```text
AGENTS.md を読み、.agent/state.json と .agent/policy/ を確認してください。
Plannerとして、現在のタスクを分解し、.agent/plan.md と .agent/state.json を更新してください。
```

実行時は次のように依頼します。

```text
Executorとして、.agent/state.json の next_action を実行してください。
作業前に .agent/policy/policy_matrix.yaml を確認し、禁止操作や承認必須操作を実行しないでください。
作業後、state.json、decisions.md、auditログを更新してください。
```

レビュー時は次のように依頼します。

```text
Reviewerとして、差分・設計・テスト・Runbook・Memory更新内容をレビューしてください。
指摘は .agent/review.md に記録し、必要に応じて state.json を review_required にしてください。
```

## v3の設計思想

Codexに対して「やってよいこと」を自然言語だけで伝えるのではなく、次の4層で制御します。

1. `AGENTS.md`: Codexが読む役割・作業ルール
2. `.agent/policy/`: Agent別・環境別・リソース別の制御ポリシー
3. `MCP Gateway`: 実際のTool実行を制御する境界
4. `Human Approval`: 本番・破壊的操作・外部通知などの承認ゲート

重要なのは、MCP Gatewayだけに依存しないことです。Codex側にも禁止事項を明示し、さらにMCP Gateway側で実行を拒否できる構成にします。

## 全体像

┌──────────────────────────────┐
│            User              │
└──────────────┬───────────────┘
               │ 依頼
               v
┌──────────────────────────────┐
│            Codex             │
│ AGENTS.md / prompts を読む.   │
└──────────────┬───────────────┘
               │ 現在状態を読む
               v
┌──────────────────────────────┐
│         .agent/state.json    │
│ 現在Agent / 状態 / 次アクション   │
└──────────────┬───────────────┘
               │ 計画・実行判断
               v
┌──────────────────────────────┐
│        Agent Prompts         │
│ Planner / Executor / Reviewer│
└──────────────┬───────────────┘
               │ Tool実行前に確認
               v
┌──────────────────────────────┐
│      policy_matrix.yaml      │
│ Agent×環境×操作×承認要否         │
└──────────────┬───────────────┘
               │ 許可された場合のみ
               v
┌──────────────────────────────┐
│          MCP Gateway         │
│ Tool実行を実際に許可/拒否         │
└──────────────┬───────────────┘
               │
       ┌───────┼────────┐
       v       v        v
   GitHub     AWS      Slack

## ディレクトリ構成

```text
AGENTS.md
README.md
.agent/
  state.json
  state.schema.json
  plan.md
  decisions.md
  review.md
  task.md
  project_rules.md
  prompts/
  policy/
    policy_matrix.yaml
    policy_schema.json
    agents/
    environments/
    resources/
    approval/
  mcp/
    gateway_policy.md
    tool_policy.md
    tool_registry.yaml
  audit/
    README.md
    audit_log.jsonl
    schemas/
  memory/
    README.md
    short_term/
    project/
    org/
    lessons/
    knowledge_graph/
.github/workflows/
  agent-harness-check.yml
scripts/
  validate_state.py
  validate_policy.py
  append_audit_log.py
docs/
  design.md
  runbook.md
examples/
  github-actions-runner-wait/
```

## 注意

このテンプレートは、Codexの行動を支援するための設計資料と検証補助です。実際の強制力は、MCP Gateway、GitHub権限、AWS IAM、Branch Protection、Human Approvalなどの外部制御と組み合わせて成立します。
