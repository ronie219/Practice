"""
1. You are given a number n, representing the number of houses.
2. In the next n rows, you are given 3 space separated numbers representing the cost of painting nth house with red or blue or green color.
3. You are required to calculate and print the minimum cost of painting all houses without painting any consecutive house with same color.
"""


def min_paint_cost(cost):
    min_red = cost[0][0]
    min_green = cost[0][1]
    min_blue = cost[0][2]

    for idx in range(1, len(cost)):
        red = min_red
        green = min_green
        blue = min_blue

        # we assign the min_ amount we need if we choose current idx colour i.e if we choose red
        # then we have to exclude the red from the previous cost that means we have to choose min blue and green.

        # we assgin for red
        min_red = min(green, blue) + cost[idx][0]

        # we assign for green
        min_green = min(red, blue) + cost[idx][1]

        # we assign for blue
        min_blue = min(red, green) + cost[idx][2]

    print(min(min_red, min_blue, min_green))


if __name__ == '__main__':
    n_house = 4
    colour_cost = []
    for _ in range(n_house):
        # tc [[1, 5, 7], [5, 8, 4], [3, 2, 9], [1, 2, 4]]
        colour_cost.append(list(map(int, input().split())))
    # print(colour_cost)
    min_paint_cost(colour_cost)
