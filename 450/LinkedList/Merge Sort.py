class Solution:
    #Function to sort the given linked list using Merge Sort.
    def _merge(self,left,right):
        if left is None and right is None:return
        if left is None:return right
        if right is None: return left

        dumy = Node(-1)
        prev = dumy
        while left and right:
            if left.data < right.data:
                prev.next = left
                prev = prev.next
                left = left.next
            else:
                prev.next = right
                prev = prev.next
                right = right.next
        
        if left is None:prev.next = right
        if right is None: prev.next = left

        return dumy.next

    def mergeSort(self, head):
        if head is None: return
        slow = head
        if head.next is None:
            return head
        fast = head.next.next

        while fast:
            if fast.next is not None:
                fast = fast.next.next
                slow = slow.next
            else:break
        mid = slow
        slow = slow.next
        mid.next = None
        left = self.mergeSort(head)
        right = self.mergeSort(slow)
        sort_head = self._merge(left,right)

        return sort_head

import atexit
import io
import sys

# Contributed by : Nagendra Jha

# Node Class
class Node:
    def __init__(self, data):  # data -> value stored in node
        self.data = data
        self.next = None


# Linked List Class
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # creates a new node with given value and appends it at the end of the linked list
    def append(self, new_value):
        new_node = Node(new_value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node    
            return
        self.tail.next = new_node
        self.tail = new_node

# prints the elements of linked list starting with head
def printList(head):
    if head is None:
        print(' ')
        return
    curr_node = head
    while curr_node:
        print(curr_node.data,end=" ")
        curr_node=curr_node.next
    print(' ')


if __name__ == '__main__':
    t=int(input())
    for cases in range(t):
        n = int(input())
        p = LinkedList() # create a new linked list 'a'.
        nodes_p = list(map(int, input().strip().split()))
        for x in nodes_p:
            p.append(x)  # add to the end of the list
        # printList(p.head)
        printList(Solution().mergeSort(p.head))

