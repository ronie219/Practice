"""
1. You are given a number n, representing the number of friends.
2. Each friend can stay single or pair up with any of it's friends.
3. You are required to print the number of ways in which these friends can stay single or pair up.
E.g.
1 person can stay single or pair up in 1 way.
2 people can stay singles or pair up in 2 ways. 12 = 1-2, 12.
3 people (123) can stay singles or pair up in 4 ways. 123 = 1-2-3, 12-3, 13-2, 23-1.
"""

# recursive + memoization


def paring(num):
    # base case
    if num == 1 or num == 2:
        return num

    # memoisze
    if dp[num] != -1:
        return dp[num]

    # recusive intiution

    # for rest of the count we f(n) + n * f(n) * n
    # f(4) = f(3) + 2 * f(2)
    # f(4) = 1 - 234, 1 - 2 - 3 - 4, 1 - 23 -4, 1 - 2 - 34 + 12 - 3 -4, 12-34, 13-24, 13-2-4,14-23,14-2-3
    dp[num] = paring(num - 1) + (paring(num - 2) * (num - 1))
    return dp[num]


# itterative + bottom to top
def itterative_paring(num):
    dp = [None for _ in range(num + 1)]
    dp[1] = 1
    dp[2] = 2
    for idx in range(3, len(dp)):
        dp[idx] = dp[idx - 1] + (idx - 1) * dp[idx - 2]

    print(dp[-1])


if __name__ == "__main__":
    num = 5
    dp = [-1 for i in range(num + 1)]
    print(paring(num))
    itterative_paring(num)
