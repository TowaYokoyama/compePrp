from itertools import product

N, K = map(int, input().split())

for p in product(range(1, K + 1), repeat=N):
    print(*p)
