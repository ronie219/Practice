for _ in range(int(input())):
    w1, w2, x1, x2, M = map(int, input().split())
    if (x1*M) <= (w2 - w1) <= (x2*M):
        print(1)
    else:
        print(0)
