N = int(input())
A = list(map(int, input().split()))

A.sort()
min_diff = float('inf')
for i in range(N - 1):
    min_diff = min(min_diff, A[i + 1] - A[i])

print(min_diff)
