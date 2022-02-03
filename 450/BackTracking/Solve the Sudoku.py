#Function to find a solved Sudoku. 
def SolveSudoku(grid,row=0,col=0):
    if col == 9:
        row = 0


def isValid(grid, row, col, po):
    for idx in range(9):
        if grid[row][idx] == po: return False
        if grid[idx][col] == po: return False
    r = row//3 * 3
    c = col//3 * 3
    for idx1 in range(r,3+r):
        for idx2 in range(c, 3 + c):
            if grid[idx1][idx2] == po: return False
    
    return True

    

#Function to print grids of the Sudoku.    
def printGrid(arr):
    for row in arr:
        print(row)

    print("*-*" * 10)


if __name__ == '__main__':
    grid = [[3,0,6,5,0,8,4,0,0],[5,2,0,0,0,0,0,0,0],[0,8,7,0,0,0,0,3,1,],[0,0,3,0,1,0,0,8,0],[9,0,0,8,6,3,0,0,5],[0,5,0,0,9,0,6,0,0],[1,3,0,0,0,0,2,5,0],[0,0,0,0,0,0,0,7,4],[0,0,5,2,0,6,3,0,0]]
    printGrid(arr=grid)
    ans = []
    SolveSudoku(grid)
