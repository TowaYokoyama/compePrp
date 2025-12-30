H, W, Q = map(int, input().split())

diff = [[0] * (W + 2) for _ in range(H + 2)]

for _ in range(Q):
    r1, c1, r2, c2 = map(int, input().split())
    diff[r1][c1] += 1
    diff[r1][c2 + 1] -= 1
    diff[r2 + 1][c1] -= 1
    diff[r2 + 1][c2 + 1] += 1

for i in range(1, H + 1):
    for j in range(1, W + 1):
        diff[i][j] += diff[i][j - 1]

for i in range(1, H + 1):
    for j in range(1, W + 1):
        diff[i][j] += diff[i - 1][j]

for i in range(1, H + 1):
    print(*diff[i][1:W + 1])
