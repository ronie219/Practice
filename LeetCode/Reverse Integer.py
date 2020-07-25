class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            x = str(x)[::-1]
            x = x[:-1]
            return int(x) * -1 if int(x)* -1 > -(2**31) else 0
        elif x > 0:
            x = str(x)[::-1]
            return int(x) if int(x) < (2**31)-1 else 0
        else:
            return 0
    
s = Solution()
print(s.reverse(-2147483648))


