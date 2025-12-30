N = int(input())
A = list(map(int, input().split()))

sorted_unique = sorted(set(A))
compress = {v: i for i, v in enumerate(sorted_unique)}

ans = [compress[a] for a in A]
print(*ans)
