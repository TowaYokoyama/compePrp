from collections import deque

H, W = map(int, input().split())
sr, sc = map(int, input().split())
sr -= 1
sc -= 1
grid = [input() for _ in range(H)]

visited = [[False] * W for _ in range(H)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

q = deque([(sr, sc)])
visited[sr][sc] = True
count = 1

while q:
    x, y = q.popleft()
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < H and 0 <= ny < W and not visited[nx][ny] and grid[nx][ny] == '.':
            visited[nx][ny] = True
            count += 1
            q.append((nx, ny))

print(count)
