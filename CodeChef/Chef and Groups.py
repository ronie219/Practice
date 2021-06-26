for _ in (range(int(input()))):
    a = input()
    group = 0
    pre= a[0]
    for i in range(1,len(a)):
        if a[i] == '0' and pre=='1':
            group += 1
        pre=a[i]

    if a[i] == '1':
        group += 1

    print(group)
