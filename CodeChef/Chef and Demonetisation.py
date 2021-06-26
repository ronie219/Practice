# Chef and Demonetisation
for _ in range(int(input())):
    S, N = map(int, input().split())
    coin_count = 0
    while S > 1:
        if N % 2 != 0:
            N = S - 1
        else:
            coin_count += S // N
            S = S % N
            N = S
    print(coin_count+1 if S == 1 else coin_count)
