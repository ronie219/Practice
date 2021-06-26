n = 20
m = 10
arr1 = [1, 1, 1, 2, 3, 5, 7, 7, 7, 9, 9, 13, 13, 14, 14, 17, 17, 19, 20, 20]
arr2 = [3, 5, 7, 9, 10, 12, 13, 14, 20, 20]

j = m - 1
while j > 0:
    last = arr1[-1]
    i = n - 2
    while i != 0:
        if arr1[i] <= arr2[j]:
            arr1[i + 1] = arr2[j]
        arr1[i + 1] = arr2[j]
        i -= 1
    arr2[j] = last
    j -= 1
print(arr1 + arr2)
