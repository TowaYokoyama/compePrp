# 配るDP：dp[i] から dp[i+1], dp[i+2] に値を配る

N = int(input())
dp = [0] * (N + 3)
dp[0] = 1

for i in range(N + 1):
    dp[i + 1] += dp[i]
    dp[i + 2] += dp[i]

print(dp[N])
