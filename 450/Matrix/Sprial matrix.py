def spirallyTraverse(matrix, r, c):
    top = 0
    down = r
    left = 0
    right = c
    direction = 0
    output = []
    while top <= down or left <= right:
        if direction == 0:
            for i in range(left, right):
                output.append(matrix[top][i])
            top += 1
        elif direction == 1:
            for i in range(top, down):
                output.append(matrix[i][right - 1])
            right -= 1
        elif direction == 2:
            for i in range(right - 1, left - 1, -1):
                output.append(matrix[down - 1][i])
            down -= 1
        elif direction == 3:
            for i in range(down - 1, top - 1, -1):
                output.append(matrix[i][left])
            left += 1

        direction = (direction + 1) % 4

    return output


martix = [[1, 2, 3, 4],
          [5, 6, 7, 8],
          [9, 10, 11, 12],
          [13, 14, 15, 16]]

print(spirallyTraverse(martix, 4, 4))

# 1 2 3 4 8 12 16 15 14 13 9 5 6 7 11 10
# 1 2 3 4 8 12 16 15 14 13 9 5 6 7 11 10
