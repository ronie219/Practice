class Node:

    # Constructor to initialize the node object
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    # Function to initialize head
    def __init__(self):
        self.head = None

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    # Utility function to print the linked LinkedList
    def printList(self):
        temp = self.head
        while (temp):
            print(temp.data)
            temp = temp.next

    def reverseListItter(self):
        prev = None
        current = self.head
        while current is not None:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev

    def reverseListRecurr(self, head):
        if head is None or head.next is None:
            return head
        list = self.reverseListRecurr(head.next)
        head.next.next = head
        head.next = None
        return list

    def kreverse(self, head, k):
        prev = None
        current = head
        next = None
        for idx in range(k):
            if current is not None:
                next = current.next
                current.next = prev
                prev = current
                current = next
            else:
                break

        if next is not None:
            current.next = self.kreverse(next,k)

        return prev



llist = LinkedList()
llist.push(20)
llist.push(4)
llist.push(15)
llist.push(85)
print("Given Linked List")
llist.printList()
kreverse = llist.kreverse(llist.head,3)

print("List reversed")

llist.printList()
