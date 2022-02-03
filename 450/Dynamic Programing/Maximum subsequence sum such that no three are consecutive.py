def maxSumWO3Consec(arr, n, a):
    till_sum = [0 for _ in range(n)]  # we store the max sum till that point or index.
    till_sum[0] = arr[0]
    till_sum[1] = arr[1] + arr[0]
    till_sum[2] = max(max(arr[1] + arr[2], arr[0] + arr[2]), till_sum[1])

    for idx in range(3, n):

        option1 = till_sum[idx - 1]  # exclude idx
        option2 = till_sum[idx - 2] + arr[idx]  # exlcude just before the idx
        option3 = (
            till_sum[idx - 3] + arr[idx] + arr[idx - 1]
        )  # exclude just two before idx

        till_sum[idx] = max(option1, option2, option3)

    print(till_sum[-1])


def maxSumWO3Consec(arr, n, memo):

    if memo[n] != -1:
        return memo[n]

    if n == 0:
        memo[n] = arr[0]
        return arr[0]

    if n == 1:
        memo[1] = arr[0] + arr[1]
        return arr[0] + arr[1]

    if n == 2:
        memo[n] = max(max(arr[0] + arr[2], arr[1] + arr[2]), arr[0] + arr[1])
        return max(max(arr[0] + arr[2], arr[1] + arr[2]), arr[0] + arr[1])

    # abc
    option1 = maxSumWO3Consec(arr, n - 1, memo)  # exclude 1 ab
    option2 = maxSumWO3Consec(arr, n - 2, memo) + arr[n]  # exclude 2 ac
    option3 = arr[n - 1] + maxSumWO3Consec(arr, n - 2, memo) + arr[n]  # exclude 3 bc
    memo[n] = max(option2, option1, option3)
    return memo[n]


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7, 8]
    n = len(arr)
    memo = [-1 for i in range(n)]
    print(maxSumWO3Consec(arr, n - 1, memo))
