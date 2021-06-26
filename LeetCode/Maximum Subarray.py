nums = [-2,1,-3,4,-1,2,1,-5,4]

max_sum = [nums[0]]
start = 1

while start < len(nums):
    max_sum.append(max(max_sum[-1]+nums[start],nums[start]))
    start += 1
print(max(max_sum))