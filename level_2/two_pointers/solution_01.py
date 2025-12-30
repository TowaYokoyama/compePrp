N, S = map(int, input().split())
A = list(map(int, input().split()))

left = 0
current_sum = 0
min_len = N + 1

for right in range(N):
    current_sum += A[right]
    while current_sum >= S:
        min_len = min(min_len, right - left + 1)
        current_sum -= A[left]
        left += 1

print(min_len if min_len <= N else 0)
