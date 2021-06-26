
def chef_dish(le,N):
    s = set(N)
    d = dict()
    for i in s:
        count = 0
        temp = le - 1
        boolen = True
        while boolen:
            if temp <= 0:
                boolen = False
            if N[temp] == i:
                temp -= 2
                count += 1
            else:
                temp -= 1
        d[i] = count
    a = [key for key in d if d[key] == max(d.values())]
    return min(a)


result = list()
for _ in range(int(input())):
    number = int(input())
    l = list(map(int, input().split()))
    result.append(chef_dish(number,l))
for i in result:
    print(i)
