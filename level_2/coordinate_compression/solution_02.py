N = int(input())
intervals = []
coords = set()

for _ in range(N):
    L, R = map(int, input().split())
    intervals.append((L, R))
    coords.add(L)
    coords.add(R + 1)

sorted_coords = sorted(coords)
compress = {v: i for i, v in enumerate(sorted_coords)}

diff = [0] * (len(sorted_coords) + 1)
for L, R in intervals:
    diff[compress[L]] += 1
    diff[compress[R + 1]] -= 1

current = 0
total = 0
for i in range(len(sorted_coords) - 1):
    current += diff[i]
    if current > 0:
        total += sorted_coords[i + 1] - sorted_coords[i]

print(total)
