import heapq

N, K = map(int, input().split())
A = list(map(int, input().split()))

heap = []

for a in A:
    heapq.heappush(heap, a)
    if len(heap) > K:
        heapq.heappop(heap)
    if len(heap) < K:
        print(-1)
    else:
        print(heap[0])
