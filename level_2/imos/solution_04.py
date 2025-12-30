N, Q = map(int, input().split())

diff1 = [0] * (N + 2)
diff2 = [0] * (N + 2)

for _ in range(Q):
    L, R = map(int, input().split())
    diff1[L] += 1
    diff1[R + 1] -= 1
    diff2[R + 1] -= (R - L + 1)

for i in range(1, N + 1):
    diff1[i] += diff1[i - 1]

for i in range(1, N + 1):
    diff2[i] += diff2[i - 1] + diff1[i]

print(*diff2[1:N + 1])
