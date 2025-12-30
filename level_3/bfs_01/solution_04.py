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

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
INF = float('inf')

dist = [[[INF] * 2 for _ in range(W)] for _ in range(H)]
dist[sx][sy][0] = 0
dq = deque([(sx, sy, 0)])

while dq:
    x, y, used = dq.popleft()
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < H and 0 <= ny < W:
            if grid[nx][ny] != '#':
                if dist[x][y][used] < dist[nx][ny][used]:
                    dist[nx][ny][used] = dist[x][y][used]
                    dq.appendleft((nx, ny, used))
            elif used == 0:
                if dist[x][y][0] + 1 < dist[nx][ny][1]:
                    dist[nx][ny][1] = dist[x][y][0] + 1
                    dq.append((nx, ny, 1))

ans = min(dist[gx][gy][0], dist[gx][gy][1])
print(ans if ans != INF else -1)
