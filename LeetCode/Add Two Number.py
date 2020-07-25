
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        num1 = ''
        num2 = ''
        curr = l1
        while curr.next:
            num1 += curr.data
            curr = curr.next
        curr = l2
        while curr.next:
            num2 += curr.data
            curr = curr.next
        num1,num2 = reversed(num1),reversed(num2)
        total = num2+num2
        total = reversed(str(total))
        