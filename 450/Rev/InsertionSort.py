def insertionSort(arr):
    for idx in range(1, len(arr)):
        bidx = idx
        while bidx > 0 and arr[bidx] < arr[bidx-1]:
            arr[bidx], arr[bidx-1] = arr[bidx-1], arr[bidx]
            bidx -= 1


if __name__ == '__main__':
    arr = [11, 9, 29, 7, 100, 2, 11, 15, 28]
    insertionSort(arr)
    print(arr)
