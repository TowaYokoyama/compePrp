# 二分探索 問題2 メモ

- bisect_left(A, X) で「X以上の最小インデックス」を取得
- idx < N なら A[idx] が答え
- 「X以下の最大」なら bisect_right(A, X) - 1 を使う
- よくあるミス：idx == N のとき A[idx] にアクセスして IndexError
- 計算量：O(N + Q log N)
