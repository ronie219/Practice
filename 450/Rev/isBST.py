class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinarySearchTree():

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

    def isBST(self, root):

        def _inner(rt):
            if rt is None:
                return [True,float('inf'), float('-inf')]

            left_bst, min_left, max_left = _inner(rt.left)
            right_bst, min_right, max_right = _inner(rt.right)
            curr_min = min(rt.data, min_left, min_right)
            curr_max = max(rt.data, max_right, max_left)

            if max_left < rt.data <= min_right and right_bst and left_bst:
                return [True, curr_min, curr_max]

            return [False, curr_min, curr_max]

        return _inner(root)[0]


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
    print(bst.isBST(bst.root))

