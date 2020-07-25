for _ in range(int(input())):
    N = int(input())
    String = list(map(int,input().split()))
    result = 0
    for i in range(N-1):
        result += abs(String[i] - String[i + 1]) - 1
    print(result)