import bisect

N, K = map(int, input().split())
A = list(map(int, input().split()))
A.sort()

count = 0
for i in range(N):
    target = K - A[i]
    j = bisect.bisect_right(A, target)
    cnt = j - i - 1
    if cnt > 0:
        count += cnt

print(count)
