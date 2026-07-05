# Memory Store

Memory Storeは、Codex Agentが次回作業を再開するための状態・知識を保存する領域である。

## 分類

```text
short_term/      今回タスクの短期状態
project/         プロジェクト固有ルール・用語・設計前提
org/             組織標準・レビュー方針・共通制約
lessons/         作業から得た教訓
knowledge_graph/ エンティティ・関係・依存の簡易表現
```

## Audit Logとの違い

- Memory Store: Agentが次に作業するための情報
- Audit Log: 人間が後から検証するための証跡

判断・失敗・Tool拒否などはAudit Logにも残す。
