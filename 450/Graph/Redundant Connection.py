class Node:

    def __init__(self):
        self.parent = -1
        self.rank = 0

def findParent(idx, arr):
    if arr[idx].parent == -1:
        return idx
    arr[idx].parent = findParent(arr[idx].parent,arr)
    return arr[idx].parent

def union(fromidx, toidx, arr):
    toN = arr[toidx]
    fromN = arr[fromidx]

    if toN.rank < fromN.rank:
        toN.parent = fromidx
    elif fromN.rank < toN.rank:
        fromN.parent = toidx
    else:
        fromN.parent = toidx
        fromN.rank += 1
    

def findRedundantConnection(edges):
    vertex = set()
    for src, dest in edges:
        vertex.add(src)
        vertex.add(dest)
    
    edges_len = len(vertex)
    arr = []
    for _ in range(edges_len+1):
        arr.append(Node())
    ans = []
    for src,des in edges:
        toP = findParent(src,arr)
        fromP = findParent(des,arr)
        if toP == fromP :
            ans = (src, des)
            return ans
        union(toP, fromP, arr)
    return ans

edg = [[1,2],[1,3],[2,3]]
print(findRedundantConnection(edg))