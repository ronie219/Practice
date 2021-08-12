class Node:

    def __init__(self,data) -> None:
        self.left = None
        self.right = None
        self.data = data
    

class binarySearchTree:

    def __init__(self) -> None:
        self.root = None

    def _insert(self,root,item):
        if root.data < item:
            if root.right:
                self._insert(root.right,item)
            else:
                root.right = Node(item)

        if root.data > item:
            if root.left:
                self._insert(root.left,item)
            else:
                root.left = Node(item)

    def insert(self,item):
        if self.root == None:
            self.root = Node(item)
        else:
            self._insert(self.root,item)


