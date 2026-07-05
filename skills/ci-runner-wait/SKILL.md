# Skill: CI Runner Wait Detection

## 目的

GitHub Actions self-hosted runnerの待機時間監視を設計・実装・レビューする。

## 手順

1. 対象RepositoryとWorkflow範囲を確認する
2. queued jobの取得方法を確認する
3. 20分閾値で検知する
4. 通知済み重複を抑制する
5. Slack通知文面を作る
6. Runbookへ反映する

## 注意

- GitHub App認証を優先する
- SecretをログやMemoryに残さない
- Rate Limitを考慮する
