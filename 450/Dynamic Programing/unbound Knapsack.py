def unboundKnapsack(W, wt, val, n):

    # itterative + tablulation
    dp = [0 for _ in range(W + 1)]
    # We know that dp[0] = 0 because if there is no space then max profit you can earn == 0

    for idx in range(1,len(dp)):
        profit = [0]
        for wtidx in range(n):
            if idx - wt[wtidx] >= 0:
                profit.append(dp[idx - wt[wtidx]] + val[wtidx])
        dp[idx] = max(profit)
    
    print(dp)

if __name__ == '__main__':
    N = 5
    W = 7
    values = [15,14,10,45,30]
    weight = [2,5,1,3,4]
    print(unboundKnapsack(W, weight, values, N))