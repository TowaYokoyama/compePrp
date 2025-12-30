N, M = map(int, input().split())
INF = float('inf')
dist = [[INF] * (N + 1) for _ in range(N + 1)]

for i in range(N + 1):
    dist[i][i] = 0

for _ in range(M):
    a, b, c = map(int, input().split())
    dist[a][b] = min(dist[a][b], c)

for k in range(1, N + 1):
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if dist[i][k] != INF and dist[k][j] != INF:
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

for i in range(1, N + 1):
    row = []
    for j in range(1, N + 1):
        row.append(str(dist[i][j]) if dist[i][j] != INF else "INF")
    print(' '.join(row))
