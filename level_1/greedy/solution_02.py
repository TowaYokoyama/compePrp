N = int(input())
jobs = []
for _ in range(N):
    L, R = map(int, input().split())
    jobs.append((R, L))

jobs.sort()

count = 0
current_end = 0
for R, L in jobs:
    if L >= current_end:
        count += 1
        current_end = R

print(count)
