# 全探索 問題2 メモ

- bin(bit).count('1') で選んだ要素数を数える
- 要素数がKのときだけ和を計算
- popcount は bit.bit_count() でも可（Python 3.10+）
- よくあるミス：要素数のチェックを忘れる
- 別解：itertools.combinations を使う
- 計算量：O(2^N × N)
