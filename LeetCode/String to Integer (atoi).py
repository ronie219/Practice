class Solution:
    def myAtoi(self, string):
        integer = ''
        for i in string:
            if i == '-' or i == ' ' or i.isdigit() or i == '+':
                integer += i
            else:
                break
        integer = integer.split()
        print(integer)
        try:
            if int(float(integer[0])) >= (2**31):
                return (2**31)-1
            elif int(float(integer[0])) <= -(2**31):
                return -(2**31)
            else:
                return int(float(integer[0]))
        except:
            return 0
s = Solution()
print(s.myAtoi("-5-"))