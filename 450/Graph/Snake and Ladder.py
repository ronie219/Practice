from collections import deque

class Solution:
    
    def snakesAndLadders(self, board):
        visited = set()
        queue = deque()
        queue.append(1)
        step_count = 0
        board_array = []

        # convert into single matrix
        reverse = False
        for idx in range(len(borad)-1,-1,-1):
            if reverse == True:
                board_array.extend(borad[idx][::-1])
            else:
                board_array.extend(borad[idx])
            reverse = not(reverse)

        # BFS call to find the minimum step
        while queue:
            
            for _ in range(len(queue)):
                current_step = queue.popleft()
                if current_step == len(board_array): return step_count
                for dice in range(1,7):
                    step = dice + current_step
                    if step not in visited and step <= len(board_array):
                        visited.add(step)
                        if board_array[step - 1] != -1: 
                            queue.append(board_array[step - 1])
                        else:
                            queue.append(step)
            step_count += 1        




sl = Solution()
borad = [[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,35,-1,-1,13,-1],[-1,-1,-1,-1,-1,-1],[-1,15,-1,-1,-1,-1]]
print(sl.snakesAndLadders(borad))