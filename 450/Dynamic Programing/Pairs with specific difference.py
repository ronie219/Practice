def maxSumPairWithDifferenceLessThanK(arr, N, K):
    arr.sort()
    pointer = N - 1
    max_sum = 0
    print(arr)
    while pointer > 0:
        if arr[pointer] - arr[pointer - 1] < K:
            max_sum += arr[pointer] + arr[pointer - 1]
            pointer -= 2
        else:
            pointer -= 1
    return max_sum


if __name__ == "__main__":
    arr = [21, 2, 21, 25, 29, 3, 5, 13, 11, 22, 17]
    k = 1

    print(maxSumPairWithDifferenceLessThanK(arr, len(arr), k))
