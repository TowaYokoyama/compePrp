N = int(input())
C = [list(map(int, input().split())) for _ in range(N)]

INF = float('inf')
dp = [[INF] * N for _ in range(1 << N)]
dp[1][0] = 0

for S in range(1 << N):
    for v in range(N):
        if dp[S][v] == INF:
            continue
        for u in range(N):
            if S & (1 << u):
                continue
            new_S = S | (1 << u)
            dp[new_S][u] = min(dp[new_S][u], dp[S][v] + C[v][u])

ans = INF
for v in range(N):
    ans = min(ans, dp[(1 << N) - 1][v] + C[v][0])

print(ans)
