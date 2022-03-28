from queue import PriorityQueue


def dijkstra(adj, n, src=0):
    pqueue = PriorityQueue()
    distance = [float('inf') for _ in range(n)]
    distance[src] = 0
    for i in adj[src]:
        pqueue.put((i[1], i[0]))
    while not pqueue.empty():
        ele = pqueue.get()


adj_weight = {
    1: [(2, 2), (4, 1)],
    2: [(1, 2), (5, 5), (3, 4)],
    3: [(2, 4), (4, 3), (5, 1)],
    4: [(1, 1), (3, 3)],
    5: [(2, 5), (3, 1)]
}
dijkstra(adj_weight, len(adj_weight.keys()))
