import bisect

N, M, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
A.sort()
B.sort()

def count_le(x):
    cnt = 0
    for a in A:
        cnt += bisect.bisect_right(B, x - a)
    return cnt

left, right = A[0] + B[0], A[-1] + B[-1]
while left < right:
    mid = (left + right) // 2
    if count_le(mid) >= K:
        right = mid
    else:
        left = mid + 1

print(left)
