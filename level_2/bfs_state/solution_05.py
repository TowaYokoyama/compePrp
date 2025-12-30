from collections import deque

H, W = map(int, input().split())
grid = [input() for _ in range(H)]

sx, sy, gx, gy = 0, 0, 0, 0
fires = []
for i in range(H):
    for j in range(W):
        if grid[i][j] == 'S':
            sx, sy = i, j
        if grid[i][j] == 'G':
            gx, gy = i, j
        if grid[i][j] == 'F':
            fires.append((i, j))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
INF = float('inf')

fire_dist = [[INF] * W for _ in range(H)]
q = deque()
for fx, fy in fires:
    fire_dist[fx][fy] = 0
    q.append((fx, fy))

while q:
    x, y = q.popleft()
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < H and 0 <= ny < W and grid[nx][ny] != '#' and fire_dist[nx][ny] == INF:
            fire_dist[nx][ny] = fire_dist[x][y] + 1
            q.append((nx, ny))

person_dist = [[INF] * W for _ in range(H)]
person_dist[sx][sy] = 0
q = deque([(sx, sy)])

while q:
    x, y = q.popleft()
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < H and 0 <= ny < W and grid[nx][ny] != '#':
            if person_dist[nx][ny] == INF and person_dist[x][y] + 1 < fire_dist[nx][ny]:
                person_dist[nx][ny] = person_dist[x][y] + 1
                q.append((nx, ny))

print("Yes" if person_dist[gx][gy] != INF else "No")
