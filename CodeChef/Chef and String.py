# Chef and String
for t in range(int(input())):
    S = input()
    pair = 0
    count = 0
    while count < len(S) - 1:
        if S[count] == 'x' and S[count + 1] == 'y' or S[count] == 'y' and S[count + 1] == 'x':
            pair += 1
            count += 2
        else:
            count += 1
    print(pair)
