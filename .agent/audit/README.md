# Audit Log

Audit Logは、Codex Agentの作業証跡を残すための領域である。

Memory StoreはAgentが次に作業するための状態管理であり、Audit Logは人間が後から検証するための証跡である。
両者は目的が異なるため分離する。

## 記録対象

- Tool実行
- Tool実行拒否
- 重要判断
- 承認待ち
- 外部通知
- GitHub / AWS / Terraform / Slack操作

## 形式

`.agent/audit/audit_log.jsonl` に1行1JSONで追記する。
