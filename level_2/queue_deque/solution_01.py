from collections import deque

N, K = map(int, input().split())
A = list(map(int, input().split()))

dq = deque()
ans = []

for i in range(N):
    while dq and A[dq[-1]] <= A[i]:
        dq.pop()
    dq.append(i)
    
    if dq[0] <= i - K:
        dq.popleft()
    
    if i >= K - 1:
        ans.append(A[dq[0]])

print(*ans)
