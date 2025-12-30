# キュー/deque応用 問題3 メモ

- deque は両端の追加・削除が O(1)
- appendleft, append, popleft, pop を使い分ける
- list だと先頭操作が O(N) なので deque を使う
- よくあるミス：list で実装して TLE
- 計算量：O(Q)
