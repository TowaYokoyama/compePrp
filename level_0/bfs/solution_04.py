from collections import deque

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

color = [-1] * (N + 1)

def bfs(start):
    q = deque([start])
    color[start] = 0
    while q:
        v = q.popleft()
        for nv in graph[v]:
            if color[nv] == -1:
                color[nv] = 1 - color[v]
                q.append(nv)
            elif color[nv] == color[v]:
                return False
    return True

is_bipartite = True
for i in range(1, N + 1):
    if color[i] == -1:
        if not bfs(i):
            is_bipartite = False
            break

print("Yes" if is_bipartite else "No")
