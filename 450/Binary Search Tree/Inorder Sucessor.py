class Node:

    def __init__(self,data) -> None:
        self.left = None
        self.right = None
        self.data = data
        self.next = -1
    

class binarySearchTree:
    prev = None

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


    def inorderSuccessor(self,root):
        if root is None: 
            return 
        self.inorderSuccessor(root.left)
        if binarySearchTree.prev is not None:
            binarySearchTree.prev.next = root
        binarySearchTree.prev = root
        self.inorderSuccessor(root.right)


    def inOrder(self,root):
        if root is None:
            return
        self.inOrder(root.left)
        if root.next == -1:
            print(-1)
        else:
            print(root.next.data)
        self.inOrder(root.right)
    


s = binarySearchTree()
s.insert(10)
s.insert(8)
s.insert(3)
s.insert(12)

s.inorderSuccessor(s.root)
s.inOrder(s.root)