def _recurion_call(first,last,n,out,final=[]):
        if last == n:
            final.append(''.join(out))
        else:
            if first > last:
                out.append(')')
                _recurion_call(first,last+1,n,out)
                out.pop()
            if first < n:
                out.append('(')
                _recurion_call(first+1,last,n,out)
                out.pop()
        return final
class Solution:
    def generateParenthesis(self, n):
        out = []
        # if n == 1:
        #     return ['()']
        return (_recurion_call(0,0,n,out))
    
s = Solution()
print(s.generateParenthesis(2))