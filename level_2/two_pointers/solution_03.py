N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))

A.sort()
B.sort()

i = j = 0
count = 0

while i < N and j < M:
    if A[i] == B[j]:
        count += 1
        i += 1
        j += 1
    elif A[i] < B[j]:
        i += 1
    else:
        j += 1

print(count)
