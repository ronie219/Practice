for _ in range(int(input())):
    k1, k2, k3, v = map(float, input().split())
    ans = float("{0:.2f}".format(100/(k1 * k2 * k3 * v)))
    if ans < 9.58:
        print("YES")
    else:
        print("NO")
