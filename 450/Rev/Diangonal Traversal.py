from collections import deque


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

    def diagonalTraversal(self, root):
        answer = []
        queue = deque()
        queue.append(root)
        while queue:
            arr = []
            size = len(queue)
            for _ in range(size):
                curr = queue.popleft()
                while curr:
                    arr.append(curr.data)
                    queue.append(curr.left)
                    curr = curr.right
            answer.append(arr)
        return answer


if __name__ == '__main__':
    bt = BinaryTree()
    rt = bt.insert()

    bt.postOrder(rt)
    print('*' * 20)
    print(bt.diagonalTraversal(rt))
