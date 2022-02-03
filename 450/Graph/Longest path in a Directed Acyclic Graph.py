from collections import defaultdict

class Graph:

    def __init__(self,v):
        self.v = v
        self.graph = defaultdict(list)
    
    def add_edge(self, u, v):
        self.graph[u].append(v)
    
    # def topologicalSort(self,s):
    #     global stack, visited
    #     if s not in visited:
    #         visited.add(s)
    #         for adj in self.graph[s]:
    #             self.topologicalSort(adj[0])
    #         Stack.append(s)

    
    # def longestPath(self,s):
    #     global Stack, visited, V
    #     dist = [float('-inf') for _ in range(V)]

    #     for idx in range(V):
    #         if idx not in visited:
    #             self.topologicalSort(idx)
    #     print(Stack)
    #     dist[s] = 0
    #     while Stack:
    #         vertex = Stack.pop()
    #         for value,weight in self.graph[vertex]:
    #             if dist[value] < dist[vertex] + weight:
    #                 dist[value] = dist[vertex] + weight
    #     print(dist)
    #     for i in range(V):
    #         print("INF ",end="") if (dist[i] == -10**9) else print(dist[i],end=" ")

    # def _dfs(self, idx, dist):
    #     for adj in self.graph[idx]:
    #         if dist[idx] != 0:
    #             return dist[idx]
            
            
    
    # def longest_path_length(self):
    #     dist = [0 for _ in range(self.v)]
    #     for idx in range(self.v):
    #         if dist[idx] == 0:
    #             self._dfs(idx, dist)

    def _dfs(self, idx, dist):
        
        for adj in self.graph[idx]:
            dist[adj] = max(dist[adj], (self._dfs(adj) + 1))
        return 1

    def longest_path_length(self):
        dist = [-1 for _ in range(self.v)]
        for idx in range(self.v):
            if dist[idx] == -1:
                dist[idx] = self._dfs(idx, dist)
        print(dist)

if __name__ == '__main__':
    V, Stack, visited = 6, [], set()
    g = Graph(V)
    g.add_edge(0,[1, 5])
    g.add_edge(0,[2, 3])
    g.add_edge(1,[3, 6])
    g.add_edge(1,[2, 2])
    g.add_edge(2,[4, 4])
    g.add_edge(2,[5, 2])
    g.add_edge(2,[3, 7])
    g.add_edge(3,[5, 1])
    g.add_edge(3,[4, -1])
    g.add_edge(4,[5, -2])
    print(g.graph)
    g.longest_path_length()

