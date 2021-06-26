from collections import namedtuple

x = int(input())
heading = list(map(str, input().split()))
marks = namedtuple('Result', heading)
total = 0
for i in range(x):
    a, b, c, d = input().split()
    result = marks(a, b, c, d)
    total += int(result.MARKS)

print(total/x)
