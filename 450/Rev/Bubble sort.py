def BubbleSort(arr):
    size = len(arr)
    for _ in range(size):
        swaped = False
        for idx in range(size-1):
            print(idx)
            if arr[idx] > arr[idx + 1]:
                arr[idx], arr[idx + 1] = arr[idx + 1], arr[idx]
                swaped = True
        if not swaped:
            break


if __name__ == '__main__':
    ar = [5, 9, 2, 1, 67, 34, 88, 34]
    ar = [1, 2, 3, 4, 5, 6, 7, 89, ]
    ar = ['Abhishek', 'Rohit', 'Aakash', 'Biswas', 'Hello']
    print(ar)
    BubbleSort(ar)
    print(ar)
