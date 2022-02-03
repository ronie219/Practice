

def queen(arr,n,x = 0,y = 0,placed=0):
    if placed == n:
        print(arr)
        return
    # do 
    for row in range(x, n):
        for col in range(y, n):
            if isItsafe(arr,row, col, n):
                arr[row][col] = 1
                placed += 1

                queen(arr, n, row, col + 1, placed)

                # undo
                arr[row][col] = 0
                placed -= 1
        y = 0

def isItsafe(arr, x, y, n):
    # we check vertically upward
    row = x
    col = y
    while col >= 0:
        if arr[row][col] == 1:
            return False
        col -= 1
    
    # we check horizontally left
    row = x
    col = y
    while row >= 0:
        if arr[row][col] == 1:
            return False
        row -= 1
    
    # we check digonally left
    row = x
    col = y
    while row >= 0 and col >= 0:
        if arr[row][col] == 1:
            return False
        row -= 1
        col -= 1

    # we check digonally right
    row = x
    col = y
    while row >= 0 and col < n:
        if arr[row][col] == 1:
            return False
        row -= 1
        col += 1
    
    return True

if __name__ == '__main__':
    n = 4
    board = [[0 for _ in range(n)] for __ in range(n)]
    queen(board, n, 0, 0)