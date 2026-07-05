# タスク

## テーマ

GitHub Actions の Self-hosted Runner 待機時間を検知し、20分以上待機しているジョブを検出・通知する仕組みを設計する。

## 背景

Self-hosted Runner環境では、Runner不足、Runner offline、ラベル不一致、ARC/EKS側のスケール遅延などにより、Workflow Jobが長時間待機する可能性がある。

この状態を早期に検知し、運用担当者が原因を切り分けられるようにする。

## 成果物

- 監視方式の設計
- GitHub API利用方針
- EventBridge Scheduler + Lambda構成案
- Slack通知方針
- テスト観点
- Runbook
- Agent HarnessのMemory更新
- 監査ログ

## 完了条件

- 20分以上待機しているJobを検出する方式が明確である
- 検出対象・除外条件・通知条件が明確である
- エラー時のログ確認手順がRunbookに記載されている
- Codex Agentの作業状態がstate.jsonに記録されている
- 重要判断がdecisions.mdに記録されている
- policy_matrix.yamlに違反する操作を行っていない
