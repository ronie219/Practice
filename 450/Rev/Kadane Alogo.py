arr = [4, 3, -2, 6, -14, 7, -1, 4, 5, 7, -10, 2, 9, -10, -5, -9, 6, 1]
max_sum = 0
for i in range(len(arr)):
    curr_sum = 0
    for j in range(i, len(arr)):
        curr_sum += arr[j]
        if max_sum < curr_sum:
            max_sum = curr_sum
print(max_sum)


def kadane(arr):
    total = 0
    curr = 0
    for idx in range(len(arr)):
        curr += arr[idx]
        if curr < 0:
            curr = 0
        if total < curr:
            total = curr
    print(total)


kadane(arr)
