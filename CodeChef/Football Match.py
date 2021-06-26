
from collections import Counter
# Football Match (Wrong)
# result = []
for _ in range(int(input())):
    l = []
    n = int(input())
    if n == 0:
        print("Draw")
    else:
        for _ in range(n):
            i = input()
            l.append(i)
            # if i in dis:
            #     dis[i] = dis[i] + 1
            # else:
            #     dis[i] = 1
        count = Counter(l)
        a = count.most_common()
        print(a[0])
        if a[0][1] == a[1][1]:
            print("Draw")
        elif a[0][1] > a[1][1]:
            print(a[0][0])
        else:
            print(a[1][0])
        # ls = [*dis.keys(),*dis.values()]
        # if ls[2] == ls[3]:
        #     result.append("Draw")
        # elif ls[2] > ls[3]:
        #     result.append(ls[0])
        # else:
        #     result.append(ls[1])


# FootBall (Correct)
# from collections import Counter
#
# for _ in range(int(input())):
#     n = int(input())
#     l = []
#     for i in range(n):
#         s = input()
#         l.append(s)
#     a = Counter(l)
#     print(a)
#     if n == 0:
#         print('Draw')
#         continue
#     b = a.most_common()[0][0]
#     c = a.most_common()[0][0]
#     print(b)
#     print(c)
#     if a.most_common()[0][1] != n // 2:
#         print(b)
#     else:
#         print('Draw')
