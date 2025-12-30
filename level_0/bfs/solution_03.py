from collections import deque

H, W = map(int, input().split())
grid = [input() for _ in range(H)]
visited = [[False] * W for _ in range(H)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(si, sj):
    q = deque([(si, sj)])
    visited[si][sj] = True
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < H and 0 <= ny < W and not visited[nx][ny] and grid[nx][ny] == '#':
                visited[nx][ny] = True
                q.append((nx, ny))

count = 0
for i in range(H):
    for j in range(W):
        if grid[i][j] == '#' and not visited[i][j]:
            bfs(i, j)
            count += 1

print(count)
