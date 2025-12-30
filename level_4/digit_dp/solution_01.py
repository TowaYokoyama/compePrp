N = input()
K = int(input())
L = len(N)

dp = [[0] * (K + 2) for _ in range(2)]
dp[1][0] = 1

for i in range(L):
    d = int(N[i])
    new_dp = [[0] * (K + 2) for _ in range(2)]
    for tight in range(2):
        for s in range(K + 2):
            if dp[tight][s] == 0:
                continue
            limit = d if tight else 9
            for digit in range(limit + 1):
                new_s = min(s + digit, K + 1)
                new_tight = tight and (digit == d)
                new_dp[new_tight][new_s] += dp[tight][s]
    dp = new_dp

ans = 0
for tight in range(2):
    for s in range(K + 1):
        ans += dp[tight][s]

print(ans)
