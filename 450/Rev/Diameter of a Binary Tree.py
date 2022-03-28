class Node:

    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


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

    def height(self, root):
        if root is None:
            return 0
        return max(self.height(root.left), self.height(root.right)) + 1

    def postOrder(self, root):  # LRN

        if root is None:
            return
        self.postOrder(root.left)
        self.postOrder(root.right)
        print(root.data, end=' ')

    def diameter(self, root):
        if root == None:
            return 0

        lheight = self.height(root.left)
        rheight = self.height(root.right)

        ldiameter = self.diameter(root.left)
        rdiameter = self.diameter(root.right)

        return max((lheight+rheight+1), max(ldiameter, rdiameter))


if __name__ == '__main__':
    bt = BinaryTree()
    rt = bt.insert()

    bt.postOrder(rt)
    print('*' * 20)
    print(bt.diameter(rt))
    print(bt.height(rt))
