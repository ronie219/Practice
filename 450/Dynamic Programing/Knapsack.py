"""
# Itterative
def Knapsack(W, wt, val, n):
    dp = [[0 for _ in range(W+1)] for __ in range(n+1)]

    # initilize the base case or the initial case in the DP array.

    # we already initilize the dp arry with Zero. So no need to run the inisialize the dp array.
    print(dp)
    for row in range(1,n+1):
        for col in range(1,W+1):
            if wt[row-1] <= col:
                # we take max of the value if we take the item or not take the item.
                with_item = val[row-1] + dp[row-1][col-wt[row-1]]
                without_item = dp[row-1][col]
                dp[row][col] =  max(with_item, without_item)
            else:
                dp[row][col] =  dp[row-1][col]
    print(dp)
    return dp[n][W]
    """

# Recursive
def Knapsack(W, wt, val, n):

    memoization = {}
    
    # recurrive function 
    def _solve(capacity,weight,value,idx):
        if capacity == 0 or idx == 0:
            return 0
        if (capacity, idx) in memoization.keys(): return memoization[(capacity, idx)]
        # we choose one item
        if capacity-weight[idx-1] >= 0:
            with_item = value[idx-1] + _solve(capacity-weight[idx-1], weight, value, idx-1)
            without_item = _solve(capacity, weight, value, idx-1)
            memoization[(capacity, idx)] = max(with_item, without_item)
            return memoization[(capacity, idx)]
        else:
            memoization[(capacity, idx)] = _solve(capacity, weight, value, idx-1)
            return memoization[(capacity, idx)]
    
    return _solve(W, wt, val, n)

if __name__ == '__main__':
    N = 58
    W = 41
    values = [57,95,13,29,1,99,34,77,61,23,24,70,73,88,33,61,43,5,41,63,8,67,20,72,98,59,46,58,64,94,97,70,46,81,42,7,1,52,20,54,81,3,73,78,81,11,41,45,18,94,24,82,9,19,59,48,2,72]
    weight = [83,84,85,76,13,87,2,23,33,82,79,100,88,85,91,78,83,44,4,50,11,68,90,88,73,83,46,16,7,35,76,31,40,49,65,2,18,47,55,38,75,58,86,77,96,94,82,92,10,86,54,49,65,44,77,22,81,52]
    print(Knapsack(W, weight, values, N))