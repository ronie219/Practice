# Deputy Chef
for _ in range(int(input())):
    N = int(input())
    attack = list(map(int, (input().split())))
    defence = list(map(int, (input().split())))
    t = -1
    for i in range(0, N - 1):
        if (attack[i - 1] + attack[i + 1]) < defence[i]:
            t = max(defence[i], t)
    if (attack[-2] + attack[0]) < defence[-1]:
        t = max(t, defence[-1])
    print(t)