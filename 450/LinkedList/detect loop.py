"""
Floyd Algorithm
"""
class Node:

    def __init__(self,data) -> None:
        self.data = data
        self.next = None
    

class LinkList:

    def __init__(self,head =None) -> None:
        self.head = head

    def push(self,data):
        if self.head is None:
            self.head = Node(data)
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = Node(data)

    def __str__(self) -> str:
        items = []
        cur = self.head
        
        while cur:
            items.append(str(cur.data))
            cur = cur.next
        return " --> ".join(items)
    
    def detect_loop(self):
        slow_p = self.head
        fast_p = self.head.next.next

        while slow_p and fast_p:
            if slow_p == fast_p: return True
            slow_p = slow_p.next
            if fast_p.next is not None:
                fast_p = fast_p.next.next
            else:
                return False
        
        return False