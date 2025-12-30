from collections import deque

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

INF = float('inf')
dist = [INF] * (N + 1)
dist[1] = 0
dq = deque([1])

while dq:
    v = dq.popleft()
    for nv, cost in graph[v]:
        if dist[v] + cost < dist[nv]:
            dist[nv] = dist[v] + cost
            if cost == 0:
                dq.appendleft(nv)
            else:
                dq.append(nv)

for i in range(1, N + 1):
    print(dist[i] if dist[i] != INF else "INF")
