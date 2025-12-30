# Fenwick Tree 問題1 メモ

- BIT（Binary Indexed Tree）とも呼ばれる
- 1点加算・区間和を O(log N) で処理
- セグメント木より実装が簡単で定数倍が軽い
- よくあるミス：1-indexed を忘れる
- 計算量：更新 O(log N)、クエリ O(log N)
