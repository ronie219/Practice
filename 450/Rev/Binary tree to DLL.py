class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:

    def __init__(self):
        self.prev = None

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
        if root is None:
            return
        self.postOrder(root.left)
        self.postOrder(root.right)
        print(root.data, end=' ')

    def bstToDLL(self, root):
        dummy = Node(-1)
        self.prev = dummy
        cur = root

        def _inner(rt):
            if not rt:
                return
            _inner(rt.left)
            self.prev.right = rt
            rt.left = self.prev
            self.prev = rt

            _inner(rt.right)

        _inner(cur)

        return dummy.right

    def printLinkList(self,root):
        curr = root
        arr = []
        while curr:
            arr.append(str(curr.data))
            curr = curr.right
        print('-->'.join(arr))


if __name__ == '__main__':
    bt = BinaryTree()
    rt = bt.insert()

    bt.postOrder(rt)
    print('*' * 20)
    root = bt.bstToDLL(rt)
    print(root.right)
    bt.printLinkList(root)

