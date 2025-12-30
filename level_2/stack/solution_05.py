S = input()

stack = []

for c in S:
    if stack and stack[-1] == c:
        stack.pop()
    else:
        stack.append(c)

print(''.join(stack) if stack else "Empty")
