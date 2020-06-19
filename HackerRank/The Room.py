
# The Room
from collections import Counter
N = int(input())
s = input().split()
result = Counter(s)
print(*[i for i,j in result.items() if j == 1])