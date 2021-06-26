for _ in range(int(input())):
    N, M = map(int,input().split())
    X, Y = map(int,input().split())
    result = ""
    for i in range(N):
        string = input()
        if string.count("F") >= X or (string.count("F") == X - 1 and string.count("P")) >= Y:
            result += "1"
        else:
            result += "0"
    print(result)