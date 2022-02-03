from collections import defaultdict

class Graph:

    def __init__(self,V):
        self.V = V
        self.graph = defaultdict(list)

    def add_egde(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)


    def find_bridge(self):
        visited = set()
        In = [None] * self.V
        low = [None] * self.V
        # global timer
        
        def dfs(node, parent,timer):
            In[node] = timer
            low[node] = timer 
            timer += 1
            visited.add(node)
            for adj in self.graph:
                if adj in visited:
                    if adj == parent: continue
                    else:
                        low[node] = min(low[node], In[adj])
                else:
                    dfs(adj,node,timer)
                    if low[adj] > In[node]:
                        print(f"{node}  --> {adj}")
                    
                    low[node] = min(low[node], In[adj])
        dfs(0,-1,0)
        


if __name__ == '__main__':
    g = Graph(5)
    g.add_egde(1,0)
    g.add_egde(1,2)
    g.add_egde(0,2)
    g.add_egde(0,3)
    g.add_egde(3,4)
    g.find_bridge()