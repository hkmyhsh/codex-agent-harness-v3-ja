# Codex Agent Harness v3 利用手順

## 目的

Codexを単なるチャットAIではなく、Planner・Executor・Reviewerなどの役割を持つAI Agentとして利用し、作業状態・設計判断・レビュー履歴を自律的に管理させる。

---

# 初回セットアップ

## 1. Harnessをリポジトリへ配置する

以下を対象リポジトリへ配置する。

```
AGENTS.md

.agent/
docs/
scripts/
.github/
```

---

## 2. Project Rulesを編集する

以下を自プロジェクト向けに修正する。

```
.agent/project_rules.md
```

例

- コーディング規約
- ブランチ戦略
- テスト方法
- PRルール
- デプロイ方法

---

## 3. Tool Policyを設定する

以下をプロジェクトに合わせて修正する。

```
.agent/policy/policy_matrix.yaml
```

例

- PlannerはGitHub Readのみ
- ExecutorはDevelopブランチのみPush可能
- Production Deployは禁止

---

## 4. MCP Gatewayを設定する

利用するToolを登録する。

例

- GitHub
- AWS
- Slack
- Jira
- Browser

Tool Registry

```
.agent/mcp/tool_registry.yaml
```

に反映する。

---

# 作業開始

## 1. Userはtask.mdだけ更新する

例

```
# タスク

GitHub ActionsのRunner待機時間監視を追加してください。

完了条件

・20分以上待機ジョブを検知

・Slack通知

・Runbook更新

・テスト追加
```

plan.mdやstate.jsonは更新しない。

---

## 2. Codexへ依頼する

```
AGENTS.mdを読み、
task.mdを確認してください。

Plannerから作業を開始してください。

task.mdからplan.mdを生成し、
state.jsonを初期化してください。

作業終了までHarnessのルールに従ってください。
```

---

# Planner

Plannerは

- task.md
- project_rules.md

を読み、

以下を更新する。

```
plan.md

state.json
```

---

# Architect

Architectは

設計を検討し、

以下を更新する。

```
docs/design.md

decisions.md
```

---

# Executor

Executorは

実装を行い、

以下を更新する。

```
ソースコード

state.json
```

---

# Tester

Testerは

- Unit Test
- Integration Test

を実施し、

review.mdへ結果を記録する。

---

# Reviewer

Reviewerは

以下を確認する。

- 要件
- 設計
- 保守性
- テスト
- セキュリティ

問題があれば

```
review.md
```

へ追記する。

---

# Documenter

Documenterは

以下を更新する。

```
Runbook

README

設計書
```

---

# state.json

state.jsonは

Harnessの現在状態を表す。

Userは編集しない。

Planner・Executor・Reviewerが更新する。

例

```
planning

executing

testing

review_required

completed
```

---

# Memory

Memoryは

```
.agent/memory/
```

配下へ蓄積する。

例

```
project/

lessons/

architecture/

patterns/
```

再利用できる知識のみ保存する。

---

# Audit Log

Agentが行った判断は

```
audit/audit_log.jsonl
```

へ保存する。

例

- Tool実行
- 判断
- Retry
- Human Approval

---

# Human Approval

以下は必ず承認を要求する。

- Production Deploy
- mainブランチへのPush
- Terraform Apply
- IAM変更
- Secret更新

---

# 作業終了

Codexは以下を更新して終了する。

```
state.json

review.md

decisions.md

Runbook

README
```

最後に

```
status = completed
```

へ更新する。

---

# 次回作業

Userは

task.mdのみ更新する。

または

チャットで

```
昨日の続きからお願いします。
```

と依頼する。

Codexは

```
state.json
```

を読み、

前回の続きから作業を再開する。

---

# 運用ルール

Userが更新するもの

- task.md

Codexが更新するもの

- plan.md
- state.json
- decisions.md
- review.md
- docs/
- memory/

MCP Gatewayが制御するもの

- Tool実行権限

Humanが担当するもの

- 最終承認
- Pull Request承認
- Production反映