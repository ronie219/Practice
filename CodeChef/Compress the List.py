# Compress the List
for _ in range(int(input())):
    n = int(input())
    N = list(map(int, input().split()))
    i = 0
    result = []
    while i < n:
        temp = [N[i]]
        for j in range(i,):
            if N[j] == N[j+1]:
                temp.append(N[j])
                i += 1
            else:
                temp.append(N[i])
                break
        else:
            i += 1
        result.append(temp)
    print(result)