def quick_sort(low, high, arr):
    if high - low < 2:return

    pivot = low
    start = low
    end = high

    while start <= end:
        if arr[start] <= arr[pivot]:
            start += 1
            continue
        elif arr[end] >= arr[pivot]:
            end -= 1
            continue
        arr[start], arr[end] = arr[end],arr[start]

    arr[end],arr[pivot] = arr[pivot],arr[end]
    quick_sort(low,end,arr)
    quick_sort(start,high,arr)

numbers = [10, 16, 8, 12, 15, 6, 3, 9, 5]
print(numbers)
quick_sort(0, len(numbers) - 1, numbers)
print(numbers)
