from collections import deque

N = int(input())
graph = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(start):
    dist = [-1] * (N + 1)
    dist[start] = 0
    q = deque([start])
    while q:
        v = q.popleft()
        for nv in graph[v]:
            if dist[nv] == -1:
                dist[nv] = dist[v] + 1
                q.append(nv)
    max_dist = 0
    farthest = start
    for i in range(1, N + 1):
        if dist[i] > max_dist:
            max_dist = dist[i]
            farthest = i
    return farthest, max_dist

u, _ = bfs(1)
_, diameter = bfs(u)
print(diameter)
