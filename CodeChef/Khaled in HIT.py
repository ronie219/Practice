# Khaled in HIT
for _ in range(int(input())):
    N = int(input())
    n = sorted(list(map(int, input().split())))
    result = []
    diff = N // 4
    x = n[diff]
    y = n[2 * diff]
    z = n[3 * diff]
    if x == n[diff-1] or y == n[(2 * diff)-1] or z == n[(3  * diff)-1]:
        print(-1)
    else:
        print(x, y, z)