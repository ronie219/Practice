# def sort012(arr):
#     result = []
#     result.extend([0] * arr.count(0))
#     result.extend([1] * arr.count(1))
#     result.extend([2] * arr.count(2))
#     return result
#
#
# print(sort012([0, 2, 1, 2, 0]))

arr = [0,2,1, 0,1]
i = 0
j = 0
k = len(arr) -1
while j <= k:
    if arr[j] == 0:
        arr[i],arr[j] = arr[j],arr[i]
        i += 1
        j += 1
    elif arr[j] == 2:
        arr[j],arr[k] = arr[k],arr[j]
        k -= 1
        # j += 1
    else:
        j += 1
print(arr)