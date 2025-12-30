MOD = 10**9 + 7

def modinv(a, m=MOD):
    return pow(a, m - 2, m)

def comb(n, r, m=MOD):
    if r < 0 or r > n:
        return 0
    num = 1
    den = 1
    for i in range(r):
        num = num * (n - i) % m
        den = den * (i + 1) % m
    return num * modinv(den, m) % m

N, R = map(int, input().split())
print(comb(N, R))
