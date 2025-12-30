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

dist = [[[INF] * 8 for _ in range(W)] for _ in range(H)]
dist[sx][sy][0] = 0
q = deque([(sx, sy, 0)])

while q:
    x, y, keys = q.popleft()
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < H and 0 <= ny < W and grid[nx][ny] != '#':
            c = grid[nx][ny]
            if c in 'ABC':
                need = ord(c) - ord('A')
                if not (keys & (1 << need)):
                    continue
            new_keys = keys
            if c in 'abc':
                new_keys |= (1 << (ord(c) - ord('a')))
            if dist[nx][ny][new_keys] > dist[x][y][keys] + 1:
                dist[nx][ny][new_keys] = dist[x][y][keys] + 1
                q.append((nx, ny, new_keys))

ans = min(dist[gx][gy])
print(ans if ans != INF else -1)
