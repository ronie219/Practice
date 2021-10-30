class Solution:


    def _tsp(self, toP, fromP, visited, matrix):
        if all(visited):
            return 0
        


    def shortest_distance(self, matrix):
        n = len(matrix)
        visited_arr = [False] * n
        visited_arr[0]= True
        arr = []
        for vertex in range(1,n):
            ans = self._tsp(0, vertex, visited_arr, matrix)
            arr.append(ans)
        



if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        n = int(input())
        matrix = []
        for _ in range(n):
            matrix.append(list(map(int, input().split())))
        obj = Solution()
        obj.shortest_distance(matrix)
        for _ in range(n):
            for __ in range(n):
                print(matrix[_][__], end = " ")
            print()