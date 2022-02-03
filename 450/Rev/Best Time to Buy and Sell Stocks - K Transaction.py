def Profit(arr, k):
    # we use the dp to store the amount of profit we store on an paritular date and within transaction.
    dp = [[0 for __ in range(len(arr))] for _ in range(k)]
    # for intial when the transaction = 0 or the day = 0 the profit = 0
    for idx in range(1, len(dp)):
        for idx1 in range(1, len(dp[0])):
            profit = dp[idx][idx1-1]
            for j in range(idx1):
                profit = max(arr[idx1] - arr[j]+dp[idx-1][j], profit)
            dp[idx][idx1] = profit
    print(dp[-1][-1])


if __name__ == '__main__':
    arr = [9, 6, 7, 6, 3, 8]
    k = 3
    Profit(arr, k)
