# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# 1->2->4, 
# 1->3->4
class Solution:
    def mergeTwoLists(self, l1, l2):
        head = ListNode(0)
        pointer = head
        while l1 and l2:
            if l2.val > l1.val:
                pointer.nex = (l1)
                pointer = pointer.next
                l1 = l1.next
            else:
                pointer.next = l2
                pointer = pointer.next
                l2 = l2.next
        if l2 is None:
            pointer.next = (l1)
        elif l1 is None:
            pointer.next = (l2)
        return head

        
s = Solution()
