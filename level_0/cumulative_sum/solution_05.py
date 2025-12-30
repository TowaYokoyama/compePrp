from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))

B = [a if i % 2 == 0 else -a for i, a in enumerate(A)]

S = [0] * (N + 1)
for i in range(N):
    S[i + 1] = S[i] + B[i]

count = 0
seen = defaultdict(int)
for i in range(N + 1):
    count += seen[S[i]]
    seen[S[i]] += 1

print(count)
