from collections import deque
from queue import PriorityQueue

def findItinerary(tickets):
    adj_list = {}
    for dep,ari in tickets:
        if dep in adj_list.keys():
            adj_list[dep].put(ari)
        else:
            d = PriorityQueue()
            d.put(ari)
            adj_list[dep] = d
    
    path = []
    def dfs(origin):
        path.append(origin)
        if origin in adj_list.keys():
            while not adj_list[origin].empty():
                dep = adj_list[origin].get()
                dfs(dep)
        return

    dfs("JFK")
    print(path)


tickets = [["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]
findItinerary(tickets)