X = 13
n = 6
arr = [1, 4, 45, 6, 10, 8]
arr.sort()

for i in range(n):
    start = i + 1
    end = n - 1
    expected_value = X - arr[i]
    while start < end:
        if expected_value < (arr[start] + arr[end]):
            end -= 1
        elif expected_value > (arr[start] + arr[end]):
            start += 1
        else:
            print(1)
            break