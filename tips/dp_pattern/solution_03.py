# 配るDP：dp[i][j] から dp[i+1][j], dp[i+1][j+w] に配る

N, C = map(int, input().split())
items = []
for _ in range(N):
    w, v = map(int, input().split())
    items.append((w, v))

dp = [[-1] * (C + 1) for _ in range(N + 1)]
dp[0][0] = 0

for i in range(N):
    w, v = items[i]
    for j in range(C + 1):
        if dp[i][j] == -1:
            continue
        # 選ばない
        dp[i + 1][j] = max(dp[i + 1][j], dp[i][j])
        # 選ぶ
        if j + w <= C:
            dp[i + 1][j + w] = max(dp[i + 1][j + w], dp[i][j] + v)

print(max(dp[N]))
