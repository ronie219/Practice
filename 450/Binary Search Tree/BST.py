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
    
    # def find_max_left(self,root):
    #     if root is None: return
    #     if root.right:
    #         return self.find_max_left(root.right)
    #     else:
    #         return root.data

    def delete_node(self,root, item):
        if root is None: return
        if root.data < item: 
            root.right = self.delete_node(root.right,item)
        elif root.data > item: 
            root.left = self.delete_node(root.left, item)
        else:
            if root.left is None and root.right is None:
                return None
            elif root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            else:
                # We take min from right subtree.
                pointer = root.right
                while pointer.left:
                    pointer = pointer.left
                root.data = pointer.data
                root.right = self.delete_node(root.right, root.data)
        return root 

    def preOrder(self,root):  # NLR
        if root is None: return
        print(root.data, end=' ')
        self.preOrder(root.left)
        self.preOrder(root.right)
    

s = binarySearchTree()
s.insert(5)
s.insert(10)
s.insert(20)
s.insert(1)
s.insert(3)
s.insert(0)
s.preOrder(s.root)
s.delete_node(s.root,5)
print("break")
s.preOrder(s.root)