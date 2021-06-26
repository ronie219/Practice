arr = [30, 8, 23, 6, 10, 9, 31, 7, 19, 20, 1, 33, 21, 27, 28, 3, 25, 26]
n = 18
sumo = 86

count = 0
arr.sort()
for i in range(n):
    left = i + 1
    right = n - 1
    while left < right:
        if arr[i] + arr[left] + arr[right] >= sumo:
            right -= 1
        else:
            count += (right - left)
            left += 1


print(count)