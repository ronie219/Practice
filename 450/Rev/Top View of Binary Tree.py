from collections import defaultdict, deque


class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class VerticalLevel:

    def __init__(self, node, level):
        self.node = node
        self.level = level


class BinaryTree:

    def insert(self):
        ele = int(input("Enter the data "))

        if ele == -1:
            return None
        root = Node(ele)
        print(f"Enter the left node for {ele} ")
        root.left = self.insert()

        print(f"Enter the right node for {ele} ")
        root.right = self.insert()

        return root

    def postOrder(self, root):  # L-R_N
        if root is None:
            return
        self.postOrder(root.left)
        self.postOrder(root.right)
        print(root.data, end='-')

    def topView(self, root):
        if not root: return []
        min_range = float('inf')
        max_range = float('-inf')
        answer = []
        level_memo = defaultdict(list)
        queue = deque()
        queue.append(VerticalLevel(root, 0))

        while queue:
            ele = queue.popleft()
            min_range = min(min_range, ele.level)
            max_range = max(max_range, ele.level)
            level_memo[ele.level].append(ele.node.data)
            if ele.node.left:
                lvl = VerticalLevel(ele.node.left, ele.level - 1)
                queue.append(lvl)
            if ele.node.right:
                lvl = VerticalLevel(ele.node.right, ele.level + 1)
                queue.append(lvl)

        for key in range(min_range,max_range+1):
            answer.append(level_memo[key][-1])
        return answer


if __name__ == '__main__':
    bt = BinaryTree()
    rt = bt.insert()
    bt.postOrder(rt)
    bt.topView(rt)
