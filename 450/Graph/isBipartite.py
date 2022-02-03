from collections import deque

class Graph:

    def __init__(self, V):
        self.V = V
        self.graph = [[0 for column in range(V)] \
                                for row in range(V)]

    """
    # bfs approach 
    def isBipartite(self, src):
        colours = [-1 for _ in range(self.V)]
        colours[0] = 1
        queue = deque()
        queue.append(src)
        while queue:
            u = queue.popleft()
            
            # if graph having self loop then we return false
            if self.graph[u][u] == 1:
                return False
            
            for v in range(self.V):
                if self.graph[u][v] == 1 and colours[v] == -1:
                    # we will assign the second colour to the adj of the node.
                    colours[v] = 3 - colours[u] # 3-2 = 1 and 3-1=2
                    queue.append(v)
                elif self.graph[u][v] == 1 and colours[v] == colours[u]:
                    # we return False if the thr adj colour are same
                    return False
        return True
        """

    def _dfs(self, src, colour_array, colour):
        if self.graph[src][src] == 1:
            return False
        for v in range(self.V):
            if self.graph[src][v] == 1 and colour_array[v] == -1:
                colour_array[v] = 3 -  colour_array[src]
                return self._dfs(v, colour_array, colour_array[v])
            elif self.graph[src][v] == 1 and colour_array[v] == colour:
                return False
        return True

    def isBipartite(self, src):
        colour_array = [-1 for _ in range(self.V)]
        colour_array[0] = 1
        flag = True
        return self._dfs(src,colour_array,1)

        






g = Graph(4)
# g.graph = [
#     [0,1,0,0,0], # 0
#     [0,0,1,0,0], # 1
#     [0,0,0,1,0], # 2
#     [0,0,0,0,1], # 3
#     [1,0,0,0,0]  # 4
# ]

g.graph = [[0, 1, 0, 1],
            [1, 0, 1, 0],
            [0, 1, 0, 1],
            [1, 0, 1, 0]
            ]          
print("Yes") if g.isBipartite(0) else print("No")