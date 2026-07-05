# 判断履歴

## D001: MemoryとAudit Logを分離する

### 判断

Agentが次に作業するための状態はMemory Storeに、人間が後から検証するための証跡はAudit Logに記録する。

### 理由

Memoryと監査ログは目的が異なるため、同じファイルに混ぜると可読性と検証性が下がるため。

## D002: RBACとABACを併用する

### 判断

Agentの役割だけでなく、環境・ブランチ・リソース・操作種別で権限制御する。

### 理由

Executorであっても、dev環境のfeatureブランチ操作とproduction環境のTerraform applyではリスクが異なるため。
