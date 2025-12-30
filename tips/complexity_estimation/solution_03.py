# N ≤ 20 → O(2^N) が間に合う（bit全探索）

N, S = map(int, input().split())
A = list(map(int, input().split()))

count = 0
for bit in range(1 << N):  # 2^N 通り
    total = 0
    for i in range(N):
        if bit & (1 << i):
            total += A[i]
    if total == S:
        count += 1

print(count)  # O(2^N × N) = 2^20 × 20 ≒ 2 × 10^7
