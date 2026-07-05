# 作業計画

## フェーズ1: Planner

- 要件を分解する
- 完了条件を明確化する
- 次にArchitectが確認すべき設計論点を整理する

## フェーズ2: Architect

- GitHub APIによる待機Job検出方式を検討する
- EventBridge Scheduler + Lambda構成を設計する
- Slack通知と監査ログの責務を分ける
- セキュリティ・権限・失敗時挙動を整理する

## フェーズ3: Executor

- 必要なサンプルコード・設定・ドキュメントを作成する
- state.jsonとdecisions.mdを更新する
- policyに反する操作を実行しない

## フェーズ4: Tester

- 20分以上待機
- 20分未満待機
- Runner offline
- ラベル不一致
- GitHub API rate limit
- Slack通知失敗

を観点としてテストする。

## フェーズ5: Reviewer

- 要件との整合
- 誤検知・検知漏れ
- 運用時の初動容易性
- 権限過多
- Runbook不足

を確認する。

## フェーズ6: Documenter

- 設計書
- Runbook
- 判断履歴
- Lessons Learned

を更新する。
