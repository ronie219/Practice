from collections import defaultdict, deque


class Graph:

    def __init__(self,V):
        self.V = V
        self.edge = defaultdict(list)

    def add_edge(self,u,v):
        self.edge[u].append(v)

    def minimumTime(self):
        queue = deque()
        in_degree = {i: 0 for i in range(self.V)}
        # now we traverse the adj and find the inDegree for each vertex
        for ad_list in range(self.V):
            for ver in self.edge[ad_list]:
                in_degree[ver] += 1
        for idx in range(self.V):
            if in_degree[idx] == 0:
                queue.append(idx)
        while queue:
            size = len(queue)
            for _ in range(size):
                cur = queue.popleft()
                queue.append()