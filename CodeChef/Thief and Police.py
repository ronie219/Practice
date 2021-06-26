for _ in range(int(input())):
    N, M = map(int, input().split())
    x, y = map(int, input().split())
    a, b = map(int, input().split())
    theif = N - x + M - y
    police = N - a + M - b - min(M - b, N - a)
    print("YES") if theif <= police else print("NO")
