# Company Logo
from collections import defaultdict (wrong)
n = input()
d = defaultdict(int)
for i in n:
    d[i] += 1
l = set(d.values())
print(d.items())