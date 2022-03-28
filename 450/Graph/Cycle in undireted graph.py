from collections import deque


class Solution:

    def _inner(self, root, parent, visited, adj):
        visited[root] = 1
        for node in adj[root]:
            if visited[node] == 1 and parent != node: return True
            if self._inner(node, root, visited, adj): return True

    def isCycle(self, V, adj):
        visited = [0] * V

        for i in range(len(adj)):
            if visited[i] == 0:
                if self._inner(i, -1, visited, adj): return True

        return False


if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        V, E = map(int, input().split())
        adj = [[] for i in range(V)]
        for _ in range(E):
            u, v = map(int, input().split())
            adj[u].append(v)
            adj[v].append(u)
        obj = Solution()
        ans = obj.isCycle(V, adj)
        if (ans):
            print("1")
        else:
            print("0")
