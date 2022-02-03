def maxProduct(arr):
    # we take to var in which we store mi = min till now, and ma = max till now
    # we use these two because if any -ve value occur then the least become the greatest and the
    # greatest become the least one.
    ma = arr[0]
    mi = arr[0]
    answer = arr[0]

    for idx in range(1, len(arr)):

        if arr[idx] <= 0:
            ma, mi = mi, ma
        ma = max(arr[idx], arr[idx] * ma)
        mi = min(arr[idx], arr[idx] * mi)
        answer = max(answer, ma)
    return answer


arr = [6, -3, -10, 0, 2]
print(maxProduct(arr))
