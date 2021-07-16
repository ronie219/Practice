class Node:

    def __init__(self,data) -> None:
        self.left = None
        self.right = None
        self.data = data


class BinaryTree:
    # "4(2(3)(1))(6(5))"
    def stringToTree(self,string,root=None):
        if len(string) == 0:
            return root
        if root is None: root = Node(string[0])
        if string[0] == '(':
            self.stringToTree(string[1:],root)
        elif string[0] == ')':
            return root
        else:
            if root.left is None:
                root.left = Node(string[0])
                self.stringToTree(string[1:],root.left)
            elif root.right is None:
                root.right = Node(string[0])
                self.stringToTree(string[1:],root.right)
        return root

    def preOrder(self, root):  # NLR

        if root is None: return
        print(root.data, end=' ')
        self.preOrder(root.left)
        self.preOrder(root.right)


s = BinaryTree()
root = s.stringToTree("4(2(3)(1))(6(5))")
s.preOrder(root)