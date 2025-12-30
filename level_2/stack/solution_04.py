N = int(input())
H = list(map(int, input().split()))

stack = []
max_area = 0

for i in range(N):
    start = i
    while stack and stack[-1][1] > H[i]:
        idx, h = stack.pop()
        max_area = max(max_area, h * (i - idx))
        start = idx
    stack.append((start, H[i]))

for idx, h in stack:
    max_area = max(max_area, h * (N - idx))

print(max_area)
