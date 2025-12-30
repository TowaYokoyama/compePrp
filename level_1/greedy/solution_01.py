N = int(input())

coins = [500, 100, 50, 10, 5, 1]
count = 0

for c in coins:
    count += N // c
    N %= c

print(count)
