N = int(input())
points = []
for i in range(N):
    x, y = map(int, input().split())
    points.append((x, y, i))

ys = sorted(set(p[1] for p in points))
compress_y = {v: i + 1 for i, v in enumerate(ys)}
M = len(ys)

bit = [0] * (M + 1)

def add(i):
    while i <= M:
        bit[i] += 1
        i += i & (-i)

def sum_query(i):
    s = 0
    while i > 0:
        s += bit[i]
        i -= i & (-i)
    return s

points.sort()
ans = [0] * N

i = 0
while i < N:
    j = i
    while j < N and points[j][0] == points[i][0]:
        j += 1
    for k in range(i, j):
        cy = compress_y[points[k][1]]
        ans[points[k][2]] = sum_query(cy - 1)
    for k in range(i, j):
        cy = compress_y[points[k][1]]
        add(cy)
    i = j

print(*ans)
