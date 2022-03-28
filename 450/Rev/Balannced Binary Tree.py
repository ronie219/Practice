class Node:

    def __init__(self, data):
        self.root = data
        self.left = None
        self.right = None


def balanceBinaryTree(inorder):
    start_idx = 0
    end_idx = len(inorder) - 1

    def _inner(srt, end):
        if srt >= end:
            return None
        mid = (end - srt) // 2
        root = Node(inorder[mid])
        root.left = _inner(srt, mid - 1)
        root.right = _inner(mid + 1, end)
        return root

    return _inner(start_idx, end_idx)


def inorder(root, arr=[]):
    if root is None:
        return None
    inorder(root.left, arr)
    arr.append(root.data)
    inorder(root.right, arr)
    return arr


in_order = [1, 2, 3, 4, 6, 7, 20]
rt = balanceBinaryTree(in_order)
print(inorder(rt))
