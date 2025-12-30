import sys
sys.setrecursionlimit(10**6)

N = int(input())
graph = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

LOG = 20
parent = [[-1] * (N + 1) for _ in range(LOG)]
depth = [0] * (N + 1)

def dfs(v, p, d):
    parent[0][v] = p
    depth[v] = d
    for nv in graph[v]:
        if nv != p:
            dfs(nv, v, d + 1)

dfs(1, -1, 0)

for k in range(1, LOG):
    for v in range(1, N + 1):
        if parent[k - 1][v] != -1:
            parent[k][v] = parent[k - 1][parent[k - 1][v]]

def lca(u, v):
    if depth[u] < depth[v]:
        u, v = v, u
    diff = depth[u] - depth[v]
    for k in range(LOG):
        if (diff >> k) & 1:
            u = parent[k][u]
    if u == v:
        return u
    for k in range(LOG - 1, -1, -1):
        if parent[k][u] != parent[k][v]:
            u = parent[k][u]
            v = parent[k][v]
    return parent[0][u]

Q = int(input())
for _ in range(Q):
    u, v = map(int, input().split())
    print(lca(u, v))
