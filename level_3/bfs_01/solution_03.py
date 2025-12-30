from collections import deque

H, W = map(int, input().split())
grid = [input() for _ in range(H)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
INF = float('inf')

dist = [[INF] * W for _ in range(H)]
dist[0][0] = 0
dq = deque([(0, 0)])

while dq:
    x, y = dq.popleft()
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < H and 0 <= ny < W:
            cost = 0 if grid[nx][ny] == grid[x][y] else 1
            if dist[x][y] + cost < dist[nx][ny]:
                dist[nx][ny] = dist[x][y] + cost
                if cost == 0:
                    dq.appendleft((nx, ny))
                else:
                    dq.append((nx, ny))

print(dist[H - 1][W - 1])
