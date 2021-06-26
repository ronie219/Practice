
# Any or All
N = int(input())
n = list(map(int, input().split()))
bol = all([i > 0 for i in n])
if bol:
    bol2 = any([str(i) == (str(i)[::-1]) for i in n])
    print(bol2)
else:
    print(bol)