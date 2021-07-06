from collections import deque

class Node:

    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None


class BinaryTree:

    def insert(self):
        data = input("Enter Data ")
        if data == '-1':
            return None
        root = Node(data)
        print("Enter the Value in Left of " + str(data))
        root.left = self.insert()

        print("Enter the Value in Right of " + str(data))
        root.right = self.insert()
        return root

    def diagonalTraversal(self,root):
        if root is None:
            return
        queue = deque()
        queue.append(root)
        output = []
        while queue:
            size = len(queue)
            component = []
            for _ in range(size):
                current = queue.popleft()
                while current:
                    component.append(current.data)
                    if current.left:queue.append(current.left)
                    current = current.right
            output.append(component)
        return output

    def diagonalTraversalHashing(self,root):
        if root is None:
            return
        
        track = {}
        stack = deque()
        stack.append([root,0])
        while stack:
            curr = stack.pop()
            if curr[1] in track.keys():
                track[curr[1]].append(curr[0].data)
            else:
                track[curr[1]] = [curr[0].data]

            if curr[0].right: stack.append([curr[0].right,curr[1]])
            if curr[0].left: stack.append([curr[0].left,curr[1]+1])
        print(track)

s = BinaryTree()
root = s.insert()
print(s.diagonalTraversal(root))
s.diagonalTraversalHashing(root)