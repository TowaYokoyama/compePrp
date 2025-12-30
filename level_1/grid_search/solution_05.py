from collections import deque

H, W = map(int, input().split())

dx = [-2, -2, -1, -1, 1, 1, 2, 2]
dy = [-1, 1, -2, 2, -2, 2, -1, 1]

dist = [[-1] * W for _ in range(H)]
dist[0][0] = 0
q = deque([(0, 0)])

while q:
    x, y = q.popleft()
    for i in range(8):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < H and 0 <= ny < W and dist[nx][ny] == -1:
            dist[nx][ny] = dist[x][y] + 1
            q.append((nx, ny))

print(dist[H - 1][W - 1])
