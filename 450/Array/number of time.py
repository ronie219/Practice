arr = [3, 1, 2, 2, 1, 2, 3, 3]
counter = {}
k = 4
for i in arr:
    if i in counter.keys():
        counter[i] += 1
    else:
        counter[i] = 1
output = []

for key, value in counter.items():
    if value > len(arr) // k:
        output.append(key)
print(output)

