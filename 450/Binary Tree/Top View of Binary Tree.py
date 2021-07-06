from collections import deque

class Node:

    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None


class BinaryTree:

    def insert(self):
        data = input("Enter Data ")
        if data == '-1':
            return None
        root = Node(data)
        print("Enter the Value in Left of " + str(data))
        root.left = self.insert()

        print("Enter the Value in Right of " + str(data))
        root.right = self.insert()
        return root
        
    def widthOfBinaryTree(self,root,level = 0,difference = [0,0]):
        if root is None:
            return None
        if root.left:
            difference[0] = min(level,difference[0])
            self.widthOfBinaryTree(root.left,level-1,difference)
        if root.right:
            difference[1] = max(level,difference[1]) 
            self.widthOfBinaryTree(root.right,level+1,difference)
        print(difference)
        return difference[1] - difference[0] + 1
    
    def verticalOrderTraversal(self,root):
        if root is None: return
        range_= [0,0]
        answer=dict()
        queue = deque()
        queue.append([root,0])
        while queue:
            size = len(queue)
            for i in range(size):
                element = queue.popleft()
                if element[1] not in answer.keys():
                    answer[element[1]] = [element[0].data,]
                else:
                    answer[element[1]].append(element[0].data)
                range_[0] = min(range_[0],element[1])
                range_[1] = max(range_[1],element[1]) 
                if element[0].left: queue.append([element[0].left,element[1]-1])
                if element[0].right: queue.append([element[0].right,element[1]+1])
        # print(answer)
        # print(range_)
        output = []
        for idx in range(range_[0],range_[1]+1):
            output.append(answer[idx])
        return output

    def topViewofBinaryTree(self,root):            
        if root is None: return
        range_= [0,0]
        answer=dict()
        queue = deque()
        queue.append([root,0])
        while queue:
            size = len(queue)
            for i in range(size):
                element = queue.popleft()
                if element[1] not in answer.keys():
                    answer[element[1]] = [element[0].data,]
                else:
                    answer[element[1]].append(element[0].data)
                range_[0] = min(range_[0],element[1])
                range_[1] = max(range_[1],element[1]) 
                if element[0].left: queue.append([element[0].left,element[1]-1])
                if element[0].right: queue.append([element[0].right,element[1]+1])
        # print(answer)
        # print(range_)
        output = []
        for idx in range(range_[0],range_[1]+1):
            output.append(answer[idx][0])
        return output

    def bottomViewofBinaryTree(self,root):
        if root is None: return
        range_= [0,0]
        answer=dict()
        queue = deque()
        queue.append([root,0])
        while queue:
            size = len(queue)
            for i in range(size):
                element = queue.popleft()
                if element[1] not in answer.keys():
                    answer[element[1]] = [element[0].data,]
                else:
                    answer[element[1]].append(element[0].data)
                range_[0] = min(range_[0],element[1])
                range_[1] = max(range_[1],element[1]) 
                if element[0].left: queue.append([element[0].left,element[1]-1])
                if element[0].right: queue.append([element[0].right,element[1]+1])
        # print(answer)
        # print(range_)
        output = []
        for idx in range(range_[0],range_[1]+1):
            output.append(answer[idx][-1])
        return output


s = BinaryTree()
root = s.insert()
# print(s.widthOfBinaryTree(root=root))
print(s.verticalOrderTraversal(root))
