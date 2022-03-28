from collections import deque


class Solution:

    def topoSort(self, V, adj):

        in_degree = {i: 0 for i in range(V)}
        # now we traverse the adj and find the inDegree for each vertex
        for ad_list in range(V):
            for ver in adj[ad_list]:
                in_degree[ver] += 1

        adj = [set(i) for i in adj]

        # we initialize the 0 inDegree and insert it into a queue
        print(in_degree)
        queue = deque()
        for idx in range(V):
            if in_degree[idx] == 0:
                queue.append(idx)
        result = []
        while queue:
            curr = queue.popleft()
            result.append(curr)
            for idx in range(V):
                if curr in adj[idx]:
                    adj[idx].remove(curr)
                    in_degree[idx] -= 1
                    if in_degree[idx] == 0:
                        queue.append(idx)

        print(result)



import sys

sys.setrecursionlimit(10 ** 6)


def check(graph, N, res):
    if N != len(res):
        return False
    map = [0] * N
    for i in range(N):
        map[res[i]] = i
    for i in range(N):
        for v in graph[i]:
            if map[i] > map[v]:
                return False
    return True


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        e, N = list(map(int, input().strip().split()))
        adj = [[] for i in range(N)]
        print(adj)
        for i in range(e):
            u, v = map(int, input().split())
            adj[u].append(v)
        print(adj)
        ob = Solution()
        print(ob.topoSort(N, adj))
