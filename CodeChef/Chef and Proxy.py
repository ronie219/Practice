# Chef and Proxy
from math import ceil
for _ in range(int(input())):
    D = int(input())
    S = [a for a in input()]
    i = 2
    proxy = 0
    present = S.count('P')
    for i in range(2, D - 2):
        if S[i] == 'A' and (S[i - 1] == 'P' or S[i - 2] == 'P') and (S[i + 1] == 'P' or S[i + 2] == 'P'):
            proxy += 1
    r = (3 * D - 4 * present) / 4
    if proxy >= r:
        print(max(int(ceil(r)), 0))
    else:
        print(-1)
