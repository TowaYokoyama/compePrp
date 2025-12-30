from itertools import permutations

N = int(input())
C = [list(map(int, input().split())) for _ in range(N)]

min_cost = float('inf')
for perm in permutations(range(1, N)):
    cost = C[0][perm[0]]
    for i in range(len(perm) - 1):
        cost += C[perm[i]][perm[i + 1]]
    cost += C[perm[-1]][0]
    min_cost = min(min_cost, cost)

print(min_cost)
