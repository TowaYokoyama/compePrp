N, Q = map(int, input().split())

diff = [0] * (N + 2)

for _ in range(Q):
    L, R, X = map(int, input().split())
    diff[L] += X
    diff[R + 1] -= X

A = [0] * (N + 1)
for i in range(1, N + 1):
    A[i] = A[i - 1] + diff[i]

print(*A[1:])
