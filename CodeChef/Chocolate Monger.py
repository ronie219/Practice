
for _ in range(int(input())):
    n, x = map(int, input().split())
    chocolates = list(map(int, input().split()))
    flavour_count = set(chocolates)
    m = len(flavour_count)
    if n == m:
        print(n - x)
    elif n - m < x:
        print(n - x)
    elif n - m >= x:
        print(m)
