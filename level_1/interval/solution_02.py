import math

N, Q = map(int, input().split())
A = list(map(int, input().split()))

LOG = max(1, int(math.log2(N)) + 1)
sparse = [[0] * N for _ in range(LOG)]
sparse[0] = A[:]

for k in range(1, LOG):
    for i in range(N - (1 << k) + 1):
        sparse[k][i] = max(sparse[k-1][i], sparse[k-1][i + (1 << (k-1))])

for _ in range(Q):
    L, R = map(int, input().split())
    L -= 1
    R -= 1
    length = R - L + 1
    k = int(math.log2(length))
    print(max(sparse[k][L], sparse[k][R - (1 << k) + 1]))
