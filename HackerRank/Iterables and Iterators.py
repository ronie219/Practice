
# Iterables and Iterators
from itertools import combinations
n = int(input())
l = input().split(" ")
e = int(input())
c = list(combinations(l,e))
count = 0
for i in c:
    if 'a' in i:
        count += 1
    else:
        continue
print("{:.4f}".format(count/len(c)))
"""
"""
for i in range(1, int(input())):
    print(str(i) * i)