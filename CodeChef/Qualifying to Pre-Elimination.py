# Qualifying to Pre-Elimination
for _ in range(int(input())):
    n, k = map(int, input().split())
    N = list(map(int, input().split()))
    N.sort(reverse=True)
    while 1:
        if k == n or N[k] != N[k - 1]:
            break
        k += 1
    print(k)
