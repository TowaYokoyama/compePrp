# 貰うDP：dp[i][j] を dp[i-1][j], dp[i-1][j-w] から貰う

N, C = map(int, input().split())
items = []
for _ in range(N):
    w, v = map(int, input().split())
    items.append((w, v))

dp = [[-1] * (C + 1) for _ in range(N + 1)]
dp[0][0] = 0

for i in range(1, N + 1):
    w, v = items[i - 1]
    for j in range(C + 1):
        # 選ばない
        if dp[i - 1][j] != -1:
            dp[i][j] = max(dp[i][j], dp[i - 1][j])
        # 選ぶ
        if j >= w and dp[i - 1][j - w] != -1:
            dp[i][j] = max(dp[i][j], dp[i - 1][j - w] + v)

print(max(dp[N]))
