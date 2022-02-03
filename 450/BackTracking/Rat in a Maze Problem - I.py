direction = [(-1,0,'U'), (1,0,'D'), (0,-1,'L'), (0,1,'R')]

def find_path(matrix,x, y, n, visited, path=""):
    if x == n-1 and y == n-1:
        print(path)
        return
    if x < 0 or y < 0 or x >= n or y >= n: return
    if visited[x][y] == 1 or matrix[x][y] == 0: return
    visited[x][y] = 1
    for row,col,direc in direction:
        find_path(matrix,x + row,y + col, n, visited, path+direc)
    visited[x][y] = 0
    


if __name__ == '__main__':
    n = 4
    matrix = [[1, 0, 0, 0],[1, 1, 0, 1], [1, 1, 0, 0],[0, 1, 1, 1]]
    visited = [[0 for _ in range(n)] for __ in range(n)]
    find_path(matrix, 0 , 0, n, visited)