def kthSmallest(arr, l, r, k):
    arr.sort()
    return arr[k]



print(kthSmallest([7, 10, 4, 3, 20, 15],0,0,3))

# 6
# 7 10 4 3 20 15
# 3