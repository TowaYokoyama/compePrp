# 基本DP 問題3 メモ

- dp[i] = 長さ i+1 の増加部分列の末尾の最小値
- 二分探索で「a を入れる位置」を探す
- dp は常にソート済みになる
- よくあるミス：bisect_left と bisect_right の使い分け（狭義なら left）
- 別解：O(N^2) の素朴なDP（dp[i] = A[i]で終わるLISの長さ）
- 計算量：O(N log N)
