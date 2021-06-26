stack_1 = []
stack_2 = []
for _ in range(int(input())):
    opertion = tuple(map(int,input().split()))
    if opertion[0] == 1:
        stack_1.append(opertion[1])
    elif opertion[0] == 2:
        if len(stack_2) == 0:
            while len(stack_1) != 0:
                stack_2.append(stack_1.pop())
        stack_2.pop()
    else:
        if len(stack_2) == 0:
            while len(stack_1) != 0:
                stack_2.append(stack_1.pop())
        print(stack_2[-1])

