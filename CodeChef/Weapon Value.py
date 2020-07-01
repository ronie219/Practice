# Weapon Value
for _ in range(int(input())):
    warrior = []
    for i in range(int(input())):
        warrior.append(input())
    winner = warrior[0]
    for i in range(1, len(warrior)):
        temp = ''
        for j, k in zip(winner, warrior[i]):
            if j == '1' and k == '1':
                temp += '0'
            elif j == '0' and k == '0':
                temp += '0'
            else:
                temp += '1'
        winner = temp
    print(winner.count('1'))
