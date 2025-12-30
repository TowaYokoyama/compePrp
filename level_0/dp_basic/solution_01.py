MOD = 10**9 + 7

N = int(input())
dp = [0] * (N + 1)
dp[0] = 1

for i in range(N + 1):
    if i + 1 <= N:
        dp[i + 1] = (dp[i + 1] + dp[i]) % MOD
    if i + 2 <= N:
        dp[i + 2] = (dp[i + 2] + dp[i]) % MOD

print(dp[N])
