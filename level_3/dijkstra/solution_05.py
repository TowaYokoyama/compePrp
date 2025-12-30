import heapq

MOD = 10**9 + 7

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

INF = float('inf')
dist = [INF] * (N + 1)
count = [0] * (N + 1)
dist[1] = 0
count[1] = 1
pq = [(0, 1)]

while pq:
    d, v = heapq.heappop(pq)
    if d > dist[v]:
        continue
    for nv, cost in graph[v]:
        if dist[v] + cost < dist[nv]:
            dist[nv] = dist[v] + cost
            count[nv] = count[v]
            heapq.heappush(pq, (dist[nv], nv))
        elif dist[v] + cost == dist[nv]:
            count[nv] = (count[nv] + count[v]) % MOD

print(count[N])
