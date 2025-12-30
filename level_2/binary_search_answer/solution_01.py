L, N = map(int, input().split())

def can_distribute(k):
    return L // k >= N

left, right = 1, L
while left < right:
    mid = (left + right + 1) // 2
    if can_distribute(mid):
        left = mid
    else:
        right = mid - 1

print(left)
