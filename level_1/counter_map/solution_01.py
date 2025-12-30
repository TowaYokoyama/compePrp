from collections import Counter

N = int(input())
A = list(map(int, input().split()))

cnt = Counter(A)
max_count = max(cnt.values())
ans = min(k for k, v in cnt.items() if v == max_count)

print(ans)
