# Smart Strategy
for _ in range(int(input())):
    N, Q = map(int,input().split())
    D = list(map(int,input().split()))
    q = list(map(int,input().split()))
    product = 1
    for i in D:
        product *= i
    result = [(i//product) for i in q]
    print(*result)
