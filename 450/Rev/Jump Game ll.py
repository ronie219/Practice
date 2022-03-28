from collections import deque
from typing import List


def jump(nums: List[int]) -> int:
    queue = deque()
    # search on the basis of idx
    seen = set()
    queue.append(0)
    jump = 0
    while queue:
        size = len(queue)
        for _ in range(size):
            node = queue.popleft()
            if node >= len(nums): continue
            if node == len(nums) - 1: return jump
            val = nums[node]
            for i in range(node + 1, node + val+1):
                if i not in seen:
                    seen.add(i)
                    queue.append(i)

        jump += 1
    print(jump)


print(jump([2, 3, 1, 1, 4]))
