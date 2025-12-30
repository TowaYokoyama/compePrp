class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return
        if self.size[px] < self.size[py]:
            px, py = py, px
        self.parent[py] = px
        self.size[px] += self.size[py]
    
    def get_size(self, x):
        return self.size[self.find(x)]

N, Q = map(int, input().split())
uf = UnionFind(N + 1)

for _ in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        uf.union(query[1], query[2])
    else:
        print(uf.get_size(query[1]))
