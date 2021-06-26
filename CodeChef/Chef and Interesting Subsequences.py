# Chef and Interesting Subsequences
from itertools import combinations
for _ in range(int(input())):
    number_subs = list(map(int,input().split()))
    subsequence = list(map(int,input().split()))
    c = combinations(subsequence,number_subs[1])
    result = []
    for i in c:
        result.append(sum(i))
    print(result.count(min(result)))