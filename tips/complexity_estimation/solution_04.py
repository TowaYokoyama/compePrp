# N ≤ 8 → O(N!) が間に合う（順列全探索）

from itertools import permutations

N = int(input())
C = [list(map(int, input().split())) for _ in range(N)]

min_cost = float('inf')
for perm in permutations(range(N)):  # N! 通り
    cost = 0
    for i in range(N - 1):
        cost += C[perm[i]][perm[i + 1]]
    min_cost = min(min_cost, cost)

print(min_cost)  # O(N! × N)
