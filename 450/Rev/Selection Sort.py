def findMin(arr, idx):
    minIdx = None
    minEle = float('inf')
    for i in range(idx, len(arr)):
        if arr[i] < minEle:
            minEle = arr[i]
            minIdx = i
    return minIdx


def selectionSort(arr):
    for idx in range(len(arr)):
        minIdx = findMin(arr, idx)
        arr[idx], arr[minIdx] = arr[minIdx], arr[idx]


if __name__ == '__main__':
    ar = [11, 9, 29, 7, 100, 2, 11, 15, 28]
    selectionSort(ar)
    print(ar)
