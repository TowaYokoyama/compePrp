N, K = map(int, input().split())
T = list(map(int, input().split()))

def can_assign(limit):
    workers = 1
    current = 0
    for t in T:
        if t > limit:
            return False
        if current + t > limit:
            workers += 1
            current = t
        else:
            current += t
    return workers <= K

left, right = max(T), sum(T)
while left < right:
    mid = (left + right) // 2
    if can_assign(mid):
        right = mid
    else:
        left = mid + 1

print(left)
