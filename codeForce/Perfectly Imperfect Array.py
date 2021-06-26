import math
for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    product = math.prod(a)
    print("NO") if product ** 0.5 == int(product ** 0.5) else print("YES")
