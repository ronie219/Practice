<<<<<<< HEAD
"""
data = []
for _ in range(int(input())):
    data.append(str(input()))


for i in data:
    if i [::-1] == i:
        if len(i) % 2 == 0:
            print("YES EVEN")
        else:
            print("YES ODD")
    else:
        print("NO")
"""
#
# for _ in range(int(input())):
#     number = int(input())
#     checkpoint = list(map(int,input().split()))
#     petrol = list(map(int,input().split(" ")))
#     output = 0
#     for i,j in zip(checkpoint,petrol):
#         output = output + (i * j)
#     print(output)
#

#
# # Covid19 Spread
# def worstcase(distance):
#     l = list()
#     count = 1
#     for i in distance:
#         if i + 1 in distance or i + 2 in distance:
#             count += 1
#         else:
#             l.append(count)
#             count = 1
#         l.append(count)
#     return max(l)
#
#
# def bestcase(distance):
#     l = []
#     count = 1
#     for i in range(len(distance) - 1):
#         if (distance[i + 1] - distance[i]) <= 2:
#             # print(distance[i+1] - distance[i])
#             count += 1
#         else:
#             l.append(count)
#             count = 1
#             continue
#         # print(count)
#     l.append(count)
#     return min(l)
#
# ls = []
# for _ in range(int(input())):
#     N = input()
#     distance = list(map(int, input().split()))
#     a = (bestcase(distance), worstcase(distance))
#     ls.append(a)
#
# for i in ls:
=======
"""
data = []
for _ in range(int(input())):
    data.append(str(input()))


for i in data:
    if i [::-1] == i:
        if len(i) % 2 == 0:
            print("YES EVEN")
        else:
            print("YES ODD")
    else:
        print("NO")
"""
#
# for _ in range(int(input())):
#     number = int(input())
#     checkpoint = list(map(int,input().split()))
#     petrol = list(map(int,input().split(" ")))
#     output = 0
#     for i,j in zip(checkpoint,petrol):
#         output = output + (i * j)
#     print(output)
#

#
# # Covid19 Spread
# def worstcase(distance):
#     l = list()
#     count = 1
#     for i in distance:
#         if i + 1 in distance or i + 2 in distance:
#             count += 1
#         else:
#             l.append(count)
#             count = 1
#         l.append(count)
#     return max(l)
#
#
# def bestcase(distance):
#     l = []
#     count = 1
#     for i in range(len(distance) - 1):
#         if (distance[i + 1] - distance[i]) <= 2:
#             # print(distance[i+1] - distance[i])
#             count += 1
#         else:
#             l.append(count)
#             count = 1
#             continue
#         # print(count)
#     l.append(count)
#     return min(l)
#
# ls = []
# for _ in range(int(input())):
#     N = input()
#     distance = list(map(int, input().split()))
#     a = (bestcase(distance), worstcase(distance))
#     ls.append(a)
#
# for i in ls:
>>>>>>> 7f688d62f8ef42d5982882d6981075fb426ea81a
#     print(*i)