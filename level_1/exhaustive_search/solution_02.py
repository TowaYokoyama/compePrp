N, K = map(int, input().split())
A = list(map(int, input().split()))

count = 0
for i in range(N):
    for j in range(i + 1, N):
        for k in range(j + 1, N):
            if A[i] + A[j] + A[k] == K:
                count += 1

print(count)
