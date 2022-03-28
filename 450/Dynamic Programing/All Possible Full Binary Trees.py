from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def allPossibleFBT(n: int) -> List:
    def generate(num):
        if n == 1: return [TreeNode()]
        if n % 2 == 0: return []
        ans = []
        for i in range(1,num,2):
            left = 6
