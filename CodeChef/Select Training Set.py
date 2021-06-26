
# Select Training Set
for _ in range(int(input())):
    di = {}
    count = 0
    for j in range(int(input())):
        key, value = input().split()
        value = int(value)
        if key in di:
            if di[key] == value:
                di.update({key: value})
                count += 1
        elif key not in di:
            di.update({key: value})
            count += 1
        else:
            continue
    print(count)

t = int(input()) # right
for i in range(t):
    n = int(input())
    dic = {}
    res = 0
    for j in range(n):
        s, a = input().split()
        a = int(a)
        if s not in dic:
            dic[s] = [0, 0]
            print(dic)
        dic[s][a] += 1
    for j in dic.values():
        res += max(j)
    print(res)