from collections import defaultdict


def count(coins, noc, total ):

    # insilize the DP array with 0 and we know that we can make sum = 0 with one possible way.
    dp = [0 for _ in range(total + 1)]
    dp[0] = 1

    ways = defaultdict(list)
    ways[0].append('')

    # loop through the all the coins 1 --> 2 ---> 3
    for idx in range(noc):
        coin = coins[idx]

        # it will check how  many possible ways are present to create the sum
        for way in range(coin,len(dp)):
            dp[way] += dp[way-coin]

            # this help to create pattern of coin requred for creating possbile sum.
            for pattern in range(-1,-(dp[way-coin]+1),-1):
                string = ways[way-coin][pattern]
                ways[way].append(string + str(coin))
    print(ways)
    print(dp)

if __name__ == '__main__':
    n = 4
    s = [1,2,3]
    m = 3
    count(s,m,n)