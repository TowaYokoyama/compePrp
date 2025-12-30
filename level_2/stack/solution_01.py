S = input()

stack = []
valid = True

for c in S:
    if c == '(':
        stack.append(c)
    else:
        if not stack:
            valid = False
            break
        stack.pop()

if stack:
    valid = False

print("Yes" if valid else "No")
