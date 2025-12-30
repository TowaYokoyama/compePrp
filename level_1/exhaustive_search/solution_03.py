import bisect

N, K = map(int, input().split())
A = list(map(int, input().split()))
A.sort()

count = 0
for i in range(N):
    for j in range(i + 1, N):
        target = K - A[i] - A[j]
        left = bisect.bisect_left(A, target, j + 1)
        right = bisect.bisect_right(A, target, j + 1)
        count += right - left

print(count)
