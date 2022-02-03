from calendar import c
from re import S
from tkinter import N
from tkinter.messagebox import NO


class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkList:

    def __init__(self):
        self.head = None

    def insertNewNode(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
        else:
            head = self.head
            while head.next:
                head = head.next

            head.next = node

    def printNode(self):
        head = self.head
        while head.next:
            print(head.data, end=' --> ')
            head = head.next
        print(head.data)

    def reverseLinkList_(self):
        curr = self.head
        prev = None
        next = None
        if curr is None:
            return
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        self.head = prev

    def reverseLinkList_(self):
        head = self.head

        def inner(head, prev=None):
            if not head.next:
                self.head = head
                head.next = prev
                return
            inner(head.next, head)
            head.next = prev

        inner(head)


if __name__ == '__main__':
    l = LinkList()
    l.insertNewNode(1)
    l.insertNewNode(2)
    l.insertNewNode(3)
    l.insertNewNode(4)
    l.insertNewNode(5)
    l.printNode()
    l.reverseLinkList()
    l.printNode()
