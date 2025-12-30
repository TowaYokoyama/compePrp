# 順列・組合せ 問題4 メモ

- itertools.product で重複順列を生成
- repeat=N で N 個選ぶ
- K^N 個の組み合わせが生成される
- よくあるミス：combinations_with_replacement と間違える
- 計算量：O(K^N × N)
