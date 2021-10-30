
from os import path


class Solution:
    
    def _dfscall(self, item, adj, stack, visited):
        visited.add(item)
        for edge in adj[item]:
            if edge not in visited:
                self._dfscall(edge, adj, stack, visited)
        stack.append(item)

    
    #Function to return list containing vertices in Topological order.
    def topoSort(self, V, adj):
        # dfs
        stack = []
        visited = set()
        for vertex in range(V):
            if vertex not in visited:
                self._dfscall(vertex, adj, stack, visited)
        return stack[::-1]


    def findOrder(self,dic, N, K):
        graph = {}
        for idx in range(N - 1):
            first = dic[idx]
            second = dic[idx + 1]
            for alph in range(len(min(first, second))):
                if first[alph] != second[alph]:
                    if first[alph] in graph: 
                        graph[first[alph]].append(second[alph])
                    else:
                        graph[first[alph]] = [second[alph],]
                    break
        ans = ''
        visited = [0] * k

        self.typosort(graph,ans, visited)
        print(graph)
        return "Hello"



#{ 
#  Driver Code Starts
#Initial Template for Python 3

class sort_by_order:
    def __init__(self,s):
        self.priority = {}
        for i in range(len(s)):
            self.priority[s[i]] = i
    
    def transform(self,word):
        new_word = ''
        for c in word:
            new_word += chr( ord('a') + self.priority[c] )
        return new_word
    
    def sort_this_list(self,lst):
        lst.sort(key = self.transform)

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        line=input().strip().split()
        n=int(line[0])
        k=int(line[1])
        
        alien_dict = [x for x in input().strip().split()]
        duplicate_dict = alien_dict.copy()
        ob=Solution()
        order = ob.findOrder(alien_dict,n,k)
        s = ""
        for i in range(k):
            s += chr(97+i)
        l = list(order)
        l.sort()
        l = "".join(l)
        if s != l:
            print(0)
        else:
            x = sort_by_order(order)
            x.sort_this_list(duplicate_dict)
            
            if duplicate_dict == alien_dict:
                print(1)
            else:
                print(0)


# } D