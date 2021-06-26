arr = [1000, 11, 445, 1, 330, 3000]
max = arr[0]
min = arr[0]


for i in arr:
    if max < i:
        max = i
    elif min > i:
        min = i
print("max " + str(max))
print("min " + str(min))
