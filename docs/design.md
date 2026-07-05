# 設計書

## 目的

GitHub Actions の Self-hosted Runner で20分以上待機しているWorkflow Jobを検知し、運用担当者が初動調査できるようにする。

## 想定構成

```text
EventBridge Scheduler
  ↓
Lambda
  ↓
GitHub API
  ↓
queued job抽出
  ↓
20分以上待機判定
  ↓
Slack通知 / CloudWatch Logs
```

## 認証

GitHub APIの認証はGitHub Appを推奨する。
PATは個人依存・権限過多になりやすいため避ける。

## 権限制御

Codex Agentは `.agent/policy/policy_matrix.yaml` に従う。
本番環境変更、Terraform apply、Secret更新、main/masterへの直接pushは禁止または承認必須とする。

## 検出ロジック

- 対象: queued状態のWorkflow Job
- 閾値: queued開始から20分以上
- 除外: 明示的に除外設定されたRepository、Label、Workflow
- 通知: SlackまたはIssue作成。ただし外部通知は承認必須にできる設計とする。

## リスク

- GitHub API rate limit
- queued開始時刻の解釈誤り
- Runner label不一致による誤検知
- Slack通知失敗
- 権限過多
