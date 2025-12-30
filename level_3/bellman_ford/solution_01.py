N, M = map(int, input().split())
edges = []
for _ in range(M):
    a, b, c = map(int, input().split())
    edges.append((a, b, c))

INF = float('inf')
dist = [INF] * (N + 1)
dist[1] = 0

for i in range(N):
    updated = False
    for a, b, c in edges:
        if dist[a] != INF and dist[a] + c < dist[b]:
            dist[b] = dist[a] + c
            updated = True
    if not updated:
        break

has_negative_cycle = False
for a, b, c in edges:
    if dist[a] != INF and dist[a] + c < dist[b]:
        has_negative_cycle = True
        break

if has_negative_cycle:
    print("NEGATIVE CYCLE")
else:
    for i in range(1, N + 1):
        print(dist[i] if dist[i] != INF else "INF")
