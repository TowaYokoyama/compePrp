import bisect

N, Q = map(int, input().split())
A = list(map(int, input().split()))

for _ in range(Q):
    X = int(input())
    idx = bisect.bisect_left(A, X)
    if idx < N and A[idx] == X:
        print("Yes")
    else:
        print("No")
