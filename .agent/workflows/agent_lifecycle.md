# Agent Lifecycle

## 標準フロー

1. Planner: 目的、制約、完了条件、作業分解を整理
2. Architect: 設計方針、責務分割、権限、障害時挙動を決定
3. Executor: 実装・調査・修正を実行
4. Tester: 正常系・異常系・退行確認を行う
5. Reviewer: 設計・実装・テスト・運用性をレビュー
6. Documenter: 設計書、Runbook、Memoryを更新

## 停止条件

- `retry_count >= max_retry_count`
- `human_approval_required = true`
- `blockers` が空でない
- 本番変更や破壊的操作が必要

## 再開条件

- 人間が承認した
- ブロッカーが解消された
- `state.json.next_action` が明確である
