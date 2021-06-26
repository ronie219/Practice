for _ in range(int(input())):
    x, y, xi, yi, D = map(int, input().split())
    print("YES") if min(x // xi, y // yi) >= D else print("NO")
