# 順列・組合せ 問題1 メモ

- itertools.permutations で順列を生成
- 辞書順で生成される
- N! 個の順列が生成される
- よくあるミス：N が大きいと TLE/MLE
- 計算量：O(N! × N)
