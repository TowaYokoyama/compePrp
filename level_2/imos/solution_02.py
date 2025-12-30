N = int(input())

events = []
for _ in range(N):
    S, E = map(int, input().split())
    events.append((S, 1))
    events.append((E, -1))

events.sort()

current = 0
max_count = 0
for time, delta in events:
    current += delta
    max_count = max(max_count, current)

print(max_count)
