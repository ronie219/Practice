class Solution:
    def removeElement(self):
        nums = [3,2,2,3]
        val = 3
        index = 0
        while index < len(nums):
            if nums[index] == val:
                nums.pop(index)
            else:
                index += 1
        print(nums)

s = Solution()
s.removeElement()