from collections import deque

N, M, K = map(int, input().split())
graph = [[] for _ in range(N + 1)]
rev_graph = [[] for _ in range(N + 1)]
indegree = [0] * (N + 1)

for _ in range(M):
    a, b = map(int, input().split())
    graph[b].append(a)
    rev_graph[a].append(b)
    indegree[a] += 1

needed = set()
q = deque([K])
needed.add(K)
while q:
    v = q.popleft()
    for nv in rev_graph[v]:
        if nv not in needed:
            needed.add(nv)
            q.append(nv)

q = deque()
for v in needed:
    cnt = 0
    for nv in rev_graph[v]:
        if nv in needed:
            cnt += 1
    if cnt == 0:
        q.append(v)

result = []
local_indegree = {v: sum(1 for nv in rev_graph[v] if nv in needed) for v in needed}
q = deque([v for v in needed if local_indegree[v] == 0])

while q:
    v = q.popleft()
    result.append(v)
    for nv in graph[v]:
        if nv in needed:
            local_indegree[nv] -= 1
            if local_indegree[nv] == 0:
                q.append(nv)

print(*result)
