# Ada and the Staircase
for _ in range(int(input())):
    N, K = map(int, input().split())
    H = list(map(int, input().split()))
    stair = 0
    for i in range(len(H) - 1):
        if (H[i + 1] - H[i]) % K == 0:
            stair += ((H[i + 1] - H[i]) // K)-1
        else:
            stair += ((H[i + 1] - H[i]) // K)
    print(stair)
