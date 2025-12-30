from collections import deque

MOD = 10**9 + 7

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
indegree = [0] * (N + 1)

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

q = deque()
for i in range(1, N + 1):
    if indegree[i] == 0:
        q.append(i)

order = []
while q:
    v = q.popleft()
    order.append(v)
    for nv in graph[v]:
        indegree[nv] -= 1
        if indegree[nv] == 0:
            q.append(nv)

dp = [0] * (N + 1)
dp[1] = 1
for v in order:
    for nv in graph[v]:
        dp[nv] = (dp[nv] + dp[v]) % MOD

print(dp[N])
