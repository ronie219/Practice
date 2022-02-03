def find_word(string, matrix):
    memo = set()
    direction = [(0, 1), (1, 0), (-1, 0), (0, -1)]

    def inner(string, matrix, x=0, y=0):
        if string == '':
            print('found')
            return 1
        if 0 > x >= len(matrix) or 0 > y >= len(matrix[0]):
            return 0
        if (x, y) in memo:
            return 0
        if matrix[x][y] != string[0]:
            return 0
        memo.add((x, y))
        for row, col in direction:
            inner(string[1:], matrix, x + row, y + col)
        memo.remove((x, y))

    inner(string, matrix)


if __name__ == '__main__':
    arr = [
        ['B', 'B', 'M', 'B', 'B', 'B'],
        ['C', 'B', 'A', 'B', 'B', 'B'],
        ['I', 'B', 'G', 'B', 'B', 'B'],
        ['G', 'B', 'I', 'B', 'B', 'B'],
        ['A', 'B', 'C', 'B', 'B', 'B'],
        ['M', 'C', 'I', 'G', 'A', 'M']
    ]
    s = "MAGIC"
    find_word(s, arr)
