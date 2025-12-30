class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return
        if self.rank[px] < self.rank[py]:
            px, py = py, px
        self.parent[py] = px
        if self.rank[px] == self.rank[py]:
            self.rank[px] += 1
    
    def same(self, x, y):
        return self.find(x) == self.find(y)

N, Q = map(int, input().split())
uf = UnionFind(N + 1)

for _ in range(Q):
    t, u, v = map(int, input().split())
    if t == 1:
        uf.union(u, v)
    else:
        print("Yes" if uf.same(u, v) else "No")
