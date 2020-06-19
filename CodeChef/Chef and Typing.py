
# Chef and Typing
for _ in range(int(input())):
    second = 0
    s = []
    for i in range(int(input())):
        data = input()
        s.append(data)
        sec = 2
        l = ['d', 'f']
        r = ['j', 'k']
        for j in range(1, len(data)):
            if data[j - 1] in l and data[j] in l or data[j - 1] in r and data[j] in r:
                sec += 4
            else:
                sec += 2
        if s.count(data) > 1:
            sec = sec // 2
        second += sec
    print(second)