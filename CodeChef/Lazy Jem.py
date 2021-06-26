# Lazy Jem
for _ in range(int(input())):
    N, B, M = list(map(int, input().split()))
    total_time = 0
    while N:
        if N % 2 == 0:
            total_time += (N // 2) * M
            N = N // 2
        else:
            total_time += ((N + 1) // 2) * M
            N = N // 2
        total_time += B
        M = M * 2
    print(int(total_time)-B)