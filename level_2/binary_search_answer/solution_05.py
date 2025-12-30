N, K = map(int, input().split())
A = list(map(int, input().split()))

def count_le(x):
    cnt = 0
    for a in A:
        if a > 0:
            cnt += min(N, x // a)
        elif a == 0:
            if x >= 0:
                cnt += N
        else:
            cnt += max(0, N - (-x) // (-a))
    return cnt

left, right = -10**18, 10**18
while left < right:
    mid = (left + right) // 2
    if count_le(mid) >= K:
        right = mid
    else:
        left = mid + 1

print(left)
