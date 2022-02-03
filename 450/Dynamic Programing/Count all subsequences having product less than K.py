def productSubSeqCount(arr, k):
    dp = [0 for _ in range(len(arr))]
    dp[0] = 1
    mulDp = [0 for _ in range(len(arr))]

    for idx in range(len(arr)):
        count = 0
        max_value = 0
        for bidx in range(idx - 1, -1, -1):
            if arr[bidx] < arr[idx] and mulDp[bidx] * arr[idx] < 10:
                count += 1
                if max_value < mulDp[bidx] * arr[idx]:
                    max_value = mulDp[bidx] * arr[idx]
        dp[idx] = count
        mulDp[idx] = max_value
    print(dp)


if __name__ == "__main__":
    arr = [1, 2, 3, 4]
    k = 10
    productSubSeqCount(arr, k)
