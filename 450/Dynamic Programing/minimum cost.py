"""
1. You are given a number n, representing the number of rows.
2. You are given a number m, representing the number of columns.
3. You are given n*m numbers, representing elements of 2d array a, which represents a maze.
4. You are standing in top-left cell and are required to move to bottom-right cell.
5. You are allowed to move 1 cell right (h move) or 1 cell down (v move) in 1 motion.
6. Each cell has a value that will have to be paid to enter that cell (even for the top-left and bottom-right cell).
7. You are required to traverse through the matrix and print the cost of path which is least costly.
"""


def minimum_cost(matrix):
    dp = [[0 for _ in range(len(matrix[0]))] for __ in range(len(matrix))]
    dp[-1][-1] = matrix[-1][-1]
    print(dp)
    for row in range(len(matrix) - 1, -1,-1):
        for col in range(len(matrix[0]) -1, -1, -1):
            if dp[row][col] == 0:
                right = float('inf')
                down = float('inf')
                if col != len(matrix[0]) - 1: right = dp[row][col + 1]
                if row != len(matrix) - 1 : down = dp[row + 1] [col]
                dp[row][col] = min(right, down) + matrix[row][col]
    print(dp)  

    
if __name__ == '__main__':
    matrix = [[2,8,4,1,6,4,2],[6,0,9,5,3,8,5], [1,4,3,4,0,6,5], [6,4,7,2,4,6,1], [1,0,3,7,1,2,7], [1,5,3,2,3,0,9], [2,2,5,1,9,8,2]]
    minimum_cost(matrix)