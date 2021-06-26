arr = [1, 2, 3, 4, 5, 6, 8, 10]
ele = 0
left = 0
right = len(arr) - 1
while left <= right:
    mid = (left + right) // 2
    if arr[mid] < ele:
        left = mid + 1
    elif arr[mid] > ele:
        right = mid -1
    else:
        print("Found at ", mid )
        break
else:
    print(-1)