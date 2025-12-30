import sys
sys.setrecursionlimit(10**6)

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)

# 0: 未訪問, 1: 訪問中, 2: 訪問済み
state = [0] * (N + 1)
has_cycle = False

def dfs(v):
    global has_cycle
    state[v] = 1
    for nv in graph[v]:
        if state[nv] == 1:
            has_cycle = True
            return
        if state[nv] == 0:
            dfs(nv)
    state[v] = 2

for i in range(1, N + 1):
    if state[i] == 0:
        dfs(i)

print("Yes" if has_cycle else "No")
