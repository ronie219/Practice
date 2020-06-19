# Mr Pr in a Dilemma
for _ in range(int(input())):
    a, b, c, d = map(int, input().split())
    if a == b:
        print("Yes")
    elif c == d:
        print("No")
    elif (a - b) - (c - d) == 0:
        print("Yes")
    else:
        print("No")