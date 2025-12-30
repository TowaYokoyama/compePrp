import heapq

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

INF = float('inf')
dist = [INF] * (N + 1)
dist[1] = 0
pq = [(0, 1)]

while pq:
    d, v = heapq.heappop(pq)
    if d > dist[v]:
        continue
    for nv, cost in graph[v]:
        if dist[v] + cost < dist[nv]:
            dist[nv] = dist[v] + cost
            heapq.heappush(pq, (dist[nv], nv))

print(dist[N] if dist[N] != INF else -1)
