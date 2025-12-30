import sys
sys.setrecursionlimit(10**6)

N = int(input())
W = [0] + list(map(int, input().split()))
graph = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

dp = [[0, 0] for _ in range(N + 1)]

def dfs(v, parent):
    dp[v][1] = W[v]
    for nv in graph[v]:
        if nv != parent:
            dfs(nv, v)
            dp[v][0] += max(dp[nv][0], dp[nv][1])
            dp[v][1] += dp[nv][0]

dfs(1, -1)
print(max(dp[1][0], dp[1][1]))
