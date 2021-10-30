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

    # def _reverse(self,head,k):
    #     pass

    # def group_reverse_itter(self,k):
    #     link_list = None
    #     current_head = self.head

    #     while current_head is not None:
    #         main_head,ll = self._reverse(current_head,k)
    #         if link_list is None:
    #             self.head = main_head
    #             link_list = ll
    #         else:
    #             link_list.next = ll
            
    #         current_head.next = main_head.next


    def group_reverse(self,head,k):
        if head is None: return
        current = head
        prev = None
        next = None
        count = 0
        while current is not None and count < k:
            next = current.next
            current.next = prev
            prev = current
            current = next
            count += 1

        if next is not None:
            head.next = self.group_reverse(next,k)
        
        return prev


if __name__ == '__main__':
    linkedList = LinkList()
    linkedList.push(1)
    linkedList.push(2)
    linkedList.push(3)
    linkedList.push(4)
    linkedList.push(5)
    print("*" * 10)
    print(linkedList)
    linkedList.head = linkedList.group_reverse(linkedList.head,3)
    print("*" * 10)
    print(linkedList)