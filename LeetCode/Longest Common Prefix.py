class Solution:
    def longestCommonPrefix(self, strs):
        # if len(strs) == 0:
        #     return ''
        prefix = ''
        for i in zip(*strs):
            if len(set(i)) == 1:
                prefix += i[0]
            else:
                break
        return prefix
        # min_string = (min(strs))
        # while len(min_string) != 0:
        #     for i in strs:
        #         if min_string != i[:len(min_string)]:
        #             min_string = min_string[:-1]
        #             break
        #     else:
        #         return min_string
        # return ''

s = Solution()
print(s.longestCommonPrefix(["flower","flow","flight"]))