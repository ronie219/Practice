# When to take medicine
for _ in range(int(input())):
    mounth = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    yyyy, mm, dd = map(int, input().split(":"))
    if yyyy % 4 == 0:
        if yyyy % 100 == 0 and yyyy % 400 == 0:
            mounth.update({2: 29})
        elif yyyy % 100 == 0 and yyyy % 400 !=0:
            mounth.update({2: 28})
        else:
            mounth.update({2: 29})
    pill = 0
    temp_bool = True
    if dd % 2 == 0:
        while temp_bool:
            for i in range(dd, mounth[mm] + 1):
                if i % 2 == 0:
                    pill += 1
            if mounth[mm] % 2 == 0:
                mm += 1
                dd = 2
            else:
                temp_bool = False
    else:
        while temp_bool:
            for i in range(dd, mounth[mm] + 1):
                if i % 2 == 1:
                    pill += 1
            if mounth[mm] % 2 == 0:
                mm += 1
                dd = 1
            else:
                temp_bool = False
    print(pill)
