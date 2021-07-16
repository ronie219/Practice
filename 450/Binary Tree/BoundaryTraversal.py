class Node:

    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None


class BinaryTree:

    def insert(self):
        data = int(input("Enter Data "))
        if data == -1:
            return None
        root = Node(data)
        print("Enter the Value in Left of " + str(data))
        root.left = self.insert()

        print("Enter the Value in Right of " + str(data))
        root.right = self.insert()
        return root
        
    def leftTree(self,root,output=[]):
        if root is None:
            return None
        output.append(root.data)
        if root.left:
            self.leftTree(root.left)
        elif root.right:
            self.leftTree(root.right)

        return output

    def rightTree(self,root,output=[]):
        if root is None:
            return None
        output.append(root.data)
        if root.right:
            self.rightTree(root.right)
        elif root.left:
            self.rightTree(root.left)

        return output

    def leafNode(self,root,output=[]):
        if root is None:
            return 
        if root.left is None and root.right is None:
            output.append(root.data)
        if root.left: self.leafNode(root.left)
        if root.right: self.leafNode(root.right)
        return output

    
    def BoundaryTraversal(self,root):
        left = self.leftTree(root)
        right = self.rightTree(root)[::-1]
        leaf = self.leafNode(root)
        # print("Left ",left)
        # print("Right ",right)
        # print("Leaf ",leaf)
        return left[:-1] + leaf + right[1:]


s = BinaryTree()
root = s.insert()
print(s.BoundaryTraversal(root))