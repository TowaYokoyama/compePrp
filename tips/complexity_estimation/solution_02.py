# N ≤ 10^4 → O(N^2) が間に合う

N, K = map(int, input().split())
A = list(map(int, input().split()))

count = 0
for i in range(N):
    for j in range(i + 1, N):
        if A[i] + A[j] == K:
            count += 1

print(count)  # O(N^2) = 10^8 でギリギリ
