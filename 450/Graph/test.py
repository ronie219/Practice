# givein int arr num return all tripelt [] i != j j += k okey
"""

arr = [0, -1 , 1, 2, -2,3,-3 ]

#-2, -1, 0, 1, 2
arr.sort()
ans = []
print(arr)
for i in range(len(arr)-1):

    for j in range(i+2,len(arr)):
        if arr[i]+arr[i+1] + arr[j] == 0:ans.append((arr[i], arr[i+1], arr[j]))
        if arr[i]+arr[i+1] + arr[j] > 0:break

print(ans)


"""



# typo sort

from collections import defaultdict
from typing import List


class Graph:

    def __init__(self,vertex):
        self.graph = defaultdict(list)
        self.V = vertex

    def addEdge(self,u, v):
        self.graph[u].append(v)

    def _dfscall(self, vertex, stack, visited):
        visited.add(vertex)
        for i in self.graph[vertex]:
            if i not in visited:
                self._dfscall(i, stack, visited)
        stack.append(vertex)



    def toposort(self):
        stack = []
        visited = set()
        for vertex in self.graph.keys():
            if vertex not in visited:
                self._dfscall(vertex, stack, visited)
        print(stack)



g = Graph(6)
g.addEdge(5, 2)
g.addEdge(5, 0)
g.addEdge(4, 0)
g.addEdge(4, 1)
g.addEdge(2, 3)
g.addEdge(3, 1)
g.toposort()



