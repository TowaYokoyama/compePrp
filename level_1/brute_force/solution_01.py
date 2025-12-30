N = int(input())
A = list(map(int, input().split()))

sums = set()
for bit in range(1, 1 << N):
    s = 0
    for i in range(N):
        if bit & (1 << i):
            s += A[i]
    sums.add(s)

print(*sorted(sums))
