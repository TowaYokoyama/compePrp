from collections import deque

H, W = map(int, input().split())
grid = [input() for _ in range(H)]

dist = [[-1] * W for _ in range(H)]
q = deque()
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

for i in range(H):
    for j in range(W):
        if grid[i][j] == 'F':
            dist[i][j] = 0
            q.append((i, j))

while q:
    x, y = q.popleft()
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < H and 0 <= ny < W and grid[nx][ny] != '#' and dist[nx][ny] == -1:
            dist[nx][ny] = dist[x][y] + 1
            q.append((nx, ny))

for row in dist:
    print(*row)
