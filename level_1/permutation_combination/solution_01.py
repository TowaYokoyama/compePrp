from itertools import permutations

N = int(input())

for p in permutations(range(1, N + 1)):
    print(*p)
