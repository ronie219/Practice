class Solution:
    def removeDuplicates(self, nums):
        # N = len(nums)
        # i = j = 1
        # while i < N:
        #     if nums[i] != nums[i-1]:
        #         nums[j] = nums[i]
        #         j += 1
        #     i += 1
        # return j
        if len(nums) <= 2:
            return len(nums)
        index = 1
        for i in range(len(nums)-1):
            if nums[i] != nums[i + 1]:
                index += 1
        
        return index

s = Solution()
print(s.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))