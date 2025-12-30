from collections import defaultdict

N, K = map(int, input().split())
A = list(map(int, input().split()))

S = [0] * (N + 1)
for i in range(N):
    S[i + 1] = S[i] + A[i]

count = 0
seen = defaultdict(int)
for i in range(N + 1):
    count += seen[S[i] - K]
    seen[S[i]] += 1

print(count)
