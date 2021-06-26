N = 9
# arr = [1, 2, 3, 6, 5, 4]
arr = [1,5,8,4,7,6,5,3,1]
end = N-1
idx = None

while end > 0:
    if arr[end] > arr[end-1]:
        idx = end
        break
    end -= 1
if idx is None:
    print(arr[::-1])
else:
    target_ele = idx - 1
    minimum_number = idx
    while idx < N:
        if arr[target_ele] < arr[idx] and arr[idx] < arr[minimum_number]:
            minimum_number = idx
        idx += 1
    start = target_ele + 1
    end = N-1
    while start <= end:
        arr[start],arr[end] = arr[end], arr[start]
        start += 1
        end -= 1
    print(arr)
