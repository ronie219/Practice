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

    def postOrder(self, root):  # LRN

        if root is None: return
        self.postOrder(root.left)
        self.postOrder(root.right)
        print(root.data, end=' ')


    def preOrder(self, root):  # NLR

        if root is None: return
        print(root.data, end=' ')
        self.preOrder(root.left)
        self.preOrder(root.right)

    def inOrder(self, root):  # LNR

        if root is None: return
        self.inOrder(root.left)
        print(root.data, end=' ')
        self.inOrder(root.right)

    def recINorder(self,root):
        stack = []
        current = root

        while current or stack:
            if current is not None:
                stack.append(current)
                current = current.left
            else:
                current = stack.pop()
                print(current.data, end=' ')
                current = current.right


    def recPreorder(self,root):
        stack = []
        current = root
        result = ''
        while current or stack:
            if current is not None:
                result += (str(current.data) + ' ')
                stack.append(current)
                current = current.left
            else:
                current = stack.pop()
                current = current.right
        print(result)

    def recPostorder(self,root):
        stack = []
        current = root

        while current or stack:
            if current is not None:
                print(current.data, end=' ')
                stack.append(current)
                current = current.left
            else:
                current = stack.pop()
                current = current.right
        print()


s = BinaryTree()
root = s.insert()
# print("Post order")
# s.postOrder(root)
# s.recPostorder(root)

print("Pre order")
s.preOrder(root)
s.recPreorder(root)

# print("In order")
# s.inOrder(root)
# s.recINorder(root)