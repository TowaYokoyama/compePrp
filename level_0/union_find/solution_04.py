class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return False
        self.parent[py] = px
        return True

N, M = map(int, input().split())
uf = UnionFind(N + 1)

for _ in range(M):
    a, b = map(int, input().split())
    if uf.union(a, b):
        print("No")
    else:
        print("Yes")
