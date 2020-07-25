# Magic Set
for _ in range(int(input())):
    N, M = map(int,input().split())
    int_set = list(map(int,input().split()))
    result = 0
    for i in range(N):
        if int_set[i] % M == 0:
            result += 1
    print(2 ** result-1)