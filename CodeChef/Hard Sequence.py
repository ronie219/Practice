# Hard Sequence
for _ in range(int(input())):
    N = int(input())
    li = [0]
    if N > 1:
        for _ in range(N - 1):
            if li[-1] not in li[:-1]:
                li.append(0)
            else:
                index = 0
                for i in range(len(li) - 1):
                    if li[i] == li[-1]:
                        index = i + 1
                li.append(len(li) - index)
    print(li.count(li[N - 1]))
