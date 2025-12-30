from collections import Counter

N = int(input())
A = list(map(int, input().split()))

cnt = Counter(A)
count = sum(1 for v in cnt.values() if v == 1)

print(count)
