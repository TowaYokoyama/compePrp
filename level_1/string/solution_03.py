S = input()

result = []
i = 0
while i < len(S):
    c = S[i]
    count = 0
    while i < len(S) and S[i] == c:
        count += 1
        i += 1
    result.append(f"{c}{count}")

print(''.join(result))
