string = input()
if len(string) <= 2:
    print("Invalid input")
else:
    counter = {}
    for i in string:
        if i in counter.keys() and i != " ":
            counter[i] += 1
        else:
            counter[i] = 1
    max_repetation = max(counter.values())
    for key,value in counter.items():
        if value == max_repetation:
            print(key, end= " ")