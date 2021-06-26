nums = [1, 2, 3]
arr_len = len(nums) - 1
idx = -1
while 0 < arr_len:
    if nums[arr_len] > nums[arr_len - 1]:
        idx = arr_len
        break
    arr_len -= 1

if arr_len == -1:
    print(nums[::-1])
else:
    idx2 = idx
    for i in range(idx + 1, len(nums)):
        if nums[idx - 1] < nums[i] <= nums[idx2]:
            idx2 = i

    nums[idx - 1], nums[idx2] = nums[idx2], nums[idx - 1]
    arr1 = nums[0:idx]
    arr2 = nums[idx:]
    print(arr1 + arr2[::-1])
