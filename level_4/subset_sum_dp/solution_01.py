N, S = map(int, input().split())
A = list(map(int, input().split()))

dp = [False] * (S + 1)
dp[0] = True

for a in A:
    for j in range(S, a - 1, -1):
        if dp[j - a]:
            dp[j] = True

print("Yes" if dp[S] else "No")
