# Input: -12, 11, -13, -5, 6, -7, 5, -3, -6
# Output: -12 -13 -5 -7 -3 -6 11 6 5
arr = [-12, 11, -13, -5, 6, -7, 5, -3, -6]
i = 0
j = len(arr) - 1
while i < j:
    if arr[i] > 0:
        arr[i], arr[j] = arr[j], arr[i]
        j -= 1
        continue
    i += 1
print(arr)
