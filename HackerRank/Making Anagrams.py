a = sorted(list(input()))
b = sorted(list(input()))

counrt = {}
for i in a:
    if i not in counrt:
        counrt[i] = 1
    else:
        counrt[i] += 1

for i in b:
    if i not in counrt:
        counrt[i] = -1
    else:
        counrt[i] -= 1

print(sum([abs(i) for i in counrt.values()]))
