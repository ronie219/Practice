from collections import deque
from typing import OrderedDict, OrderedDict

class Solution:
    

    def _dfscall(self, item, adj, stack, visited):
        visited.add(item)
        for edge in adj[item]:
            if edge not in visited:
                self._dfscall(edge, adj, stack, visited)
        stack.append(item)

    
    #Function to return list containing vertices in Topological order.
    def topoSort(self, V, adj):
        # dfs
        stack = []
        visited = set()
        for vertex in range(V):
            if vertex not in visited:
                self._dfscall(vertex, adj, stack, visited)
        return stack[::-1]
    

    # def topoSort(self, V, adj):
    #     # bfs
    #     inDegree = {}
    #     queue = deque()
    #     for idx in range(V):
    #         if idx not in inDegree:
    #             inDegree[idx] = 0
    #         for element in adj[idx]:
    #             if element not in inDegree:
    #                 inDegree[element] = 1
    #             else:
    #                 inDegree[element] += 1
    #     print(inDegree)

            
import sys
sys.setrecursionlimit(10**6)
        
def check(graph, N, res):
    if N!=len(res):
        return False
    map=[0]*N
    for i in range(N):
        map[res[i]]=i
    for i in range(N):
        for v in graph[i]:
            if map[i] > map[v]:
                return False
    return True

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        e,N = list(map(int, input().strip().split()))
        adj = [[] for i in range(N)]
        print(adj)
        for i in range(e):
            u,v=map(int,input().split())
            adj[u].append(v)
        print(adj)
        ob = Solution()
        
        res = ob.topoSort(N, adj)
        
        # if check(adj, N, res):
        #     print(1)
        # else:
        #     print(0)
        # print(res[::-1])