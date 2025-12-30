N, X = map(int, input().split())
C = list(map(int, input().split()))

INF = float('inf')
dp = [INF] * (X + 1)
dp[0] = 0

for c in C:
    for j in range(c, X + 1):
        if dp[j - c] != INF:
            dp[j] = min(dp[j], dp[j - c] + 1)

print(dp[X] if dp[X] != INF else -1)
