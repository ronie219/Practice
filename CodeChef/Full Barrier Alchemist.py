
# Full Barrier Alchemist
for _ in range(int(input())):
    N, H, Y1, Y2, L = map(int, input().split())
    barrier = []
    count = 0
    for i in range(N):
        barrier.append(tuple(map(int,input().split())))
    for i in barrier:
        if i[0] == 1:
            if H - Y1 <= i[1]:
                count += 1
            elif L > 1:
                L -= 1
                count += 1
            else:

                break
        if i[0] == 2:
            if Y2 >= i[1]:
                count += 1
            elif L > 1:
                L -= 1
                count += 1
            else:

                break
    print(count)
