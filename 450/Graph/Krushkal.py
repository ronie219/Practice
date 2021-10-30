class Node:

    def __init__(self):
        self.rank = 0
        self.parent = -1

class Graph:

    def __init__(self, vertices):
        self.V = vertices
        self.graph = []


    def addEdge(self, u, v, w):
        self.graph.append([u, v, w])

    def sort_weight(self):
        self.graph.sort(key= lambda x : x[-1])
    
    def find_parent(self, edge, arr):
        if arr[edge].parent == -1:
            return edge
        arr[edge].parent = self.find_parent(arr[edge].parent, arr)
        return arr[edge].parent
    
    def union(self, idx1, idx2, arr):
        if arr[idx1].rank < arr[idx2].rank:
            arr[idx1].parent = idx2
        elif arr[idx1].rank > arr[idx2].rank:
            arr[idx2].parent = idx1
        else:
            arr[idx1].parent = idx2
            arr[idx1].rank += 1
    
    def KruskalMST(self):
        self.sort_weight()
        ans = []
        arr = []
        for _ in range(self.V):
            new_node = Node()
            arr.append(new_node)
        for edge in self.graph:
            fromP = self.find_parent(edge[0], arr)
            toP = self.find_parent(edge[1], arr)
            if fromP != toP:
                ans.append(edge)
                self.union(fromP, toP, arr)
        for edge in ans:
            print(f'{edge[0]} ---> {edge[1]} === {edge[2]}')



g = Graph(4)
g.addEdge(0, 1, 10)
g.addEdge(0, 2, 6)
g.addEdge(0, 3, 5)
g.addEdge(1, 3, 15)
g.addEdge(2, 3, 4)

g.KruskalMST()
