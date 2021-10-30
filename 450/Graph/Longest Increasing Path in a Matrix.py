def longestIncreasingPath(matrix):
    path = 0
    memo = {}
    direction = [(0,-1),(0,1),(-1,0),(1,0)]
    
    def dfs(row, col):
        
        if (row, col) in memo.keys(): return memo[(row, col)]
        curr_path = 0
        for row_dir,col_dir in direction:
            if 0 <= (row+row_dir) < len(matrix) and 0 <= (col+col_dir) < len(matrix[0]) and matrix[row+row_dir][col+col_dir] > matrix[row][col]:
                curr_path = max(curr_path, dfs(row+row_dir,col+col_dir))
            
        memo[(row, col)] = curr_path + 1
        return curr_path + 1


    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            print(dfs(row, col))
            path = max(path, dfs(row, col))
        # print(memo)
    return path



matrix = [[9,9,4],[6,6,8],[2,1,1]]
print(longestIncreasingPath(matrix))