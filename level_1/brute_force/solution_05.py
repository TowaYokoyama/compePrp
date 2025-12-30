N, S = map(int, input().split())
A = list(map(int, input().split()))

half = N // 2
A1 = A[:half]
A2 = A[half:]

sums1 = set()
for bit in range(1 << len(A1)):
    s = 0
    for i in range(len(A1)):
        if bit & (1 << i):
            s += A1[i]
    sums1.add(s)

found = False
for bit in range(1 << len(A2)):
    s = 0
    for i in range(len(A2)):
        if bit & (1 << i):
            s += A2[i]
    if S - s in sums1:
        found = True
        break

print("Yes" if found else "No")
