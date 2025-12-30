N = int(input())
S = input()

left = 0
right = N - 1
T = []

while left <= right:
    if S[left:right+1] <= S[left:right+1][::-1]:
        T.append(S[left])
        left += 1
    else:
        T.append(S[right])
        right -= 1

print(''.join(T))
