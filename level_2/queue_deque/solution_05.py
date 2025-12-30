from collections import deque

N = int(input())
A = list(map(int, input().split()))

dq = deque()
ans = [0] * N

for i in range(N):
    while dq and A[dq[-1]] >= A[i]:
        dq.pop()
    if dq:
        ans[i] = dq[-1] + 1
    else:
        ans[i] = 0
    dq.append(i)

print(*ans)
