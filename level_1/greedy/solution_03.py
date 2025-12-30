import heapq

N = int(input())
jobs = []
for _ in range(N):
    D, P = map(int, input().split())
    jobs.append((D, P))

jobs.sort()

heap = []
for D, P in jobs:
    heapq.heappush(heap, P)
    if len(heap) > D:
        heapq.heappop(heap)

print(sum(heap))
