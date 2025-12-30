N = int(input())
S = [input() for _ in range(N)]

if N == 0:
    print("")
else:
    prefix = S[0]
    for s in S[1:]:
        while not s.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                break
    print(prefix)
