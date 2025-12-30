N, Q = map(int, input().split())
intervals = []
for _ in range(N):
    L, R = map(int, input().split())
    intervals.append((L, R))

for _ in range(Q):
    A, B = map(int, input().split())
    count = 0
    for L, R in intervals:
        if not (R < A or B < L):
            count += 1
    print(count)
