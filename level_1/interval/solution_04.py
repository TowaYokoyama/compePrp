N = int(input())
intervals = []
for _ in range(N):
    L, R = map(int, input().split())
    intervals.append((L, R))

intervals.sort()

merged = []
for L, R in intervals:
    if merged and merged[-1][1] >= L:
        merged[-1] = (merged[-1][0], max(merged[-1][1], R))
    else:
        merged.append((L, R))

print(len(merged))
