N, K = map(int, input().split())
A = list(map(int, input().split()))

def count_le(x):
    cnt = 0
    for a in A:
        cnt += min(N, x // a)
    return cnt

left, right = 1, A[-1] * N
while left < right:
    mid = (left + right) // 2
    if count_le(mid) >= K:
        right = mid
    else:
        left = mid + 1

print(left)
