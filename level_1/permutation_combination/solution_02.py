from itertools import combinations

N, R = map(int, input().split())

for c in combinations(range(1, N + 1), R):
    print(*c)
