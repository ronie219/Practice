import copy

class Solution:
    
    def isNegativeWeightCycle(self, n, edges):
        dp_arr = [float('inf')] * n
        dp_arr[0] = 0
        
        for _ in range(n-1):
            for edge in edges:
                toP = edge[0]
                fromP = edge[1]
                weight = edge[2]
                if dp_arr[toP] + weight < dp_arr[fromP]:
                    dp_arr[fromP] = dp_arr[toP] + weight
        arr = copy.deepcopy(dp_arr)
        for edge in edges:
                toP = edge[0]
                fromP = edge[1]
                weight = edge[2]
                if arr[toP] + weight < arr[fromP]:
                    arr[fromP] = arr[toP] + weight
        
        if arr == dp_arr:
            return False 
        return True


if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n, m = input().split()
		n = int(n)
		m = int(m)
		edges = []
		for _ in range(m):
			edges.append(list(map(int, input().split())))
		obj = Solution()
		ans = obj.isNegativeWeightCycle(n, edges)
		print(ans)

