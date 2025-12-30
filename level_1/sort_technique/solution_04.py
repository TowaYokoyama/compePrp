N = int(input())
events = []
for _ in range(N):
    L, R = map(int, input().split())
    events.append((L, 1))
    events.append((R, -1))

events.sort()

current = 0
max_count = 0
for pos, delta in events:
    current += delta
    max_count = max(max_count, current)

print(max_count)
