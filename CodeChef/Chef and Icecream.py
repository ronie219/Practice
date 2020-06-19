
# Chef and Icecream
for t in range(int(input())):
    N = int(input())
    money = list(map(int, input().split()))
    ten = []
    five = []
    for m in money:
        if m == 5:
            five.append(m)
        if m == 10:
            try:
                ten.append(m)
                five.pop()
            except IndexError:
                print("NO")
                break
        if m == 15:
            try:
                ten.pop()
            except IndexError:
                print("NO")
                break
    else:
        print("YES")