N = int(input())
A = list(map(int, input().split()))

sorted_unique = sorted(set(A))
compress = {v: i for i, v in enumerate(sorted_unique)}
decompress = {i: v for v, i in compress.items()}

compressed = [compress[a] for a in A]
M = len(sorted_unique)

cnt = [0] * M
for c in compressed:
    cnt[c] += 1

for i in range(M):
    if cnt[i] > 0:
        print(decompress[i], cnt[i])
