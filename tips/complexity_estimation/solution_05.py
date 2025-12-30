# N ≤ 2 × 10^5 → O(N^2) は TLE、O(N log N) または O(N) が必要

from collections import Counter

N, K = map(int, input().split())
A = list(map(int, input().split()))

cnt = Counter(A)
count = 0

for a in A:
    target = K - a
    if target in cnt:
        count += cnt[target]
        if target == a:
            count -= 1  # 自分自身を除く

print(count // 2)  # 各ペアを2回数えているので2で割る
# O(N)
