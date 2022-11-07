from typing import List


def minOperations(nums: List[int], x: int) -> int:
    len_long_sub_arr = sum(nums) - x
    hash_map = {0: -1} # map of sum and idx
    prefix_sum = 0
    result = float('-inf')
    for idx in range(len(nums)):
        prefix_sum += (nums[idx])
        hash_map[prefix_sum] = idx
        if prefix_sum - len_long_sub_arr in hash_map:
            result = max(result, idx - hash_map[prefix_sum - len_long_sub_arr])
    return -1 if result == float('-inf') else len(nums) - result

array =[3,2,20,1,1,3]
x = 10

print(minOperations(array, x))