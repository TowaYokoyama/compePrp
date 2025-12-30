from collections import deque

N, Q = map(int, input().split())
A = deque(map(int, input().split()))

for _ in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        K = query[1] % N
        A.rotate(K)
    else:
        print(A[query[1] - 1])
