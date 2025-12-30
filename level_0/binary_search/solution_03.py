N, K = map(int, input().split())
W = list(map(int, input().split()))

def can_carry(capacity):
    trucks = 1
    current = 0
    for w in W:
        if current + w > capacity:
            trucks += 1
            current = w
        else:
            current += w
    return trucks <= K

left, right = max(W), sum(W)
while left < right:
    mid = (left + right) // 2
    if can_carry(mid):
        right = mid
    else:
        left = mid + 1

print(left)
