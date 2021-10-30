class Solution:
    def _dfs(self, x, y, visited, m, n, ans, string=''):
        if x >= n or y >= n or x < 0 or y < 0: return
        if m[x][y] == 0 or (x, y) in visited: return
        if x == n - 1 and y == n - 1:
            ans.append(string)
            return

        visited.add((x, y))

        self._dfs(x + 1, y, visited, m, n, ans, string + 'D')
        self._dfs(x - 1, y, visited, m, n, ans, string + 'U')
        self._dfs(x, y - 1, visited, m, n, ans, string + 'L')
        self._dfs(x, y + 1, visited, m, n, ans, string + 'R')
        visited.remove((x, y))

    def findPath(self, m, n):
        visited = set()
        ans = []
        self._dfs(0, 0, visited, m, n, ans)
        ans.sort()
        return ans


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))

        matrix = [[0 for i in range(n[0])] for j in range(n[0])]
        k = 0
        for i in range(n[0]):
            for j in range(n[0]):
                matrix[i][j] = arr[k]
                k += 1
        ob = Solution()
        result = ob.findPath(matrix, n[0])
        if len(result) == 0:
            print(-1)
        else:
            for x in result:
                print(x, end=" ")
            print()
