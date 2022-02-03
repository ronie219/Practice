class Graph:

    def __init__(self,vertex):
        self.V = vertex
        self.graph = [[0 for column in range(vertex)]
                    for row in range(vertex)]
    def print_mst(self,parent):
        print("printing the MST....")
        for idx in range(1, self.V):
            print(f"{parent[idx]} --- {idx} == {self.graph[idx][parent[idx]]}")


    def minimum_idx(self, key, mstSet):
        min_idx = None
        min_val = float('inf')

        for idx in range(self.V):
            if key[idx] < min_val and mstSet[idx] != True:
                min_idx = idx
                min_val = key[idx]
        return min_idx
    
    def primMST(self):
        key = [float("inf")] * self.V # [0, 1, 2, ]...
        key[0] = 0 
        parent = [-1] * self.V
        mstSet = [False] * self.V

        for col in range(self.V):

            min_idx = self.minimum_idx(key,mstSet)
            mstSet[min_idx] = True
            for rw in range(self.V):

                if self.graph[min_idx][rw] !=0 and mstSet[rw] == False and key[rw] != [float("inf")] and key[rw] > self.graph[min_idx][rw]:
                    key[rw] = self.graph[min_idx][rw]
                    parent[rw] = min_idx
        
        print(parent)
        print(key)

        self.print_mst(parent)

g = Graph(5)
g.graph = [ [0, 2, 0, 6, 0],
            [2, 0, 3, 8, 5],
            [0, 3, 0, 0, 7],
            [6, 8, 0, 0, 9],
            [0, 5, 7, 9, 0]]

g.primMST()