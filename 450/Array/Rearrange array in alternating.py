arr = [-5, -2, 5, 2, 4, 7, 1, 8, 0, -8]
# arr = [1, 2, 3, -4, -1, 4]
end = len(arr) - 1
start = 0
while start <= end:
    if arr[start] < 0 and arr[end] >= 0:
        arr[end],arr[start] = arr[start],arr[end]
        start += 1
        end -= 1
    elif arr[start] >= 0:
        start += 1
    elif arr[end] < 0:
        end -= 1

print(arr)
# print("end",end)
# print("start",arr[start])
end = len(arr) - 1
start = 0
while start <= end:
    if arr[end] < 0 and arr[start] >= 0:
        arr[end],arr[start] = arr[start],arr[end]
        end -= 1
        start += 2
    else:
        break

print(arr)