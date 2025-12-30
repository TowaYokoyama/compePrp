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
dir_char = ['D', 'U', 'R', 'L']

dist = [[-1] * W for _ in range(H)]
prev = [[None] * W for _ in range(H)]
dist[sx][sy] = 0
q = deque([(sx, sy)])

while q:
    x, y = q.popleft()
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < H and 0 <= ny < W and grid[nx][ny] != '#' and dist[nx][ny] == -1:
            dist[nx][ny] = dist[x][y] + 1
            prev[nx][ny] = (x, y, dir_char[i])
            q.append((nx, ny))

if dist[gx][gy] == -1:
    print(-1)
else:
    path = []
    x, y = gx, gy
    while (x, y) != (sx, sy):
        px, py, d = prev[x][y]
        path.append(d)
        x, y = px, py
    print(''.join(reversed(path)))
