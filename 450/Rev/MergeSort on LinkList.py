class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)


class LinkList:

    def __init__(self):
        self.head = None

    def __str__(self):
        arr = []
        head = self.head
        while head:
            arr.append(str(head.data))
            head = head.next
        return " -> ".join(arr)

    def push(self, ele):
        node = Node(ele)
        if self.head is None:
            self.head = node
        else:
            head = self.head
            while head.next:
                head = head.next
            head.next = node

    @staticmethod
    def mergeTwoSortedArray(head1, head2):
        dummy_node = Node(float('-inf'))
        prev = dummy_node
        h1 = head1
        h2 = head2

        while h1 is not None and h2 is not None:
            if h1.data < h2.data:
                prev.next = h1
                prev = prev.next
                h1 = h1.next
            else:
                prev.next = h2
                prev = prev.next
                h2 = h2.next

        if h1:
            prev.next = h1
        if h2:
            prev.next = h2

        return dummy_node.next

    @staticmethod
    def findMidNode(head):
        slw = head
        fast = head

        while fast.next is not None and fast.next.next:
            slw = slw.next
            fast = fast.next.next

        return slw

    def findTail(self):
        head = self.head
        tail = None
        while head:
            tail = head
            head = head.next
        return tail

    def mergeSort(self):
        head = self.head
        tail = self.findTail()

        def _inner(h, t):
            if h == t:
                return h
            mid_node = LinkList.findMidNode(h)
            right_head = mid_node.next
            mid_node.next = None
            left = _inner(h, mid_node)
            right = _inner(right_head, t)

            return LinkList.mergeTwoSortedArray(left, right)

        self.head = _inner(head, tail)


if __name__ == '__main__':
    l1 = LinkList()
    l1.push(1)
    l1.push(2)
    l1.push(3)
    l1.push(15)
    l1.push(80)
    l1.push(200)
    l1.push(4000)
    l1.push(200000)
    print(l1)
    l1.mergeSort()
    print(l1)
    # l2 = LinkList()
    # l2.push(1)
    # l2.push(2)
    # l2.push(3)
    # l2.push(8)
    # l2.push(9)
    # l2.push(20)
    # print(l2)
    # l3 = LinkList()
    # l3.head = LinkList.mergeTwoSortedArray(l1.head, l2.head)
    # print(l3)
