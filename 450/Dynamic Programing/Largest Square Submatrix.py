def square_matrix(matrix, size):
    dp = []
    # insilize the dp, edged with the same value and zero with zero
    # we define storage and meaning to each cell. meaning -> in each cell we define that
    # how bigger square you can make using that cell as upper left part
    for row in range(size):
        line = []
        for col in range(size):
            if matrix[row][col] == 0:
                line.append(0)
            elif row == size - 1 or col == size - 1:
                line.append(matrix[row][col])
            else:
                line.append(None)
        dp.append(line)

    max_size = 0

    for row in range(size - 1, -1, -1):
        for col in range(size - 1, -1, -1):
            if dp[row][col] == None:
                # we take the minimum of the adj row + 1, col + 1, row+1col+1
                attri = []
                if row + 1 != size:
                    attri.append(dp[row + 1][col])
                if col + 1 != size:
                    attri.append(dp[row][col + 1])
                if col + 1 != size and row + 1 != size:
                    attri.append(dp[row + 1][col + 1])

                dp[row][col] = min(attri) + 1
                if dp[row][col] > max_size:
                    max_size = dp[row][col]
    print(max_size)


if __name__ == "__main__":
    size = 6
    matrix = []
    for _ in range(size):
        matrix.append(list(map(int, input().split())))
    square_matrix(matrix, size)
