def subArrayExists(arr, n):
    till_sum = arr[0]
    sum_count = {arr[0]}
    for i in arr[1:]:
        if i == 0: return True
        till_sum += i
        if till_sum in sum_count or till_sum == 0: return True
        sum_count.add(till_sum)

    return False

# arr = [1, 2, 3, 4, 5]
arr = [4, 2,-3, 1, 6]
# arr = [10, -10]

print(subArrayExists(arr, 5))
