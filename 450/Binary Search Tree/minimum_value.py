def minValue(root):
    # recureSive call
    if root.left is None:
        return root.data
    return minValue(root.left)
    
def minValue(root):
    # iterative
    pointer = root
    while pointer.left:
        pointer = pointer.left
    return pointer.data