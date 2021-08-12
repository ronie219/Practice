class Node:

    def __init__(self,data) -> None:
        self.data = data
        self.left = None
        self.right =None

INT_MIN = float("-infinity")
INT_MAX = float("infinity")
idx = 0

def PreToBST(arr,idx=0,lr=INT_MIN,hr=INT_MAX):
    if idx > len(arr) or arr[idx] < lr or arr[idx] > hr:
        return None
    node = Node(arr[idx])
    idx += 1
    node.left = PreToBST(arr,idx,lr,node.data)
    node.right = PreToBST(arr,idx,node.data,hr)

    return node




def preOrder(root):  # NLR
    if root is None: return
    print(root.data, end=' ')
    preOrder(root.left)
    preOrder(root.right)


arr = [30,20,10,15,25,23,39,35,42]
root = PreToBST(arr)
preOrder(root)