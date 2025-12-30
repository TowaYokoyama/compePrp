from collections import Counter

N = int(input())
A = list(map(int, input().split()))

cnt = Counter(A)
ans = 0
for v in cnt.values():
    ans += v * (v - 1) // 2

print(ans)
