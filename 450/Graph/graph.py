"""
class Graph:

    def __init__(self, edges):
        self.edge = {}
        for start, end in edges:
            if start in self.edge:
                self.edge[start].append(end)
            else:
                self.edge[start] = [end, ]

    def _find_paths(self, start, end, path):
        path = path + [start]
        if start == end:
            return [path]
        if start not in self.edge:
            return []
        paths = []
        for destination in self.edge[start]:
            if destination not in path:
                route = self._find_paths(destination, end, path)
                # print(route)
                for p in route:
                    paths.append(p)
        return paths

    def get_path(self, start, end):
        paths = self._find_paths(start, end, [])
        for path in paths:
            print(" --> ".join(path))

    def find_shorted_paths(self, start, end):
        paths = self._find_paths(start, end, [])
        short_path = []
        length = float('inf')
        for path in paths:
            if len(path) < length:
                short_path = [path,]
                length = len(path)
            elif len(path) == length:
                short_path.append(path)
        for path in short_path:
            print(" --> ".join(path))


if __name__ == '__main__':
    routes = [
        ('Mumbai', 'Paris'),
        ('Mumbai', 'Dubai'),
        ('Paris', 'Dubai'),
        ('Paris', 'New York'),
        ('New York', 'Toronto'),
        ('Dubai', 'New York')
    ]

    graph = Graph(routes)
    print(graph.edge)
    graph.get_path('Mumbai', 'Toronto')
    print('*' * 50)
    graph.find_shorted_paths('Mumbai', 'Toronto')

"""
from collections import defaultdict, deque


class Graph:

    def __init__(self):
        self.graph = defaultdict(list)

    def add_edges(self, u, vertex):
        self.graph[u].append(vertex)

    def BFS(self, start):
        # visited = [False] * (max(self.graph) + 1)
        visited = set()
        result = []
        queue = deque()
        queue.append(start)
        while queue:
            var = queue.popleft()
            if var not in visited:
                result.append(var)
                queue.extend(self.graph[var])
                visited.add(var)
        print(result)

    def _dfs(self, element, visited, arr):
        visited.add(element)

        arr.append(element)
        for neighbour in self.graph[element]:
            if neighbour not in visited:
                self._dfs(neighbour, visited, arr)


    def DFS(self, start):
        visited = set()
        arr = []
        self._dfs(start,visited, arr)
        print(arr)

if __name__ == '__main__':
    graph = Graph()
    graph.add_edges(0, 1)
    graph.add_edges(0, 2)
    graph.add_edges(1, 2)
    graph.add_edges(2, 0)
    graph.add_edges(2, 3)
    graph.add_edges(3, 8)
    graph.add_edges(8, 7)
    graph.add_edges(7, 9)
    graph.add_edges(9, 6)
    graph.BFS(1)
    graph.DFS(1)
