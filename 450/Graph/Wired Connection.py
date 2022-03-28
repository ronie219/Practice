from collections import defaultdict
from typing import List


class Solution:

    def _dfs(self, root, adj, visited):
        visited.add(root)
        for nei in adj[root]:
            if nei not in visited:
                self._dfs(nei, adj, visited)

    def makeConnected1(self, n: int, connections: List[List[int]]) -> int:
        _adj = defaultdict(list)
        for src, des in connections:
            _adj[src].append(des)
            _adj[des].append(src)
        visited = set()
        component = 0
        edges = len(connections)
        if n - 1 > edges: return -1
        print(_adj)
        for idx in range(n):
            if idx not in visited:
                self._dfs(idx, _adj, visited)
                component += 1
        print(_adj)
        return component - 1

    def makeConnected(self, n, connections):
        if len(connections) < n - 1: return -1
        G = [set() for i in range(n)]
        for i, j in connections:
            G[i].add(j)
            G[j].add(i)
        seen = [0] * n
        print(
            G
        )
        def dfs(i):
            if seen[i]: return 0
            seen[i] = 1
            for j in G[i]: dfs(j)
            return 1

        return sum(dfs(i) for i in range(n)) - 1


s = Solution()
adj_matrix = [[1, 4], [0, 3], [1, 3], [3, 7], [2, 7], [0, 1], [2, 4], [3, 6], [5, 6], [6, 7], [4, 7], [0, 7], [5, 7]]
print(s.makeConnected(len(adj_matrix), adj_matrix))
print(s.makeConnected1(len(adj_matrix), adj_matrix))
