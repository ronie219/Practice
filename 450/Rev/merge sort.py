def mergeSort(arr):
    if len(arr) <= 1:
        return
    mid = len(arr) // 2
    # left = mergeSort(arr[:mid])
    # right = mergeSort(arr[mid:])
    # return mergeSortedarray(left, right)
    left = arr[:mid]
    right = arr[mid:]
    mergeSort(left)
    mergeSort(right)
    mergeSortedarray(left, right, arr)


def mergeSortedarray(ar1, ar2, arr):
    # sorted_arry = []
    idx1 = idx2 = k = 0
    while idx1 < len(ar1) and idx2 < len(ar2):
        if ar1[idx1] < ar2[idx2]:
            # sorted_arry.append(ar1[idx1])
            arr[k] = ar1[idx1]
            idx1 += 1
        else:
            # sorted_arry.append(ar2[idx2])
            arr[k] = ar2[idx2]
            idx2 += 1
        k += 1
    if len(ar1) > idx1:
        while len(ar1) > idx1:
            # sorted_arry.append(ar1[idx1])
            arr[k] = ar1[idx1]
            idx1 += 1
            k += 1
    elif len(ar2) > idx2:
        while len(ar2) > idx2:
            # sorted_arry.append(ar2[idx2])
            arr[k] = ar2[idx2]
            idx2 += 1
            k += 1
    # return sorted_arry


if __name__ == '__main__':
    arr = [10, 3, 15, 7, 8, 23, 98, 23]
    print(mergeSort(arr))
    # mergeSortedarray([1, 2, 4, 5, 7], [3, 6, 8, 10])
    print(arr)
