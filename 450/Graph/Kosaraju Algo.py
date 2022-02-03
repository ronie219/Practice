# used for finding the strongest connected graph

class Solution:

    def _dfs1(self, idx, adj, stack, visited):
        if idx not in visited:
            visited.add(idx)
            for node in adj[idx]:
                self._dfs1(node, adj, stack, visited)
            stack.append(idx)
    

    def _reverse_graph(self, adj,V):
        reverse_graph = [[] for _ in range(V)]
        for idx in range(V):
            for node in adj[idx]:
                reverse_graph[node].append(idx)
        return reverse_graph

    def _dfs2(self, adj, visited, node):
        if node not in visited:
            visited.add(node)
            for node in adj[node]:
                self._dfs2(adj, visited, node)
    
    #Function to find number of strongly connected components in the graph.
    def kosaraju(self, V, adj):
        # code here
        stack = []
        visited = set()
        for idx in range(V):
            if idx not in visited:
                self._dfs1(idx, adj, stack, visited)
        
        reverse_g = self._reverse_graph(adj,V)
        visited.clear()
        count = 0
        while stack:
            node = stack.pop()
            if node not in visited:
                self._dfs2(reverse_g,visited, node)
                count += 1
        return count

#  Driver Code Starts
#Initial Template for Python 3

from collections import OrderedDict 
import sys 

sys.setrecursionlimit(10**6) 
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        V,E = list(map(int, input().strip().split()))
        adj = [[] for i in range(V)]
        for i in range(E):
            a,b = map(int,input().strip().split())
            adj[a].append(b)
        ob = Solution()
        
        print(ob.kosaraju(V, adj))
