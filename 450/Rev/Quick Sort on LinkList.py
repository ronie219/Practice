class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkList:

    def __init__(self):
        self.head = None

    def __str__(self):
        arr = []
        curr = self.head
        while curr:
            arr.append(str(curr.data))
            curr = curr.next
        return '-->'.join(arr)

    def push(self, ele):
        node = Node(ele)
        if not self.head:
            self.head = node
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = node

    @staticmethod
    def _segregate(head):
        small_head = Node(float('inf'))
        large_head = Node(float('inf'))
        pivot = head
        smlp = small_head
        lrgp = large_head
        curr = head
        while curr:
            if curr.data < pivot.data:
                smlp.next = curr
                smlp = smlp.next
            elif curr.data > pivot.data:
                lrgp.next = curr
                lrgp.next = curr
            else:
                if curr is not pivot:
                    lrgp.next = curr
                    lrgp = lrgp.next
            curr = curr.next
        smlp.next = None
        lrgp.next = None
        pivot.next = None
        return small_head.next, large_head.next, pivot

    @staticmethod
    def _mergeLinkList(h1, pvt, h2):
        lw = h1
        if h1:
            while h1.next:
                h1 = h1.next
            h1.next = pvt
        if h2:
            while h2.next:
                h2 = h2.next
            pvt.next = h2
        return lw if lw else pvt

    def quickSort(self):
        h = self.head

        def _inner(head):
            if head is None or head.next is None:
                return head
            left_h, pivot, right_h = LinkList._segregate(head)
            left = _inner(left_h)
            right = _inner(right_h)
            return LinkList._mergeLinkList(left, pivot, right)
        self.head = _inner(h)


if __name__ == '__main__':
    ll = LinkList()
    ll.push(5)
    ll.push(6)
    ll.push(8)
    ll.push(2)
    ll.push(1)
    ll.push(7)
    print(ll)
    ll.quickSort()
