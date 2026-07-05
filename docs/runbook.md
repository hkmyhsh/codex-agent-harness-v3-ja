# Runbook: Self-hosted Runner待機時間監視

## 検知内容

20分以上queued状態のGitHub Actions Jobを検知する。

## 初動確認

1. 通知されたRepository、Workflow、Job名を確認する。
2. Jobに指定されているruns-on labelを確認する。
3. 対応するSelf-hosted Runnerがonlineか確認する。
4. ARC/EKSを利用している場合、Runner Podの起動状況を確認する。
5. GitHub API rate limitまたは認証エラーがないかCloudWatch Logsを確認する。

## 代表原因

- Runner不足
- Runner offline
- Label不一致
- ARCのスケール遅延
- Kubernetes Node不足
- GitHub API障害
- Repository側のWorkflow設定ミス

## エスカレーション

以下の場合は運用担当者へエスカレーションする。

- 複数Repositoryで同時多発している
- 30分以上継続している
- Production releaseに影響している
- Runner基盤側の障害が疑われる

## 復旧後確認

- queued Jobが解消していること
- Runnerがonlineであること
- 再発防止メモを `.agent/memory/lessons/` に残すこと
- 必要に応じてRunbookを更新すること
