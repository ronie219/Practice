class Solution():
    def intToRoman(self, num):
        dic = {1000:'M',900:'CM',500:'D',400:'CD',100:'C',90:'XC',50:'L',40:'XL',10:'X',9:'IX',5:'V',4:"IV",1:'I'}
        roman = ''
        for i in dic.keys():
            if num // i > 0:
                # print(str(num // i), dic[i])
                roman += (dic[i] * (num // i))
                num = num % i
        return roman
s = Solution()
print(s.intToRoman(1994))