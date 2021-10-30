from collections import defaultdict, deque

class Graph:

    def __init__(self, vertex):
        self.graph = defaultdict(list)
        self.V = vertex

    def add_edges(self, u, v):
        self.graph[u].append(v)
    
    def _dfsCall(self, visited, idx):
        visited.add(idx)
        for edges in self.graph[idx]:
            if edges in visited: 
                return True
            if self._dfsCall(visited, edges): return True
            visited.remove(edges)
        return False

    """
    def isCycle(self):
        # usimg DFS
        visited = set()
        for idx in range(1, self.V + 1):
            if self._dfsCall(visited, idx):return True
        return False
    """

    def isCycle(self):
        visited = set()
        queue = deque()
        queue.append(0)
        while queue:
            vertex = queue.popleft()
            if vertex in visited: return True
            visited.add(vertex)
            for edge in self.graph[vertex]:
                if edge not in queue:queue.append(edge)
        return False



if __name__ == "__main__":
    g = Graph(2)
    g.add_edges(0,1)
    g.add_edges(1,0)
    print(g.isCycle())