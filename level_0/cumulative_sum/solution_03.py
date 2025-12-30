H, W, Q = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]

S = [[0] * (W + 1) for _ in range(H + 1)]
for i in range(H):
    for j in range(W):
        S[i + 1][j + 1] = S[i][j + 1] + S[i + 1][j] - S[i][j] + A[i][j]

for _ in range(Q):
    r1, c1, r2, c2 = map(int, input().split())
    ans = S[r2][c2] - S[r1 - 1][c2] - S[r2][c1 - 1] + S[r1 - 1][c1 - 1]
    print(ans)
