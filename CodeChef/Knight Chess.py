# Knight Chess
for _ in range(int(input())):
    knight = []
    for n in range(int(input())):
        knight.append(tuple(map(int, input().split())))
    king = list(map(int, input().split()))
    posible_king_place = [(king[0] + 1, king[1]), (king[0] - 1, king[1]), (king[0], king[1] + 1),
                          (king[0], king[1] - 1), (king[0] - 1, king[1] - 1), (king[0] + 1, king[1] + 1),
                          (king[0] + 1, king[1] - 1), (king[0] - 1, king[1] + 1)]

    for p in knight:
        if (p[0] + 1, p[1] + 3) in posible_king_place or (p[0] + 1, p[1] - 3) in posible_king_place or (
        p[0] - 1, p[1] - 3) in posible_king_place or (p[0] - 1, p[1] + 3) in posible_king_place:
            print("YES")
            break
    else:
        print("NO")