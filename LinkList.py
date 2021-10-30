<<<<<<< HEAD
class Node():
    def __init__(self, value):
        self.value = value
        self.pointer = None


class LinkList:
    def __init__(self):
        self.head = None

    def Push(self, item):
        node = Node(item)
        if self.head is None:
            self.head = node
        else:
            cur_node = self.head
            while cur_node.pointer:
                cur_node = cur_node.pointer
            cur_node.pointer = node

    def iterative_length(self):
        initial = self.head
        count = 0
        while initial:
            count += 1
            initial = initial.pointer
        return count

    def recursive_length(self, node):
        while node:
            if node.pointer is None:
                return 1
            else:
                node = node.pointer
                return 1 + self.recursive_length(node)

    def Print(self):
        curr_node = self.head
        while curr_node:
            print(curr_node.value)
            curr_node = curr_node.pointer

    def find_ele_recursive(self, node, ele):
        while node is not None:
            if node.value == ele:
                return True
            else:
                return self.find_ele_recursive(node.pointer, ele)
        return False

    def find_ele_iterative(self, ele):
        node = self.head
        while node:
            if node.value == ele:
                return True
            node = node.pointer
        return False

    def get_node(self, index):
        node = self.head
        count = 0
        while node:
            if index == count:
                return node.value
            node = node.pointer
            count += 1
        raise IndexError


l1 = LinkList()
l1.Push(10)
l1.Push(20)
l1.Push(30)
l1.Push(40)
l1.Push(50)
l1.Print()
# print(l1.iterative_length())
# print(l1.recursive_length(l1.head))
# print(l1.find_ele_recursive(l1.head, 10))
# print(l1.find_ele_iterative(50))
# print(l1.get_node(1))
# isPalindrome(l1)
=======
class Node():
    def __init__(self, value):
        self.value = value
        self.pointer = None


class LinkList:
    def __init__(self):
        self.head = None

    def Push(self, item):
        node = Node(item)
        if self.head is None:
            self.head = node
        else:
            cur_node = self.head
            while cur_node.pointer:
                cur_node = cur_node.pointer
            cur_node.pointer = node

    def iterative_length(self):
        initial = self.head
        count = 0
        while initial:
            count += 1
            initial = initial.pointer
        return count

    def recursive_length(self, node):
        while node:
            if node.pointer is None:
                return 1
            else:
                node = node.pointer
                return 1 + self.recursive_length(node)

    def Print(self):
        curr_node = self.head
        while curr_node:
            print(curr_node.value)
            curr_node = curr_node.pointer

    def find_ele_recursive(self, node, ele):
        while node is not None:
            if node.value == ele:
                return True
            else:
                return self.find_ele_recursive(node.pointer, ele)
        return False

    def find_ele_iterative(self, ele):
        node = self.head
        while node:
            if node.value == ele:
                return True
            node = node.pointer
        return False

    def get_node(self, index):
        node = self.head
        count = 0
        while node:
            if index == count:
                return node.value
            node = node.pointer
            count += 1
        raise IndexError


l1 = LinkList()
l1.Push(10)
l1.Push(20)
l1.Push(30)
l1.Push(40)
l1.Push(50)
l1.Print()
# print(l1.iterative_length())
# print(l1.recursive_length(l1.head))
# print(l1.find_ele_recursive(l1.head, 10))
# print(l1.find_ele_iterative(50))
# print(l1.get_node(1))
# isPalindrome(l1)
>>>>>>> 7f688d62f8ef42d5982882d6981075fb426ea81a
