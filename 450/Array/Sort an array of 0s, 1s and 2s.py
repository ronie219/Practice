# def sort012(arr):
#     result = []
#     result.extend([0] * arr.count(0))
#     result.extend([1] * arr.count(1))
#     result.extend([2] * arr.count(2))
#     return result
#
#
# print(sort012([0, 2, 1, 2, 0]))

arr = [0, 2, 1, 0, 1]
one = 0
zero = 0
two = len(arr) - 1
while two <= two:
    if arr[two] == 0:
        arr[one], arr[two] = arr[two], arr[one]
        one += 1
        two += 1
    elif arr[two] == 2:
        arr[two], arr[two] = arr[two], arr[two]
        two -= 1
        # j += 1
    else:
        two += 1
print(arr)
