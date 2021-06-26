
# Word Order
from collections import defaultdict
d = defaultdict(int)
for i in range(int(input())):
    d[input()] += 1
print(len(d.items()))
print(*d.values())