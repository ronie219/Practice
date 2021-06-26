# Approach 1: Hashing
# arr = [1,3,4,2,2]
# s = set()
# for i in arr:
#     if i not in s:
#         s.add(i)
#     else:
#         print(i)
#
#
# Approach 2: Sorting
arr = [1,3,4,2,2]
arr.sort()
start = 0
while start < len(arr) - 1:
    if arr[start] == arr[start + 1]:
        print(arr[start])
    start += 1