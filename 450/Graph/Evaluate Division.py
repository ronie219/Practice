from collections import defaultdict
def calcEquation(equations, values, queries):
    graph = defaultdict(list)
    for (a, b), v in zip(equations, values):
        graph[a].append([b, v])
        graph[b].append([a, 1/v])
        
    def dfs(src, dst, res, seen):
        if src == dst: return res
        if src in seen: return -1
        seen.add(src)
        for nei, w in graph[src]:
            tmp = dfs(nei, dst, res * w, seen)
            if tmp != -1:
                return tmp
        return -1
        
    ans = []
    for a, b in queries:
        if a not in graph or b not in graph:
            ans.append(-1)
        else:
            ans.append(dfs(a, b, 1, set()))
    return ans



    


equation = [["a","b"],["b","c"]]
values = [2.0,3.0]
queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
print(calcEquation(equation, values, queries))