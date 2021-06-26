

# time complexity n * M
def merge_array(arr1,arr2):
    arr_idx1 = 0
    arr_idx2 = 0
    while arr_idx1 < len(arr1) and arr_idx2 < len(arr2):
        if arr1[arr_idx1] <= arr2[arr_idx2]:
            arr_idx1 += 1
        else:
            arr1[arr_idx1],arr2[arr_idx2] = arr2[arr_idx2],arr1[arr_idx1]
            for idx in range(arr_idx2,len(arr2)-1):
                if arr2[idx] > arr2[idx + 1]:
                    arr2[idx],arr2[idx + 1] = arr2[idx+1],arr2[idx]
                else:
                    break
            arr_idx2 += 1
# print(merge_array(arr1,arr2))


# insertion sort

def insertion_SORT(arr1, arr2,m,n):
    if arr2[0] > arr1[-1]:
        return
    arr1_idx = m-1
    arr2_idx = n-1
    while arr2_idx >= 0:
        last = arr1[-1]
        while arr1_idx < 0 and arr1[arr1_idx + 1] > arr2[arr2_idx]:
            arr1[arr1_idx] = arr1[arr1_idx + 1]
            arr1_idx -= 1
        arr1[arr1_idx] = arr2[arr2_idx]
        arr2[arr2_idx] = last
        arr2_idx -= 1

arr2 = [0, 2, 6, 8, 9]
arr1 = [1, 3, 5, 7]
insertion_SORT(arr1,arr2,4,5)
