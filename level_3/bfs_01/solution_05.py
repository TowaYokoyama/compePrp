from collections import deque

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append((b, 0))
    graph[b].append((a, 1))

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

print(dist[N] if dist[N] != INF else -1)
