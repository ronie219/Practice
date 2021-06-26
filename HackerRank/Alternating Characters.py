for i in range(int(input())):
    deletetion = 0
    string = input()
    for j in range(len(string) - 1):
        if string[j] == string[j+1]:
            deletetion += 1
    print(deletetion)