# Counter/Map活用 問題3 メモ

- Counter 同士は == で比較可能
- ソートして比較でも可：sorted(S) == sorted(T)
- Counter の方が O(N) で高速
- よくあるミス：長さチェックを忘れる（Counter比較なら不要）
- 計算量：O(N)
