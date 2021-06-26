# Sock Merchant
from collections import Counter

n = int(input())
colour = list(map(int, input().split()))
colour = colour[:n]
count = Counter(colour)
print(sum((i[1] // 2) for i in count.items()))
