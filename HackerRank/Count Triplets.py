# Count Triplets
from collections import Counter, defaultdict


def countTriplets(arr, r):
    d1 = defaultdict(int)
    d2 = defaultdict(int)
    result = 0
    for i in reversed(arr):
        if i * r in d1:
            result += d2[i * r]
        if i * r in d2:
            d2[i] += d1[i * r]
        d1[i] += 1
    return result


nr = input().rstrip().split()
n = int(nr[0])
r = int(nr[1])
arr = list(map(int, input().rstrip().split()))
print(countTriplets(arr, r))
