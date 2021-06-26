# matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
matrix = [[1]]
target = 1
previous_arr = None

for i in matrix:
    if i[0] <= target:
        previous_arr = i
    else:
        break

if previous_arr is None or target not in previous_arr:
    print(False)
else:
    print(True)
