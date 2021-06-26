# Frequency Queries
from collections import Counter


def freqQuery(queries):
    result = []
    dic = Counter()
    val = Counter()
    for i in queries:
        if i[0] == 1:
            val[dic[1]] -= 1
            dic[i[1]] += 1
            val[dic[1]] += 1
        elif i[0] == 2:
            if dic[1] > 0:
                val[dic[1]] -= 1
                dic[i[1]] -= 1
                val[dic[1]] += 1
        else:
            result.append(1 if val[1] > 0 else 0)
    return result


q = int(input().strip())
queries = []
for _ in range(q):
    queries.append(list(map(int, input().rstrip().split())))
print(freqQuery(queries))
