class Solution:
    def divide(self, dividend, divisor):
        quotient  = 0
        while dividend > divisor:
            dividend = dividend - divisor
            quotient += 1
        return(quotient)

s = Solution
print(s.divide('self', dividend = 10,divisor= 3))

