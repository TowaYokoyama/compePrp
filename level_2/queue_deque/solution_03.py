from collections import deque

Q = int(input())
dq = deque()

for _ in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        dq.appendleft(query[1])
    elif query[0] == 2:
        dq.append(query[1])
    elif query[0] == 3:
        print(dq.popleft())
    else:
        print(dq.pop())
