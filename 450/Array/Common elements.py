n1 = 6
A = [1, 5, 10, 20, 40, 80]
n2 = 5
B = [6, 7, 20, 80, 100]
n3 = 8
C = [3, 4, 15, 20, 30, 70, 80, 120]

tracker = {}
for i in A:
    if i in tracker.keys():
        tracker[i].add("A")
    else:
        tracker[i] = {"A"}

for i in B:
    if i in tracker.keys():
        tracker[i].add("B")
    else:
        tracker[i] = {"B"}

for i in C:
    if i in tracker.keys():
        tracker[i].add("C")
    else:
        tracker[i] = {"C"}
output = []
for keys,values in tracker.items():
    if len(values) == 3:
        output.append(keys)
print(output)