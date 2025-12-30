N, K, S = map(int, input().split())
A = list(map(int, input().split()))

count = 0
for bit in range(1 << N):
    if bin(bit).count('1') == K:
        s = 0
        for i in range(N):
            if bit & (1 << i):
                s += A[i]
        if s == S:
            count += 1

print(count)
