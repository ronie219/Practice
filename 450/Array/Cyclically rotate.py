# n = 8
# arr = [9, 8, 7, 6, 4, 2, 1, 3]
n = 5
arr = [1, 2, 3, 4, 5]
i = len(arr) - 1
while i >= n-1:
    arr.insert(0,arr.pop())
    i -= 1
print(arr)