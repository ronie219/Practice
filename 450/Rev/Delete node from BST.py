class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)


class BinarySearchTree:

    salary = 1000
    incre = 5

    def __init__(self):
        self.root = None

    def _insert(self, root, data):
        if root.data <= data:
            if root.right:
                self._insert(root.right, data)
            else:
                root.right = Node(data)

        if root.data > data:
            if root.left:
                self._insert(root.left, data)
            else:
                root.left = Node(data)

    def insert(self, data):
        if not self.root:
            self.root = Node(data)
        else:
            self._insert(self.root, data)

    def _inOrder(self, rt):
        if not rt:
            return
        self._inOrder(rt.left)
        print(rt.data, end=' ')
        self._inOrder(rt.right)

    def inOrder(self):
        root = self.root
        self._inOrder(root)

    @staticmethod
    def _findMiniNode(root):
        curr = root
        min_node = None
        while curr:
            min_node = curr
            curr = curr.left
        return min_node

    def _deleteNode(self, root, key):
        if root is None:
            print(f"Key '{key}' is not found")
            return
        if root.data < key:
            root.right = self._deleteNode(root.right, key)
        elif root.data > key:
            root.left = self._deleteNode(root.left, key)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            else:
                min_right = self._findMiniNode(root.right)
                root.data = min_right.data
                root.right = self._deleteNode(root.right, min_right.data)
        return root

    def deleteNode(self, key):
        root = self.root
        self._deleteNode(root, key)

    @classmethod
    def func(cls):
        cls.salary = cls.salary * cls.incre



if __name__ == '__main__':
    bst = BinarySearchTree()
    bst.insert(5)
    bst.insert(6)
    bst.insert(8)
    bst.insert(2)
    bst.insert(0)
    bst.insert(1)
    bst.insert(10)
    bst.insert(22)
    bst.insert(7)
    bst.insert(7)
    bst.inOrder()
    bst.deleteNode(1000)
    print()
    bst.inOrder()
