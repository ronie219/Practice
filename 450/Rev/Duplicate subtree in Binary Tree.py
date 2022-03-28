class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


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
        if root is None:
            return
        self.postOrder(root.left)
        self.postOrder(root.right)
        print(root.data, end=' ')

    def findDuplicate(self, rt):
        tree_memo = set()

        def _inner(root):
            if root is None:
                return '$', False

            left, l_checked = _inner(root.left)
            right, r_checked = _inner(root.right)
            string = left + str(root.data) + right

            if string in tree_memo and len(string) >= 6:
                return left + str(root.data) + right, True
            tree_memo.add(string)
            return left + str(root.data) + right, (l_checked or r_checked)

        _, flag = _inner(rt)
        return flag


if __name__ == '__main__':
    bt = BinaryTree()
    rt = bt.insert()

    bt.postOrder(rt)
    print('*' * 20)
    print(bt.findDuplicate(rt))
