# N ≤ 10^6 → O(N) または O(N log N) が必要

N = int(input())
A = list(map(int, input().split()))

print(sum(A))  # O(N)
