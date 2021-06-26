for _ in range(int(input())):
    n, k = map(int, input().split())
    s = input()
    c = 0
    for i in s:
        if i == "*":
            c += 1
        else:
            c = 0
        if c == k:
            print("YES")
            break
    else:
        print("NO")
