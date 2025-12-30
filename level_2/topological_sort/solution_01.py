import heapq

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
indegree = [0] * (N + 1)

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

heap = []
for i in range(1, N + 1):
    if indegree[i] == 0:
        heapq.heappush(heap, i)

result = []
while heap:
    v = heapq.heappop(heap)
    result.append(v)
    for nv in graph[v]:
        indegree[nv] -= 1
        if indegree[nv] == 0:
            heapq.heappush(heap, nv)

print(*result)
