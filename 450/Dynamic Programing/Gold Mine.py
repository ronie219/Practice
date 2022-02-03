"""
1. You are given a number n, representing the number of rows.
2. You are given a number m, representing the number of columns.
3. You are given n*m numbers, representing elements of 2d array a, which represents a gold mine.
4. You are standing in front of left wall and are supposed to dig to the right wall. You can start from any row in the left wall.

5. You are allowed to move 1 cell right-up (d1), 1 cell right (d2) or 1 cell right-down(d3). 
"""

from os import path


def gold_mine(mine,m,n):
    
    # we create a dp 2d array in which we store in cell, how much gold i can collect from right to left
    dpmine = [[0 for _ in range(n)] for __ in range(m)]

    # as we know at the right colum we can collect the gold which equual to the cell 
    # because from there we cannot travel further right.
    # we will intialate the last colum with the mine last cell value.

    for ini in range(m):
        dpmine[ini][n-1] = mine[ini][n-1]
    
    # now we fill rest of the dp matrix on the basis of these values.
    # we move from top to down in the matrix as per filling the data and from right to left.

    for col in range(n-2,-1,-1):
        gold = []
        for row in range(m):
            if row - 1 >= 0: gold.append(dpmine[row - 1][col + 1]) # up-right
            gold.append(dpmine[row][col + 1]) # side value
            if row + 1 < m: gold.append(dpmine[row + 1][col + 1]) # down right
            dpmine[row][col] = max(gold) + mine[row][col]
    
    for i in dpmine:
        print(i)

if __name__ == '__main__':
    mine = [[0,1,4,2,8,2], 
            [4,3,6,5,0,4],
            [1,2,4,1,4,6],
            [2,0,7,3,2,2],
            [3,1,5,9,2,4],
            [2,7,0,8,5,1]] 
    rows = 6
    cols = 6
    print(gold_mine(mine, rows, cols))
