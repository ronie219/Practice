class Node:
    def __init__(self):
        self.inDegrees = 0
        self.outDegrees = []
        
import collections
class Solution:
    def findOrder(self, numCourses, prerequisites):
        
        graph = collections.defaultdict(Node)
        
        totalDeps = 0
        # print(graph)
        for p in prerequisites:
            nextCourse, prevCourse = p[0], p[1]
            graph[nextCourse].inDegrees += 1
            graph[prevCourse].outDegrees.append(nextCourse)
            totalDeps += 1
        # print(graph)
        queue = collections.deque([])
        
        for course, node in graph.items():
            if node.inDegrees == 0:
                queue.append(course)
        
        res = []
        
        for i in range(numCourses):
            if i not in graph:
                res.append(i)
        
        while queue:
            course = queue.popleft()
            res.append(course)
            
            for nextCourse in graph[course].outDegrees:
                graph[nextCourse].inDegrees -= 1
                if graph[nextCourse].inDegrees == 0:
                    queue.append(nextCourse)
                    
                          
        if len(res) < numCourses:
            return []
        
        return res

s = Solution()
p = [[1,0],[2,0],[3,1],[3,2]]
print(s.findOrder(4, p))