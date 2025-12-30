N, M = map(int, input().split())
X = list(map(int, input().split()))
X.sort()

def can_place(d):
    count = 1
    last = X[0]
    for i in range(1, N):
        if X[i] - last >= d:
            count += 1
            last = X[i]
    return count >= M

left, right = 1, X[-1] - X[0]
while left < right:
    mid = (left + right + 1) // 2
    if can_place(mid):
        left = mid
    else:
        right = mid - 1

print(left)
