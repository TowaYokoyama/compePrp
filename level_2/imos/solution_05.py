N, M = map(int, input().split())

diff = [0] * (M + 2)

for _ in range(N):
    L, R = map(int, input().split())
    diff[L] += 1
    diff[R + 1] -= 1

for i in range(1, M + 2):
    diff[i] += diff[i - 1]

print(*diff[:M + 1])
