<<<<<<< HEAD
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
=======
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
>>>>>>> 7f688d62f8ef42d5982882d6981075fb426ea81a
            print(key, end= " ")