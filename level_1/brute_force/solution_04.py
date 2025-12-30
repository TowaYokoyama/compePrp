N, S = map(int, input().split())
A = list(map(int, input().split()))

found = False
for i in range(N):
    for j in range(i + 1, N):
        for k in range(j + 1, N):
            if A[i] + A[j] + A[k] == S:
                found = True

print("Yes" if found else "No")
