def _length(head):
    count = 0
    while head:
        count += 1
        head = head.next
    return count

def _segredate(head,idx):
    pivot = head
    while idx < 0:
        pivot = pivot.next
        idx -= 1
    large = Node(-1)
    small = Node(-1)
    smlpt = small 
    lgpt = large
    curr = head
    while curr:
        if curr.data < pivot.data:
            smlpt.next = curr
            smlpt = smlpt.next
        elif curr.data > pivot.data:
            lgpt.next = curr
            lgpt = lgpt.next
        curr = curr.next
    smlpt.next = None
    lgpt.next = None
    pivot.next = None

    return small.next,large.next,pivot

def mergeSortedList(left,pivot,right):
    head = None
    tail = None
    if not left[0] and not right[0]:
        left[1].next = pivot
        pivot.next = right[0]
        head = left[0]
        tail = right[1]
    elif left[0] is None:
        head = pivot
        head.next = right[0]
        tail = right[1]
    elif right[0] is None:
        head = left[0]
        left[1].next = pivot
        tail = pivot
    else:
        head = pivot
        tail = pivot

    return head,tail

def _quicksort(head):
    if head is None or head.next is None: return head,head
    length = _length(head)
    pivotIDX = length // 2
    left_head,right_head,pivot = _segredate(head,pivotIDX)

    sorted_left = _quicksort(left_head)
    sorted_right = _quicksort(right_head)

    return mergeSortedList(sorted_left, pivot, sorted_right)



def quickSort(head):
    return _quicksort(head)[0]


########################### Driver Function #############################
from collections import defaultdict
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Llist:
    def __init__(self):
        self.head=None
    
    def insert(self,data,tail):
        node=Node(data)
        
        if not self.head:
            self.head=node
            return node
        
        tail.next=node
        return node
        
def nodeID(head,dic):
    while head:
        dic[head.data].append(id(head))
        head=head.next
        


def printList(head,dic):
    while head:
        if id(head) not in dic[head.data]:
            print("Do'nt swap data, swap pointer/node")
            return
        print(head.data,end=' ')
        head=head.next
        
if __name__ == '__main__':
    t=int(input())
    
    for tcs in range(t):
        n=int(input())
        
        arr=[int(x) for x in input().split()]
        
        ll=Llist()
        tail=None
        
        for nodeData in arr:
            tail=ll.insert(nodeData,tail)
            
        dic=defaultdict(list)   # dictonary to keep data and id of node
        nodeID(ll.head,dic)     # putting data and its id
        
        resHead=quickSort(ll.head)
        printList(resHead,dic)  #verifying and printing
        print()
