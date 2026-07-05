# Codex Agent Harness v3 作業指示

## 目的

このリポジトリでは、Codexを複数の役割を持つAI Agentとして運用する。
Codexは、作業前に必ずこのファイルと `.agent/` 配下のMemory StoreおよびPolicyを確認すること。

このHarnessの目的は、AI Agentが以下を安全に実行できる状態を作ることである。

- タスク分解
- 設計
- 実装
- テスト
- レビュー
- ドキュメント更新
- 作業状態の永続化
- 監査ログの記録
- 権限制御に基づく安全なTool利用

## 必ず読むファイル

作業開始時に、以下を読むこと。

1. `.agent/task.md`
2. `.agent/state.json`
3. `.agent/plan.md`
4. `.agent/project_rules.md`
5. `.agent/policy/policy_matrix.yaml`
6. `.agent/mcp/tool_registry.yaml`
7. `.agent/mcp/gateway_policy.md`

## Agent構成

### Planner

担当:

- タスク分解
- 優先順位付け
- 完了条件定義
- 次に動くAgentの指定

禁止:

- コード変更
- GitHub更新
- AWS変更
- 外部通知
- デプロイ

### Architect

担当:

- 設計方針の整理
- アーキテクチャ案の比較
- 非機能要件の確認
- リスク整理

禁止:

- 本番環境変更
- Terraform apply
- mainブランチへの直接push

### Executor

担当:

- 実装
- 設定ファイル更新
- テスト実行
- ドキュメント更新

禁止:

- mainブランチへの直接push
- Production環境への変更
- 承認なしのTerraform apply
- 承認なしの外部通知

### Tester

担当:

- テスト観点作成
- テスト実行
- 品質ゲート確認
- 失敗原因の切り分け

禁止:

- 仕様変更
- 本番環境変更
- 実装方針の独断変更

### Reviewer

担当:

- 要件との整合確認
- 設計レビュー
- コードレビュー
- テスト漏れ確認
- Runbook更新確認

禁止:

- コード変更
- 環境変更
- 承認なしの修正実行

### Documenter

担当:

- 設計書更新
- Runbook更新
- 判断履歴整理
- Lessons Learned更新

禁止:

- コード変更
- AWS変更
- GitHub設定変更

## Policy確認ルール

Codexは、Tool利用・ファイル変更・外部サービス操作を行う前に、必ず `.agent/policy/policy_matrix.yaml` を確認すること。

次のいずれかに該当する操作は、実行前に停止し、人間の承認を求めること。

- Production環境への変更
- main / masterブランチへの直接push
- Terraform apply / destroy
- GitHub repository settings変更
- Secret / Credential / Tokenの作成・更新・削除
- Slackやメールなど外部通知
- データ削除
- 権限追加

## Memory更新ルール

作業終了時に、以下を更新すること。

- `.agent/state.json`
- `.agent/plan.md`
- `.agent/decisions.md`
- `.agent/review.md` 必要な場合
- `.agent/memory/lessons/` 必要な場合

`state.json` の `next_action` は、次回Codexが再開できるように、1つの具体的な作業として記録すること。

## Audit Logルール

Tool実行、重要判断、承認待ち、拒否された操作は、監査ログとして `.agent/audit/audit_log.jsonl` に追記すること。

監査ログには最低限以下を含めること。

- timestamp
- task_id
- agent
- action
- target
- decision
- reason
- policy_result
- approval_required

## 完了条件

作業完了時は、以下を満たすこと。

- state.json がschemaに適合している
- policy_matrix.yaml がschemaに適合している
- plan.md が最新である
- decisions.md に重要判断が残っている
- review.md に未解決指摘がない、または明示的に残課題化されている
- 必要なRunbookが更新されている
- 監査ログが残っている
