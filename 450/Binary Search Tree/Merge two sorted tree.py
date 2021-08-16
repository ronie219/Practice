class Node:

    def __init__(self,data) -> None:
        self.data = data
        self.left = None
        self.right = None


def inorder(root,arr):
    if root is None: return

    inorder(root.left,arr)
    arr.append(root.data)
    inorder(root.right,arr)


def merge_sorted_arr(arr1,arr2):
    arr = []
    counter1 = 0
    counter2 = 0
    while len(arr1) > counter1 and len(arr2) > counter2:
        if arr1[counter1] < arr2[counter2]:
            arr.append(arr1[counter1])
            counter1 +=1
        elif arr1[counter1] >= arr2[counter2]:
            arr.append(arr2[counter2])
            counter2 +=1
    if len(arr2) > counter2:
        arr.extend(arr2[counter2:])
    if len(arr1) > counter1:
        arr.extend(arr1[counter1:])
    
    return arr
    
def insert(root, val):
    if not root:
        return Node(val)
    if root.data == val:
        return root
    elif root.data > val:
        root.left = insert(root.left, val)
    else:
        root.right = insert(root.right, val)
    return root


def arr_to_bst(nodes,start,end):

    if start > end:return
    mid_idx = (end + start) // 2
    root = Node(nodes[mid_idx])
    root.left = arr_to_bst(nodes,start,mid_idx-1)
    root.right = arr_to_bst(nodes,mid_idx+1,end)

    return root

if __name__=='__main__':
    root1 = root2 = None
     
    # Inserting values in first tree
    root1 = insert(root1, 100)
    root1 = insert(root1, 50)
    root1 = insert(root1, 300)
    root1 = insert(root1, 20)
    root1 = insert(root1, 70)
     
    # Inserting values in second tree
    root2 = insert(root2, 80)
    root2 = insert(root2, 40)
    root2 = insert(root2, 120)
    arr1 = []
    inorder(root1, arr1)
    arr2 = []
    inorder(root2, arr2)
    arr = merge_sorted_arr(arr1, arr2)
    root = arr_to_bst(arr,0,len(arr)-1)
    res = []
    inorder(root, res)
    print('Following is Inorder traversal of the merged tree')
    for i in res:
      print(i, end = ' ')



# arr1 = [4,5,7,10,20,50]
# arr2 = [1,2,6,30,100]

# print(merge_sorted_arr(arr1,arr2))


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        
        if root1 is None and root2 is None:return
        if root1 is None and root2 is not None: return root2
        if root1 is not None and root2 is None: return root1
        new_node = TreeNode(root1.val + root2.val)
        new_node.left = self.mergeTrees(root1.left,root2.left)
        new_node.right = self.mergeTrees(root1.right,root2.right)
        
        return new_node