class FenwickTree:
    def __init__(self, n):
        self.n = n
        self.data = [0] * (n + 1)
    
    def add(self, i, x):
        while i <= self.n:
            self.data[i] += x
            i += i & (-i)
    
    def sum(self, i):
        s = 0
        while i > 0:
            s += self.data[i]
            i -= i & (-i)
        return s
    
    def range_sum(self, l, r):
        return self.sum(r) - self.sum(l - 1)

N, Q = map(int, input().split())
A = list(map(int, input().split()))

ft = FenwickTree(N)
for i in range(N):
    ft.add(i + 1, A[i])

for _ in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        ft.add(query[1], query[2])
    else:
        print(ft.range_sum(query[1], query[2]))
