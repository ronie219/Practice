
from operator import itemgetter
N, M = map(int,input().split())
detail = []
for _ in range(N):
    detail.append(list(map(int,input().split())))
K = int(input())
arr = sorted(detail,key=itemgetter(K))
[print(*i) for i in arr]