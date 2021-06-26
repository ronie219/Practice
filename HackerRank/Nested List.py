

# Nested List
if __name__ == '__main__':
    data = []
    Fname = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        data.append([name, score])
    data = [['Harry', 8], ['Berry', 8.9], ['Tina', 9.5], ['Akriti', 10]]
    for i in range(len(data)):
        count = 0
        while count < len(data):
            if data[i][1] > data[count][1]:
                data[i],data[count] = data[count],data[i]
            else:
                pass
            count += 1
    low = []
    for i in data:
        low.append(i[1])
    low = set(low)
    low = (sorted(low))
    low = list(low)
    a = low[1]
    for i in data:
        if a in i:
            Fname.append(i[0])
    for el in sorted(Fname):
        print(el)