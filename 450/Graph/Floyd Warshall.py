class Solution:
    def shortest_distance(self, matrix):
        size = len(matrix)
        for vertex in range(size):
            for row in range(size):
                for col in range(len(matrix[row])):
                    if matrix[row][vertex]==-1 or matrix[vertex][col]==-1:
                        continue
                    elif matrix[row][col] == -1:
                        matrix[row][col] = matrix[row][vertex] + matrix[vertex][col]
                    elif matrix[row][col] > matrix[row][vertex] + matrix[vertex][col]:
                        matrix[row][col] = matrix[row][vertex] + matrix[vertex][col]
                        
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

# {0,1,43},{1,0,6},{-1,-1,0}}
# Output: {{0,1,7},{1,0,6},{-1,-1,0}