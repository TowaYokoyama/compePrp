from collections import deque

H, W = map(int, input().split())
grid = [input() for _ in range(H)]

sx, sy, gx, gy = 0, 0, 0, 0
for i in range(H):
    for j in range(W):
        if grid[i][j] == 'S':
            sx, sy = i, j
        if grid[i][j] == 'G':
            gx, gy = i, j

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
INF = float('inf')

dist = [[[INF] * 4 for _ in range(W)] for _ in range(H)]
dist[sx][sy][1] = 0
q = deque([(sx, sy, 1)])

while q:
    x, y, d = q.popleft()
    nx, ny = x + dx[d], y + dy[d]
    if 0 <= nx < H and 0 <= ny < W and grid[nx][ny] != '#':
        if dist[nx][ny][d] > dist[x][y][d] + 1:
            dist[nx][ny][d] = dist[x][y][d] + 1
            q.append((nx, ny, d))
    
    for nd in [(d + 1) % 4, (d + 3) % 4]:
        if dist[x][y][nd] > dist[x][y][d] + 1:
            dist[x][y][nd] = dist[x][y][d] + 1
            q.append((x, y, nd))

ans = min(dist[gx][gy])
print(ans if ans != INF else -1)
