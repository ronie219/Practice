class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkList:

    th = None
    tt = None

    def __init__(self):
        self.head = None

    def __str__(self):
        items = []
        cur = self.head

        while cur:
            items.append(str(cur.data))
            cur = cur.next
        return " --> ".join(items)

    def listLength(self):
        curr = self.head
        length = 0
        while curr:
            curr = curr.next
            length += 1
        return length

    def addFirst(self, element):
        if LinkList.th == None and LinkList.tt == None:
            LinkList.th = element
            LinkList.tt = element
        else:
            element.next = LinkList.th
            LinkList.th = element

    def K_reverse(self, k):
        length = self.listLength()
        current = self.head
        orign_h = None
        orign_t = None

        while current and length >= k:
            for _ in range(k):
                frwd = current.next
                current.next = None
                self.addFirst(current)
                current = frwd
            length -= k
            if orign_h == None and orign_t == None:
                orign_h = LinkList.th
                orign_t = LinkList.tt
            else:
                orign_t.next = LinkList.th
                orign_t = LinkList.tt
            LinkList.th = None
            LinkList.tt = None
        orign_t.next = current
        self.head = orign_h

    def push(self, ele):
        curr = self.head
        n = Node(ele)
        if curr is None:
            self.head = n
        else:
            while curr.next:
                curr = curr.next
            curr.next = n


if __name__ == '__main__':
    linkedList = LinkList()
    linkedList.push(1)
    linkedList.push(2)
    linkedList.push(3)
    linkedList.push(4)
    linkedList.push(5)
    linkedList.push(6)
    linkedList.push(7)
    linkedList.push(8)
    linkedList.push(9)
    linkedList.push(10)
    linkedList.push(11)
    linkedList.push(12)
    print(linkedList)
    linkedList.K_reverse(3)
    print(linkedList)
