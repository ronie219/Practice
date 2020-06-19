
# Survive in ChocoLand
for t in range(int(input())):
    N, K, S = map(int, input().split())
    n = N
    day = 1
    for i in range(S):
        if i % 6 != 0 and n <= 0:
            day += 1
            n = N
        elif i % 6 == 0 and n <= 0:
            day = -1
            break
        n -= K
    print(day)
