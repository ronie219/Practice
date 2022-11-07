from typing import List, Dict
from collections import defaultdict
import heapq


def create_adj_mapping(points: List[List[int]]) -> Dict:
    adj_matrix = defaultdict(list)
    for src in range(len(points) - 1):
        for des in range(src + 1, len(points)):
            cost = abs(points[src][0] - points[des][0]) + abs(points[src][1] - points[des][1])
            adj_matrix[src].append([des, cost])
            adj_matrix[des].append([src, cost])
    return adj_matrix


def minCostConnectPoints(points: List[List[int]]) -> int:
    adj_matrix = create_adj_mapping(points)
    total_cost = 0
    # cost, des, parent
    buffer = [[0, 0, -1]]
    heapq.heapify(buffer)
    visited = set()
    while buffer:
        smallest = heapq.heappop(buffer)
        if smallest[1] not in visited:
            visited.add(smallest[1])
            total_cost += smallest[0]
            for item in adj_matrix[smallest[1]]:
                buffer.append([item[1], item[0], smallest[1]])
    return total_cost


array = [[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]

print(create_adj_mapping(array))
print(minCostConnectPoints(array))
