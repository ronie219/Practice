class Solution:
    def threeSumClosest(self, nums, target):
        nums.sort()
        result = []
        for i in range(len(nums) - 2):
            j = i + 1
            k = len(nums) - 1
            if i < 0 and nums[i] == nums[i-1]:
                continue
            else:
                while j < k:
                    addition = nums[i]+nums[j]+nums[k]
                    if addition == target:
                        result.append([nums[i], nums[j], nums[k]])
                        while nums[j] == nums[j+1]:
                            j += 1
                        while nums[k] == nums[k-1]:
                            k -= 1
                        k -= 1
                        j += 1
                    elif addition > target:
                        k -= 1
                    else:
                        j += 1
        return result

s = Solution()
print(s.threeSumClosest([-1,2,1,-4],1))