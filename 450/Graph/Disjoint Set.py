from collections import defaultdict

class Graph:

    def __init__(self,vertices):
        self.V= vertices 
        self.graph = defaultdict(list)
  
 
    def addEdge(self,u,v):
        self.graph[u].append(v)


    def find_parent(self, vertex, arr):
        idx = vertex
        while arr[idx] != -1:
            idx = arr[idx]
        return idx

    def union(self, e1, e2, arr):
        arr[e1] = e2

    def is_cycle(self):
        parents = [-1] * self.V
        for vertex in self.graph:
            for edge in self.graph[vertex]:
                absp1 = self.find_parent(edge, parents)
                absp2 = self.find_parent(vertex, parents)
                if absp2 == absp1:
                    return True
                self.union(absp1,absp2, parents)


g = Graph(5)
g.addEdge(0, 1)
g.addEdge(1, 2)
g.addEdge(2, 3)
g.addEdge(3, 4)
g.addEdge(0, 4)
if g.is_cycle():
    print("The Graph has Cycle")
else:
    print("There is no Cycle Present")