"""
1. You are given a number N.
2. You have to find the minimum number of squares that sum to N.
3. You can always represent a number as a sum of squares of other numbers.
For eg - In worst case N can be represented as (1*1) + (1*1) + (1*1)..... N times.
"""


def minSquare(num):
    # we create a dp in which we keep the min number of sq required to make that number.
    dp = [0 for _ in range(num+1)]
    dp[0] = 0
    dp[1] = 1

    for idx in range(2, num+1):
        min_sq = float('inf')
        for i in range(1, idx):
            if idx - (i * i) >= 0:
                if min_sq > dp[idx-(i*i)]:
                    min_sq = dp[idx-(i*i)]
            else:
                break
        dp[idx] = min_sq + 1
    print(dp[-1])


if __name__ == '__main__':
    minSquare(100007)
