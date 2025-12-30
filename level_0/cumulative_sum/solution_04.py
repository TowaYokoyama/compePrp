N = int(input())
A = list(map(int, input().split()))

S = [0] * (N + 1)
for i in range(N):
    S[i + 1] = S[i] + A[i]

min_s = 0
ans = S[1]
for i in range(1, N + 1):
    ans = max(ans, S[i] - min_s)
    min_s = min(min_s, S[i])

print(ans)
