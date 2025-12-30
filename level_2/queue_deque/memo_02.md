# キュー/deque応用 問題2 メモ

- deque.rotate(K) で右に K 回転
- 負の値で左回転
- K % N で無駄な回転を省く
- よくあるミス：回転方向を間違える
- 計算量：O(K) per rotate、または offset 管理で O(1)
