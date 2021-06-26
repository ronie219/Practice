string = []
queies = []

for _ in range(int(input())):
    string.append(input())

for _ in range(int(input())):
    queies.append(input())

for i in queies:
    print(string.count(i))

