# 順列・組合せ 問題2 メモ

- itertools.combinations で組み合わせを生成
- nCr 個の組み合わせが生成される
- 順序は考慮しない（{1,2} と {2,1} は同じ）
- よくあるミス：permutations と間違える
- 計算量：O(nCr × r)
