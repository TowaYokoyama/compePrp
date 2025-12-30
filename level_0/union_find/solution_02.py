class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px != py:
            self.parent[py] = px

N, M = map(int, input().split())
uf = UnionFind(N + 1)

for _ in range(M):
    a, b = map(int, input().split())
    uf.union(a, b)

roots = set()
for i in range(1, N + 1):
    roots.add(uf.find(i))

print(len(roots))
