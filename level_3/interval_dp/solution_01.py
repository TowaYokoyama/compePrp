N = int(input())
P = list(map(int, input().split()))

INF = float('inf')
dp = [[INF] * (N + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    dp[i][i] = 0

for length in range(2, N + 1):
    for i in range(1, N - length + 2):
        j = i + length - 1
        for k in range(i, j):
            cost = dp[i][k] + dp[k + 1][j] + P[i - 1] * P[k] * P[j]
            dp[i][j] = min(dp[i][j], cost)

print(dp[1][N])
