def partition(arr, low, high):
    pivot_idx = low
    low = low + 1
    while low < high:
        while low < len(arr) and arr[pivot_idx] >= arr[low]:
            low += 1
        while arr[pivot_idx] < arr[high]:
            high -= 1
        if low < high:
            arr[low], arr[high] = arr[high], arr[low]
    arr[high], arr[pivot_idx] = arr[pivot_idx], arr[high]

    return high


def quickSort(arr, start, end):
    if start < end:
        pi = partition(arr, start, end)
        quickSort(arr, start, pi-1)
        quickSort(arr, pi + 1, end)


if __name__ == '__main__':
    arr = [11, 9, 29, 7, 2, 15, 28]
    quickSort(arr, 0, len(arr)-1)
    print(arr)
