"""
1. You are given a number n and a number k separated by a space, representing the number of houses and number of colors.
2. In the next n rows, you are given k space separated numbers representing the cost of painting nth house with one of the k colors.
3. You are required to calculate and print the minimum cost of painting all houses without painting any consecutive house with same color.
"""


def min_paint_cost(cost, house, colour):
    # In this DP we store min cost to colour the house if we include that colour
    dp = [[0 for _ in range(len(cost[0]))] for __ in range(len(cost))]

    # we inisiate the base case as to colour the 1st house min colour is requuired is list co colour cost
    for idx in range(colour):
        dp[0][idx] = cost[0][idx]

    for idx in range(1, house):
        for col in range(colour):
            dp[idx][col] = min(dp[idx - 1][0:col]+dp[idx - 1]
                               [col:]) + cost[idx][col]

    print(min(dp[-1]))


if __name__ == '__main__':
    houses, colour = 316, 6
    cost_arr = []
    for _ in range(houses):

        cost_arr.append(list(map(int, (input().rstrip()).split())))
    min_paint_cost(cost_arr, houses, colour)
