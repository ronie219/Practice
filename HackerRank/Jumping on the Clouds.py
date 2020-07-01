# Jumping on the Clouds
def jumpingOnClouds(n, c):
    i = 0
    path = 0
    while i < len(c):
        if i + 2 < len(c) and c[i + 2] == 0:
            path += 1
            i += 2
        elif i + 1 < len(c) and c[i + 1] == 0:
            path += 1
            i += 1
        else:
            i += 1
    return path


n = int(input())
c = list(map(int, input().rstrip().split()))
print(jumpingOnClouds(n, c))
