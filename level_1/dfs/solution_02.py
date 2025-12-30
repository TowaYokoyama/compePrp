import sys
sys.setrecursionlimit(10**6)

N = int(input())
graph = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

subtree_size = [0] * (N + 1)

def dfs(v, parent):
    subtree_size[v] = 1
    for nv in graph[v]:
        if nv != parent:
            dfs(nv, v)
            subtree_size[v] += subtree_size[nv]

dfs(1, -1)

for i in range(1, N + 1):
    print(subtree_size[i])
