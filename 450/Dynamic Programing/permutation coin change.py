"""
1. You are given a number n, representing the count of coins.
2. You are given n numbers, representing the denominations of n coins.
3. You are given a number "amt".
4. You are required to calculate and print the number of permutations of the n coins using which the amount "amt" can be paid.
Note1 - You have an infinite supply of each coin denomination i.e. same coin denomination can be used for many installments in payment of "amt"
Note2 - You are required to find the count of permutations and not combinations i.e.
2 + 2 + 3 = 7 and 2 + 3 + 2 = 7 and 3 + 2 + 2 = 7 are different permutations of same combination. You should treat them as 3 and not 1.
"""
from collections import defaultdict


def coinChnage(coins, m, target):
    # we create a DP of target + 1 size in which we store no. of ways
    dp = [0 for _ in range(target + 1)]

    # we know we can make 0 rs. with one way
    dp[0] = 1
    ways = defaultdict(list)
    ways[0] = ['']

    for tar in range(1,target+1):
        for coin in coins:
            if tar-coin >= 0 and dp[tar-coin] > 0:
                dp[tar] += dp[tar-coin]
                for way in ways[tar-coin]:
                    ways[tar].append(way + str(coin))
    print(dp)
    print(ways)




if __name__ == '__main__':
    n = 7
    s = [2,3,5]
    m = 3
    coinChnage(s,m,n)