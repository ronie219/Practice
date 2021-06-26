socks = list(map(int, input().split()))
if len(set(socks)) != 3:
    print("YES")
else:
    print("NO")
