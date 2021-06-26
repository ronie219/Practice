class Vertex:

    def __init__(self, n):
        self.name = n
        self.neighbour = []
        self.distance = 9999
        self.visited = False

    def add_neighbour(self, v):
        if v not in self.neighbour:
            self.neighbour.append(v)
            self.neighbour.sort()


class Graph:
    vertices = {}

    def add_vertices(self, vertex):
        if isinstance(vertex, Vertex) and vertex.name not in self.vertices.keys():
            self.vertices[vertex.name] = vertex
            return True
        return False

    def add_edge(self, u, v):
        if u in self.vertices and v in self.vertices:
            for key, value in self.vertices.items():
                if key == u:
                    value.add_neighbour(v)
                elif key == v:
                    value.add_neighbour(u)
            return True
        return False

    def print_graph(self):
        for key in sorted(list(self.vertices.keys())):
            print(key + str(self.vertices[key].neighbour) + " " + str(self.vertices[key].distance))

    def bfs(self, vert):
        q = []
        vert.distance = 0
        vert.visited = True
        for v in vert.neighbour:
            self.vertices[v].distance = vert.distance + 1
            q.append(v)

        while len(q) > 0:
            u = q.pop(0)
            node_u = self.vertices[u]
            node_u.visited = True

            for v in node_u.neighbour:
                node_v = self.vertices[v]
                if not node_v.visited:
                    q.append(v)
                    if node_v.distance > node_u.distance + 1:
                        node_v.distance = node_u.distance + 1


g = Graph()
a = Vertex("A")
g.add_vertices(a)
g.add_vertices(Vertex("B"))

for i in range(ord("A"), ord("K")):
    g.add_vertices(Vertex(chr(i)))

edges = ["AB", "AE", "BF", "CG", "DE", "DH", "EH", "FG", "FI", "FJ", "GJ", "HI"]
for edge in edges:
    # print(edge[0])
    g.add_edge(edge[0], edge[1])

g.bfs(a)
# g.print_graph()
print(a)
