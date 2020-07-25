class Solution:
    def convert(self, s, numRows):
        # lis = []
        # converion = ''
        # interval = numRows + (numRows//2)
        # index = 0
        # while index < len(s):
        #     converion += s[index]
        #     lis.append(s[index+1:interval])
        #     index = interval
        #     interval += interval
        # while len(converion) != len(s):
        #     index = 0
        #     for i in lis:
        #         if len(i) == 1:
        #             converion += i
        #             index += 1
        #         elif len(i) >= 2:
        #             converion += (i[0] + i[-1])
        #             lis[index] = i[1:-2]
        #             index +=1
        # print(converion)
        if numRows == 1:
            return s
        vector = -1
        result = ['' for i in range(numRows)]
        row = 0
        for i in s:
            if row == 0 or row == (numRows-1):
                vector *= -1
            result[row]+= i
            row += vector
        out = ''
        for i in result:
            out += i
        print(out)
s = Solution()
s.convert('AB',1)

# pinalsigyphigg
# PINALSIGYAHRPI