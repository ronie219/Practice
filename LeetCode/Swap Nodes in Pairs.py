# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head):
        if head is None:
            return head
        if head.next is None:
            return head
        current = head
        next_ = head.next

        while next_ is not None:
            current.val,next_.val = next_.val,current.val
            if next_.next_ is not None and next_.next.next is not None:
                current = next_.next_
                next_ = current.next
            else:
                break

        return head