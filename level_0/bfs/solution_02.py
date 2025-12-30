from collections import deque

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

dist = [-1] * (N + 1)
dist[1] = 0
q = deque([1])

while q:
    v = q.popleft()
    for nv in graph[v]:
        if dist[nv] == -1:
            dist[nv] = dist[v] + 1
            q.append(nv)

for i in range(1, N + 1):
    print(dist[i])
