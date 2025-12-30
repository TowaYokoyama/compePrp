N = int(input())
C = list(map(int, input().split()))

INF = float('inf')
dp = [INF] * N
dp[0] = C[0]

for i in range(N):
    if i + 1 < N:
        dp[i + 1] = min(dp[i + 1], dp[i] + C[i + 1])
    if i + 2 < N:
        dp[i + 2] = min(dp[i + 2], dp[i] + C[i + 2])

print(dp[N - 1])
