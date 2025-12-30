N, K = map(int, input().split())
A = list(map(int, input().split()))

pair_sums = {}
for i in range(N):
    for j in range(i + 1, N):
        s = A[i] + A[j]
        if s not in pair_sums:
            pair_sums[s] = []
        pair_sums[s].append((i, j))

count = 0
for i in range(N):
    for j in range(i + 1, N):
        target = K - A[i] - A[j]
        if target in pair_sums:
            for (a, b) in pair_sums[target]:
                if a > j:
                    count += 1

print(count)
