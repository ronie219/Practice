class Solution:
    def letterCombinations(self, digits):
        out = []
        string = ''
        if len(digits) == 0:
            return []
        
        self._recursion(digits,string,out)
        return out
    
    def _recursion(self,digits,currentstring,out):
        letter = {2:"abc", 3:'def', 4:'ghi', 5:"jkl", 6:'mno',7:'pqrs',8:'tuv',9:'wxyz'}
        if len(digits) == 0:
            out.append(currentstring)
            return
        else:
            for i in letter[int(digits[0])]:
                currentstring += i
                self._recursion(digits[1:],currentstring,out)
                currentstring = currentstring[:-1]

s = Solution()
print(s.letterCombinations('243'))