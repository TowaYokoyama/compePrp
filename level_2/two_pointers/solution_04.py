N, S = map(int, input().split())
A = list(map(int, input().split()))

left = 0
current_sum = 0
count = 0

for right in range(N):
    current_sum += A[right]
    while current_sum > S and left <= right:
        current_sum -= A[left]
        left += 1
    if current_sum == S:
        count += 1

print(count)
