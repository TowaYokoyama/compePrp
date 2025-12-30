# 1次元配列で省メモリ：後ろから更新

N, C = map(int, input().split())
items = []
for _ in range(N):
    w, v = map(int, input().split())
    items.append((w, v))

dp = [0] * (C + 1)

for w, v in items:
    # 後ろから更新（同じ品物を複数回使わないため）
    for j in range(C, w - 1, -1):
        dp[j] = max(dp[j], dp[j - w] + v)

print(dp[C])
