import math

S = "}{{}}{{{"
stack = []
if len(S) % 2 != 0:
    print("No")
for i in S:
    if (len(stack) != 0 and stack[-1] == '{') and i == '}':
        stack.pop()
    else:
        stack.append(i)

m = 0
n = 0
for i in stack:
    if i == '{':
        m += 1
    else:
        n += 1
print(math.ceil(m/2) + math.ceil(n/2))