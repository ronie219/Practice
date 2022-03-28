from collections import defaultdict, deque


# Class to represent a graph
class Graph:

    def __init__(self, vertices, edges):

        # Dictionary containing adjacency List
        self.graph = defaultdict(list)

        # No. of vertices
        self.n = vertices

        # No. of edges
        self.m = edges

        # Function to add an edge to graph

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def _findIndegree(self, n):
        inDegree = {}
        for idx in range(1, n + 1):
            if idx not in inDegree:
                inDegree[idx] = 0
            else:
                inDegree[idx] += 1
            for edge in self.graph[idx]:
                if edge in inDegree:
                    inDegree[edge] += 1
                else:
                    inDegree[edge] = 0
        return inDegree

    def minimunTime(self, n, m):
        inDegree = self._findIndegree(n)
        time_arr = [0] * n
        queue = deque()
        for idx in inDegree:
            if inDegree[idx] == 0:
                time_arr[idx - 1] = 1
                queue.append(idx)
        while queue:
            vertex = queue.popleft()
            for edge in self.graph[vertex]:
                inDegree[edge] -= 1
                if inDegree[edge] == 0:
                    queue.append(edge)
                    var = time_arr[vertex - 1]
                    time_arr[edge - 1] = var + 1
        return time_arr


if __name__ == '__main__':
    n = 10
    m = 13

    g = Graph(n, m)

    # Given Directed Edges of graph
    g.addEdge(1, 3)
    g.addEdge(1, 4)
    g.addEdge(1, 5)
    g.addEdge(2, 3)
    g.addEdge(2, 8)
    g.addEdge(2, 9)
    g.addEdge(3, 6)
    g.addEdge(4, 6)
    g.addEdge(4, 8)
    g.addEdge(5, 8)
    g.addEdge(6, 7)
    g.addEdge(7, 8)
    g.addEdge(8, 10)

    # Function Call
    print(g.minimunTime(n, m))
