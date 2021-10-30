import sys
from collections import deque
sys.setrecursionlimit(10 ** 6)


class Solution:

    # def _dfs(self, visited, n, m, row, col, grid):
    #     # if 0 > row > m and 0 > col > n and (row, col) in visited and grid[row][col] == 0: return
    #     if (row < 0 or row >= n) or (col < 0 or col >= m) or (row, col) in visited or int(grid[row][col]) == 0 : return
    #     visited.add((row, col))
    #     self._dfs(visited, n, m, row + 1, col, grid)
    #     self._dfs(visited, n, m, row - 1, col, grid)
    #     self._dfs(visited, n, m, row, col + 1, grid)
    #     self._dfs(visited, n, m, row, col - 1, grid)

    #     self._dfs(visited, n, m, row + 1, col + 1, grid)
    #     self._dfs(visited, n, m, row + 1, col - 1, grid)
    #     self._dfs(visited, n, m, row - 1, col - 1, grid)
    #     self._dfs(visited, n, m, row - 1, col + 1, grid)

    # def numIslands(self, grid):
    #     rows = len(grid)
    #     cols = len(grid[0])
    #     visited = set()
    #     is_land = 0
    #     for row in range(rows):
    #         for column in range(cols):
    #             if int(grid[row][column]) != 0 and (row, column) not in visited:
    #                 self._dfs(visited, rows, cols, row, column, grid)
    #                 is_land += 1
    #     return is_land

    def _bfs(self,grid, n, m, row, col, visited):
        queue = deque()
        queue.append((row, col))
        visited.add((row,col))
        while queue:
            row, col = queue.popleft()
            row = int(row)
            col = int(col)
            if (0 <= row + 1 < n and 0 <= col < m) and (row+1,col) not in visited and int(grid[row+1][col]) == 1:
                queue.append((row+1,col))
                visited.add((row+1,col))
            if (0 <= row - 1 < n and 0 <= col < m) and (row-1,col) not in visited and int(grid[row-1][col]) == 1:
                queue.append((row-1,col))
                visited.add((row-1,col))
            if (0 <= row < n and 0 <= col + 1 < m) and (row,col+1) not in visited and int(grid[row][col + 1]) == 1:
                queue.append((row,col+1))
                visited.add((row,col+1))
            if (0 <= row < n and 0 <= col - 1 < m) and (row,col-1) not in visited and int(grid[row][col- 1]) == 1:
                queue.append((row,col-1))
                visited.add((row,col-1))


            if (0 <= row + 1 < n and 0 <= col + 1 < m) and (row+1,col+1) not in visited and int(grid[row+1][col+ 1]) == 1:
                queue.append((row+1,col+1))
                visited.add((row+1,col+1))
            
            if (0 <= row - 1 < n and 0 <= col + 1 < m) and (row-1,col+1) not in visited and int(grid[row-1][col+1]) == 1:
                queue.append((row-1,col+1))
                visited.add((row-1,col+1))
            
            if (0 <= row - 1 < n and 0 <= col - 1 < m) and (row-1,col-1) not in visited and int(grid[row-1][col-1]) == 1:
                queue.append((row-1,col-1))
                visited.add((row-1,col-1))
            
            if (0 <= row + 1 < n and 0 <= col - 1 < m) and (row+1,col-1) not in visited and int(grid[row+1][col-1]) == 1:
                queue.append((row+1,col-1))
                visited.add((row+1,col-1))


    def numIslands(self,grid):
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        island = 0
        for row in range(rows):
            for col in range(cols):
                if (row, col) not in visited and int(grid[row][col]) == 1:
                    self._bfs(grid, rows, cols, row, col, visited)
                    island += 1
        return island

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        n, m = map(int, input().split())
        grid = []
        for _ in range(n):
            a = list(input().split())
            grid.append(a)
        obj = Solution()
        ans = obj.numIslands(grid)
        print(ans)
