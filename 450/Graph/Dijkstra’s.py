class Graph():
 
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)]
                    for row in range(vertices)]
    

    def minimum_value(self,values,processd):
        idx = None
        minimum = float("inf")
        for rw_idx in range(self.V):
            if values[rw_idx] < minimum and processd[rw_idx] == False:
                minimum = values[rw_idx]
                idx = rw_idx

        return idx



    def dijkstra(self, start):
        parent = [-1] * self.V
        values = [float("inf")] * self.V
        values[start] = 0
        processed = [False] * self.V

        for _ in range(self.V):
            idx = self.minimum_value(values,processed)
            processed[idx] = True

            for rw in range(self.V):
                if self.graph[idx][rw] > 0 and processed[rw] == False and values[idx] != float('inf') and (values[idx] + self.graph[idx][rw]) < values[rw]:
                    values[rw] =  values[idx] + self.graph[idx][rw]
                    parent[rw] = idx
        
        print(values)
        self.print_graph(values)

    def print_graph(self,values):
        for idx in range(self.V):
            print(f"{idx} ----> {values[idx]}")

g = Graph(9)
g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
        [4, 0, 8, 0, 0, 0, 0, 11, 0],
        [0, 8, 0, 7, 0, 4, 0, 0, 2],
        [0, 0, 7, 0, 9, 14, 0, 0, 0],
        [0, 0, 0, 9, 0, 10, 0, 0, 0],
        [0, 0, 4, 14, 10, 0, 2, 0, 0],
        [0, 0, 0, 0, 0, 2, 0, 1, 6],
        [8, 11, 0, 0, 0, 0, 1, 0, 7],
        [0, 0, 2, 0, 0, 0, 6, 7, 0]
        ]
 
g.dijkstra(0)