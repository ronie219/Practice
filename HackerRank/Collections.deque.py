from collections import deque

d = deque()
for _ in range(int(input())):
    try:
        operation = input().split()
        if operation[0] == 'appendleft':
            d.appendleft(operation[1])
        elif operation[0] == 'append':
            d.append(operation[1])
        elif operation[0] == 'pop':
            d.pop()
        else:
            d.popleft()
    except IndexError:
        continue
print(*d)