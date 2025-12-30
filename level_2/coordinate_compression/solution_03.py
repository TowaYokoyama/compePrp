N = int(input())
A = list(map(int, input().split()))

sorted_unique = sorted(set(A))
compress = {v: i + 1 for i, v in enumerate(sorted_unique)}
M = len(sorted_unique)

bit = [0] * (M + 1)

def add(i):
    while i <= M:
        bit[i] += 1
        i += i & (-i)

def sum_query(i):
    s = 0
    while i > 0:
        s += bit[i]
        i -= i & (-i)
    return s

ans = 0
for a in A:
    c = compress[a]
    ans += sum_query(M) - sum_query(c)
    add(c)

print(ans)
