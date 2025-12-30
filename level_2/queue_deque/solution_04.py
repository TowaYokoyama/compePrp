from collections import deque

N, K = map(int, input().split())
A = list(map(int, input().split()))

dq = deque()
total = 0

for a in A:
    dq.append(a)
    total += a
    if len(dq) > K:
        total -= dq.popleft()
    print(total // len(dq))
