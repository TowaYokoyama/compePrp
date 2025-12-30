class SegmentTree:
    def __init__(self, n, e, op):
        self.e = e
        self.op = op
        self.size = 1
        while self.size < n:
            self.size *= 2
        self.data = [e] * (2 * self.size)
    
    def update(self, i, x):
        i += self.size
        self.data[i] = x
        while i > 1:
            i //= 2
            self.data[i] = self.op(self.data[2 * i], self.data[2 * i + 1])
    
    def query(self, l, r):
        l += self.size
        r += self.size
        res = self.e
        while l < r:
            if l & 1:
                res = self.op(res, self.data[l])
                l += 1
            if r & 1:
                r -= 1
                res = self.op(res, self.data[r])
            l //= 2
            r //= 2
        return res

N, Q = map(int, input().split())
A = list(map(int, input().split()))

INF = float('inf')
st = SegmentTree(N, INF, min)
for i in range(N):
    st.update(i, A[i])

for _ in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        st.update(query[1] - 1, query[2])
    else:
        print(st.query(query[1] - 1, query[2]))
