# ダイクストラ法 問題5 メモ

- count[v] = 頂点vへの最短経路の本数
- 距離が更新されたら count[nv] = count[v]
- 距離が同じなら count[nv] += count[v]
- よくあるミス：MOD を取り忘れる
- 計算量：O((N + M) log N)
