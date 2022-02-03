def bst(arr,start, end, num):
    if start > end:
        return
    mid = (end - start // 2) + start
    if arr[mid] < num:
        return bst(arr,mid + 1, end, num)
    elif arr[mid] > num:
        return bst(arr,start, mid - 1, num)
    else:
        return mid

arr = [1,2,2,3,4,5]
# print(bst(arr,0,len(arr)-1, 8))
