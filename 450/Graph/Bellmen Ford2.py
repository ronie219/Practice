from collections import defaultdict
import copy

class Edge:
    
    def __init__(self):
        self.src = 0
        self.dest = 0
        self.weight = 0


class Graph:

    def __init__(self,E,V):
        self.Edge = E
        self.Vertex = V
        self.edges = [Edge() for _ in range(self.Edge)]

    
def isNegCycleBellmanFord(graph, src):
    edges = graph.edges
    distance = [float('inf') for _ in range(graph.Vertex)]
    # strp for relaxtion of each nodes
    distance[0] = 0
    for _ in range(graph.Edge):
        for edge in edges:
            u = edge.src
            v = edge.dest
            w = edge.weight
            if distance[u] + w < distance[v]:
                distance[v] = distance[u] + w
    
    copy_array = copy.deepcopy(distance)
    for edge in edges:
            u = edge.src
            v = edge.dest
            w = edge.weight
            if distance[u] + w < distance[v]:
                distance[v] = distance[u] + w
    return copy_array == distance
    

graph = Graph(8, 5)
graph.edges[0].src = 0
graph.edges[0].dest = 1;
graph.edges[0].weight = -1;

# add edges 0-2 (or A-C in above figure)
graph.edges[1].src = 0;
graph.edges[1].dest = 2;
graph.edges[1].weight = 4;

# add edges 1-2 (or B-C in above figure)
graph.edges[2].src = 1;
graph.edges[2].dest = 2;
graph.edges[2].weight = 3;

# add edges 1-3 (or B-D in above figure)
graph.edges[3].src = 1;
graph.edges[3].dest = 3;
graph.edges[3].weight = 2;

# add edges 1-4 (or A-E in above figure)
graph.edges[4].src = 1;
graph.edges[4].dest = 4;
graph.edges[4].weight = 2;

# add edges 3-2 (or D-C in above figure)
graph.edges[5].src = 3;
graph.edges[5].dest = 2;
graph.edges[5].weight = 5;

# add edges 3-1 (or D-B in above figure)
graph.edges[6].src = 3;
graph.edges[6].dest = 1;
graph.edges[6].weight = 1;

# add edges 4-3 (or E-D in above figure)
graph.edges[7].src = 4;
graph.edges[7].dest = 3;
graph.edges[7].weight = -3;

if (isNegCycleBellmanFord(graph, 0)):
    print("Yes")
else:
    print("No")
