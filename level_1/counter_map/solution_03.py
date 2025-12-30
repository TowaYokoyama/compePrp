from collections import Counter

S = input()
T = input()

print("Yes" if Counter(S) == Counter(T) else "No")
