from typing import Counter


class Node:

    def __init__(self,data) -> None:
        self.data = data
        self.next = None

class LinkList:

    def __init__(self) -> None:
        self.head = None 


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

    def reverse(self):
        prev = None
        curr = self.head
        next = None
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        self.head = prev
    
    def _recursive_reverse(self,head,prev):
        if head.next is None: 
            self.head = head
            head.next = prev
            return
        self._recursive_reverse(head.next,head)
        head.next = prev


    def recursive_reverse(self):
        if self.head is not None:
            self._recursive_reverse(self.head,None)
            
    

linkedList = LinkList()
linkedList.push(20)
linkedList.push(4)
linkedList.push(15)
linkedList.push(85)

print("*" * 10)
print(linkedList)
linkedList.recursive_reverse()
print(("*" * 10 )+ " reversed list " + ("*" * 10))
print(linkedList)
