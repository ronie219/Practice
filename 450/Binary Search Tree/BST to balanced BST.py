class Node:

    def __init__(self,data) -> None:
        self.data = data
        self.right = None
        self.left = None


def storeBstNodes(root,nodes):
    """
    store the values of the binary tree using the traversal method in an array.
    """
    if root is None:return
    storeBstNodes(root.left,nodes)
    nodes.append(root.data)
    storeBstNodes(root.right,nodes)


def buildTreeUtil(nodes,start,end):
    """
    Build the binary tree using the inorder traversal
    """
    if start > end:return
    mid_idx = (end + start) // 2
    root = Node(nodes[mid_idx])
    root.left = buildTreeUtil(nodes,start,mid_idx-1)
    root.right = buildTreeUtil(nodes,mid_idx+1,end)

    return root


def preOrder(root):
    if not root:
        return
    print("{} ".format(root.data),end="")
    preOrder(root.left)
    preOrder(root.right)

def buildTree(root):
    nodes = []
    storeBstNodes(root,nodes)
    n = len(nodes) - 1
    return buildTreeUtil(nodes,0,n)



if __name__=='__main__':
    # Constructed skewed binary tree is
    #         10
    #         /
    #         8
    #         /
    #     7
    #     /
    #     6
    #     /
    # 5
    root = Node(10)
    root.left = Node(8)
    root.left.left = Node(7)
    root.left.left.left = Node(6)
    root.left.left.left.left = Node(5)
    root = buildTree(root)
    print("Preorder traversal of balanced BST is :")
    preOrder(root)