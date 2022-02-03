"""
1. You are given a number n representing the length of a floor space which is 2m wide. It's a 2 * n board.
2. You've an infinite supply of 2 * 1 tiles.
3. You are required to calculate and print the number of ways floor can be tiled using tiles.
"""

# recurssion


def tiling(floor):
    # base case
    if floor == 1 or floor == 2:
        return floor

    # recursive intution
    return tiling(floor - 1) + tiling(floor-2)


if __name__ == '__main__':
    print(tiling(4))
