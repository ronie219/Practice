# Chef and Price Control
for t in range(int(input())):
    N, K = map(int,input().split())
    P = list(map(int,input().split()))
    ceiling_price = []
    for i in P:
        if i > K:
            ceiling_price.append(K)
        else:
            ceiling_price.append(i)
    print(sum(P)-sum(ceiling_price))