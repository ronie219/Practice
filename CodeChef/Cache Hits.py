# Cache Hits
for _ in range(int(input())):
    N, B, M = map(int, input().split())
    m = list(map(int, input().split()))
    count = 1
    for j in range(1, M):
        if (m[j - 1]) // B != (m[j]) // B:
            count += 1
    print(count)
