"""
1. You are given a number n, representing the number of rows.
2. You are given a number m, representing the number of columns.
3. You are given n*m numbers, representing elements of 2d array a, which represents a maze.
4. You are standing in top-left cell and are required to move to bottom-right cell.
5. You are allowed to move 1 cell right (h move) or 1 cell down (v move) in 1 motion.
6. Each cell has a value that will have to be paid to enter that cell (even for the top-left and bottom-right cell).
7. You are required to traverse through the matrix and print the cost of the path which is least costly.
8. Also, you have to print all the paths with minimum cost.
"""
from collections import deque


class Path:

    def __init__(self, x, y, psf) -> None:
        self.x = x
        self.y = y
        self.psf = psf


def minimumPath(rows, cols, matrix):
    # first we create a DP matrix in which we store min cost to reach destination from that cell.
    dp = [[0 for _ in range(cols)] for __ in range(rows)]

    # now we inisilize the dp and travel and solve.

    for row in range(rows-1, -1, -1):
        for col in range(cols-1, -1, -1):
            if row == rows - 1 and col == cols - 1:
                dp[row][col] = matrix[row][col]
            elif row == rows - 1:
                dp[row][col] = matrix[row][col] + dp[row][col + 1]
            elif col == cols - 1:
                dp[row][col] = matrix[row][col] + dp[row + 1][col]
            else:
                dp[row][col] = matrix[row][col] + \
                    min(dp[row + 1][col], dp[row][col + 1])

    # now we find the path using reverse engineering and BFS from 0,0 node of DP

    queue = deque()
    queue.append(Path(0, 0, ''))

    while queue:
        path = queue.popleft()
        if path.x == rows-1 and path.y == cols-1:
            print(path.psf)
        elif path.x == rows-1:
            queue.append(Path(path.x, path.y+1, path.psf + 'H'))
        elif path.y == cols-1:
            queue.append(Path(path.x + 1, path.y, path.psf + 'V'))
        else:
            if dp[path.x+1][path.y] > dp[path.x][path.y+1]:
                queue.append(Path(path.x, path.y+1, path.psf + 'H'))
            elif dp[path.x+1][path.y] < dp[path.x][path.y+1]:
                queue.append(Path(path.x+1, path.y, path.psf + 'V'))
            else:
                queue.append(Path(path.x, path.y+1, path.psf + 'H'))
                queue.append(Path(path.x+1, path.y, path.psf + 'V'))


if __name__ == '__main__':
    n = 5  # row
    m = 5  # col
    matrix = []
    for _ in range(n):
        matrix.append(list(map(int, input().split())))

    minimumPath(n, m, matrix)
