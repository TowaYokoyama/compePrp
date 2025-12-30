import sys
sys.setrecursionlimit(10**6)

N, S = map(int, input().split())
A = list(map(int, input().split()))

def solve(i, current_sum):
    if current_sum == S:
        return True
    if i == N:
        return False
    if solve(i + 1, current_sum + A[i]):
        return True
    if solve(i + 1, current_sum):
        return True
    return False

print("Yes" if solve(0, 0) else "No")
