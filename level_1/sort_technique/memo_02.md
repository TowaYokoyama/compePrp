# ソート＋工夫 問題2 メモ

- 降順ソートして K-1 番目（0-indexed）を取る
- 昇順なら A[N-K] でも可
- heapq.nlargest(K, A)[-1] でも求まる
- よくあるミス：1-indexed と 0-indexed の変換ミス
- 計算量：O(N log N)
