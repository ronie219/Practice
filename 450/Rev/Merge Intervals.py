def merge(arr):
    arr.sort(key=lambda x: x[0])
    final_schedule = []
    start = arr[0][0]
    end = arr[0][1]
    idx = 1
    while idx < len(arr):
        if start <= arr[idx][0] <= end or arr[idx][0] <= end <= arr[idx][1]:
            end = max(arr[idx][1], end)
            idx += 1
        else:
            final_schedule.append((start, end))
            start = arr[idx + 1][0]
            end = arr[idx + 1][1]
            idx += 2

    print(final_schedule)


arr = [(22, 28), (1, 8), (25, 27), (14, 19), (27, 30), (5, 12)]
merge(arr)
