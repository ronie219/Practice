"""
In this problem, 
1. You are given a number n, which represents the length of a road. The road has n plots on it's each side.
2. The road is to be so planned that there should not be consecutive buildings on either side of the road.
3. You are required to find and print the number of ways in which the buildings can be built on both side of roads.
"""


def buildingArangeMent(n):
    # B B S B --> Wrong
    # B S S B --> Right

    # create dp, I know that if n == 1 the there is only one possiblity.
    buildingCount = 1
    SpaceCount = 1

    for _ in range(n-1):
        temp = buildingCount
        buildingCount = SpaceCount
        SpaceCount = temp + SpaceCount

    print((buildingCount + SpaceCount)**2)


if __name__ == '__main__':
    buildingArangeMent(38)
