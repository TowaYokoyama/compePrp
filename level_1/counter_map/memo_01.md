# Counter/Map活用 問題1 メモ

- Counter で各値の出現回数を数える
- most_common() で頻度順に取得可能
- 最小値を求めるなら条件付きで min を取る
- よくあるミス：most_common(1)[0][0] だと最小が取れない
- 計算量：O(N)
