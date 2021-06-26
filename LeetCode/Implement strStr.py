class Solution:
    def strStr(self, haystack, needle):
        if needle is None or '':
            return 0
        return(haystack.find(needle))

s = Solution()
s.strStr('hello','ll')