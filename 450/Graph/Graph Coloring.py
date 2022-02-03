from collections import defaultdict
import collections


class Graph:

    def __init__(self,v):
        self.graph = defaultdict(list)
        self.v = v
    
    def add_edge(self,u,v):
        self.graph[u].append(v)
        self.graph[v].append(u)
    
    def graph_colouring(self):

        colours = [False] * self.v
        colour_node = [-1] * self.v
        colour_node[0] = 0

        for node in range(1,self.v):
            for adj in self.graph[node]:
                if colour_node[adj] != -1:
                    colours[colour_node[adj]] =  True
            
            for idx in range(self.v):
                if colours[idx] == False:
                    colour_node[node] = idx
                    break
            colours = [False] * self.v

        return len(set(colour_node))

g = Graph(5)
g.add_edge(0,1)
g.add_edge(0,4)
g.add_edge(0,2)
g.add_edge(1,3)
g.add_edge(1,4)
g.add_edge(2,3)
g.add_edge(2,4)
print(g.graph_colouring())