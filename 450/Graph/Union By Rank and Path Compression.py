from collections import defaultdict

class Node:
    
    def __init__(self):
        self.parent = -1
        self.rank = 0

class Graph:

    def __init__(self, num_of_v):
        self.num_of_v = num_of_v
        self.edges = defaultdict(list)
 
    def add_edge(self, u, v):
        self.edges[u].append(v)

    def find_parent(self, edge, arr):
        if arr[edge].parent == -1:
            return edge
        arr[edge].parent = self.find_parent(arr[edge].parent,arr)
        return arr[edge].parent

    
    def union(self, idx1, idx2, arr):
        toP = arr[idx1]
        fromP = arr[idx2]
        if toP.rank < fromP.rank:
            toP.parent = idx2
        elif toP.rank > fromP.rank:
            fromP.parent = idx1
        else:
            fromP.parent = idx1
            fromP.rank += 1

    def isCycle(self):
        # arr = [Node()] * self.num_of_v
        arr = []
        for _ in range(self.num_of_v):
            new_node = Node()
            arr.append(new_node)
        
        for Toedge in self.edges:
            for Fromedge in self.edges[Toedge]:
                toP = self.find_parent(Toedge, arr)
                fromP = self.find_parent(Fromedge, arr)
                print(toP, fromP)
                if toP == fromP: return True
                self.union(toP, fromP, arr)
        return False



g = Graph(4)
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(2, 3)
g.add_edge(3, 1)


print(g.isCycle())