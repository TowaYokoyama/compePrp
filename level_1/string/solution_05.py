S = input()
N = len(S)

Z = [0] * N
Z[0] = N
l, r = 0, 0

for i in range(1, N):
    if i < r:
        Z[i] = min(r - i, Z[i - l])
    while i + Z[i] < N and S[Z[i]] == S[i + Z[i]]:
        Z[i] += 1
    if i + Z[i] > r:
        l, r = i, i + Z[i]

print(*Z)
