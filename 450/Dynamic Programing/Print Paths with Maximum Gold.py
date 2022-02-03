"""
1. You are given a number n, representing the number of rows.
2. You are given a number m, representing the number of columns.
3. You are given n*m numbers, representing elements of 2d array a, which represents a gold mine.
4. You are standing in front of left wall and are supposed to dig to the right wall. You can start from any row in the left wall.
5. You are allowed to move 1 cell right-up (d1), 1 cell right (d2) or 1 cell right-down(d3).
6. Each cell has a value that is the amount of gold available in the cell.
7. You are required to identify the maximum amount of gold that can be dug out from the mine.
8. Also, you have to print all paths with maximum gold.
"""


from collections import deque


class Path():

    def __init__(self, x, y, psf):
        self.x = x
        self.y = y
        self.psf = psf


def printPath(rows, cols, matrix):
    dp = [[0 for _ in range(cols)] for __ in range(rows)]
    max_gold = 0
    for col in range(cols-1, -1, -1):
        for row in range(rows):
            if col == cols - 1:
                dp[row][col] = matrix[row][col]
            else:
                if row == rows-1:
                    dp[row][col] = max(
                        dp[row][col+1], dp[row-1][col+1]) + matrix[row][col]
                elif row == 0:
                    dp[row][col] = max(
                        dp[row][col+1], dp[row+1][col+1]) + matrix[row][col]
                else:
                    dp[row][col] = max(
                        dp[row][col+1], dp[row+1][col+1], dp[row-1][col+1]) + matrix[row][col]
            if max_gold < dp[row][col]:
                max_gold = dp[row][col]
    print(max_gold)
    queue = deque()
    for row in range(rows):
        if dp[row][0] == max_gold:
            queue.append(Path(row, 0, f'{row} --> '))

    while queue:
        path = queue.popleft()
        if cols - 1 == path.y:
            print(path.psf)
        else:
            if path.x == 0:
                val = max(dp[path.x][path.y+1], dp[path.x+1][path.y+1])
                if val == dp[path.x][path.y+1]:
                    queue.append(Path(path.x, path.y+1, path.psf + '--> d2'))
                if val == dp[path.x+1][path.y+1]:
                    queue.append(Path(path.x+1, path.y+1, path.psf + '--> d3'))
            elif path.x == cols-1:
                val = max(dp[path.x][path.y+1], dp[path.x-1][path.y+1])
                if val == dp[path.x][path.y+1]:
                    queue.append(Path(path.x, path.y+1, path.psf + '--> d2'))
                if val == dp[path.x-1][path.y+1]:
                    queue.append(Path(path.x-1, path.y+1, path.psf + '--> d1'))
            else:
                val = max(dp[path.x][path.y+1], dp[path.x-1]
                          [path.y+1], dp[path.x+1][path.y+1])
                if val == dp[path.x][path.y+1]:
                    queue.append(Path(path.x, path.y+1, path.psf + '--> d2'))
                if val == dp[path.x-1][path.y+1]:
                    queue.append(Path(path.x-1, path.y+1, path.psf + '--> d1'))
                if val == dp[path.x+1][path.y+1]:
                    queue.append(Path(path.x+1, path.y+1, path.psf + '--> d3'))


if __name__ == '__main__':
    n = 4
    m = 4
    matrix = []
    for _ in range(n):
        matrix.append(list(map(int, input().split())))
    printPath(n, m, matrix)
