import heapq

def dijkstra(start, graph, N):
    INF = float('inf')
    dist = [INF] * (N + 1)
    dist[start] = 0
    pq = [(0, start)]
    while pq:
        d, v = heapq.heappop(pq)
        if d > dist[v]:
            continue
        for nv, cost in graph[v]:
            if dist[v] + cost < dist[nv]:
                dist[nv] = dist[v] + cost
                heapq.heappush(pq, (dist[nv], nv))
    return dist

N, M, K = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

dist1 = dijkstra(1, graph, N)
distK = dijkstra(K, graph, N)

INF = float('inf')
ans = dist1[K] + distK[N]
print(ans if ans < INF else -1)
