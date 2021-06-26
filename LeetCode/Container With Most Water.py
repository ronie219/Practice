class Solution:
    def maxArea(self, height):
        # vol = 0
        # for i in range(len(height)):
        #     j = i + 1
        #     width = 1
        #     while j < len(height):
        #         if min(height[i],height[j]) * width > vol:
        #             vol = min(height[i],height[j]) * width
        #         j+=1
        #         width += 1
        # return(vol)
        max_vol = 0
        i = 0
        j = len(height) - 1
        while i < j:
            if min(height[i],height[j]) * (j-i) > max_vol:
                max_vol = min(height[i],height[j]) * (j-i)
            if height[i] > height[j]:
                j-=1
            else:
                i+=1
        print(max_vol)
s = Solution()
s.maxArea([1,2,4,3])