arr = [-1, 1, -2, 0, 10, 3, 4, 5, 17]

for i in range(1,len(arr)):
    print(i,arr[i])
    j = i-1
    ele = arr[i]
    while j >= 0:
        if arr[j] > ele:
            arr[j+1] = arr[j]
            j -= 1
        else:
            break
        print(arr)
    arr[j+1] = ele
    print("Final", arr)

print(arr)
