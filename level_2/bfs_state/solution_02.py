from collections import deque, defaultdict

H, W = map(int, input().split())
grid = [input() for _ in range(H)]

sx, sy, gx, gy = 0, 0, 0, 0
warps = defaultdict(list)

for i in range(H):
    for j in range(W):
        if grid[i][j] == 'S':
            sx, sy = i, j
        elif grid[i][j] == 'G':
            gx, gy = i, j
        elif grid[i][j].islower():
            warps[grid[i][j]].append((i, j))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

dist = [[-1] * W for _ in range(H)]
dist[sx][sy] = 0
q = deque([(sx, sy)])

while q:
    x, y = q.popleft()
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < H and 0 <= ny < W and grid[nx][ny] != '#' and dist[nx][ny] == -1:
            dist[nx][ny] = dist[x][y] + 1
            q.append((nx, ny))
    
    c = grid[x][y]
    if c in warps:
        for wx, wy in warps[c]:
            if dist[wx][wy] == -1:
                dist[wx][wy] = dist[x][y] + 1
                q.append((wx, wy))
        del warps[c]

print(dist[gx][gy])
