import sys
sys.setrecursionlimit(10**6)

N = int(input())
graph = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

def dfs(start):
    dist = [-1] * (N + 1)
    dist[start] = 0
    
    def rec(v):
        for nv, cost in graph[v]:
            if dist[nv] == -1:
                dist[nv] = dist[v] + cost
                rec(nv)
    
    rec(start)
    max_dist = 0
    farthest = start
    for i in range(1, N + 1):
        if dist[i] > max_dist:
            max_dist = dist[i]
            farthest = i
    return farthest, max_dist

u, _ = dfs(1)
_, diameter = dfs(u)
print(diameter)
