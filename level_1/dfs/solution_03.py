import sys
sys.setrecursionlimit(10**6)

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)

visited = [False] * (N + 1)
count = 0

def dfs(v):
    global count
    if v == N:
        count += 1
        return
    visited[v] = True
    for nv in graph[v]:
        if not visited[nv]:
            dfs(nv)
    visited[v] = False

dfs(1)
print(count)
