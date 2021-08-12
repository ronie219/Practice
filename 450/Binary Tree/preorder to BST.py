INT_MIN = float("-infinity")
INT_MAX = float("infinity")

class Node:

    def __init__(self,data) -> None:
        self.left = None
        self.right = None
        self.data = data
    

class BinaryTree:
    
    def preOrder(self, root):  # NLR

        if root is None: return
        print(root.data, end=' ')
        self.preOrder(root.left)
        self.preOrder(root.right)

    def BSTtoTree(arr = []):
        if arr is []:
            return
        
