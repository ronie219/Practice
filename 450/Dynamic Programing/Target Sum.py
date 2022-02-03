"""
1. You are given a number n, representing the count of elements.
2. You are given n numbers.
3. You are given a number "target".
4. You are required to calculate and print true or false, if there is a subset the elements of which add up to "target" or not.
"""


# itterative using 2d matrix
def target_sum_i(arr,n, target):

    # dp array
    dp = [[None for _ in range(target + 1)] for __ in range(n+1)]

    # ini dp with for wmpty subset
    for idx in range(target+1):
        dp[0][idx] = False

    # ini dp with the base case for 0 sum
    for idx in range(n+1):
        dp[idx][0] = True

    # now we fill the data for rest of the result in DP

    for row in range(1, n+1):
        for col in range(1, target+1):
            # in first case we will try to include the item
            if col - arr[row-1] < 0:
                dp[row][col] = dp[row-1][col]
            else:
                item_take = dp[row - 1][col - arr[row-1]]
                item_refused = dp[row-1][col]
                dp[row][col] = item_refused or item_take

    return dp[n][target]


# recursive (no need of memoize evey call is differnet)
def target_sum_r(arr, n, target, step=0):
    # base case 
    if target == 0 : return True
    if step == n: return False

    # recusive intution
    # option 1 is select that item
    if target - arr[step] >= 0:
        take_item = target_sum_r(arr, n, target-arr[step], step+1) 
        #option 2 is not to select that item
        not_take_item = target_sum_r(arr, n, target,step + 1)
        return take_item or not_take_item
    # if target sum is less that arr value then we have to exclude it.

    return target_sum_r(arr, n, target,step + 1)

if __name__ == '__main__':
    tar = 10
    arr = [4,7,2,1,3]
    n = 5
    print(target_sum_i(arr,n, tar))
    print(target_sum_r(arr,n, tar))