def findSubArrays(arr, n):
    dp = {0:1}
    count = 0
    till_sum = 0
    for ele in arr:
        till_sum += ele
        if till_sum in dp.keys():
            count += dp[till_sum]
            dp[till_sum] += 1
        else:
            dp[till_sum] = 1

    print(dp)
    print(count)

findSubArrays([6,-1,-3,4,-2,2,4,6,-12,-7],6)
