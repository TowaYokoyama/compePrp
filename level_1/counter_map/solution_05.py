from collections import defaultdict

N, K = map(int, input().split())
A = list(map(int, input().split()))

cnt = defaultdict(int)
distinct = 0

for i in range(K):
    if cnt[A[i]] == 0:
        distinct += 1
    cnt[A[i]] += 1

max_distinct = distinct

for i in range(K, N):
    cnt[A[i - K]] -= 1
    if cnt[A[i - K]] == 0:
        distinct -= 1
    
    if cnt[A[i]] == 0:
        distinct += 1
    cnt[A[i]] += 1
    
    max_distinct = max(max_distinct, distinct)

print(max_distinct)
