from collections import defaultdict

N, K = map(int, input().split())
A = list(map(int, input().split()))

cnt = defaultdict(int)
left = 0
distinct = 0
max_len = 0

for right in range(N):
    if cnt[A[right]] == 0:
        distinct += 1
    cnt[A[right]] += 1
    
    while distinct > K:
        cnt[A[left]] -= 1
        if cnt[A[left]] == 0:
            distinct -= 1
        left += 1
    
    max_len = max(max_len, right - left + 1)

print(max_len)
