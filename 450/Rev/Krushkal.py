class UnionFind:

    def __init__(self):
        self.parent = -1
        self.rank = 1

    @classmethod
    def findParent(cls,edge, arr):
        if arr[edge].parent == -1: return edge
        arr[edge].parent = cls.findParent(arr[edge].parent,arr)
        return arr[edge].parent

    @classmethod
    def union(cls,idx1, idx2, arr):
        if arr[idx1].rank < arr[idx2].rank:
            arr[idx1].parent = idx2
        elif arr[idx1].rank > arr[idx2].rank:
            arr[idx2].parent = idx1
        else:
            arr[idx2].parent = idx1
            arr[idx2].rank += 1



class Graph:

    def __init__(self, vertex):
        self.vertex = vertex
        self.graph = []

    def add_edge(self, from_edge, to_edge, weight):
        self.graph.append((from_edge, to_edge, weight))

    def KruskalMST(self):
        self.graph.sort(key=lambda x: x[2])
        answer = []
        parent_rank_arr = []
        # we initialize for the parent_rank_arr with default value of parent = -1 and rank = 1
        for idx in range(self.vertex):
            parent_rank_arr.append(UnionFind())

        # now for each edges we check if the two edges are present in our MST using union find
        for edge in self.graph:
            p1 = UnionFind.findParent(edge[0],parent_rank_arr)
            p2 = UnionFind.findParent(edge[1], parent_rank_arr)
            if p1 != p2:
                answer.append(edge)
                UnionFind.union(p1,p2, parent_rank_arr)

        print(answer)


if __name__ == '__main__':
    g = Graph(4)
    g.add_edge(0, 1, 10)
    g.add_edge(0, 2, 6)
    g.add_edge(0, 3, 5)
    g.add_edge(1, 3, 15)
    g.add_edge(2, 3, 4)
    g.KruskalMST()
