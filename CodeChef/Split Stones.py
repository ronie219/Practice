# Split Stones
for _ in range(int(input())):
    a, b, c, x, y = map(int,input().split())
    if a + b + c != x+y:
        print("NO")
    else:
        if min(a,b,c) <= min(x,y):
            print("YES")
        else:
            print("NO")
