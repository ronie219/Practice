from collections import defaultdict


def find_colour(graph, vertex, colour_arr, colour):
    for adj in graph[vertex]:
        if colour_arr[adj] != -1:
            colour[colour_arr[adj]] = True


def colour_graph(vertex, colour_arr, colour, k):
    for col in range(k):
        if colour[col] == False:
            colour_arr[vertex] = col
            return True

    return False


def graphColoring(graph, k, V):
    colour = [False] * k
    colour_arr = [-1] * V
    # colour_arr[0] = 0

    for vertex in range(V):
        if colour_arr[vertex] == -1:
            find_colour(graph, vertex, colour_arr, colour)
            out = colour_graph(vertex, colour_arr, colour, k)
            if out == False: return False
            colour = [False] * k
    return True


def createGraph(edges):
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    return graph


edges = [(0, 1), (1, 2), (0, 2)]
graph = createGraph(edges)
print(graph)
print(graphColoring(graph, 2, 3))
