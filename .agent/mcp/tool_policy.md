# MCP / Tool権限制御ポリシー

## 基本方針

MCP Gatewayを通じてToolを公開する場合、Agentごとに利用可能なToolを制限する。

## Agent別Tool許可例

| Agent | 許可Tool | 禁止または承認必須Tool |
|---|---|---|
| Planner | read-only file, issue search | deploy, write secret |
| Architect | read-only file, docs, diagram | production change |
| Executor | repository write, test, local command | production apply |
| Tester | test command, CI read | secret read/write |
| Reviewer | diff read, static analysis | destructive command |
| Documenter | docs write | deploy |

## 承認必須操作

- 本番環境変更
- Secret操作
- Terraform apply / destroy
- GitHub branch protection変更
- Organization / Enterprise設定変更
- Slackなど外部通知の大量送信

## 監査ログ記録項目

- 日時
- Agent名
- Tool名
- 実行目的
- 入力の要約
- 出力の要約
- 成否
- 承認者
- 関連するDecision ID
