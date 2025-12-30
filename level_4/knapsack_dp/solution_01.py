N, C = map(int, input().split())
items = []
for _ in range(N):
    w, v = map(int, input().split())
    items.append((w, v))

dp = [0] * (C + 1)

for w, v in items:
    for j in range(C, w - 1, -1):
        dp[j] = max(dp[j], dp[j - w] + v)

print(dp[C])
