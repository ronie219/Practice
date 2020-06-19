
# Piling Up!
from collections import deque
for _ in range(int(input())):
    number = int(input())
    len_cude = list(map(float,input().split()))
    lst = deque(len_cude)
    rm = lst.pop()
    lm = lst.popleft()
    stack = max(lm, rm)
    flag = False
    while len(lst) > 0:
        if rm <= lm <= stack:
            stack = lm
            lm = lst.popleft()

        elif lm < rm <= stack:
            stack = rm
            rm = lst.pop()
        else:
            flag = True
            break
    if flag:
        print("Yes")
    else:
        print("No")