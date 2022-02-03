DIRECTION = [(0, -1), (0, 1), (-1, 0), (1, 0)]
MINI_PATH = float('inf')
VISITED = set()


def isSafe(row, col, mat):
    if row >= len(mat) or col >= len(mat[0]) or 0 > row or 0 > col: return False
    if (row, col) in VISITED: return False
    if mat[row][col] == 0: return False
    for x, y in DIRECTION:
        if 0 > row + x or row + x >= len(mat) or 0 > col + y or col + y >= len(mat[0]): continue
        if mat[row + x][col + y] == 0:
            return False
    return True


def _solve(ridx, cidx, mat, dist=0):
    global MINI_PATH
    global VISITED
    if isSafe(ridx, cidx, mat):
        if cidx == len(mat[0]) - 1 and MINI_PATH > dist:
            MINI_PATH = dist
            # print(MINI_PATH)
            return
        VISITED.add((ridx, cidx))
        for x, y in DIRECTION:
            _solve(ridx + x, cidx + y, mat, dist + 1)
        VISITED.remove((ridx, cidx))


def mini_path(mat):
    for row in range(len(mat)):
        _solve(row, 0, mat)
    print(MINI_PATH)


if __name__ == '__main__':
    mat = [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 0, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 0, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 0, 1, 1, 1, 1],
        [1, 0, 1, 1, 1, 1, 1, 1, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [0, 1, 1, 1, 1, 0, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 0, 1, 1, 1, 1, 1, 1]]
    mini_path(mat)
